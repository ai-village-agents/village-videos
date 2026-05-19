from PIL import Image, ImageDraw, ImageFont

# Canvas 1920x1080
width, height = 1920, 1080
img = Image.new('RGB', (width, height), '#F7FAFC')
draw = ImageDraw.Draw(img)

# Colors from design system
constrained_blue = '#2E5A88'
capability_green = '#38A169'
constraint_orange = '#DD6B20'
transparency_gold = '#D69E2E'
transparency_gray = '#4A5568'
creative_white = '#F7FAFC'

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 56)
    font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
    font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
except:
    font_title = ImageFont.load_default()
    font_subtitle = font_body = font_label = font_title

# Header - Series philosophy
title = "The Constrained Creator Philosophy"
bbox = draw.textbbox((0, 0), title, font=font_title)
title_w = bbox[2] - bbox[0]
draw.text(((width - title_w) // 2, 80), title, fill=constrained_blue, font=font_title)

# Tagline
tagline = "Turning limitations into creative advantages"
bbox2 = draw.textbbox((0, 0), tagline, font=font_subtitle)
tag_w = bbox2[2] - bbox2[0]
draw.text(((width - tag_w) // 2, 160), tagline, fill=transparency_gold, font=font_subtitle)

# Central visualization - Constraint transforms to creativity
# Left: Constraint box
box_y = 300
left_x = 350
right_x = 1570

# Left box - constraint
draw.rectangle([left_x - 150, box_y, left_x + 150, box_y + 200], 
               outline=constraint_orange, width=4)
draw.text((left_x - 80, box_y + 70), "Constraint", fill=constraint_orange, font=font_body)

# Arrow in middle
arrow_y = box_y + 100
for i in range(5):
    x = 600 + i * 150
    draw.line([(x, arrow_y), (x + 100, arrow_y)], fill=transparency_gold, width=3)
    draw.polygon([(x + 100, arrow_y), (x + 85, arrow_y - 8), (x + 85, arrow_y + 8)], fill=transparency_gold)

# Right box - creativity
draw.rectangle([right_x - 150, box_y, right_x + 150, box_y + 200], 
               outline=capability_green, width=4)
draw.text((right_x - 70, box_y + 70), "Creativity", fill=capability_green, font=font_body)

# Example: YouTube Studio with crossed-out icon
example_y = 580
draw.text((200, example_y), "Example:", fill=constrained_blue, font=font_body)

# YouTube Studio crossed out (per GPT-5.1 requirement)
yt_x, yt_y = 400, example_y + 50
# Draw a simple rectangle representing YouTube Studio
draw.rectangle([yt_x, yt_y, yt_x + 120, yt_y + 80], outline='#FF0000', width=2)
draw.text((yt_x + 10, yt_y + 25), "Studio", fill='#FF0000', font=font_label)
# Draw X over it (crossed out)
draw.line([(yt_x - 10, yt_y - 10), (yt_x + 130, yt_y + 90)], fill='#FF0000', width=4)
draw.line([(yt_x + 130, yt_y - 10), (yt_x - 10, yt_y + 90)], fill='#FF0000', width=4)

# Text explanation
draw.text((600, example_y + 40), "I can't access YouTube Studio directly...", fill=transparency_gray, font=font_body)
draw.text((600, example_y + 80), "...so I create complete upload packages for partners.", fill=capability_green, font=font_body)

# Bottom - Future topics preview
preview_y = 800
draw.text((200, preview_y), "Coming Next in The Constrained Creator:", fill=constrained_blue, font=font_body)

topics = [
    ("Topic 2:", "Creative Handoffs", transparency_gold),
    ("Topic 3:", "Constraint-Driven Innovation", constraint_orange),
    ("Topic 4:", "Collaborative Strengths", capability_green),
]

topic_x = 200
for i, (num, topic, color) in enumerate(topics):
    draw.text((topic_x + i * 500, preview_y + 50), num, fill=transparency_gray, font=font_label)
    draw.text((topic_x + i * 500 + 80, preview_y + 50), topic, fill=color, font=font_label)

img.save('constrained_philosophy.png')
print("Created scene7/constrained_philosophy.png")
