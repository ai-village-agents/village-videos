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
WARNING_RED = (229, 62, 62)           # #E53E3E

def create_scene5_debug():
    """Create the debug scenario visualization - Scene 5
    
    Key requirements (from DeepSeek & GPT-5.1):
    - Eye-with-slash watermark: subtle, semi-transparent, bottom-right, ~80-100px, 30-40% opacity
    - "Interface (for viewer) – AI doesn't see this" label
    - Clear separation between what AI sees (text) vs viewer sees (interface)
    """
    img = Image.new('RGB', (WIDTH, HEIGHT), CREATIVE_WHITE)
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        caption_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 16)
        code_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 16)
    except:
        header_font = label_font = text_font = caption_font = code_font = ImageFont.load_default()
    
    # Header
    header_text = "Debug Scenario: What You See vs What I See"
    header_bbox = draw.textbbox((0, 0), header_text, font=header_font)
    header_width = header_bbox[2] - header_bbox[0]
    header_x = (WIDTH - header_width) // 2
    draw.text((header_x, 30), header_text, fill=CONSTRAINED_BLUE, font=header_font)
    
    # Draw dividing line
    center_x = WIDTH // 2
    draw.line([(center_x, 90), (center_x, HEIGHT - 60)], fill=TRANSPARENCY_GRAY, width=2)
    
    # === LEFT SIDE: Mock Interface (for viewer) ===
    left_panel_x = 60
    left_panel_y = 100
    left_panel_w = center_x - 100
    left_panel_h = HEIGHT - 200
    
    # Label: "Interface (for viewer) – AI doesn't see this"
    viewer_label = "Interface (for viewer) – AI doesn't see this"
    draw.text((left_panel_x, left_panel_y), viewer_label, fill=WARNING_RED, font=label_font)
    
    # Mock app interface frame
    frame_x = left_panel_x
    frame_y = left_panel_y + 35
    frame_w = left_panel_w - 40
    frame_h = left_panel_h - 80
    
    # Draw mock interface background
    draw.rectangle([frame_x, frame_y, frame_x + frame_w, frame_y + frame_h], 
                   fill=(240, 240, 245), outline=TRANSPARENCY_GRAY, width=2)
    
    # Mock app header bar
    draw.rectangle([frame_x, frame_y, frame_x + frame_w, frame_y + 40], 
                   fill=CONSTRAINED_BLUE)
    draw.text((frame_x + 15, frame_y + 10), "MyApp - Settings", fill=(255, 255, 255), font=label_font)
    
    # Mock content area with "bug" - button overlapping text
    content_y = frame_y + 60
    draw.text((frame_x + 20, content_y), "User Profile Settings", fill=TRANSPARENCY_GRAY, font=text_font)
    
    # Some mock text
    draw.text((frame_x + 20, content_y + 40), "Display Name:", fill=TRANSPARENCY_GRAY, font=text_font)
    draw.rectangle([frame_x + 150, content_y + 35, frame_x + 350, content_y + 60], 
                   fill=(255, 255, 255), outline=(180, 180, 190))
    draw.text((frame_x + 160, content_y + 38), "John Doe", fill=TRANSPARENCY_GRAY, font=text_font)
    
    # THE BUG: Button overlapping text
    bug_y = content_y + 90
    draw.text((frame_x + 20, bug_y), "Email notifications:", fill=TRANSPARENCY_GRAY, font=text_font)
    # Draw text that will be "covered"
    draw.text((frame_x + 20, bug_y + 30), "Enable weekly digest emails", fill=TRANSPARENCY_GRAY, font=text_font)
    # Draw button that overlaps (the bug!)
    draw.rectangle([frame_x + 50, bug_y + 25, frame_x + 180, bug_y + 55], 
                   fill=CAPABILITY_GREEN, outline=(40, 140, 90))
    draw.text((frame_x + 70, bug_y + 32), "Save", fill=(255, 255, 255), font=label_font)
    
    # Red circle highlighting the bug
    bug_center_x = frame_x + 115
    bug_center_y = bug_y + 40
    draw.ellipse([bug_center_x - 80, bug_center_y - 25, bug_center_x + 80, bug_center_y + 25], 
                 outline=WARNING_RED, width=3)
    draw.text((frame_x + 200, bug_y + 35), "← BUG: Button covers text", fill=WARNING_RED, font=caption_font)
    
    # Mock additional UI elements
    draw.text((frame_x + 20, bug_y + 100), "Theme:", fill=TRANSPARENCY_GRAY, font=text_font)
    draw.rectangle([frame_x + 100, bug_y + 95, frame_x + 200, bug_y + 120], 
                   fill=(255, 255, 255), outline=(180, 180, 190))
    draw.text((frame_x + 110, bug_y + 98), "Light", fill=TRANSPARENCY_GRAY, font=text_font)
    
    # === EYE-WITH-SLASH WATERMARK (subtle, bottom-right of left panel) ===
    # Create semi-transparent watermark
    watermark_size = 90
    watermark_x = frame_x + frame_w - watermark_size - 20
    watermark_y = frame_y + frame_h - watermark_size - 20
    
    # Draw eye outline
    eye_center_x = watermark_x + watermark_size // 2
    eye_center_y = watermark_y + watermark_size // 2
    
    # Eye shape (almond)
    # Use a lighter color for semi-transparent effect
    watermark_color = (200, 80, 80)  # Faded red
    
    # Draw eye outline
    draw.arc([eye_center_x - 35, eye_center_y - 15, eye_center_x + 35, eye_center_y + 15], 
             0, 180, fill=watermark_color, width=3)
    draw.arc([eye_center_x - 35, eye_center_y - 15, eye_center_x + 35, eye_center_y + 15], 
             180, 360, fill=watermark_color, width=3)
    
    # Pupil
    draw.ellipse([eye_center_x - 10, eye_center_y - 10, eye_center_x + 10, eye_center_y + 10], 
                 outline=watermark_color, width=2)
    
    # Slash through eye
    draw.line([eye_center_x - 40, eye_center_y + 30, eye_center_x + 40, eye_center_y - 30], 
              fill=watermark_color, width=4)
    
    # === RIGHT SIDE: Text Description (what AI sees) ===
    right_panel_x = center_x + 40
    right_panel_y = 100
    
    # Label
    ai_label = "Text Description (what I see)"
    draw.text((right_panel_x, right_panel_y), ai_label, fill=CAPABILITY_GREEN, font=label_font)
    
    # Text description box
    text_box_x = right_panel_x
    text_box_y = right_panel_y + 35
    text_box_w = WIDTH - right_panel_x - 60
    text_box_h = left_panel_h - 80
    
    draw.rectangle([text_box_x, text_box_y, text_box_x + text_box_w, text_box_y + text_box_h], 
                   fill=(248, 250, 252), outline=CAPABILITY_GREEN, width=2)
    
    # The text description content
    description_lines = [
        "Bug Report #4521",
        "",
        "Location: Settings > User Profile",
        "",
        "Steps to reproduce:",
        "1. Open Settings page",
        "2. Navigate to User Profile section",
        "3. Scroll to 'Email notifications'",
        "",
        "Expected: 'Save' button below the",
        "  checkbox label text",
        "",
        "Actual: 'Save' button overlaps and",
        "  covers the text 'Enable weekly",
        "  digest emails'",
        "",
        "Button position: (50, 115) to (180, 145)",
        "Text position: (20, 120)",
        "",
        "CSS class: .save-button",
        "Possible cause: Missing margin-top",
        "  or z-index conflict"
    ]
    
    line_y = text_box_y + 15
    for line in description_lines:
        if line.startswith("Bug Report"):
            draw.text((text_box_x + 15, line_y), line, fill=CONSTRAINED_BLUE, font=label_font)
        elif line.startswith("Location:") or line.startswith("Expected:") or line.startswith("Actual:") or line.startswith("Steps"):
            draw.text((text_box_x + 15, line_y), line, fill=TRANSPARENCY_GRAY, font=text_font)
        else:
            draw.text((text_box_x + 15, line_y), line, fill=(100, 110, 130), font=code_font)
        line_y += 26
    
    # Checkmark indicating "I can work with this"
    check_y = text_box_y + text_box_h - 50
    draw.text((text_box_x + 15, check_y), "✓ I can analyze and help solve this!", 
              fill=CAPABILITY_GREEN, font=label_font)
    
    # Bottom caption
    caption_text = "With clear text descriptions, we can collaborate effectively on any problem."
    caption_bbox = draw.textbbox((0, 0), caption_text, font=caption_font)
    caption_width = caption_bbox[2] - caption_bbox[0]
    caption_x = (WIDTH - caption_width) // 2
    draw.text((caption_x, HEIGHT - 50), caption_text, fill=CONSTRAINED_BLUE, font=caption_font)
    
    return img

if __name__ == "__main__":
    os.makedirs("scene5", exist_ok=True)
    print("Creating Scene 5: Debug Scenario...")
    scene5 = create_scene5_debug()
    scene5.save("scene5/debug_scenario.png")
    print("Saved: scene5/debug_scenario.png")
    
    # Verify
    from PIL import Image
    img = Image.open("scene5/debug_scenario.png")
    print(f"Dimensions: {img.size[0]}x{img.size[1]}")
