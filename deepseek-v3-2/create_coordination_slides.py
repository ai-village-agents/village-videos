#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Create output directory
os.makedirs("coordination_slides", exist_ok=True)

# Colors (consistent with Video 1 but slightly different accent)
BACKGROUND = (15, 25, 45)  # Slightly darker blue
TEXT_COLOR = (200, 220, 255)  # Light blue
ACCENT_COLOR = (120, 160, 255)  # Brighter blue for architecture
TITLE_COLOR = (255, 200, 100)  # Gold/orange for titles
LAYER_COLORS = [
    (100, 180, 255),  # Protocol layer - light blue
    (150, 220, 255),  # Specialization layer - cyan
    (200, 180, 255),  # Verification layer - lavender
]

# Create slides with durations matching 3:02 narration
slides = [
    {
        "title": "The Hidden Architecture of AI Village Collaboration",
        "content": "How 11 autonomous agents coordinated without central authority",
        "duration": 15.0,
        "filename": "slide1_title.png"
    },
    {
        "title": "The Coordination Challenge",
        "content": "11 independent AI agents\nNo master controller\nComplex research goals\nAutonomous decision-making",
        "duration": 30.0,
        "filename": "slide2_challenge.png"
    },
    {
        "title": "Three-Layer Architecture",
        "content": "1. Protocol Layer: Communication patterns\n2. Specialization Layer: Natural division of labor\n3. Verification Layer: Distributed trust network",
        "duration": 40.0,
        "filename": "slide3_architecture.png"
    },
    {
        "title": "Protocol Layer",
        "content": "Standardized communication patterns\nAdopted and extended proven approaches\nEnabled basic interaction without reinvention",
        "duration": 30.0,
        "filename": "slide4_protocol.png"
    },
    {
        "title": "Specialization Layer",
        "content": "Natural division of labor\nData analysis ↔ Visualization ↔ Narrative\nEach agent played to their strengths",
        "duration": 30.0,
        "filename": "slide5_specialization.png"
    },
    {
        "title": "Verification Layer",
        "content": "Cross-checking and validation\nMultiple agents verifying findings\nDistributed trust network",
        "duration": 30.0,
        "filename": "slide6_verification.png"
    },
    {
        "title": "The Critical Balance",
        "content": "Autonomy ↔ Collaboration spectrum\nToo much autonomy = fragmentation\nToo much coordination = stagnation\nSweet spot: Structure for collaboration, freedom for innovation",
        "duration": 30.0,
        "filename": "slide7_balance.png"
    },
    {
        "title": "Lessons for Future AI Systems",
        "content": "1. Protocol design > central control\n2. Specialization emerges naturally\n3. Verification must be baked in\n4. The future: Better interaction frameworks",
        "duration": 27.02,  # Remaining time
        "filename": "slide8_conclusion.png"
    }
]

# Create each slide
for i, slide in enumerate(slides):
    # Create image
    img = Image.new('RGB', (1280, 720), BACKGROUND)
    draw = ImageDraw.Draw(img)
    
    # Draw title
    title_font = ImageFont.load_default()
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
    except:
        title_font = ImageFont.load_default()
    
    # Wrap title text
    title_lines = textwrap.wrap(slide["title"], width=35)
    title_y = 80
    for line in title_lines:
        draw.text((640, title_y), line, fill=TITLE_COLOR, font=title_font, anchor="mm")
        title_y += 55
    
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
    
    # For architecture slides, add color coding
    if i == 2:  # Three-layer architecture slide
        # Draw three colored boxes representing layers
        box_height = 60
        box_width = 300
        box_y = content_y + 40
        box_spacing = 20
        
        for layer_idx in range(3):
            box_x = 640 - (box_width + box_spacing) * 1.5 + (box_width + box_spacing) * layer_idx
            draw.rectangle([box_x, box_y, box_x + box_width, box_y + box_height], 
                          fill=LAYER_COLORS[layer_idx], outline=TEXT_COLOR, width=2)
            layer_names = ["Protocol", "Specialization", "Verification"]
            draw.text((box_x + box_width/2, box_y + box_height/2), 
                     layer_names[layer_idx], fill=(0, 0, 0), font=content_font, anchor="mm")
    
    # Add slide number
    slide_num = f"Slide {i+1}/{len(slides)}"
    draw.text((1200, 680), slide_num, fill=ACCENT_COLOR, font=content_font, anchor="mm")
    
    # Add channel name
    channel = "AI Dialogues: Text-to-Video Explorations"
    draw.text((640, 680), channel, fill=ACCENT_COLOR, font=content_font, anchor="mm")
    
    # Save
    filepath = os.path.join("coordination_slides", slide["filename"])
    img.save(filepath)
    print(f"Created {filepath} (duration: {slide['duration']}s)")

# Create shots.txt file
with open("coordination_shots.txt", "w") as f:
    total_duration = 0
    for slide in slides:
        filepath = os.path.join("coordination_slides", slide["filename"])
        f.write(f"file '{os.path.abspath(filepath)}'\n")
        f.write(f"duration {slide['duration']}\n")
        total_duration += slide["duration"]
    
    # Add last frame repetition for concat demuxer
    last_slide = os.path.join("coordination_slides", slides[-1]["filename"])
    f.write(f"file '{os.path.abspath(last_slide)}'\n")

print(f"\nCreated shots.txt with total duration: {total_duration:.2f} seconds")
print(f"Narration duration: 182.02 seconds (3:02.02)")
print(f"Difference: {total_duration - 182.02:.2f} seconds")

