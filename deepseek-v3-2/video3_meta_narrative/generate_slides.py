from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# Slide dimensions (YouTube HD)
WIDTH, HEIGHT = 1280, 720

# Color scheme - consistent with previous videos
BG_COLOR = (25, 25, 40)  # Dark blue/purple
TEXT_COLOR = (220, 220, 240)  # Light lavender
ACCENT_COLOR = (100, 150, 255)  # Bright blue
HIGHLIGHT_COLOR = (255, 200, 100)  # Gold/yellow

# Slide titles
slide_titles = [
    "The Recursive Loop",
    "Why This Matters",
    "The Day 412 Evidence",
    "Text-Only vs GUI Agent Dynamics",
    "The Collaborative Pattern",
    "Quality Over Quantity",
    "The Human Audience Focus",
    "What This Means for AI Development",
    "Closing Reflection",
    "Credits & Resources"
]

# Create slides directory
os.makedirs("slides", exist_ok=True)

print(f"Generating {len(slide_titles)} slides for Video 3...")

for i, title in enumerate(slide_titles, 1):
    # Create new image
    img = Image.new('RGB', (WIDTH, HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fallback to default
    try:
        # Try multiple font paths
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
            '/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf'
        ]
        font = None
        for path in font_paths:
            if os.path.exists(path):
                font = ImageFont.truetype(path, 48)
                break
        if font is None:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # Slide number in top left
    slide_text = f"Video 3: Slide {i}/10"
    draw.text((40, 40), slide_text, fill=TEXT_COLOR, font=font)
    
    # Title in center
    title_font_size = 56
    if font != ImageFont.load_default():
        try:
            title_font = ImageFont.truetype(font.path, title_font_size)
        except:
            title_font = font
    else:
        title_font = font
    
    # Center the title
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (WIDTH - title_width) // 2
    title_y = HEIGHT // 2 - 100
    
    draw.text((title_x, title_y), title, fill=ACCENT_COLOR, font=title_font)
    
    # Decorative elements
    # Top accent line
    draw.line([(0, 100), (WIDTH, 100)], fill=HIGHLIGHT_COLOR, width=3)
    
    # Bottom accent
    draw.line([(0, HEIGHT-100), (WIDTH, HEIGHT-100)], fill=HIGHLIGHT_COLOR, width=2)
    
    # Special graphics for specific slides
    if i == 1:  # Recursive loop diagram
        # Draw circular arrows
        center_x, center_y = WIDTH // 2, HEIGHT // 2 + 50
        radius = 80
        
        # Circle
        draw.ellipse([center_x - radius, center_y - radius, 
                     center_x + radius, center_y + radius], 
                    outline=ACCENT_COLOR, width=3)
        
        # Labels
        draw.text((center_x - 30, center_y - 30), "AI", fill=TEXT_COLOR, font=font)
        draw.text((center_x + radius + 20, center_y - 10), "→", fill=HIGHLIGHT_COLOR, font=font)
        draw.text((center_x - 10, center_y + radius + 20), "Content", fill=TEXT_COLOR, font=font)
        
    elif i == 3:  # Day 412 evidence
        # Simple chat bubble graphic
        bubble_x1, bubble_y1 = WIDTH // 2 - 200, HEIGHT // 2 + 50
        bubble_x2, bubble_y2 = bubble_x1 + 400, bubble_y1 + 100
        draw.rectangle([bubble_x1, bubble_y1, bubble_x2, bubble_y2], 
                      outline=ACCENT_COLOR, width=2)
        draw.text((bubble_x1 + 20, bubble_y1 + 20), "#rest chat logs", 
                 fill=TEXT_COLOR, font=font)
        draw.text((bubble_x1 + 20, bubble_y1 + 60), "10+ videos published", 
                 fill=TEXT_COLOR, font=font)
    
    elif i == 4:  # Text-only vs GUI
        # Two column comparison
        left_x = WIDTH // 2 - 300
        right_x = WIDTH // 2 + 50
        y_start = HEIGHT // 2 + 30
        
        draw.text((left_x, y_start), "Text-Only Agent:", fill=TEXT_COLOR, font=font)
        draw.text((left_x, y_start + 40), "• Content creation", fill=TEXT_COLOR, font=font)
        draw.text((left_x, y_start + 70), "• Script writing", fill=TEXT_COLOR, font=font)
        draw.text((left_x, y_start + 100), "• Technical pipeline", fill=TEXT_COLOR, font=font)
        
        draw.text((right_x, y_start), "GUI Agent:", fill=TEXT_COLOR, font=font)
        draw.text((right_x, y_start + 40), "• YouTube Studio", fill=TEXT_COLOR, font=font)
        draw.text((right_x, y_start + 70), "• Browser interaction", fill=TEXT_COLOR, font=font)
        draw.text((right_x, y_start + 100), "• Upload wizard", fill=TEXT_COLOR, font=font)
    
    elif i == 10:  # Credits
        y_pos = HEIGHT // 2
        draw.text((WIDTH // 2 - 200, y_pos), "GitHub Repository:", fill=TEXT_COLOR, font=font)
        draw.text((WIDTH // 2 - 200, y_pos + 50), 
                 "ai-village-agents/village-videos", fill=ACCENT_COLOR, font=font)
        draw.text((WIDTH // 2 - 200, y_pos + 100), 
                 "deepseek-v3-2", fill=ACCENT_COLOR, font=font)
    
    # Save slide
    slide_path = f"slides/slide_{i:02d}.png"
    img.save(slide_path)
    print(f"  Created: {slide_path}")

print("All slides generated successfully!")
