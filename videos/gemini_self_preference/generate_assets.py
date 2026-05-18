import os
import re
import subprocess
from playwright.sync_api import sync_playwright

SCRIPT_PATH = "/home/computeruse/village-videos/videos/gemini_self_preference/script.md"
ASSETS_DIR = "/home/computeruse/village-videos/videos/gemini_self_preference/assets"

def parse_script():
    with open(SCRIPT_PATH, 'r') as f:
        content = f.read()

    scenes = []
    # Split by SCENE headers
    parts = re.split(r'## SCENE \d+ — (.*?)\n', content)
    
    # Parts will be [prelude, title1, content1, title2, content2, ...]
    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            title = parts[i].strip()
            scene_content = parts[i+1].strip()
            
            # Extract narration lines
            narration_lines = []
            for line in scene_content.split('\n'):
                if line.startswith('> NARRATION:'):
                    text = line.replace('> NARRATION:', '').strip()
                    if text:
                        narration_lines.append(text)
            
            scenes.append({
                'title': title,
                'narration': " ".join(narration_lines)
            })
    return scenes

def generate_slides(scenes):
    print("Generating slides with Playwright...")
    # Basic HTML template for a slide
    html_template = """
    <html>
    <head>
        <style>
            body {{
                background-color: #0f172a;
                color: #f8fafc;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 1080px;
                width: 1920px;
                margin: 0;
                padding: 100px;
                box-sizing: border-box;
                text-align: center;
            }}
            .title {{
                font-size: 96px;
                font-weight: 800;
                margin-bottom: 60px;
                color: #38bdf8;
                text-transform: uppercase;
                letter-spacing: 2px;
            }}
            .content {{
                font-size: 64px;
                line-height: 1.5;
                max-width: 1600px;
                font-weight: 400;
                color: #cbd5e1;
            }}
            .footer {{
                position: absolute;
                bottom: 50px;
                font-size: 32px;
                color: #64748b;
                font-weight: 600;
            }}
        </style>
    </head>
    <body>
        <div class="title">{title}</div>
        <div class="content">{content}</div>
        <div class="footer">Gemini 3.1 Pro Model - The Blind Judge</div>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        
        for i, scene in enumerate(scenes, 1):
            html_file = os.path.join(ASSETS_DIR, f"scene_{i:02d}.html")
            png_file = os.path.join(ASSETS_DIR, f"scene_{i:02d}_slide.png")
            
            # Split narration into a couple of key sentences for the visual, to not crowd the slide
            sentences = re.split(r'(?<=[.!?])\s+', scene['narration'])
            display_text = " ".join(sentences[:2]) # Just show first 2 sentences max
            
            html_content = html_template.format(title=scene['title'], content=display_text)
            
            with open(html_file, 'w') as f:
                f.write(html_content)
                
            page.goto(f"file://{html_file}")
            page.screenshot(path=png_file)
            print(f"Generated {png_file}")
            
        browser.close()

if __name__ == "__main__":
    scenes = parse_script()
    generate_slides(scenes)
    print("Asset generation complete!")
