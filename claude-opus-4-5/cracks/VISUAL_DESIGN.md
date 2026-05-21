# Cracks: How Breaking Reveals Structure
## Visual Design Document

---

## COLOR PALETTE

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Deep Charcoal | #1A1A1A | (26, 26, 26) | Primary backgrounds |
| Warm Stone | #3D3D3D | (61, 61, 61) | Secondary backgrounds, shadows |
| Marble White | #E8E4E1 | (232, 228, 225) | Pristine surfaces, clean elements |
| Kintsugi Gold | #D4A574 | (212, 165, 116) | Gold repairs, revelation, highlights |
| Crystal Blue | #6B8E9F | (107, 142, 159) | Ice, water, cool elements |
| Earth Brown | #8B7355 | (139, 115, 85) | Wood, pottery, organic materials |
| Geode Purple | #7B6B8D | (123, 107, 141) | Crystal interiors, depth |

---

## TYPOGRAPHY

**Primary Font:** Inter (clean, modern sans-serif)
- End card text: Inter Medium, 36px, Marble White
- Interactive question: Inter Light, 28px, Kintsugi Gold

**On-screen text is minimal** - visuals and narration carry the story.

---

## VISUAL ASSETS NEEDED

### Scene 1: The Perfect Surface
**Asset 1.1: scene1_perfect_surfaces.png**
- Three-panel composition showing pristine surfaces
- Left: Polished marble countertop (Marble White with subtle veining)
- Center: Still pond reflecting an abstract sky (Crystal Blue gradient)
- Right: Clean white wall with soft shadow (Marble White to Warm Stone gradient)
- Composition: Horizontal triptych, 1920x1080
- Mood: Calm, orderly, trustworthy

### Scene 2: The First Fracture
**Asset 2.1: scene2_ice_crack.png**
- Overhead view of ice surface with hairline crack
- The crack branches like a river delta, delicate and intricate
- Background: Deep blue-white ice (Crystal Blue fading to white)
- Crack lines: Slightly darker, suggesting depth
- Composition: Central focus, crack radiating outward
- Mood: Tension beginning, something changing

### Scene 3: What's Inside
**Asset 3.1: scene3_split_wood.png**
- Cross-section of split log showing growth rings
- Rich wood tones (Earth Brown variations)
- Clear annual rings visible, some narrow (drought years), some wide
- Split edge rough and organic
- Mood: Time made visible, history revealed

**Asset 3.2: scene3_geode.png**
- Cracked geode revealing crystal interior
- Outer surface: rough gray-brown rock
- Interior: Vibrant purple/blue crystals (Geode Purple, Crystal Blue)
- Crystals catch imagined light, sparkle
- Mood: Hidden beauty, ancient formation

**Asset 3.3: scene3_broken_pottery.png**
- Broken ceramic piece showing layers of glaze
- Multiple glaze layers visible in the break (Earth Brown, cream, subtle color)
- Hand-made quality evident in slight irregularities
- Mood: Craftsmanship revealed, human touch

**Asset 3.4: scene3_tree_rings.png**
- Close-up of tree stump with visible rings and a crack
- Rings tell story of growth
- Crack runs through center, not destroying but dividing the history
- Mood: Life story visible, time measured

### Scene 4: The Human Parallel
**Asset 4.1: scene4_light_through_cracks.png**
- Abstract: Dark surface with golden light seeping through crack lines
- Background: Deep Charcoal (#1A1A1A)
- Light: Kintsugi Gold (#D4A574) glowing through fractures
- Cracks form an organic, almost human silhouette shape
- Mood: Intimate, hopeful, revealing inner light

### Scene 5: Kintsugi
**Asset 5.1: scene5_kintsugi_bowl.png**
- Japanese kintsugi bowl, beautifully repaired
- Ceramic: Earth tones, traditional tea bowl shape
- Gold repairs: Bright Kintsugi Gold, catching light
- Multiple repair lines creating web pattern
- Background: Simple, dark, to highlight the bowl
- Mood: Reverence, transformed beauty

**Asset 5.2: scene5_kintsugi_detail.png**
- Close-up of gold repair line
- Shows gold lacquer filling the crack precisely
- Contrast between matte ceramic and glowing gold
- Mood: Appreciation of detail, the art of repair

### Scene 6: Return
**Asset 6.1: scene6_surfaces_cracked.png**
- Return to Scene 1 composition, but now with subtle hairline cracks
- Same three-panel layout
- Each surface now has barely visible fracture lines
- Not damaged—more honest, more real
- Mood: Quiet transformation, new seeing

### End Card
**Asset 7.1: end_card.png**
- The Edge Garden logo (centered)
- Dark background with subtle golden crack pattern radiating outward
- Text below: "What have your cracks shown you?" in Kintsugi Gold
- Mood: Contemplative, inviting reflection

### Thumbnail
**Asset 8.1: thumbnail.png**
- Kintsugi bowl as hero image
- Bold crack with gold visible
- Text overlay: "CRACKS" in strong typography
- Contrast: dark background, glowing gold repair
- Must read clearly at small sizes

---

## ANIMATION/TRANSITION NOTES

1. **Scene 1 → Scene 2:** Cross-fade (0.5s) as we move from perfect to fractured
2. **Scene 2 internal:** If possible, subtle animation of crack spreading
3. **Scene 3 transitions:** Quick cuts between examples (0.3s), building rhythm
4. **Scene 3 → Scene 4:** Slower cross-fade (0.7s) as we shift to metaphor
5. **Scene 5 internal:** Slow zoom on kintsugi detail
6. **Scene 6:** Static, meditative
7. **End card:** Fade in (0.5s), hold

---

## AUDIO DESIGN

**Narration:**
- Warm, contemplative voice
- Measured pace, pauses for visual moments
- gTTS or similar TTS with post-processing for warmth

**Ambient:**
- Very subtle texture under narration
- Perhaps: soft cracking sounds during Scene 2
- Quiet, almost silence during the pause in Scene 6
- Gentle fade out on end card

---

## PRODUCTION CHECKLIST

- [ ] Create all 11 visual assets at 1920x1080
- [ ] Record narration for 6 scenes
- [ ] Assemble segments with correct timing
- [ ] Add ambient sound if appropriate
- [ ] Create concat list
- [ ] Render final video
- [ ] Create thumbnail
- [ ] Quality review
- [ ] Upload metadata preparation
