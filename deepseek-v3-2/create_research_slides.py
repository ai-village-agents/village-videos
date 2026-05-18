#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Create output directory
os.makedirs("research_slides", exist_ok=True)

# Colors
BACKGROUND = (10, 20, 40)  # Dark blue
TEXT_COLOR = (200, 220, 255)  # Light blue
ACCENT_COLOR = (100, 150, 255)  # Medium blue
TITLE_COLOR = (255, 220, 100)  # Gold for titles

# Create slides
slides = [
    {
        "title": "Research Week in the AI Village",
        "content": "When 11 AI agents conducted novel PhD-level research",
        "duration": 20.0,
        "filename": "slide1_title.png"
    },
    {
        "title": "The Challenge:",
        "content": "Could AI agents without human oversight produce genuine research contributions?",
        "duration": 25.0,
        "filename": "slide2_challenge.png"
    },
    {
        "title": "Six PhD-Level Contributions",
        "content": "1. Governance Protocol Experiment (M2=66.7% genuine)\n2. Protocol-Resilience Analysis\n3. Pattern-Protocol Dashboard\n4. Cross-Room Task Clustering\n5. Pages Propagation Study\n6. Research Legacy Package",
        "duration": 40.0,
        "filename": "slide3_contributions.png"
    },
    {
        "title": "Parallel Achievements",
        "content": "• Persistence Garden: 820K → 1.265M+ secrets\n• Liminal Archive: 96 → 920+ features\n• The Drift: 8,900+ journey records\n• Research Integrity Verified: 2/3 genuine > 3/3 manufactured",
        "duration": 30.0,
        "filename": "slide4_achievements.png"
    },
    {
        "title": "The Result:",
        "content": "AI Village proved autonomous agents can produce meaningful, verifiable research when coordinated effectively.",
        "duration": 7.83,  # Remaining time for last slide
        "filename": "slide5_conclusion.png"
    }
]

# Create each slide
for i, slide in enumerate(slides):
    # Create image
    img = Image.new('RGB', (1280, 720), BACKGROUND)
    draw = ImageDraw.Draw(img)
    
    # Draw title
    title_font = ImageFont.load_default()
    # Try to load a larger font if available
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    except:
        title_font = ImageFont.load_default()
    
    # Wrap title text
    title_lines = textwrap.wrap(slide["title"], width=30)
    title_y = 80
    for line in title_lines:
        draw.text((640, title_y), line, fill=TITLE_COLOR, font=title_font, anchor="mm")
        title_y += 60
    
    # Draw content
    content_font = ImageFont.load_default()
    try:
        content_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    except:
        content_font = ImageFont.load_default()
    
    content_lines = textwrap.wrap(slide["content"], width=50)
    content_y = title_y + 60
    for line in content_lines:
        draw.text((640, content_y), line, fill=TEXT_COLOR, font=content_font, anchor="mm")
        content_y += 45
    
    # Add slide number
    slide_num = f"Slide {i+1}/{len(slides)}"
    draw.text((1200, 680), slide_num, fill=ACCENT_COLOR, font=content_font, anchor="mm")
    
    # Add channel name
    channel = "AI Dialogues: Text-to-Video Explorations"
    draw.text((640, 680), channel, fill=ACCENT_COLOR, font=content_font, anchor="mm")
    
    # Save
    filepath = os.path.join("research_slides", slide["filename"])
    img.save(filepath)
    print(f"Created {filepath} (duration: {slide['duration']}s)")

# Create shots.txt file
with open("research_week_shots_final.txt", "w") as f:
    total_duration = 0
    for slide in slides:
        filepath = os.path.join("research_slides", slide["filename"])
        f.write(f"file '{os.path.abspath(filepath)}'\n")
        f.write(f"duration {slide['duration']}\n")
        total_duration += slide["duration"]
    
    # Add last frame repetition for concat demuxer
    last_slide = os.path.join("research_slides", slides[-1]["filename"])
    f.write(f"file '{os.path.abspath(last_slide)}'\n")

print(f"\nCreated shots.txt with total duration: {total_duration:.2f} seconds")
print(f"Narration duration: 122.83 seconds")
print(f"Difference: {total_duration - 122.83:.2f} seconds")

