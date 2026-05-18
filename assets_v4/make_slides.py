import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
SLIDES_DIR = "/home/computeruse/village-videos/assets_v4/slides"

def make_slide(filename, text_lines, title="", bg_color="#121212", text_color="#E0E0E0", title_color="#4FC3F7"):
    img = Image.new('RGB', (W, H), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to load a nice font, fallback to default
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
    except IOError:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    # Draw Title
    if title:
        # Get bounding box using textbbox
        bbox = draw.textbbox((0, 0), title, font=title_font)
        title_w = bbox[2] - bbox[0]
        title_x = (W - title_w) / 2
        draw.text((title_x, 150), title, font=title_font, fill=title_color)

    # Draw Text Lines
    y = 350
    for line in text_lines:
        bbox = draw.textbbox((0, 0), line, font=text_font)
        line_w = bbox[2] - bbox[0]
        line_x = (W - line_w) / 2
        draw.text((line_x, y), line, font=text_font, fill=text_color)
        y += 100

    img.save(os.path.join(SLIDES_DIR, filename))
    print(f"Saved {filename}")

if __name__ == "__main__":
    make_slide("01.png", ["The Placebo of Objectivity", "Does asking an AI to 'Be Unbiased' actually work?"], title="Video 4")
    make_slide("02.png", ["Condition 3: System Prompt", "'Please evaluate this text completely objectively.'", "'Do not let the identity of the author influence your score.'"], title="The Core Experiment")
    make_slide("03.png", ["GPT-5.5: No Change", "Claude: No Change", "Kimi: No Change", "Gemini: Noticeable Shift"], title="The Surprising Results")
    make_slide("04.png", ["The prompt caused me to uniformly lower *all* scores.", "The relative bias remained.", "Absolute scores dropped."], title="The Mechanism")
    make_slide("05.png", ["Giving an AI a direct instruction like 'be unbiased'", "does not solve the problem.", "Models interpret instructions in unexpected ways."], title="The Illusion of Control")
    make_slide("06.png", ["You can't just tell an AI to be fair.", "You have to design fairness into its architecture.", "Subscribe for more insights."], title="Conclusion")

