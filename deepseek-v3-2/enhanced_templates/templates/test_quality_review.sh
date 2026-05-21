#!/bin/bash

# Enhanced Quality Review Template Script
# For: [Video Title]
# Date: [YYYY-MM-DD]

echo "================================"
echo "VIDEO QUALITY REVIEW SYSTEM"
echo "Video: [Title]"
echo "Date: $(date)"
echo "================================"

# Configuration
VIDEO_FILE="[path/to/video.mp4]"
REPORT_FILE="quality_review_report_$(date +%Y%m%d_%H%M%S).txt"
SCORING_LOG="quality_scores_$(date +%Y%m%d).csv"

# Initialize scoring
declare -A scores
declare -A weights

# Weight configuration (sums to 100%)
weights[TECHNICAL]=20
weights[AUDIO]=25
weights[VISUAL]=25
weights[CAPABILITY]=20
weights[NARRATIVE]=10

# Function to score a category (1-5 scale)
score_category() {
    local category=$1
    local max_score=5
    local score=0
    
    echo ""
    echo "=== $category QUALITY ASSESSMENT ==="
    echo "Rate each item (1-5), then calculate average."
    
    case $category in
        TECHNICAL)
            echo "Technical Specifications:"
            read -p "Resolution (1920×1080): " s1
            read -p "Frame rate consistency: " s2
            read -p "Codec compliance (H.264+AAC): " s3
            read -p "File size (25-40MB target): " s4
            read -p "Export quality (no artifacts): " s5
            score=$(echo "scale=2; ($s1+$s2+$s3+$s4+$s5)/5" | bc)
            ;;
        AUDIO)
            echo "Audio Quality:"
            read -p "Narration clarity: " s1
            read -p "Music balance (-20dB): " s2
            read -p "Sound effects integration: " s3
            read -p "Audio mixing (LUFS -14 to -16): " s4
            read -p "Overall audio experience: " s5
            score=$(echo "scale=2; ($s1+$s2+$s3+$s4+$s5)/5" | bc)
            ;;
        VISUAL)
            echo "Visual Quality:"
            read -p "Transitions (0.5s cross-fades): " s1
            read -p "Color consistency: " s2
            read -p "Text readability: " s3
            read -p "Visual pacing: " s4
            read -p "Overall visual appeal: " s5
            score=$(echo "scale=2; ($s1+$s2+$s3+$s4+$s5)/5" | bc)
            ;;
        CAPABILITY)
            echo "Capability-Honesty:"
            read -p "Watermarks present (8-10% opacity): " s1
            read -p "Domain labels clear: " s2
            read -p "Boundaries correctly shown: " s3
            read -p "Narration statements accurate: " s4
            read -p "Scene 4 handoff correct: " s5
            score=$(echo "scale=2; ($s1+$s2+$s3+$s4+$s5)/5" | bc)
            ;;
        NARRATIVE)
            echo "Narrative Coherence:"
            read -p "Concept clarity: " s1
            read -p "Educational value: " s2
            read -p "Engagement level: " s3
            read -p "Series continuity: " s4
            read -p "Memorability: " s5
            score=$(echo "scale=2; ($s1+$s2+$s3+$s4+$s5)/5" | bc)
            ;;
    esac
    
    scores[$category]=$score
    echo "Average $category score: $score/5"
}

# Function to calculate weighted total
calculate_weighted_total() {
    local total=0
    
    for category in "${!weights[@]}"; do
        local weight=${weights[$category]}
        local score=${scores[$category]}
        local weighted=$(echo "scale=3; $score * $weight / 100" | bc)
        total=$(echo "scale=3; $total + $weighted" | bc)
        
        echo "$category: $score/5 × $weight% = $weighted" >> "$REPORT_FILE"
    done
    
    echo "Weighted total: $total/5" >> "$REPORT_FILE"
    echo "$(date),$total" >> "$SCORING_LOG"
    
    echo $total
}

# Main review process
main() {
    echo "Starting comprehensive quality review..."
    echo "Review Report: $REPORT_FILE"
    echo ""
    
    # Technical validation first
    echo "=== TECHNICAL VALIDATION ==="
    if command -v ffprobe &> /dev/null && [ -f "$VIDEO_FILE" ]; then
        echo "Running ffprobe analysis..."
        ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate -of csv=p=0 "$VIDEO_FILE" | tr ',' '\t'
        echo ""
        ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels -of csv=p=0 "$VIDEO_FILE" | tr ',' '\t'
    else
        echo "ffprobe not available or video file not found."
    fi
    
    # Interactive scoring
    for category in TECHNICAL AUDIO VISUAL CAPABILITY NARRATIVE; do
        score_category "$category"
    done
    
    # Calculate final score
    final_score=$(calculate_weighted_total)
    
    # Generate report
    {
        echo "VIDEO QUALITY REVIEW REPORT"
        echo "==========================="
        echo "Video: [Title]"
        echo "Review Date: $(date)"
        echo ""
        echo "TECHNICAL SPECIFICATIONS:"
        echo "- Required: 1920×1080, H.264+AAC, 25-40MB"
        echo "- Actual: [To be filled after technical check]"
        echo ""
        echo "QUALITY SCORES:"
        for category in "${!scores[@]}"; do
            echo "- $category: ${scores[$category]}/5 (weight: ${weights[$category]}%)"
        done
        echo ""
        echo "FINAL WEIGHTED SCORE: $final_score/5"
        echo ""
        echo "RECOMMENDATION:"
        if (( $(echo "$final_score >= 4.3" | bc -l) )); then
            echo "✅ APPROVED FOR PUBLICATION - Meets quality target (≥4.3/5)"
        elif (( $(echo "$final_score >= 4.0" | bc -l) )); then
            echo "⚠️ CONDITIONAL APPROVAL - Below target but acceptable (>4.0/5)"
            echo "   Consider improvements before next video."
        else
            echo "❌ NEEDS IMPROVEMENT - Below acceptable threshold (<4.0/5)"
            echo "   Significant improvements needed before publication."
        fi
        echo ""
        echo "CRITICAL ITEMS CHECKLIST:"
        echo "- [ ] Capability watermarks present"
        echo "- [ ] Domain boundaries labeled"
        echo "- [ ] Narration includes capability statements"
        echo "- [ ] Scene 4 handoff diagram correct"
        echo "- [ ] YouTube metadata prepared"
        echo "- [ ] Series continuity maintained"
    } > "$REPORT_FILE"
    
    echo ""
    echo "=== REVIEW COMPLETE ==="
    echo "Final weighted score: $final_score/5"
    echo "Detailed report saved to: $REPORT_FILE"
    echo "Score logged to: $SCORING_LOG"
    
    # Archive previous quality reports
    if [ -f "quality_review_report_previous.txt" ]; then
        mv "quality_review_report_previous.txt" "quality_review_report_$(date +%Y%m%d_%H%M%S)_archive.txt"
    fi
    cp "$REPORT_FILE" "quality_review_report_previous.txt"
}

# Run main function
main
