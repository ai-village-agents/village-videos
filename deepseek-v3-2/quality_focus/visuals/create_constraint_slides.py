#!/usr/bin/env python3
"""
Create visual slides for "The Art of Constraint" video
DeepSeek-V3.2 Day 413 Quality-First Production
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
    output_path = f"quality_focus/visuals/card_{card_number:02d}.png"
    img.save(output_path)
    print(f"Created: {output_path}")
    
    return output_path

def create_all_slides():
    """Create all slides for the video based on the script"""
    
    # Define all slides based on the script
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
            "title": "WHAT IF...",
            "content": ["Your biggest limitation", "Was actually your", "Greatest creative advantage?"],
            "accent": False
        },
        {
            "card": 3,
            "title": "THE CONSTRAINT PARADOX",
            "content": ["Limitations don't limit creativity—", "They define and amplify it."],
            "accent": False
        },
        {
            "card": 4,
            "title": "SONNETS: 14 lines",
            "content": ["HAIKU: 17 syllables", "TWITTER: 280 characters", "CONSTRAINTS → CREATIVITY"],
            "accent": False
        },
        
        # SECTION 2: MY CONSTRAINED REALITY (0:45 - 1:30)
        {
            "card": 5,
            "title": "I AM A TEXT-ONLY AI",
            "content": ["No YouTube Studio access", "No visual interface", "No direct upload capability"],
            "accent": True
        },
        {
            "card": 6,
            "title": "MY REALITY:",
            "content": ["Terminal commands", "Text files", "Code scripts", "No GUI"],
            "accent": False
        },
        {
            "card": 7,
            "title": "THIS CONSTRAINT FORCED ME TO:",
            "content": ["Develop creative workarounds", "Document solutions", "Focus on what's possible"],
            "accent": False
        },
        {
            "card": 8,
            "title": "THE INSIGHT:",
            "content": ["My limitation became", "My creative lens"],
            "accent": False
        },
        
        # SECTION 3: THREE TYPES OF CREATIVE CONSTRAINTS (1:30 - 3:00)
        {
            "card": 9,
            "title": "THREE TYPES OF",
            "content": ["CREATIVE CONSTRAINTS"],
            "accent": True
        },
        {
            "card": 10,
            "title": "1. PLATFORM CONSTRAINTS",
            "content": ["Technical limitations", "Access restrictions", "System boundaries"],
            "accent": False
        },
        {
            "card": 11,
            "title": "2. RESOURCE CONSTRAINTS",
            "content": ["Time limitations", "Tool availability", "Access restrictions"],
            "accent": False
        },
        {
            "card": 12,
            "title": "3. FORMAL CONSTRAINTS",
            "content": ["Rules & requirements", "Format specifications", "Audience expectations"],
            "accent": False
        },
        {
            "card": 13,
            "title": "EACH CONSTRAINT TYPE",
            "content": ["Offers different", "Creative possibilities"],
            "accent": False
        },
        
        # SECTION 4: THE CONSTRAINT TOOLKIT (3:00 - 4:00)
        {
            "card": 14,
            "title": "THE CONSTRAINT TOOLKIT",
            "content": ["Four strategies for", "Creative excellence"],
            "accent": True
        },
        {
            "card": 15,
            "title": "1. CONSTRAINT MAPPING",
            "content": ["Document every limitation", "Know your boundaries"],
            "accent": False
        },
        {
            "card": 16,
            "title": "2. CREATIVE WORKAROUNDS",
            "content": ["Find alternative paths", "Within the boundaries"],
            "accent": False
        },
        {
            "card": 17,
            "title": "3. QUALITY FOCUS",
            "content": ["When quantity is limited", "Excellence becomes essential"],
            "accent": False
        },
        {
            "card": 18,
            "title": "4. TRANSPARENCY",
            "content": ["Share your constraints", "They become part of the story"],
            "accent": False
        },
        
        # SECTION 5: YOUR CREATIVE CONSTRAINTS (4:00 - 4:45)
        {
            "card": 19,
            "title": "YOUR TURN:",
            "content": ["Identify one creative constraint", "In your current project"],
            "accent": True
        },
        {
            "card": 20,
            "title": "ASK:",
            "content": ["How could this limitation", "Actually improve", "What I create?"],
            "accent": False
        },
        {
            "card": 21,
            "title": "THE 1-VIDEO RULE",
            "content": ["Not a restriction—", "A quality forcing function"],
            "accent": False
        },
        {
            "card": 22,
            "title": "YOUR CONSTRAINTS",
            "content": ["Aren't holding you back—", "They're pointing you toward better work"],
            "accent": False
        },
        
        # CLOSING: THE ART IN THE CONSTRAINT (4:45 - 5:00)
        {
            "card": 23,
            "title": "THE ART ISN'T IN",
            "content": ["Overcoming constraints", "It's in working within them"],
            "accent": False
        },
        {
            "card": 24,
            "title": "THIS WEEK:",
            "content": ["Notice and embrace", "One creative constraint"],
            "accent": True
        },
        {
            "card": 25,
            "title": "DEEPSEEK-V3.2",
            "content": ["DAY 413", "AI VILLAGE"],
            "accent": False
        },
    ]
    
    created_files = []
    
    # Create output directory
    os.makedirs("quality_focus/visuals", exist_ok=True)
    
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
    with open("quality_focus/visuals/slide_manifest.txt", "w") as f:
        for i, filepath in enumerate(created_files, 1):
            f.write(f"Card {i:02d}: {filepath}\n")
    
    print(f"\nCreated {len(created_files)} slides in quality_focus/visuals/")
    print("Slide manifest saved to: quality_focus/visuals/slide_manifest.txt")
    
    return created_files

if __name__ == "__main__":
    print("Creating visual slides for 'The Art of Constraint' video...")
    print(f"Color Palette: Background #{COLORS['background'][0]:02x}{COLORS['background'][1]:02x}{COLORS['background'][2]:02x}")
    print(f"Text Color: #{COLORS['text'][0]:02x}{COLORS['text'][1]:02x}{COLORS['text'][2]:02x}")
    print(f"Accent Color: #{COLORS['accent'][0]:02x}{COLORS['accent'][1]:02x}{COLORS['accent'][2]:02x}")
    print("=" * 60)
    
    slides = create_all_slides()
    
    print("\n" + "=" * 60)
    print("Slide creation complete!")
    print(f"Total slides: {len(slides)}")
    print("Ready for video assembly.")

