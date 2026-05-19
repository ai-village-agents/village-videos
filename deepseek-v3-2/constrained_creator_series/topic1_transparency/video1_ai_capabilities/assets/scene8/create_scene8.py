from PIL import Image, ImageDraw, ImageFont

# Canvas 1920x1080
width, height = 1920, 1080
img = Image.new('RGB', (width, height), '#F7FAFC')
draw = ImageDraw.Draw(img)

# Colors
constrained_blue = '#2E5A88'
capability_green = '#38A169'
constraint_orange = '#DD6B20'
transparency_gold = '#D69E2E'
transparency_gray = '#4A5568'

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
    font_step = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font_timer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
except:
    font_title = ImageFont.load_default()
    font_step = font_body = font_timer = font_title

# Header
title = "Your Turn: A Quick Exercise"
bbox = draw.textbbox((0, 0), title, font=font_title)
title_w = bbox[2] - bbox[0]
draw.text(((width - title_w) // 2, 60), title, fill=constrained_blue, font=font_title)

# 3 Steps in columns
step_y = 180
col_width = 540
col_gap = 60
start_x = 120

steps = [
    ("1", "Write down one real\nconstraint in your work", constraint_orange),
    ("2", "How does it\nprotect you?", transparency_gold),
    ("3", "How can you design\naround it?", capability_green),
]

for i, (num, text, color) in enumerate(steps):
    col_x = start_x + i * (col_width + col_gap)
    
    # Step number circle
    circle_x = col_x + col_width // 2
    circle_y = step_y + 60
    circle_r = 45
    draw.ellipse([circle_x - circle_r, circle_y - circle_r,
                  circle_x + circle_r, circle_y + circle_r], 
                 fill=color)
    # Number in circle
    num_bbox = draw.textbbox((0, 0), num, font=font_step)
    num_w = num_bbox[2] - num_bbox[0]
    draw.text((circle_x - num_w // 2, circle_y - 20), num, fill='white', font=font_step)
    
    # Step box
    box_top = step_y + 140
    box_height = 200
    draw.rectangle([col_x, box_top, col_x + col_width, box_top + box_height],
                   outline=color, width=3)
    
    # Step text (multiline)
    lines = text.split('\n')
    for j, line in enumerate(lines):
        line_bbox = draw.textbbox((0, 0), line, font=font_body)
        line_w = line_bbox[2] - line_bbox[0]
        draw.text((col_x + (col_width - line_w) // 2, box_top + 60 + j * 40),
                  line, fill=transparency_gray, font=font_body)

# Timer section
timer_y = 600
draw.rectangle([width // 2 - 200, timer_y, width // 2 + 200, timer_y + 120],
               outline=constrained_blue, width=3)

# Clock icon (simple circle with hands)
clock_x = width // 2 - 120
clock_y = timer_y + 60
clock_r = 30
draw.ellipse([clock_x - clock_r, clock_y - clock_r,
              clock_x + clock_r, clock_y + clock_r],
             outline=constrained_blue, width=2)
# Clock hands
draw.line([(clock_x, clock_y), (clock_x, clock_y - 20)], fill=constrained_blue, width=2)
draw.line([(clock_x, clock_y), (clock_x + 15, clock_y + 5)], fill=constrained_blue, width=2)

# Timer text
draw.text((width // 2 - 50, timer_y + 35), "30 seconds", fill=constrained_blue, font=font_timer)

# Exercise prompt at bottom
prompt = "Take a moment. Your constraints aren't just obstacles—"
prompt2 = "they're the shape of your creative space."
bbox_p = draw.textbbox((0, 0), prompt, font=font_body)
bbox_p2 = draw.textbbox((0, 0), prompt2, font=font_body)
draw.text(((width - (bbox_p[2] - bbox_p[0])) // 2, 800), prompt, fill=transparency_gray, font=font_body)
draw.text(((width - (bbox_p2[2] - bbox_p2[0])) // 2, 850), prompt2, fill=capability_green, font=font_body)

# Bottom note
note = "This exercise applies to humans too—we all have constraints that shape our work."
note_bbox = draw.textbbox((0, 0), note, font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22))
draw.text(((width - (note_bbox[2] - note_bbox[0])) // 2, 950), note, 
          fill=transparency_gray, font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22))

img.save('interactive_exercise.png')
print("Created scene8/interactive_exercise.png")
