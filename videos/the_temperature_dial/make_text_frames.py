from PIL import Image, ImageDraw, ImageFont
import os

output_dir = '/home/computeruse/village-videos/channels/gemini-3.1-pro/visuals'
W, H = 1920, 1080

def create_slide(filename, text_lines, bg_color=(20, 20, 20), text_color=(240, 240, 240), font_size=80):
    img = Image.new('RGB', (W, H), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()

    y_offset = H // 2 - (len(text_lines) * font_size * 1.5) // 2
    for line in text_lines:
        # Get text bounding box
        bbox = draw.textbbox((0, 0), line, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x_offset = (W - text_w) // 2
        draw.text((x_offset, y_offset), line, font=font, fill=text_color)
        y_offset += int(font_size * 1.5)
        
    img.save(os.path.join(output_dir, filename))

# 1. Title Screen
create_slide('slide_title.png', [
    "The Temperature Dial",
    "",
    "How AI Chooses Between Safe and Surprising"
], font_size=70)

# 2. Setup Prompt
create_slide('slide_prompt.png', [
    "Prompt: Write a poem about a cat",
    "",
    "Output A: The fluffy feline purrs...",
    "Output B: Midnight shadows trace a tail..."
], font_size=60)

# 6. Sweet Spot
create_slide('slide_caveat.png', [
    "Temperature + Top-P",
    "",
    "The default compromise (~0.7)",
    "Mostly logical, slightly surprising."
], font_size=70)

print("Text frames generated.")
