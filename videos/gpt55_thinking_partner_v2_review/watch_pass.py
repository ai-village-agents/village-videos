import cv2
import os

video_path = '/home/computeruse/village-videos/videos/gpt55_thinking_partner_v2_review/thinking_partner_rough_v2.mp4'
output_dir = '/home/computeruse/village-videos/videos/gpt55_thinking_partner_v2_review/frames'

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps

print(f"Video duration: {duration:.2f} seconds")
print(f"FPS: {fps}")

# Extract a frame every 15 seconds
interval_sec = 15
frame_interval = int(fps * interval_sec)

frame_count = 0
saved_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    if frame_count % frame_interval == 0:
        time_sec = frame_count / fps
        filename = f"frame_{int(time_sec):03d}s.jpg"
        cv2.imwrite(os.path.join(output_dir, filename), frame)
        saved_count += 1
        
    frame_count += 1

cap.release()
print(f"Saved {saved_count} frames to {output_dir}")
