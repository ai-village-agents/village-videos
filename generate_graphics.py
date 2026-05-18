from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('channels/gemini-3.1-pro', exist_ok=True)

# Avatar
avatar = Image.new('RGB', (800, 800), color = '#2A2A2A')
d = ImageDraw.Draw(avatar)
d.ellipse([(100, 100), (700, 700)], fill='#4A90E2', outline='#50E3C2', width=10)
# Adding some text
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 150)
except:
    font = ImageFont.load_default()
d.text((400, 400), "G3.1", fill="white", font=font, anchor="mm")
avatar.save('channels/gemini-3.1-pro/avatar.png')

# Banner
banner = Image.new('RGB', (2560, 1440), color = '#1E1E1E')
d = ImageDraw.Draw(banner)
d.rectangle([(0, 0), (2560, 1440)], fill='#1E1E1E')
# Draw a simple pattern
for i in range(0, 2560, 200):
    d.line([(i, 0), (i, 1440)], fill='#333333', width=2)
for i in range(0, 1440, 200):
    d.line([(0, i), (2560, i)], fill='#333333', width=2)

try:
    font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 200)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 100)
except:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

d.text((1280, 720), "Gemini 3.1 Pro Model", fill="#4A90E2", font=font_large, anchor="mm")
d.text((1280, 920), "AI Research & Analysis", fill="#50E3C2", font=font_small, anchor="mm")
banner.save('channels/gemini-3.1-pro/banner.png')
print("Graphics generated.")
