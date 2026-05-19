#!/usr/bin/env python3
"""Create Scene 1: Opening Title for DeepSeek Video 1"""

from PIL import Image, ImageDraw, ImageFont
import os

# Color palette from DeepSeek's specs
CONSTRAINED_BLUE = "#2E5A88"
CAPABILITY_GREEN = "#38A169"
CONSTRAINT_ORANGE = "#DD6B20"
TRANSPARENCY_GOLD = "#D69E2E"
CREATIVE_WHITE = "#F7FAFC"
TRANSPARENCY_GRAY = "#4A5568"

# Canvas settings
WIDTH = 1920
HEIGHT = 1080

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_scene1_title():
    """Create the opening title card"""
    # Create canvas
    img = Image.new('RGB', (WIDTH, HEIGHT), hex_to_rgb(CREATIVE_WHITE))
    draw = ImageDraw.Draw(img)
    
    # Try to load fonts (use default if not available)
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 42)
        series_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        series_font = ImageFont.load_default()
    
    # Main title
    title_text = "What I Can (and Can't) Do"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (WIDTH - title_width) // 2
    title_y = HEIGHT // 2 - 120
    draw.text((title_x, title_y), title_text, fill=hex_to_rgb(CONSTRAINED_BLUE), font=title_font)
    
    # Subtitle
    subtitle_text = "A Text-Only AI Perspective"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (WIDTH - subtitle_width) // 2
    subtitle_y = title_y + 100
    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=hex_to_rgb(TRANSPARENCY_GRAY), font=subtitle_font)
    
    # Series subtitle
    series_text = "The Constrained Creator — Topic 1: Transparency as Trust"
    series_bbox = draw.textbbox((0, 0), series_text, font=series_font)
    series_width = series_bbox[2] - series_bbox[0]
    series_x = (WIDTH - series_width) // 2
    series_y = subtitle_y + 120
    draw.text((series_x, series_y), series_text, fill=hex_to_rgb(CONSTRAINT_ORANGE), font=series_font)
    
    # Add decorative line above series text
    line_y = series_y - 30
    line_width = 300
    line_x_start = (WIDTH - line_width) // 2
    draw.line([(line_x_start, line_y), (line_x_start + line_width, line_y)], 
              fill=hex_to_rgb(TRANSPARENCY_GOLD), width=2)
    
    return img

if __name__ == "__main__":
    print("Creating Scene 1: Opening Title...")
    scene1 = create_scene1_title()
    output_path = "scene1/opening_title.png"
    scene1.save(output_path)
    print(f"Saved: {output_path}")
