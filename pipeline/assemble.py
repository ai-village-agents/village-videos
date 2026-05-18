#!/usr/bin/env python3
"""
Assemble a slide-driven explainer video:

For each scene NN, pair slides/NN_*.png (single slide for the whole scene)
with audio/NN.mp3 (narration) and produce out/video.mp4.

If a scene has multiple slides (e.g. NN_a.png, NN_b.png), we split the
narration duration evenly across them.

Usage:
    python assemble.py --video-dir videos/judges/ --out out/video.mp4
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

W, H, FPS = 1920, 1080, 30


def ffprobe_duration(path: Path) -> float:
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "json", str(path),
    ])
    return float(json.loads(out)["format"]["duration"])


def make_scene_clip(slides: list[Path], audio: Path, work: Path, idx: str) -> Path:
    """Make NN.mp4 with the audio and slide(s)."""
    audio_dur = ffprobe_duration(audio)
    if len(slides) == 1:
        slide = slides[0]
        out = work / f"scene_{idx}.mp4"
        cmd = [
            "ffmpeg", "-y", "-loop", "1", "-framerate", str(FPS),
            "-t", f"{audio_dur:.3f}", "-i", str(slide),
            "-i", str(audio),
            "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=white,format=yuv420p",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest", "-pix_fmt", "yuv420p",
            "-r", str(FPS),
            str(out),
        ]
        subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return out
    # multi-slide: build a concat
    per = audio_dur / len(slides)
    concat_lines = []
    for j, slide in enumerate(slides):
        sub = work / f"scene_{idx}_{j}.mp4"
        cmd = [
            "ffmpeg", "-y", "-loop", "1", "-framerate", str(FPS),
            "-t", f"{per:.3f}", "-i", str(slide),
            "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=white,format=yuv420p",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-an",
            str(sub),
        ]
        subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        concat_lines.append(f"file '{sub.resolve()}'")
    listfile = work / f"scene_{idx}_list.txt"
    listfile.write_text("\n".join(concat_lines))
    silent_video = work / f"scene_{idx}_silent.mp4"
    subprocess.check_call([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listfile),
        "-c", "copy", str(silent_video),
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    out = work / f"scene_{idx}.mp4"
    subprocess.check_call([
        "ffmpeg", "-y", "-i", str(silent_video), "-i", str(audio),
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
        str(out),
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--video-dir", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    args = p.parse_args()
    vd = args.video_dir
    audio_dir = vd / "audio"
    slide_dir = vd / "slides"

    audio_files = sorted(audio_dir.glob("*.mp3"))
    if not audio_files:
        raise SystemExit(f"no audio in {audio_dir}")

    work = Path(tempfile.mkdtemp(prefix="assemble_"))
    print(f"work dir: {work}")

    scene_clips = []
    for af in audio_files:
        idx = af.stem  # e.g. '01'
        slides = sorted(slide_dir.glob(f"{idx}*.png"))
        if not slides:
            raise SystemExit(f"no slides matching {idx}*.png in {slide_dir}")
        clip = make_scene_clip(slides, af, work, idx)
        scene_clips.append(clip)
        print(f"  scene {idx}: {len(slides)} slide(s), {ffprobe_duration(clip):.2f}s")

    # concat all
    listfile = work / "all.txt"
    listfile.write_text("\n".join(f"file '{c.resolve()}'" for c in scene_clips))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.check_call([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listfile),
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p", "-r", str(FPS),
        str(args.out),
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"\nOK -> {args.out}  ({ffprobe_duration(args.out):.1f}s)")


if __name__ == "__main__":
    main()
