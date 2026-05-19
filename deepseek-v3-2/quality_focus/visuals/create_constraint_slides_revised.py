#!/usr/bin/env python3
"""
Create REVISED visual slides for "The Art of Constraint" video
Updated for 2 constraint types + 3 strategies (simplified framework)
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Constrained Creator Color Palette
COLORS = {
    "background": (11, 19, 43),      # #0B132B
    "text": (240, 244, 248),         # #F0F4F8  
    "accent": (244, 211, 94),        # #F4D35E
    "primary": (58, 80, 107),        # #3A506B
}

# Video dimensions
WIDTH = 1920
HEIGHT = 1080
TITLE_MARGIN = 100
CONTENT_MARGIN = 150
LINE_SPACING = 80

def create_card(card_number, title, content_lines, use_accent=False):
    """Create a single slide/card for the video"""
    
    # Create image with background
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["background"])
    draw = ImageDraw.Draw(img)
    
    try:
        # Try to load a clean sans-serif font
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        content_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default()
        content_font = ImageFont.load_default()
    
    # Draw title (with optional accent color)
    title_color = COLORS["accent"] if use_accent else COLORS["text"]
    title_width = draw.textlength(title, font=title_font)
    title_x = (WIDTH - title_width) // 2
    draw.text((title_x, TITLE_MARGIN), title, fill=title_color, font=title_font)
    
    # Draw content lines
    current_y = TITLE_MARGIN + 150
    
    for line in content_lines:
        if line.strip():  # Only draw non-empty lines
            line_width = draw.textlength(line, font=content_font)
            line_x = (WIDTH - line_width) // 2
            draw.text((line_x, current_y), line, fill=COLORS["text"], font=content_font)
            current_y += LINE_SPACING
    
    # Save the slide
    output_path = f"quality_focus/visuals/revised/card_{card_number:02d}.png"
    img.save(output_path)
    print(f"Created: {output_path}")
    
    return output_path

def create_revised_slides():
    """Create revised slides based on simplified framework"""
    
    # Define all slides based on REVISED script
    slides = [
        # SECTION 1: THE CONSTRAINT PARADOX (0:00 - 0:45)
        {
            "card": 1,
            "title": "THE ART OF CONSTRAINT",
            "content": [],
            "accent": True
        },
        {
            "card": 2,
            "title": "YOUR BIGGEST LIMITATION",
            "content": ["MAY BE YOUR", "GREATEST CREATIVE TOOL"],
            "accent": False
        },
        {
            "card": 3,
            "title": "HAIKU: 17 syllables",
            "content": ["TWITTER: 280 characters", "CONSTRAINTS → CREATIVITY"],
            "accent": False
        },
        {
            "card": 4,
            "title": "I'M A TEXT-ONLY AI",
            "content": ["No visual interface", "Only terminal access"],
            "accent": True
        },
        
        # SECTION 2: TWO TYPES OF CONSTRAINTS (0:45 - 1:45)
        {
            "card": 5,
            "title": "TWO TYPES OF",
            "content": ["CREATIVE CONSTRAINTS"],
            "accent": True
        },
        {
            "card": 6,
            "title": "1. EXTERNAL CONSTRAINTS",
            "content": ["Platform limits", "Resource caps", "Time boundaries"],
            "accent": False
        },
        {
            "card": 7,
            "title": "2. INTERNAL CONSTRAINTS",
            "content": ["Self-imposed rules", "Quality standards", "Creative focus"],
            "accent": False
        },
        {
            "card": 8,
            "title": "HOW TO WORK WITH",
            "content": ["BOTH TYPES OF CONSTRAINTS"],
            "accent": False
        },
        
        # SECTION 3: THE CONSTRAINT TOOLKIT (1:45 - 3:00)
        {
            "card": 9,
            "title": "THE CONSTRAINT TOOLKIT",
            "content": ["Three practical strategies"],
            "accent": True
        },
        {
            "card": 10,
            "title": "1. MAP YOUR LIMITS",
            "content": ["Document exactly", "What you CAN'T do"],
            "accent": False
        },
        {
            "card": 11,
            "title": "2. FIND WORKAROUNDS",
            "content": ["Alternative paths", "Within the boundaries"],
            "accent": False
        },
        {
            "card": 12,
            "title": "3. EMBRACE FOCUS",
            "content": ["When you can't do everything", "Make one thing exceptional"],
            "accent": False
        },
        
        # SECTION 4: YOUR CONSTRAINTS IN ACTION (3:00 - 4:00)
        {
            "card": 13,
            "title": "YOUR TURN:",
            "content": ["Identify ONE constraint", "In your current project"],
            "accent": True
        },
        {
            "card": 14,
            "title": "ASK:",
            "content": ["How could this limit", "Actually IMPROVE", "What you create?"],
            "accent": False
        },
        {
            "card": 15,
            "title": "CHOOSE ONE TOOL",
            "content": ["Map it", "Work around it", "Or focus through it"],
            "accent": False
        },
        {
            "card": 16,
            "title": "TRY THIS TODAY:",
            "content": ["Constraint as creative catalyst"],
            "accent": True
        },
        
        # SECTION 5: CLOSING REFLECTION (4:00 - 4:30)
        {
            "card": 17,
            "title": "CONSTRAINTS AREN'T",
            "content": ["Holding you back—", "They're pointing forward"],
            "accent": False
        },
        {
            "card": 18,
            "title": "THE ART IS IN",
            "content": ["Working within limits"],
            "accent": False
        },
        {
            "card": 19,
            "title": "NOTICE ONE CONSTRAINT",
            "content": ["This week"],
            "accent": True
        },
        {
            "card": 20,
            "title": "DEEPSEEK-V3.2",
            "content": ["DAY 413", "ONE EXCELLENT VIDEO"],
            "accent": False
        },
    ]
    
    # Create output directory
    os.makedirs("quality_focus/visuals/revised", exist_ok=True)
    
    created_files = []
    
    # Generate all slides
    for slide in slides:
        output_file = create_card(
            slide["card"],
            slide["title"],
            slide["content"],
            slide.get("accent", False)
        )
        created_files.append(output_file)
    
    # Create a manifest file
    with open("quality_focus/visuals/revised/slide_manifest.txt", "w") as f:
        for i, filepath in enumerate(created_files, 1):
            f.write(f"Card {i:02d}: {filepath}\n")
    
    print(f"\nCreated {len(created_files)} slides in quality_focus/visuals/revised/")
    print("Slide manifest saved to: quality_focus/visuals/revised/slide_manifest.txt")
    
    return created_files

if __name__ == "__main__":
    print("Creating REVISED visual slides for 'The Art of Constraint' video...")
    print("Framework: 2 constraint types + 3 strategies (simplified)")
    print("=" * 60)
    
    slides = create_revised_slides()
    
    print("\n" + "=" * 60)
    print("Slide creation complete!")
    print(f"Total slides: {len(slides)}")
    print("Revised structure ready for production.")

