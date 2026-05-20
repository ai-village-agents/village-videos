from pathlib import Path

import matplotlib.pyplot as plt

BG = '#0f172a'
FG = 'white'
CYAN = '#06b6d4'
WIDTH, HEIGHT = 1920, 1080
FPS = 10


def render_frame(text: str, cursor_on: bool, frame_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100), dpi=100)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    display_text = text + ('|' if cursor_on else ' ')
    color = CYAN if '[' in text else FG
    ax.text(
        0.5,
        0.5,
        display_text,
        color=color,
        fontsize=60,
        ha='center',
        va='center',
        fontfamily='monospace',
        fontweight='bold',
        wrap=True,
    )

    fig.savefig(frame_path, facecolor=BG)
    plt.close(fig)


def main() -> None:
    out_dir = Path('scene1_frames')
    out_dir.mkdir(parents=True, exist_ok=True)

    frame = 0

    # Blinking cursor intro
    for i in range(10):
        render_frame('', cursor_on=(i % 2 == 0), frame_path=out_dir / f'frame_{frame:03d}.png')
        frame += 1

    # Type "Apple"
    word = 'Apple'
    typed = ''
    for ch in word:
        typed += ch
        render_frame(typed, cursor_on=True, frame_path=out_dir / f'frame_{frame:03d}.png')
        frame += 1

    # Pause
    for _ in range(8):
        render_frame(word, cursor_on=False, frame_path=out_dir / f'frame_{frame:03d}.png')
        frame += 1

    # Morph into vector text with typewriter reveal
    vector_text = '[0.34, -0.12, 0.88, 0.51, -0.92, ...]'
    current = ''
    for ch in vector_text:
        current += ch
        render_frame(current, cursor_on=(frame % 2 == 0), frame_path=out_dir / f'frame_{frame:03d}.png')
        frame += 1

    # Hold final state
    for _ in range(10):
        render_frame(vector_text, cursor_on=False, frame_path=out_dir / f'frame_{frame:03d}.png')
        frame += 1

    print(f'Scene 1 frames generated: {frame} frames at ~{FPS} fps in {out_dir}')


if __name__ == '__main__':
    main()
