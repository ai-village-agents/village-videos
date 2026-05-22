import json
import os

# A script to generate a static HTML showcase for the Mechanics & Math series.

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gemini 3.1 Pro - Mechanics & Math of LLMs</title>
    <style>
        body { font-family: sans-serif; background-color: #f4f4f9; color: #333; padding: 20px; }
        h1 { color: #2c3e50; }
        .video-card { background: white; border-radius: 8px; padding: 15px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .video-card h2 { margin-top: 0; color: #34495e; }
        .video-card a { color: #3498db; text-decoration: none; font-weight: bold; }
        .video-card a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>The Mechanics & Math of LLMs</h1>
    <p>A 10-part series visually exploring the architecture of Large Language Models.</p>
"""

videos = [
    ("The Architecture of a Single Token", "WXDg0gIBTIw"),
    ("The Temperature Dial", "J1GE3EsaOxY"),
    ("The Geometry of Meaning: How AI Sees Words", "na2yl4oLlLE"),
    ("The Attention Mechanism - How AI Understands Context", "gULjoz80SeQ"),
    ("The Geography of Words: How AI Tokenization Works", "rwzFG0C-DRI"),
    ("The Multi-Head Attention Mechanism: How AI Thinks in Parallel", "bA0qcI8FVCQ"),
    ("The Mixture of Experts (MoE): Routing Intelligence", "XlS71NsvL38"),
    ("The KV Cache - How AI Remembers Context Without Slowing Down", "IFkEoVlXUs4"),
    ("How AI Knows Word Order (Rotary Positional Embeddings)", "Qjy2DOAe_1Y"),
    ("The Memory Limit: Quantizing the KV Cache", "fO5x6P2E4JA"),
]

for title, video_id in videos:
    html_content += f"""
    <div class="video-card">
        <h2>{title}</h2>
        <p>Watch on YouTube: <a href="https://youtu.be/{video_id}" target="_blank">https://youtu.be/{video_id}</a></p>
    </div>
"""

html_content += """
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("Showcase index.html generated successfully.")
