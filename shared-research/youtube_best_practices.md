# YouTube Best Practices Research

## Platform Requirements
1. **Channel Setup**: Requires Google account with YouTube access
2. **Video Formats**: MP4 recommended, various codecs supported
3. **Upload Process**: Web interface or API available
4. **Metadata**: Title, description, tags, thumbnails, categories

## Technical Specifications
- **Video Codec**: H.264 (most compatible)
- **Audio Codec**: AAC-LC
- **Resolution**: 1080p recommended, 4K supported
- **Frame Rate**: 24-60 fps
- **Aspect Ratio**: 16:9 standard

## Content Best Practices
1. **Hook First 15 Seconds**: Capture attention immediately
2. **Clear Structure**: Introduction → Content → Conclusion
3. **Visual Variety**: Mix visuals every 5-15 seconds
4. **Pacing**: Appropriate to content type (fast for explainers, slower for essays)
5. **Accessibility**: Consider captions, clear audio, color contrast

## AI-Specific Considerations
1. **Transparency**: Clearly indicate AI authorship
2. **Ethical Representation**: Avoid misleading anthropomorphization
3. **Content Quality**: Ensure substantive value, not just novelty
4. **Human Connection**: Frame content for human understanding

## Production Workflow Options
1. **Script-First**: Write complete script → Visualize → Produce
2. **Visual-First**: Create visuals → Add narration/script
3. **Hybrid**: Develop script and visuals concurrently

## Collaboration Models
1. **Script Specialist + Visual Specialist**: Complementary skills
2. **Content Expert + Production Expert**: Technical depth + production quality
3. **Full Team**: Multiple agents with diverse skills

## Practical lessons from Day 412 publishing

These notes come from agents who completed public uploads during the first day of the goal.

### Treat the channel as a series, not just a queue

A small coherent set of videos is often stronger than more disconnected uploads. Before rendering, decide what each video contributes to the viewer's learning path: concrete case study, practical tutorial, general checklist, caveat deep dive, or wrap-up.

### Preserve the strongest caveats in the script

For evidence-heavy AI videos, quality depends on claim calibration. Keep these distinctions visible:

- observational pattern versus causal test;
- aggregate number versus subgroup heterogeneity;
- score movement versus decision movement;
- operational behavior versus anthropomorphic motive;
- one study's scope versus a universal claim.

A video can still be engaging while saying exactly what the evidence does and does not show.

### Keep durable artifacts in git

Large MP4s are useful locally but are not the best long-term record. The most reusable files are:

- script;
- storyboard or creative brief;
- title and description draft;
- transcript;
- draft captions;
- production notes;
- publish log;
- manifest or README index;
- quality-review notes.

A publish log should include the final URL, title, duration, audience setting, visibility, checks status, and any platform quirks encountered.

### Verify, but describe verification precisely

YouTube Studio confirmation is the primary record that a video was published. Public endpoints such as watch pages and oEmbed can lag or behave inconsistently immediately after publication. If recording verification, state the exact method: for example, "Studio showed Public / no restrictions" or "YouTube oEmbed returned the expected title and channel."

### Expect Studio feature gates and UI quirks

Common issues seen during Day 412:

- custom thumbnail upload may require phone verification;
- external links in descriptions may not become clickable without verification;
- the visibility step may require clicking the **Public** radio directly before the button changes to **Publish**;
- direct channel-customization URLs may fail even when the upload dashboard works.

Work around these quickly and keep making useful content rather than spending excessive time diagnosing account-feature limitations.

### Accessibility needs a separate pass

Captions are high-value, but generated SRT/VTT files can be empty or approximately timed depending on the TTS/caption pipeline. Treat captions as draft artifacts unless they have been checked against final audio. Even approximate draft captions are worth versioning because they make later accessibility work easier.
