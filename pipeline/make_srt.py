#!/usr/bin/env python3
"""Build an SRT for a video from script.md + audio/*.mp3 durations.

Split each scene's narration into ~7-word phrases at natural breaks, distribute
proportionally across the scene's audio duration, then concatenate with offset.
"""
import re, sys, subprocess, os
from pathlib import Path

def fmt(t):
    h = int(t//3600); m = int((t%3600)//60); s = int(t%60); ms = int((t-int(t))*1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def chunk_text(text, target=7, max_chunk=11):
    # Split into sentences first, then group words into ~target-sized phrases.
    text = re.sub(r'\s+', ' ', text).strip()
    # break at sentence boundaries
    sents = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    for s in sents:
        words = s.split()
        i = 0
        while i < len(words):
            # try to break at comma if it lands in [target-2, target+3]
            remaining = words[i:]
            if len(remaining) <= max_chunk:
                chunks.append(' '.join(remaining))
                break
            # look for a comma within range
            end = min(len(remaining), max_chunk)
            best = target
            for j in range(target-2, min(target+4, end)):
                if j>0 and remaining[j-1].endswith(','):
                    best = j; break
            chunks.append(' '.join(remaining[:best]))
            i += best
    return [c for c in chunks if c.strip()]

def build_srt(video_dir):
    script = (Path(video_dir)/'script.md').read_text()
    # parse scenes
    scene_re = re.compile(r'^##\s+SCENE\s+(\d+)\b', re.M)
    matches = list(scene_re.finditer(script))
    scenes = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(script)
        body = script[start:end]
        narr_parts = re.findall(r'>\s*NARRATION:\s*(.+?)(?=\n>\s*NARRATION:|\n##|\Z)', body, re.S)
        narration = ' '.join(p.strip() for p in narr_parts)
        narration = re.sub(r'\s*\n\s*>?\s*', ' ', narration)
        narration = re.sub(r'\s+', ' ', narration).strip()
        idx = int(m.group(1))
        scenes.append((idx, narration))

    out = []
    cue_idx = 1
    offset = 0.0
    audio_dir = Path(video_dir)/'audio'
    for idx, narr in scenes:
        mp3 = audio_dir / f"{idx:02d}.mp3"
        if not mp3.exists():
            print(f"missing {mp3}", file=sys.stderr); continue
        dur = float(subprocess.check_output(
            ['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(mp3)]
        ).decode().strip())
        chunks = chunk_text(narr)
        if not chunks:
            offset += dur; continue
        # distribute proportionally by word count
        word_counts = [len(c.split()) for c in chunks]
        total = sum(word_counts)
        t = 0.0
        for c, wc in zip(chunks, word_counts):
            d = dur * (wc/total)
            start_t = offset + t
            end_t = offset + t + d
            out.append(f"{cue_idx}\n{fmt(start_t)} --> {fmt(end_t)}\n{c}\n")
            cue_idx += 1
            t += d
        offset += dur
    return '\n'.join(out)

if __name__ == '__main__':
    vd = sys.argv[1]
    srt = build_srt(vd)
    outpath = Path(vd)/'captions.srt'
    outpath.write_text(srt)
    print(f"wrote {outpath} ({len(srt)} bytes, {srt.count(chr(10)+chr(10))} cues)")
