import os
import re
import asyncio
from playwright.async_api import async_playwright

async def generate_assets():
    print("Starting asset generation for Video 2...")
    
    script_path = "script2.md"
    audio_dir = "audio2"
    slides_dir = "slides2"
    
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(slides_dir, exist_ok=True)
    
    with open(script_path, "r") as f:
        content = f.read()
        
    scenes = re.split(r"\[SCENE \d+:[^\]]+\]", content)[1:]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # 16:9 aspect ratio for YouTube
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        for i, scene in enumerate(scenes, 1):
            print(f"Processing Scene {i}...")
            
            # Extract narration
            narration_match = re.search(r"NARRATOR\s*(?:\(Voiceover\):)?\s*(.*?)(?=\n\n\[|$)", scene, re.DOTALL)
            if narration_match:
                narration = narration_match.group(1).strip()
                # Clean up newlines for TTS
                narration = " ".join(narration.split())
                # Escape double quotes for bash
                narration_escaped = narration.replace('"', '\\"')
                
                audio_file = os.path.join(audio_dir, f"scene_{i}.mp3")
                print(f"  Generating audio: {audio_file}")
                # Use edge-tts directly via system call
                os.system(f'edge-tts --voice en-US-JennyNeural --text "{narration_escaped}" --write-media {audio_file}')
            
            # Generate a visual (we'll capture the actual grid page)
            print("  Generating visual...")
            slide_file = os.path.join(slides_dir, f"scene_{i}.png")
            
            # Load the local grid.html
            grid_url = "file:///home/computeruse/gemini-interactive-world/grid.html"
            await page.goto(grid_url)
            
            # Wait for grid to render
            await page.wait_for_timeout(3000)
            
            # Take screenshots of grid.html as is for now since camera isn't globally exposed
            await page.screenshot(path=slide_file)
            
        await browser.close()
    print("Asset generation complete!")

if __name__ == "__main__":
    asyncio.run(generate_assets())
