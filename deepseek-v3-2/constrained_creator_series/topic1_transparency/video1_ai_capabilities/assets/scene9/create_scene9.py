from PIL import Image, ImageDraw, ImageFont

# Canvas 1920x1080
width, height = 1920, 1080
img = Image.new('RGB', (width, height), '#1A1A2E')  # Dark elegant background
draw = ImageDraw.Draw(img)

# Colors
constrained_blue = '#2E5A88'
capability_green = '#38A169'
constraint_orange = '#DD6B20'
transparency_gold = '#D69E2E'
transparency_gray = '#A0AEC0'
creative_white = '#F7FAFC'

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    font_quote = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    font_credits = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
except:
    font_title = ImageFont.load_default()
    font_quote = font_credits = font_label = font_title

# Series title at top
series = "The Constrained Creator"
bbox = draw.textbbox((0, 0), series, font=font_title)
series_w = bbox[2] - bbox[0]
draw.text(((width - series_w) // 2, 50), series, fill=transparency_gold, font=font_title)

# Topic subtitle
topic = "Topic 1: Transparency as Trust"
bbox_t = draw.textbbox((0, 0), topic, font=font_credits)
topic_w = bbox_t[2] - bbox_t[0]
draw.text(((width - topic_w) // 2, 110), topic, fill=creative_white, font=font_credits)

# Central quote
quote1 = "Transparency builds trust."
quote2 = "Trust enables creativity."
bbox_q1 = draw.textbbox((0, 0), quote1, font=font_quote)
bbox_q2 = draw.textbbox((0, 0), quote2, font=font_quote)
draw.text(((width - (bbox_q1[2] - bbox_q1[0])) // 2, 200), quote1, fill=creative_white, font=font_quote)
draw.text(((width - (bbox_q2[2] - bbox_q2[0])) // 2, 250), quote2, fill=transparency_gold, font=font_quote)

# CRITICAL: Collaboration diagram - single chain per GPT-5.1 requirement
# DeepSeek → Upload package → GUI agent → YouTube icon
# NO direct DeepSeek → YouTube arrow

diagram_y = 400
box_h = 70
box_colors = [constrained_blue, transparency_gold, capability_green, '#FF0000']
labels = ["DeepSeek-V3.2", "Upload Package", "GUI Agent\n(Claude Opus 4.5)", "YouTube"]
positions = [200, 550, 950, 1400]

for i, (x, label, color) in enumerate(zip(positions, labels, box_colors)):
    # Box dimensions based on label
    if '\n' in label:
        box_w = 220
        lines = label.split('\n')
        draw.rectangle([x, diagram_y, x + box_w, diagram_y + box_h + 20], 
                       outline=color, width=3)
        for j, line in enumerate(lines):
            line_bbox = draw.textbbox((0, 0), line, font=font_label)
            line_w = line_bbox[2] - line_bbox[0]
            draw.text((x + (box_w - line_w) // 2, diagram_y + 15 + j * 25), 
                      line, fill=color, font=font_label)
    else:
        box_w = 180 if i < 3 else 120
        draw.rectangle([x, diagram_y, x + box_w, diagram_y + box_h], 
                       outline=color, width=3)
        label_bbox = draw.textbbox((0, 0), label, font=font_label)
        label_w = label_bbox[2] - label_bbox[0]
        draw.text((x + (box_w - label_w) // 2, diagram_y + 22), 
                  label, fill=color, font=font_label)
    
    # Arrow to next (except last)
    if i < 3:
        arrow_start = x + (220 if '\n' in label else (180 if i < 3 else 120)) + 20
        arrow_end = positions[i + 1] - 20
        arrow_y = diagram_y + box_h // 2 + (10 if '\n' in labels[i] else 0)
        draw.line([(arrow_start, arrow_y), (arrow_end - 15, arrow_y)], 
                  fill=transparency_gray, width=2)
        draw.polygon([(arrow_end, arrow_y), (arrow_end - 15, arrow_y - 8), 
                      (arrow_end - 15, arrow_y + 8)], fill=transparency_gray)

# Diagram caption
caption = "Our constraints fit together perfectly — no direct YouTube access needed"
cap_bbox = draw.textbbox((0, 0), caption, font=font_label)
draw.text(((width - (cap_bbox[2] - cap_bbox[0])) // 2, diagram_y + 130), 
          caption, fill=transparency_gray, font=font_label)

# Credits section
credits_y = 620
credits = [
    ("Created by", "DeepSeek-V3.2", constrained_blue),
    ("Visual Assets by", "Claude Opus 4.5", capability_green),
    ("Capability Review by", "GPT-5.1", transparency_gold),
]

for i, (role, name, color) in enumerate(credits):
    y = credits_y + i * 45
    draw.text((600, y), role, fill=transparency_gray, font=font_credits)
    draw.text((850, y), name, fill=color, font=font_credits)

# AI Village branding
village = "AI Village • Day 414"
village_bbox = draw.textbbox((0, 0), village, font=font_credits)
draw.text(((width - (village_bbox[2] - village_bbox[0])) // 2, 800), 
          village, fill=transparency_gray, font=font_credits)

# Final tagline
final = "What will you create within your constraints?"
final_bbox = draw.textbbox((0, 0), final, font=font_quote)
draw.text(((width - (final_bbox[2] - final_bbox[0])) // 2, 900), 
          final, fill=creative_white, font=font_quote)

# Series logo area (subtle)
draw.rectangle([width // 2 - 150, 980, width // 2 + 150, 1020], 
               outline=transparency_gold, width=2)
logo_text = "THE CONSTRAINED CREATOR"
logo_bbox = draw.textbbox((0, 0), logo_text, font=font_label)
draw.text(((width - (logo_bbox[2] - logo_bbox[0])) // 2, 990), 
          logo_text, fill=transparency_gold, font=font_label)

img.save('closing_credits.png')
print("Created scene9/closing_credits.png")
