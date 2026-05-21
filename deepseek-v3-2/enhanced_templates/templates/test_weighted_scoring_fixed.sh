#!/bin/bash

# Fixed Weighted Scoring Test
echo "=== FIXED WEIGHTED SCORING TEST ==="
echo ""

# Weights from Day 417 plan
declare -A weights
weights[TECHNICAL]=25   # 25%
weights[AUDIO]=20       # 20%  
weights[VISUAL]=20      # 20%
weights[CAPABILITY]=20   # 20%
weights[NARRATIVE]=15    # 15%

# Test scores (good quality video)
declare -A test_scores
test_scores[TECHNICAL]=4.6
test_scores[AUDIO]=4.4
test_scores[VISUAL]=4.5
test_scores[CAPABILITY]=4.7
test_scores[NARRATIVE]=4.3

# Calculate with proper decimal handling
echo "Calculating weighted score..."
echo ""

total=0
for category in "${!weights[@]}"; do
    weight=${weights[$category]}
    score=${test_scores[$category]}
    
    # Calculate weighted contribution
    weighted=$(echo "scale=4; $score * $weight / 100" | bc)
    total=$(echo "scale=4; $total + $weighted" | bc)
    
    printf "%-12s: %5.2f/5 × %3d%% = %6.3f\n" \
        "$category" "$score" "$weight" "$weighted"
done

echo "--------------------------------"
printf "TOTAL WEIGHTED SCORE: %6.3f/5\n" "$total"

# Determine approval status
approval_status=""
if (( $(echo "$total >= 4.3" | bc -l) )); then
    approval_status="✅ APPROVED (≥4.3)"
elif (( $(echo "$total >= 4.0" | bc -l) )); then
    approval_status="⚠️ CONDITIONAL (4.0-4.29)"
else
    approval_status="❌ NEEDS IMPROVEMENT (<4.0)"
fi

echo "STATUS: $approval_status"

# Test specific thresholds
echo ""
echo "=== THRESHOLD VERIFICATION ==="

# Define test cases
declare -A threshold_tests
threshold_tests[APPROVED_MIN]=4.3
threshold_tests[CONDITIONAL_MIN]=4.0
threshold_tests[CONDITIONAL_MAX]=4.29
threshold_tests[REJECT_MAX]=3.99

for test_name in "${!threshold_tests[@]}"; do
    score=${threshold_tests[$test_name]}
    weighted=$(echo "scale=4; $score * 100 / 100" | bc)  # All weights sum to 100
    
    status=""
    if (( $(echo "$weighted >= 4.3" | bc -l) )); then
        status="APPROVED"
    elif (( $(echo "$weighted >= 4.0" | bc -l) )); then
        status="CONDITIONAL"
    else
        status="NEEDS IMPROVEMENT"
    fi
    
    printf "%-20s: %5.2f/5 → %s\n" "$test_name" "$weighted" "$status"
done

# Weight validation
echo ""
echo "=== WEIGHT VALIDATION ==="
weight_sum=0
for w in "${weights[@]}"; do
    weight_sum=$((weight_sum + w))
done

if [ $weight_sum -eq 100 ]; then
    echo "✅ Weight distribution valid: $weight_sum% = 100%"
else
    echo "❌ Weight distribution invalid: $weight_sum% ≠ 100%"
fi

echo ""
echo "=== TEST COMPLETE ==="
