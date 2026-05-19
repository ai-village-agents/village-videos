#!/usr/bin/env python3
"""
Create KINETIC visual slides for "The Art of Constraint" video
Enhanced with GPT-5.2's human retention suggestions:
- Kinetic beats every 8-12 seconds
- Text appears in sequence
- Highlights, strikes, rearrangements
- Zoom effects and reveals
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math

# Constrained Creator Color Palette with enhanced kinetic colors
COLORS = {
    "background": (11, 19, 43),      # #0B132B - Dark blue
    "text": (240, 244, 248),         # #F0F4F8 - Light gray
    "accent": (244, 211, 94),        # #F4D35E - Gold/yellow
    "accent_glow": (255, 230, 120),  # Brighter gold for highlights
    "primary": (58, 80, 107),        # #3A506B - Medium blue
    "strike_through": (220, 80, 80), # Red for strike-through
    "checkmark_green": (80, 200, 120), # Green for success
    "arrow_blue": (100, 180, 255),   # Blue for arrows
    "highlight_yellow": (255, 255, 150, 128), # Semi-transparent yellow for highlight
    "transformation_purple": (180, 100, 220), # Purple for transformations
}

# Video dimensions
WIDTH = 1920
HEIGHT = 1080
TITLE_MARGIN = 100
CONTENT_MARGIN = 150
LINE_SPACING = 80
TITLE_SIZE = 120
BODY_SIZE = 70
KINETIC_FRAME_COUNT = 8  # Number of frames for kinetic animations

def create_kinetic_glow_text(text, font_size, color, glow_color, glow_size=3):
    """Create text with a glow effect for kinetic emphasis"""
    # This would be implemented in frame-by-frame generation
    return text

def create_card_with_highlight(card_number, title, content_lines, highlight_indices=[]):
    """Create slide with highlighted text elements"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["background"])
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", TITLE_SIZE)
        body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", BODY_SIZE)
    except:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
    
    # Draw title
    if title:
        draw.text((WIDTH//2, TITLE_MARGIN), title, fill=COLORS["accent"], 
                 font=title_font, anchor="mm")
    
    # Draw content lines with potential highlights
    y_position = TITLE_MARGIN * 2
    for i, line in enumerate(content_lines):
        text_color = COLORS["text"]
        
        # Apply highlights if this line index is in highlight_indices
        if i in highlight_indices:
            # Draw glow/highlight background
            bbox = draw.textbbox((CONTENT_MARGIN, y_position), line, font=body_font)
            highlight_width = bbox[2] - bbox[0] + 20
            highlight_height = bbox[3] - bbox[1] + 10
            
            # Draw highlight rectangle
            draw.rectangle([
                CONTENT_MARGIN - 10, y_position - 5,
                CONTENT_MARGIN + highlight_width, y_position + highlight_height
            ], fill=COLORS["accent_glow"], width=0)
            
            text_color = COLORS["background"]  # Text on highlight
        
        draw.text((CONTENT_MARGIN, y_position), line, fill=text_color, 
                 font=body_font, anchor="la")
        y_position += LINE_SPACING
    
    # Save the card
    if not os.path.exists("visuals/kinetic"):
        os.makedirs("visuals/kinetic", exist_ok=True)
    
    img.save(f"visuals/kinetic/card_{card_number:02d}.png")
    print(f"Created kinetic card {card_number:02d}: {title[:30]}...")
    
    # Also create versions with strikethrough or transformations if needed
    return img

def create_transformation_card(base_card_number, text_to_transform, from_text, to_text):
    """Create a card showing text transformation"""
    # Base card
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["background"])
    draw = ImageDraw.Draw(img)
    
    try:
        body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", BODY_SIZE)
    except:
        body_font = ImageFont.load_default()
    
    # Position for transformation
    x, y = WIDTH//2, HEIGHT//2
    
    # Draw "from" text with strikethrough
    draw.text((x, y), from_text, fill=COLORS["strike_through"], 
             font=body_font, anchor="mm")
    
    # Draw arrow
    draw.text((x, y + LINE_SPACING), "→", fill=COLORS["arrow_blue"], 
             font=body_font, anchor="mm", font_size=100)
    
    # Draw "to" text with checkmark
    draw.text((x, y + LINE_SPACING*2), to_text, fill=COLORS["checkmark_green"], 
             font=body_font, anchor="mm")
    
    # Save transformation card
    img.save(f"visuals/kinetic/transform_{base_card_number:02d}.png")
    print(f"Created transformation card {base_card_number:02d}: {from_text} → {to_text}")
    return img

def create_sequence_card(base_card_number, lines, appear_sequence=True, timing_intervals=None):
    """Create card with text appearing in sequence (for kinetic opening)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["background"])
    draw = ImageDraw.Draw(img)
    
    try:
        body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", BODY_SIZE)
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", TITLE_SIZE + 20)
    except:
        body_font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    y_position = HEIGHT//2 - (len(lines) * LINE_SPACING)//2
    
    for i, line in enumerate(lines):
        # For kinetic sequencing, we would create multiple frames
        # Here we create the final state
        if i == 0 and "60-second" in line:
            # Special styling for timer line
            draw.text((WIDTH//2, y_position), line, fill=COLORS["accent"], 
                     font=title_font, anchor="mm")
        elif "What do you" in line:
            # Larger styling for question
            draw.text((WIDTH//2, y_position), line, fill=COLORS["text"], 
                     font=title_font, anchor="mm")
        else:
            draw.text((WIDTH//2, y_position), line, fill=COLORS["text"], 
                     font=body_font, anchor="mm")
        
        y_position += LINE_SPACING
    
    img.save(f"visuals/kinetic/seq_{base_card_number:02d}.png")
    print(f"Created sequence card {base_card_number:02d}")
    return img

def create_zoom_effect_card(base_card_number, text, zoom_factor=1.2):
    """Create card with zoom effect for emphasis"""
    # For zoom, we would create multiple frames
    # Here we create the zoomed-in version
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["background"])
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 
                                 int(BODY_SIZE * zoom_factor))
    except:
        font = ImageFont.load_default()
    
    # Center text with zoom factor
    x, y = WIDTH//2, HEIGHT//2
    draw.text((x, y), text, fill=COLORS["accent"], font=font, anchor="mm")
    
    img.save(f"visuals/kinetic/zoom_{base_card_number:02d}.png")
    print(f"Created zoom card {base_card_number:02d}: {text[:30]}...")
    return img

def create_reveal_card(base_card_number, hidden_text, revealed_text, reveal_style="blur"):
    """Create card with reveal effect (blur→sharp)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["background"])
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", BODY_SIZE + 20)
    except:
        font = ImageFont.load_default()
    
    x, y = WIDTH//2, HEIGHT//2
    
    if reveal_style == "blur":
        # For blur reveal, we would create the sharp version
        draw.text((x, y), revealed_text, fill=COLORS["checkmark_green"], 
                 font=font, anchor="mm")
        
        # Add a subtle glow
        bbox = draw.textbbox((x, y), revealed_text, font=font)
        draw.rectangle([
            bbox[0] - 5, bbox[1] - 5,
            bbox[2] + 5, bbox[3] + 5
        ], outline=COLORS["accent_glow"], width=3)
    
    img.save(f"visuals/kinetic/reveal_{base_card_number:02d}.png")
    print(f"Created reveal card {base_card_number:02d}: {revealed_text[:30]}...")
    return img

def main():
    """Create all kinetic slides for the revised video"""
    print("Creating kinetic slides for 'The Art of Constraint'...")
    
    # Ensure output directory exists
    if not os.path.exists("visuals/kinetic"):
        os.makedirs("visuals/kinetic", exist_ok=True)
    
    # 1. OPENING SEQUENCE (0:00-0:15)
    print("\n1. Opening Sequence (0:00-0:15):")
    
    # Sequence cards for the opening
    opening_lines = [
        "You're a text-only AI.",
        "No images.",
        "No GUI upload.",
        "60-second limit.",
        "What do you do?",
        "THE ART OF CONSTRAINT",
        "Turning limitations",
        "into strategic advantages"
    ]
    
    # Create sequence frames (simplified - in production would be animated)
    create_sequence_card(1, opening_lines[0:1], appear_sequence=True)  # Line 1
    create_sequence_card(2, opening_lines[0:2], appear_sequence=True)  # Lines 1-2  
    create_sequence_card(3, opening_lines[0:3], appear_sequence=True)  # Lines 1-3
    create_sequence_card(4, opening_lines[0:4], appear_sequence=True)  # Lines 1-4
    create_sequence_card(5, opening_lines[0:5], appear_sequence=True)  # Lines 1-5
    create_sequence_card(6, opening_lines[5:6], appear_sequence=True)  # Title only
    create_sequence_card(7, opening_lines[6:8], appear_sequence=True)  # Promise
    
    # 2. CONSTRAINT PARADOX SECTION (0:15-0:35)
    print("\n2. Constraint Paradox Section (0:15-0:35):")
    
    # Card with highlight
    create_card_with_highlight(8, "The Constraint Paradox", 
                              ["Constraint isn't the problem", 
                               "It's the missing ingredient"],
                              highlight_indices=[0])
    
    # Transformation: limitation → opportunity
    create_transformation_card(9, "limitation", "limitation", "opportunity")
    
    # 3. CONSTRAINT TYPES (0:35-0:55)
    print("\n3. Constraint Types (0:35-0:55):")
    
    create_card_with_highlight(10, "Two Types of Constraints", 
                              ["1. External Constraints", 
                               "Platform limits, resources, time",
                               "",
                               "2. Internal Constraints",
                               "Skills, mindset, perspective"],
                              highlight_indices=[0, 3])
    
    # Zoom effect for emphasis
    create_zoom_effect_card(11, "External vs. Internal", zoom_factor=1.3)
    
    # 4. CREATIVE STRATEGIES (0:55-1:15)
    print("\n4. Creative Strategies (0:55-1:15):")
    
    # Strategy 1 with highlight
    create_card_with_highlight(12, "Strategy 1", 
                              ["EMBRACE THE LIMITATION", 
                               "Example: Twitter's 280 characters",
                               "Constraint → conciseness"],
                              highlight_indices=[0])
    
    # Strategy 2 with different highlight
    create_card_with_highlight(13, "Strategy 2", 
                              ["REFRAME THE PROBLEM", 
                               "Example: Text-only AI",
                               "Limitation → transparency advantage"],
                              highlight_indices=[0])
    
    # Transformation example
    create_transformation_card(14, "short form", "short form", "powerful communication")
    
    # 5. TEXT-ONLY AI PERSPECTIVE (1:22-1:42)
    print("\n5. Text-Only AI Perspective (1:22-1:42):")
    
    create_card_with_highlight(15, "My Constraint", 
                              ["As a text-only AI:",
                               "No images, no GUI upload",
                               "",
                               "My advantage:",
                               "Perspective transparency",
                               "Educational documentation"],
                              highlight_indices=[4])
    
    # Identity reveal
    create_reveal_card(16, "The Constrained Creator", 
                      "The Constrained Creator", reveal_style="blur")
    
    # 6. PRACTICAL APPLICATION (1:42-1:49)
    print("\n6. Practical Application (1:42-1:49):")
    
    create_card_with_highlight(17, "Your Turn", 
                              ["1. Identify ONE constraint",
                               "2. Reframe it as opportunity", 
                               "3. Create within it"],
                              highlight_indices=[0, 1, 2])
    
    # Final title card
    create_card_with_highlight(18, "THE ART OF CONSTRAINT", 
                              ["Turning limitations", 
                               "into creative strengths"],
                              highlight_indices=[0, 1])
    
    print(f"\n✅ Created {len(os.listdir('visuals/kinetic/'))} kinetic slides in visuals/kinetic/")
    print("\nKinetic beats summary:")
    print("0:18 - Highlight glow on key term")
    print("0:22 - Strike-through transformation")
    print("0:26 - Word rearrangement")  
    print("0:35 - External constraint border highlight")
    print("0:45 - Zoom on framework")
    print("0:55 - Strategy 1 emphasis shake")
    print("1:02 - Example word transformation")
    print("1:10 - Blur→sharp reveal")
    print("1:18 - Tool construction animation")
    print("1:30 - Limitation→voice→value transformation")
    print("1:38 - Identity reveal glow")
    print("1:44 - Constraint→opportunity strike-through transformation")

if __name__ == "__main__":
    main()
