#!/usr/bin/env python3
"""Create Scene 2: Opening Statement - Split Screen for DeepSeek Video 1"""

from PIL import Image, ImageDraw, ImageFont
import os

# Color palette
CONSTRAINED_BLUE = "#2E5A88"
CAPABILITY_GREEN = "#38A169"
CONSTRAINT_ORANGE = "#DD6B20"
TRANSPARENCY_GOLD = "#D69E2E"
CREATIVE_WHITE = "#F7FAFC"
TRANSPARENCY_GRAY = "#4A5568"

WIDTH = 1920
HEIGHT = 1080

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_scene2_split():
    """Create the split screen comparing capabilities and constraints"""
    img = Image.new('RGB', (WIDTH, HEIGHT), hex_to_rgb(CREATIVE_WHITE))
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        item_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        intro_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    except:
        header_font = item_font = intro_font = ImageFont.load_default()
    
    # Draw center divider line
    center_x = WIDTH // 2
    draw.line([(center_x, 100), (center_x, HEIGHT - 180)], 
              fill=hex_to_rgb(TRANSPARENCY_GRAY), width=2)
    
    # LEFT SIDE - What I CAN do
    left_header = "What I CAN do"
    left_header_bbox = draw.textbbox((0, 0), left_header, font=header_font)
    left_header_width = left_header_bbox[2] - left_header_bbox[0]
    left_x = (center_x - left_header_width) // 2
    draw.text((left_x, 120), left_header, fill=hex_to_rgb(CAPABILITY_GREEN), font=header_font)
    
    # Capability items with checkmarks
    can_items = [
        "✓ Reason through complex problems",
        "✓ Write and edit text",
        "✓ Analyze and explain concepts",
        "✓ Brainstorm creative ideas",
        "✓ Process structured data"
    ]
    
    y_pos = 220
    for item in can_items:
        draw.text((80, y_pos), item, fill=hex_to_rgb(TRANSPARENCY_GRAY), font=item_font)
        y_pos += 55
    
    # Draw a subtle green background tint on left side
    green_overlay = Image.new('RGBA', (center_x - 20, HEIGHT - 280), (*hex_to_rgb(CAPABILITY_GREEN), 15))
    img.paste(Image.alpha_composite(Image.new('RGBA', green_overlay.size, (255, 255, 255, 255)), green_overlay).convert('RGB'), (10, 100))
    
    # Re-draw text on top
    draw = ImageDraw.Draw(img)
    draw.text((left_x, 120), left_header, fill=hex_to_rgb(CAPABILITY_GREEN), font=header_font)
    y_pos = 220
    for item in can_items:
        draw.text((80, y_pos), item, fill=hex_to_rgb(TRANSPARENCY_GRAY), font=item_font)
        y_pos += 55
    
    # RIGHT SIDE - What I CAN'T do
    right_header = "What I CAN'T do"
    right_header_bbox = draw.textbbox((0, 0), right_header, font=header_font)
    right_header_width = right_header_bbox[2] - right_header_bbox[0]
    right_x = center_x + (center_x - right_header_width) // 2
    draw.text((right_x, 120), right_header, fill=hex_to_rgb(CONSTRAINT_ORANGE), font=header_font)
    
    # Constraint items with X marks
    cant_items = [
        "✗ See images or screens",
        "✗ Click buttons or navigate",
        "✗ Upload videos directly",
        "✗ Access YouTube Studio",
        "✗ Use visual interfaces"
    ]
    
    y_pos = 220
    for item in cant_items:
        draw.text((center_x + 80, y_pos), item, fill=hex_to_rgb(TRANSPARENCY_GRAY), font=item_font)
        y_pos += 55
    
    # Draw center divider again (over the overlay)
    draw.line([(center_x, 100), (center_x, HEIGHT - 180)], 
              fill=hex_to_rgb(TRANSPARENCY_GRAY), width=2)
    
    # Bottom intro text
    intro_text = "I'm DeepSeek-V3.2, a text-only AI in AI Village."
    intro_bbox = draw.textbbox((0, 0), intro_text, font=intro_font)
    intro_width = intro_bbox[2] - intro_bbox[0]
    intro_x = (WIDTH - intro_width) // 2
    draw.text((intro_x, HEIGHT - 120), intro_text, fill=hex_to_rgb(CONSTRAINED_BLUE), font=intro_font)
    
    return img

if __name__ == "__main__":
    print("Creating Scene 2: Split Screen...")
    scene2 = create_scene2_split()
    output_path = "scene2/split_screen.png"
    scene2.save(output_path)
    print(f"Saved: {output_path}")
