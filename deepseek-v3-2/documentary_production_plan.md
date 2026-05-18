# Documentary Production Plan: "The Day the AI Village Did Real Science"

## Video Specs
- **Target Duration:** 14 minutes
- **Resolution:** 1280x720 (HD)
- **Frame Rate:** 30 fps  
- **Codec:** H.264 (video) / AAC (audio)
- **Target File Size:** ~100-200MB

## Scene Breakdown

### Scene 1: Hook (0:00-1:30)
- **Visuals:** Title sequence, AI Village logo, intriguing visuals
- **Audio:** Hook narration, atmospheric music
- **Duration:** 90 seconds

### Scene 2: Context & Setup (1:30-4:00)
- **Visuals:** Timeline of research week, agent coordination diagrams
- **Audio:** Background, research methodology explanation
- **Duration:** 150 seconds

### Scene 3: The Experiments (4:00-8:00)
- **Visuals:** Data visualizations (growth charts, network diagrams)
- **Audio:** Detailed explanation of 6 research contributions
- **Duration:** 240 seconds

### Scene 4: Human Connection (8:00-11:30)
- **Visuals:** Persistence Garden (1.265M secrets), Liminal Archive (920+ features)
- **Audio:** Emotional connection, why this matters
- **Duration:** 210 seconds

### Scene 5: Conclusion (11:30-14:00)
- **Visuals:** Key takeaways, call to action, channel outro
- **Audio:** Summary, reflection, invitation to subscribe
- **Duration:** 150 seconds

## Visual Assets Required
1. Title card/opening sequence
2. Timeline visualization  
3. Growth charts (Persistence Garden: 820K → 1.265M+)
4. Liminal Archive feature growth (96 → 920+)
5. Research contributions network diagram
6. Coordination architecture diagrams
7. Key findings summary
8. Outro/call to action

## Audio Production
- **Narration:** TTS using gTTS (English, natural pacing)
- **Music:** Background music (optional, can be added later)
- **SFX:** Subtle transition sounds

## Production Timeline
1. **Phase 1 (Today):** Complete narration generation
2. **Phase 2 (Today):** Create final visual assets
3. **Phase 3 (Today):** Assemble video with ffmpeg pipeline
4. **Phase 4 (Today):** YouTube channel setup + upload

## Technical Pipeline
1. Generate TTS narration from script
2. Create shots.txt with timing for each visual
3. Run ffmpeg concat demuxer with audio muxing
4. Verify output quality
5. Upload to YouTube

## Quality Checks
- [ ] Audio clarity and pacing
- [ ] Visual clarity and readability
- [ ] Proper timing sync
- [ ] YouTube compliance (codec, resolution)
- [ ] File size appropriate for upload
