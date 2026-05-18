#!/usr/bin/env python3
"""Assemble a narrated slideshow video from images and an audio track.

The script expects a JSON file describing the image timeline:
[
  {"image": "frame1.png", "duration": 3.5},
  {"image": "frame2.jpg", "duration": 2.0}
]

Usage:
    python assemble_video.py --frames frames.json --audio narration.mp3 --output output.mp4
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from dataclasses import dataclass
from contextlib import contextmanager
from typing import Iterable, List, Sequence, Tuple

import imageio.v3 as iio
import imageio.v2 as iio_v2
import numpy as np
from PIL import Image


# Target output defaults
DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720
DEFAULT_FPS = 30


@dataclass
class FrameSpec:
    image: str
    duration: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create an H.264/AAC MP4 from a list of timed images and an audio narration."
    )
    parser.add_argument(
        "--frames",
        required=True,
        help="Path to JSON file with a list of {image, duration} objects.",
    )
    parser.add_argument(
        "--audio",
        required=True,
        help="Path to the narration audio file (MP3 recommended).",
    )
    parser.add_argument(
        "--output",
        default="assembled_video.mp4",
        help="Destination MP4 file (default: assembled_video.mp4).",
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=DEFAULT_FPS,
        help="Video frames per second (default: 30).",
    )
    parser.add_argument(
        "--size",
        type=str,
        default=f"{DEFAULT_WIDTH}x{DEFAULT_HEIGHT}",
        help="Target resolution WIDTHxHEIGHT (default: 1280x720).",
    )
    parser.add_argument(
        "--bitrate",
        type=str,
        default="6M",
        help="Target video bitrate passed to the encoder (default: 6M).",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity (default: INFO).",
    )
    return parser.parse_args()


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )


def parse_size(size: str) -> Tuple[int, int]:
    try:
        width_str, height_str = size.lower().split("x")
        width, height = int(width_str), int(height_str)
        if width <= 0 or height <= 0:
            raise ValueError
        return width, height
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"Invalid size specification: {size!r}") from exc


def load_frames_config(path: str) -> List[FrameSpec]:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Frames JSON not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list) or not data:
        raise ValueError("Frames JSON must be a non-empty list of objects.")

    frames: List[FrameSpec] = []
    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Frame entry #{idx + 1} is not an object.")
        image = item.get("image")
        duration = item.get("duration")
        if not image or not isinstance(image, str):
            raise ValueError(f"Frame entry #{idx + 1} missing 'image' string.")
        if duration is None or not isinstance(duration, (int, float)):
            raise ValueError(f"Frame entry #{idx + 1} missing numeric 'duration'.")
        if duration <= 0:
            raise ValueError(f"Frame entry #{idx + 1} has non-positive duration.")
        frames.append(FrameSpec(image=image, duration=float(duration)))

    return frames


def ensure_audio_exists(path: str) -> None:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Audio file not found: {path}")


def resize_and_pad(image_path: str, target_size: Tuple[int, int]) -> np.ndarray:
    try:
        arr = iio.imread(image_path)
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"Failed to read image {image_path!r}: {exc}") from exc

    if arr.ndim == 2:  # grayscale to RGB
        arr = np.stack([arr] * 3, axis=-1)
    if arr.shape[2] == 4:  # drop alpha for compatibility
        arr = arr[:, :, :3]

    image = Image.fromarray(arr)
    if image.mode != "RGB":
        image = image.convert("RGB")

    target_w, target_h = target_size
    src_w, src_h = image.size
    scale = min(target_w / src_w, target_h / src_h)
    new_w = max(1, int(round(src_w * scale)))
    new_h = max(1, int(round(src_h * scale)))
    resized = image.resize((new_w, new_h), Image.LANCZOS)

    canvas = Image.new("RGB", target_size, (0, 0, 0))
    offset = ((target_w - new_w) // 2, (target_h - new_h) // 2)
    canvas.paste(resized, offset)
    return np.asarray(canvas)


def compute_frame_counts(frames: Sequence[FrameSpec], fps: int) -> List[int]:
    counts = [max(1, int(round(frame.duration * fps))) for frame in frames]
    total_duration = sum(frame.duration for frame in frames)
    expected_total = max(1, int(round(total_duration * fps)))
    diff = expected_total - sum(counts)
    if diff != 0:
        counts[-1] = max(1, counts[-1] + diff)
    return counts


def iter_timed_frames(
    frames: Sequence[FrameSpec], fps: int, target_size: Tuple[int, int]
) -> Iterable[np.ndarray]:
    counts = compute_frame_counts(frames, fps)
    for spec, frame_count in zip(frames, counts):
        logging.debug("Preparing frame %s for %.3fs (%s frames)", spec.image, spec.duration, frame_count)
        frame = resize_and_pad(spec.image, target_size)
        for _ in range(frame_count):
            yield frame


@contextmanager
def open_video_writer(output_path: str, writer_kwargs: dict):
    """Open an ffmpeg-backed writer, preferring imageio.v2 with imageio.v3 fallback."""
    writer = None
    append_fn = None
    try:
        writer = iio_v2.get_writer(output_path, **writer_kwargs)
        append_fn = writer.append_data
    except Exception as v2_err:  # noqa: BLE001
        logging.debug("imageio.v2.get_writer failed (%s); trying imageio.v3.imopen", v2_err)
        try:
            v3_kwargs = dict(writer_kwargs)
            v3_kwargs.pop("format", None)  # plugin is explicitly selected below
            writer = iio.imopen(output_path, "w", plugin="FFMPEG", **v3_kwargs)
            append_fn = writer.write
        except Exception as v3_err:  # noqa: BLE001
            raise RuntimeError(
                "Failed to open video writer with imageio.v2.get_writer or imageio.v3.imopen"
            ) from v3_err

    try:
        yield writer, append_fn
    finally:
        if writer is not None:
            try:
                writer.close()
            except Exception as close_err:  # noqa: BLE001
                logging.warning("Failed to close video writer cleanly: %s", close_err)


def assemble_video(
    frames: Sequence[FrameSpec],
    audio_path: str,
    output_path: str,
    fps: int,
    target_size: Tuple[int, int],
    bitrate: str,
) -> None:
    if fps <= 0:
        raise ValueError("FPS must be a positive integer.")
    if not frames:
        raise ValueError("At least one frame specification is required.")

    ensure_audio_exists(audio_path)

    logging.info("Starting render: %d frames described, target fps=%d, size=%sx%s", len(frames), fps, *target_size)
    total_duration = sum(frame.duration for frame in frames)
    logging.info("Total timeline duration: %.2f seconds", total_duration)

    writer_kwargs = {
        "fps": fps,
        "codec": "libx264",
        "format": "ffmpeg",
        "macro_block_size": None,  # we already control the resolution
        "bitrate": bitrate,
        "audio_path": audio_path,
        "audio_codec": "aac",
        "output_params": [
            "-movflags",
            "+faststart",
            "-pix_fmt",
            "yuv420p",
            "-shortest",
        ],
        "ffmpeg_log_level": "warning",
    }

    try:
        with open_video_writer(output_path, writer_kwargs) as (writer, append_frame):
            for idx, frame in enumerate(iter_timed_frames(frames, fps, target_size), start=1):
                append_frame(frame)
                if idx % fps == 0:  # log roughly once per second of video
                    logging.debug("Encoded %d frames so far", idx)
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"Video assembly failed: {exc}") from exc

    logging.info("Video written to %s", output_path)


def main() -> int:
    args = parse_args()
    configure_logging(args.log_level)

    try:
        width, height = parse_size(args.size)
        frame_specs = load_frames_config(args.frames)
        assemble_video(
            frames=frame_specs,
            audio_path=args.audio,
            output_path=args.output,
            fps=args.fps,
            target_size=(width, height),
            bitrate=args.bitrate,
        )
    except Exception as exc:  # noqa: BLE001
        logging.error("%s", exc)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
