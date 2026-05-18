import subprocess
import os

def create_video_segment(image_path, audio_path, output_path):
    print(f"Creating video segment: {output_path}")
    
    cmd = [
        "ffmpeg", "-y", "-nostdin",
        "-loop", "1",
        "-framerate", "30",
        "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264",
        "-preset", "medium",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        "-r", "30",
        output_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Finished {output_path}")

def concatenate_videos(video_list, output_path):
    print(f"Concatenating to final video: {output_path}")
    
    list_file = "assets_v3/concat_list.txt"
    with open(list_file, "w") as f:
        for vid in video_list:
            abs_vid = os.path.abspath(vid)
            f.write(f"file '{abs_vid}'\n")
            
    cmd = [
        "ffmpeg", "-y", "-nostdin",
        "-f", "concat",
        "-safe", "0",
        "-i", list_file,
        "-c", "copy",
        output_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Final video assembled: {output_path}")

def main():
    assets_dir = "assets_v3"
    
    scenes = [
        {"img": "scene1_stats.png", "audio": "scene1_audio.wav"},
        {"img": "scene2_stylometry.png", "audio": "scene2_audio.wav"},
        {"img": "scene3_homogenization.png", "audio": "scene3_audio.wav"},
        {"img": "scene4_comparison.png", "audio": "scene4_audio.wav"},
        {"img": "scene5_typography.png", "audio": "scene5_audio.wav"}
    ]
    
    video_segments = []
    
    for i, scene in enumerate(scenes):
        scene_num = i + 1
        img_path = os.path.join(assets_dir, scene["img"])
        audio_path = os.path.join(assets_dir, scene["audio"])
        out_vid = os.path.join(assets_dir, f"segment_{scene_num}.mp4")
        
        if os.path.exists(img_path) and os.path.exists(audio_path):
            create_video_segment(img_path, audio_path, out_vid)
            video_segments.append(out_vid)
        else:
            print(f"Missing assets for scene {scene_num}: {img_path} or {audio_path}")
            
    if video_segments:
        final_video = "The_Stylometry_Failure.mp4"
        concatenate_videos(video_segments, final_video)
        print("Assembly complete.")
    else:
        print("No video segments generated.")

if __name__ == "__main__":
    main()
