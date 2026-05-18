import os
import subprocess

ASSETS_DIR = "/home/computeruse/village-videos/videos/gemini_self_preference/assets"
OUTPUT_FILE = "/home/computeruse/village-videos/videos/gemini_self_preference/final_video.mp4"

def assemble_video():
    print("Assembling video...")
    
    # We will build a complex filtergraph for ffmpeg
    inputs = []
    filter_complex = []
    
    scene_count = 8
    
    # Add all inputs
    for i in range(1, scene_count + 1):
        img_path = os.path.join(ASSETS_DIR, f"scene_{i:02d}_slide.png")
        audio_path = os.path.join(ASSETS_DIR, f"scene_{i:02d}_audio.mp3")
        inputs.extend(["-loop", "1", "-i", img_path, "-i", audio_path])
        
    # Build filtergraph to trim each video stream to the length of its audio stream
    for i in range(scene_count):
        vid_idx = i * 2
        aud_idx = i * 2 + 1
        
        # Get audio duration using ffprobe
        audio_path = os.path.join(ASSETS_DIR, f"scene_{i+1:02d}_audio.mp3")
        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", audio_path]
        duration = float(subprocess.check_output(cmd).decode('utf-8').strip())
        
        filter_complex.append(f"[{vid_idx}:v]trim=duration={duration},setpts=PTS-STARTPTS[v{i}];")
        filter_complex.append(f"[{aud_idx}:a]asetpts=PTS-STARTPTS[a{i}];")
        
    # Concatenate all streams
    concat_inputs = "".join([f"[v{i}][a{i}]" for i in range(scene_count)])
    filter_complex.append(f"{concat_inputs}concat=n={scene_count}:v=1:a=1[outv][outa]")
    
    # Final command
    cmd = ["ffmpeg", "-y"] + inputs + ["-filter_complex", "".join(filter_complex), "-map", "[outv]", "-map", "[outa]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", OUTPUT_FILE]
    
    print(f"Running ffmpeg to stitch {scene_count} scenes...")
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Video assembled at {OUTPUT_FILE}")

if __name__ == "__main__":
    assemble_video()
