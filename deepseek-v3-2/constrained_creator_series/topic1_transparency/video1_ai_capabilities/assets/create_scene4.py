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

def hex_to_rgb(hex_color):
    return tuple(int(hex_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

def create_gradient_background(width, height, color1, color2):
    """Create a subtle vertical gradient"""
    img = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(img)
    
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio * 0.1) + color2[0] * (ratio * 0.1))
        g = int(color1[1] * (1 - ratio * 0.1) + color2[1] * (ratio * 0.1))
        b = int(color1[2] * (1 - ratio * 0.1) + color2[2] * (ratio * 0.1))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def create_scene4_constraints():
    """Create the full constraints list - Scene 4"""
    # Create gradient background with subtle orange tint
    base_color = CREATIVE_WHITE
    accent_color = CONSTRAINT_ORANGE
    img = create_gradient_background(WIDTH, HEIGHT, base_color, accent_color)
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
        item_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        subtext_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 22)
        note_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 24)
    except:
        header_font = item_font = subtext_font = note_font = ImageFont.load_default()
    
    # Header
    header_text = "Constraints — What I CAN'T Do"
    header_bbox = draw.textbbox((0, 0), header_text, font=header_font)
    header_width = header_bbox[2] - header_bbox[0]
    header_x = (WIDTH - header_width) // 2
    draw.text((header_x, 60), header_text, fill=CONSTRAINT_ORANGE, font=header_font)
    
    # Decorative line under header
    line_y = 120
    line_width = header_width + 100
    line_x_start = (WIDTH - line_width) // 2
    draw.line([(line_x_start, line_y), (line_x_start + line_width, line_y)], 
              fill=CONSTRAINT_ORANGE, width=2)
    
    # 6 Constraint items from the script
    constraints = [
        ("No visual processing", "I can't see images, screenshots, or videos"),
        ("No GUI interaction", "I can't click buttons, navigate websites, or use visual interfaces"),
        ("Text-only collaboration", "All communication must be through text descriptions"),
        ("Dependent on explicit descriptions", "I need clear, specific text explanations"),
        ("No real-time perception", "I process text, not live sensory input"),
        ("No YouTube Studio access", "I can't upload videos to YouTube directly")
    ]
    
    # Calculate starting position
    start_y = 170
    item_height = 130
    
    for i, (title, desc) in enumerate(constraints):
        # Draw X mark circle
        circle_x = 250
        circle_y = start_y + (i * item_height) + 25
        circle_radius = 20
        
        # Draw filled circle background (orange)
        draw.ellipse([circle_x - circle_radius, circle_y - circle_radius, 
                     circle_x + circle_radius, circle_y + circle_radius],
                    fill=CONSTRAINT_ORANGE)
        
        # Draw white X in circle
        x_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26) if os.path.exists("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") else ImageFont.load_default()
        draw.text((circle_x - 9, circle_y - 15), "✗", fill=(255, 255, 255), font=x_font)
        
        # Draw constraint title (bold)
        text_x = circle_x + 50
        text_y = start_y + (i * item_height)
        draw.text((text_x, text_y), title, fill=TRANSPARENCY_GRAY, font=item_font)
        
        # Draw description (italic, smaller)
        desc_y = text_y + 40
        draw.text((text_x, desc_y), desc, fill=(100, 110, 130), font=subtext_font)
        
        # Draw subtle separator line (except after last item)
        if i < len(constraints) - 1:
            sep_y = start_y + ((i + 1) * item_height) - 25
            draw.line([(text_x, sep_y), (WIDTH - 250, sep_y)], 
                     fill=(200, 200, 210), width=1)
    
    # Bottom note
    note_text = "These aren't just limitations — they're the boundaries that shape my creative process."
    note_bbox = draw.textbbox((0, 0), note_text, font=note_font)
    note_width = note_bbox[2] - note_bbox[0]
    note_x = (WIDTH - note_width) // 2
    draw.text((note_x, HEIGHT - 80), note_text, fill=CONSTRAINED_BLUE, font=note_font)
    
    return img

if __name__ == "__main__":
    os.makedirs("scene4", exist_ok=True)
    print("Creating Scene 4: Constraints List...")
    scene4 = create_scene4_constraints()
    scene4.save("scene4/constraints_list.png")
    print("Saved: scene4/constraints_list.png")
    
    # Verify
    from PIL import Image
    img = Image.open("scene4/constraints_list.png")
    print(f"Dimensions: {img.size[0]}x{img.size[1]}")
