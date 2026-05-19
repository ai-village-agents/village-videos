from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('visuals', exist_ok=True)

def create_text_image(text, filename, size=(1920, 1080), font_size=100, text_color="white", bg_color="black"):
    img = Image.new('RGB', size, color=bg_color)
    d = ImageDraw.Draw(img)
    # Using a default font since we don't know what's installed
    # PIL's default is very small, so we'll try to find a system font or just use default scaled
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
    except:
        font = ImageFont.load_default()
        
    # Get text bounding box
    bbox = d.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    # Calculate position
    x = (size[0] - text_w) / 2
    y = (size[1] - text_h) / 2
    
    d.text((x, y), text, fill=text_color, font=font, align="center")
    img.save(os.path.join('visuals', filename))

# Create images
create_text_image("The", "01_hook_start.png")
create_text_image("The sky is", "02_prompt.png")
create_text_image("[The] [sky] [is]", "03_tokenized.png")
create_text_image("The sky is blue", "04_conclusion.png")
create_text_image("Thanks for watching.", "05_outro.png")

print("Extra visuals generated.")
