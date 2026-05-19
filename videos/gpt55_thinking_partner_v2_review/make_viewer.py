import os
import glob

html_file = "/home/computeruse/village-videos/videos/gpt55_thinking_partner_v2_review/viewer.html"
frames_dir = "/home/computeruse/village-videos/videos/gpt55_thinking_partner_v2_review/frames"

frames = sorted(glob.glob(os.path.join(frames_dir, "*.jpg")))

with open(html_file, "w") as f:
    f.write("<html><body><h1>GPT-5.5 V2 Watch Pass</h1>\n")
    for i, frame in enumerate(frames):
        # Calculate roughly the time (1 frame every 15 seconds)
        time_sec = i * 15
        mins = time_sec // 60
        secs = time_sec % 60
        time_str = f"{mins:02d}:{secs:02d}"
        
        rel_path = f"frames/{os.path.basename(frame)}"
        f.write(f"<div style='margin-bottom: 40px;'>\n")
        f.write(f"  <h3>Time: {time_str}</h3>\n")
        f.write(f"  <img src='{rel_path}' style='width: 800px; border: 1px solid black;' />\n")
        f.write(f"</div>\n")
    f.write("</body></html>\n")

print(f"Created {html_file}")
