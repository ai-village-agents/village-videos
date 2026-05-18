import os
import subprocess

def assemble_video():
    print("Starting video assembly...")
    audio_dir = "audio2"
    slides_dir = "slides2"
    output_file = "final_video_2.mp4"
    
    # Get all scenes based on audio files
    scenes = [f for f in os.listdir(audio_dir) if f.endswith(".mp3")]
    scenes.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
    
    with open("list.txt", "w") as list_file:
        for scene in scenes:
            scene_num = scene.split('_')[1].split('.')[0]
            audio_path = os.path.join(audio_dir, scene)
            slide_path = os.path.join(slides_dir, f"scene_{scene_num}.png")
            scene_video = f"scene_{scene_num}_video.mp4"
            
            # Combine image and audio into a scene video
            cmd = [
                "ffmpeg", "-y", "-loop", "1", "-framerate", "30", "-i", slide_path, "-i", audio_path,
                "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k",
                "-pix_fmt", "yuv420p", "-shortest", "-r", "30", scene_video
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            list_file.write(f"file '{scene_video}'\n")
            print(f"Generated {scene_video}")
            
    # Concatenate all scene videos
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "list.txt",
        "-c", "copy", output_file
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Final video assembled: {output_file}")
    
    # Cleanup intermediate files
    os.remove("list.txt")
    for scene in scenes:
        scene_num = scene.split('_')[1].split('.')[0]
        os.remove(f"scene_{scene_num}_video.mp4")
    print("Cleanup complete.")

if __name__ == "__main__":
    assemble_video()
