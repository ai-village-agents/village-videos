#!/usr/bin/env python3
"""
Render narration blocks from a script.md into per-scene mp3 + vtt files using edge-tts.

Script format expected:
  ## SCENE 01 — Hook
  > NARRATION: This is the hook. Multiple lines OK, no blank line.
  > And continued narration on next line is appended.

  ## SCENE 02 — Setup
  > NARRATION: Next scene.

Output: <out_dir>/01.mp3, 01.vtt, 02.mp3, 02.vtt, ...
"""
from __future__ import annotations

import argparse
import asyncio
import re
import sys
from pathlib import Path

import edge_tts

SCENE_RE = re.compile(r"^##\s+SCENE\s+(\d+)\b", re.IGNORECASE)
NARR_RE = re.compile(r"^>\s*NARRATION:\s*(.*)$", re.IGNORECASE)
NARR_CONT_RE = re.compile(r"^>\s+(.*)$")


def parse_script(text: str) -> list[tuple[str, str]]:
    """Return list of (scene_num_str, narration_text)."""
    scenes: list[tuple[str, str]] = []
    cur_num: str | None = None
    cur_narr_lines: list[str] = []
    in_narr = False

    def flush():
        if cur_num is not None and cur_narr_lines:
            narr = " ".join(s.strip() for s in cur_narr_lines).strip()
            scenes.append((cur_num, narr))

    for raw in text.splitlines():
        line = raw.rstrip()
        m = SCENE_RE.match(line)
        if m:
            flush()
            cur_num = m.group(1).zfill(2)
            cur_narr_lines = []
            in_narr = False
            continue
        m = NARR_RE.match(line)
        if m:
            in_narr = True
            if m.group(1):
                cur_narr_lines.append(m.group(1))
            continue
        if in_narr:
            m2 = NARR_CONT_RE.match(line)
            if m2:
                cur_narr_lines.append(m2.group(1))
                continue
            # blank/non-blockquote ends narration
            if line.strip() == "" or not line.startswith(">"):
                # narration ended; keep collected lines until next scene
                in_narr = False
    flush()
    return scenes


async def synth_one(text: str, voice: str, rate: str, mp3_path: Path, vtt_path: Path):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    submaker = edge_tts.SubMaker()
    with open(mp3_path, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
    with open(vtt_path, "w") as f:
        f.write(submaker.get_srt())


async def main():
    p = argparse.ArgumentParser()
    p.add_argument("--script", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    p.add_argument("--voice", default="en-US-AndrewMultilingualNeural")
    p.add_argument("--rate", default="-5%", help="speech rate, e.g. -5%% or +0%%")
    args = p.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    text = args.script.read_text()
    scenes = parse_script(text)
    if not scenes:
        print("No scenes parsed!", file=sys.stderr)
        sys.exit(1)
    for num, narr in scenes:
        mp3 = args.out / f"{num}.mp3"
        vtt = args.out / f"{num}.srt"
        print(f"[{num}] {len(narr)} chars -> {mp3.name}", file=sys.stderr)
        await synth_one(narr, args.voice, args.rate, mp3, vtt)
    print(f"Done: {len(scenes)} scenes -> {args.out}", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
