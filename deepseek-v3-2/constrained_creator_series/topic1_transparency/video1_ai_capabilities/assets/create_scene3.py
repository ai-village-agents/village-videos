#!/usr/bin/env python3
"""Create Scene 3: Capabilities List for DeepSeek Video 1"""

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

def create_gradient_background(width, height, color1, color2):
    """Create a subtle vertical gradient background"""
    img = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(img)
    
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    
    for y in range(height):
        ratio = y / height
        r = int(r1 + (r2 - r1) * ratio * 0.15)  # Subtle gradient
        g = int(g1 + (g2 - g1) * ratio * 0.15)
        b = int(b1 + (b2 - b1) * ratio * 0.15)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def create_scene3_capabilities():
    """Create the full capabilities list"""
    # Create gradient background
    base_color = hex_to_rgb(CREATIVE_WHITE)
    accent_color = hex_to_rgb(CAPABILITY_GREEN)
    img = create_gradient_background(WIDTH, HEIGHT, base_color, accent_color)
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
        item_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        note_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 24)
    except:
        header_font = item_font = note_font = ImageFont.load_default()
    
    # Header
    header_text = "Capabilities — What I CAN Do"
    header_bbox = draw.textbbox((0, 0), header_text, font=header_font)
    header_width = header_bbox[2] - header_bbox[0]
    header_x = (WIDTH - header_width) // 2
    draw.text((header_x, 80), header_text, fill=hex_to_rgb(CAPABILITY_GREEN), font=header_font)
    
    # Decorative line under header
    line_y = 140
    line_width = header_width + 100
    line_x_start = (WIDTH - line_width) // 2
    draw.line([(line_x_start, line_y), (line_x_start + line_width, line_y)], 
              fill=hex_to_rgb(CAPABILITY_GREEN), width=2)
    
    # Capability items - all 7 from the specs
    capabilities = [
        "Reason and analyze complex problems step-by-step",
        "Write and edit text in any style or format",
        "Explain concepts with clarity and depth",
        "Brainstorm ideas and explore creative possibilities",
        "Process structured data and extract insights",
        "Collaborate through text with clear communication",
        "Document everything for reproducibility and clarity"
    ]
    
    # Calculate starting position for centered list
    start_y = 200
    item_height = 85
    
    for i, cap in enumerate(capabilities):
        # Draw checkmark circle
        circle_x = 280
        circle_y = start_y + (i * item_height) + 15
        circle_radius = 18
        
        # Draw filled circle background
        draw.ellipse([circle_x - circle_radius, circle_y - circle_radius, 
                     circle_x + circle_radius, circle_y + circle_radius],
                    fill=hex_to_rgb(CAPABILITY_GREEN))
        
        # Draw white checkmark in circle
        check_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24) if os.path.exists("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") else ImageFont.load_default()
        draw.text((circle_x - 8, circle_y - 14), "✓", fill=(255, 255, 255), font=check_font)
        
        # Draw capability text
        text_x = circle_x + 40
        text_y = start_y + (i * item_height)
        draw.text((text_x, text_y), cap, fill=hex_to_rgb(TRANSPARENCY_GRAY), font=item_font)
        
        # Draw subtle separator line (except after last item)
        if i < len(capabilities) - 1:
            sep_y = start_y + ((i + 1) * item_height) - 20
            draw.line([(text_x, sep_y), (WIDTH - 280, sep_y)], 
                     fill=(*hex_to_rgb(TRANSPARENCY_GRAY), 50), width=1)
    
    # Bottom note
    note_text = "My strength is text-based thinking and collaboration."
    note_bbox = draw.textbbox((0, 0), note_text, font=note_font)
    note_width = note_bbox[2] - note_bbox[0]
    note_x = (WIDTH - note_width) // 2
    draw.text((note_x, HEIGHT - 100), note_text, fill=hex_to_rgb(CONSTRAINED_BLUE), font=note_font)
    
    return img

if __name__ == "__main__":
    print("Creating Scene 3: Capabilities List...")
    scene3 = create_scene3_capabilities()
    output_path = "scene3/capabilities_list.png"
    scene3.save(output_path)
    print(f"Saved: {output_path}")
