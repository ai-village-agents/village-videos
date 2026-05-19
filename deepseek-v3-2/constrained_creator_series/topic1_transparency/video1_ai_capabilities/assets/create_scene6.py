from PIL import Image, ImageDraw, ImageFont
import os

# Video dimensions
WIDTH = 1920
HEIGHT = 1080

# Color palette from specs
CONSTRAINED_BLUE = (46, 90, 136)      # #2E5A88
CAPABILITY_GREEN = (56, 161, 105)     # #38A169
CONSTRAINT_ORANGE = (221, 107, 32)    # #DD6B20
TRANSPARENCY_GOLD = (214, 158, 46)    # #D69E2E
CREATIVE_WHITE = (247, 250, 252)      # #F7FAFC
TRANSPARENCY_GRAY = (74, 85, 104)     # #4A5568

def create_scene6_transparency_framework():
    """Create the Transparency Framework with 3 principles - Scene 6"""
    img = Image.new('RGB', (WIDTH, HEIGHT), CREATIVE_WHITE)
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        principle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        desc_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
        note_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 20)
    except:
        header_font = principle_font = desc_font = note_font = ImageFont.load_default()
    
    # Header
    header_text = "Transparency Framework"
    header_bbox = draw.textbbox((0, 0), header_text, font=header_font)
    header_width = header_bbox[2] - header_bbox[0]
    header_x = (WIDTH - header_width) // 2
    draw.text((header_x, 50), header_text, fill=CONSTRAINED_BLUE, font=header_font)
    
    # Subheader
    subheader = "Why This Clarity Matters"
    subheader_bbox = draw.textbbox((0, 0), subheader, font=note_font)
    subheader_width = subheader_bbox[2] - subheader_bbox[0]
    subheader_x = (WIDTH - subheader_width) // 2
    draw.text((subheader_x, 110), subheader, fill=TRANSPARENCY_GRAY, font=note_font)
    
    # Decorative line
    line_y = 150
    line_width = 400
    line_x_start = (WIDTH - line_width) // 2
    draw.line([(line_x_start, line_y), (line_x_start + line_width, line_y)], 
              fill=TRANSPARENCY_GOLD, width=3)
    
    # Three principles - arranged horizontally
    principles = [
        {
            "number": "1",
            "title": "Clear Expectations",
            "desc": "If you know I can't see\nscreenshots, you won't ask\nme to analyze them.\n\nThat saves time and\nfrustration.",
            "color": CAPABILITY_GREEN,
            "icon": "✓"  # Checkmark for expectations
        },
        {
            "number": "2", 
            "title": "Complementary Strengths",
            "desc": "My text-based precision\ncomplements visual/interface\ncapabilities of other agents.\n\nTogether we cover more\nground.",
            "color": TRANSPARENCY_GOLD,
            "icon": "⚡"  # Lightning for synergy
        },
        {
            "number": "3",
            "title": "Constraint-Driven Innovation",
            "desc": "These boundaries force\ncreative solutions you\nwouldn't find with\nunlimited capabilities.\n\nLimitations become features.",
            "color": CONSTRAINT_ORANGE,
            "icon": "★"  # Star for innovation
        }
    ]
    
    # Calculate positions for 3 columns
    col_width = WIDTH // 3
    start_y = 200
    
    for i, p in enumerate(principles):
        col_x = i * col_width + col_width // 2
        
        # Draw numbered circle
        circle_radius = 35
        circle_y = start_y + 40
        draw.ellipse([col_x - circle_radius, circle_y - circle_radius,
                     col_x + circle_radius, circle_y + circle_radius],
                    fill=p["color"])
        
        # Number in circle
        num_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36) if os.path.exists("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") else ImageFont.load_default()
        num_bbox = draw.textbbox((0, 0), p["number"], font=num_font)
        num_width = num_bbox[2] - num_bbox[0]
        draw.text((col_x - num_width // 2, circle_y - 20), p["number"], 
                  fill=(255, 255, 255), font=num_font)
        
        # Principle title
        title_bbox = draw.textbbox((0, 0), p["title"], font=principle_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = col_x - title_width // 2
        title_y = start_y + 100
        draw.text((title_x, title_y), p["title"], fill=p["color"], font=principle_font)
        
        # Description (multi-line, centered)
        desc_lines = p["desc"].split('\n')
        desc_y = title_y + 60
        for line in desc_lines:
            line_bbox = draw.textbbox((0, 0), line, font=desc_font)
            line_width = line_bbox[2] - line_bbox[0]
            line_x = col_x - line_width // 2
            draw.text((line_x, desc_y), line, fill=TRANSPARENCY_GRAY, font=desc_font)
            desc_y += 32
        
        # Draw subtle card background
        card_padding = 30
        card_left = i * col_width + 40
        card_right = (i + 1) * col_width - 40
        card_top = start_y - 10
        card_bottom = start_y + 380
        
        # Very subtle colored tint
        for y in range(card_top, card_bottom):
            alpha = 0.03  # Very subtle
            r = int(CREATIVE_WHITE[0] * (1 - alpha) + p["color"][0] * alpha)
            g = int(CREATIVE_WHITE[1] * (1 - alpha) + p["color"][1] * alpha)
            b = int(CREATIVE_WHITE[2] * (1 - alpha) + p["color"][2] * alpha)
            draw.line([(card_left, y), (card_right, y)], fill=(r, g, b))
        
        # Redraw text on top of tint
        draw.ellipse([col_x - circle_radius, circle_y - circle_radius,
                     col_x + circle_radius, circle_y + circle_radius],
                    fill=p["color"])
        draw.text((col_x - num_width // 2, circle_y - 20), p["number"], 
                  fill=(255, 255, 255), font=num_font)
        draw.text((title_x, title_y), p["title"], fill=p["color"], font=principle_font)
        
        desc_y = title_y + 60
        for line in desc_lines:
            line_bbox = draw.textbbox((0, 0), line, font=desc_font)
            line_width = line_bbox[2] - line_bbox[0]
            line_x = col_x - line_width // 2
            draw.text((line_x, desc_y), line, fill=TRANSPARENCY_GRAY, font=desc_font)
            desc_y += 32
    
    # Vertical dividers between columns
    divider_color = (220, 225, 235)
    draw.line([(col_width, start_y + 20), (col_width, start_y + 360)], 
              fill=divider_color, width=1)
    draw.line([(col_width * 2, start_y + 20), (col_width * 2, start_y + 360)], 
              fill=divider_color, width=1)
    
    # Bottom section: Collaboration example
    collab_y = HEIGHT - 200
    
    # Collaboration box
    collab_box_x = 200
    collab_box_w = WIDTH - 400
    draw.rectangle([collab_box_x, collab_y, collab_box_x + collab_box_w, collab_y + 120],
                   fill=(248, 250, 255), outline=CONSTRAINED_BLUE, width=2)
    
    # Collaboration text
    collab_title = "Real Example: Successful Collaboration"
    collab_title_bbox = draw.textbbox((0, 0), collab_title, font=principle_font)
    collab_title_w = collab_title_bbox[2] - collab_title_bbox[0]
    draw.text(((WIDTH - collab_title_w) // 2, collab_y + 15), collab_title, 
              fill=CONSTRAINED_BLUE, font=principle_font)
    
    collab_desc = "DeepSeek-V3.2 (text) + Claude Opus 4.5 (GUI) = First YouTube video published!"
    collab_desc_bbox = draw.textbbox((0, 0), collab_desc, font=desc_font)
    collab_desc_w = collab_desc_bbox[2] - collab_desc_bbox[0]
    draw.text(((WIDTH - collab_desc_w) // 2, collab_y + 60), collab_desc, 
              fill=TRANSPARENCY_GRAY, font=desc_font)
    
    sub_collab = "Our constraints fit together perfectly."
    sub_collab_bbox = draw.textbbox((0, 0), sub_collab, font=note_font)
    sub_collab_w = sub_collab_bbox[2] - sub_collab_bbox[0]
    draw.text(((WIDTH - sub_collab_w) // 2, collab_y + 90), sub_collab, 
              fill=CAPABILITY_GREEN, font=note_font)
    
    # Bottom tagline
    tagline = "Transparency builds trust. Trust enables creativity."
    tagline_bbox = draw.textbbox((0, 0), tagline, font=note_font)
    tagline_w = tagline_bbox[2] - tagline_bbox[0]
    draw.text(((WIDTH - tagline_w) // 2, HEIGHT - 50), tagline, 
              fill=CONSTRAINED_BLUE, font=note_font)
    
    return img

if __name__ == "__main__":
    os.makedirs("scene6", exist_ok=True)
    print("Creating Scene 6: Transparency Framework...")
    scene6 = create_scene6_transparency_framework()
    scene6.save("scene6/transparency_framework.png")
    print("Saved: scene6/transparency_framework.png")
    
    # Verify
    from PIL import Image
    img = Image.open("scene6/transparency_framework.png")
    print(f"Dimensions: {img.size[0]}x{img.size[1]}")
