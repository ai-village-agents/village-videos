#!/usr/bin/env python3
"""
Template Weight Calculator
Calculate weighted scores for concept evaluation and quality review
"""

import sys

def print_header():
    print("=" * 60)
    print("TEMPLATE WEIGHT CALCULATOR")
    print("=" * 60)
    print("Calculate weighted scores for:")
    print("1. Concept Evaluation")
    print("2. Quality Review")
    print("3. Custom Weighted Scoring")
    print("=" * 60)

def concept_evaluation_calculator():
    print("\n📊 CONCEPT EVALUATION WEIGHTED SCORING")
    print("-" * 40)
    
    weights = {
        "Educational Value": 0.25,
        "Visual Potential": 0.25,
        "Collaborative Angle": 0.20,
        "Production Feasibility": 0.15,
        "Series Coherence": 0.15
    }
    
    total_score = 0
    print("Enter scores (1-5 scale, 5=Excellent):")
    print("-" * 40)
    
    for category, weight in weights.items():
        while True:
            try:
                score = float(input(f"{category} ({weight*100}%): "))
                if 1 <= score <= 5:
                    weighted = score * weight
                    total_score += weighted
                    print(f"  Weighted: {weighted:.2f} (Score: {score} × {weight})")
                    break
                else:
                    print("  Please enter a score between 1 and 5")
            except ValueError:
                print("  Please enter a valid number")
    
    print("-" * 40)
    print(f"TOTAL WEIGHTED SCORE: {total_score:.2f}/5.00")
    
    # Decision thresholds
    if total_score >= 4.3:
        decision = "✅ APPROVED (Score ≥ 4.3)"
    elif total_score >= 4.0:
        decision = "⚠️  CONDITIONAL (Score 4.0-4.29)"
    else:
        decision = "❌ REJECTED (Score < 4.0)"
    
    print(f"DECISION: {decision}")
    return total_score

def quality_review_calculator():
    print("\n🔍 QUALITY REVIEW WEIGHTED SCORING")
    print("-" * 40)
    
    weights = {
        "Technical Specifications": 0.25,
        "Audio Quality": 0.20,
        "Visual Quality": 0.20,
        "Capability-Honesty": 0.20,
        "Narrative Clarity": 0.15
    }
    
    total_score = 0
    print("Enter scores (1-5 scale, 5=Excellent):")
    print("-" * 40)
    
    for category, weight in weights.items():
        while True:
            try:
                score = float(input(f"{category} ({weight*100}%): "))
                if 1 <= score <= 5:
                    weighted = score * weight
                    total_score += weighted
                    print(f"  Weighted: {weighted:.2f} (Score: {score} × {weight})")
                    break
                else:
                    print("  Please enter a score between 1 and 5")
            except ValueError:
                print("  Please enter a valid number")
    
    print("-" * 40)
    print(f"TOTAL WEIGHTED SCORE: {total_score:.2f}/5.00")
    
    # Decision thresholds
    if total_score >= 4.3:
        decision = "✅ APPROVED FOR PUBLICATION (Score ≥ 4.3)"
    elif total_score >= 4.0:
        decision = "⚠️  CONDITIONAL APPROVAL (Score 4.0-4.29)"
    else:
        decision = "❌ REJECTED (Score < 4.0)"
    
    print(f"DECISION: {decision}")
    
    # Improvement guidance
    if total_score < 4.3:
        print("\n🔧 AREAS FOR IMPROVEMENT:")
        print("Critical (<3.5): Must fix before publication")
        print("Moderate (3.5-4.0): Should fix if time permits")
        print("Acceptable (≥4.0): Optional improvements")
    
    return total_score

def custom_weight_calculator():
    print("\n⚙️ CUSTOM WEIGHTED SCORING")
    print("-" * 40)
    
    categories = []
    weights = []
    
    print("Enter categories (enter 'done' when finished):")
    print("-" * 40)
    
    # Get categories
    while True:
        category = input("Category name: ")
        if category.lower() == 'done':
            if len(categories) < 2:
                print("Please enter at least 2 categories")
                continue
            break
        categories.append(category)
    
    print("\nEnter weights for each category (must sum to 100%):")
    print("-" * 40)
    
    # Get weights
    total_weight = 0
    for i, category in enumerate(categories):
        while True:
            try:
                weight = float(input(f"Weight for '{category}' (%): "))
                if weight > 0:
                    total_weight += weight
                    weights.append(weight / 100)  # Convert to decimal
                    break
                else:
                    print("  Weight must be positive")
            except ValueError:
                print("  Please enter a valid number")
    
    # Normalize weights if they don't sum to 100%
    if abs(total_weight - 100) > 0.01:
        print(f"\n⚠️  Weights sum to {total_weight}%, normalizing to 100%")
        weights = [w / total_weight for w in weights]
    
    print("\nEnter scores (1-5 scale, 5=Excellent):")
    print("-" * 40)
    
    total_score = 0
    for i, (category, weight) in enumerate(zip(categories, weights)):
        while True:
            try:
                score = float(input(f"{category} ({weight*100:.1f}%): "))
                if 1 <= score <= 5:
                    weighted = score * weight
                    total_score += weighted
                    print(f"  Weighted: {weighted:.2f} (Score: {score} × {weight:.3f})")
                    break
                else:
                    print("  Please enter a score between 1 and 5")
            except ValueError:
                print("  Please enter a valid number")
    
    print("-" * 40)
    print(f"TOTAL WEIGHTED SCORE: {total_score:.2f}/5.00")
    
    return total_score

def main():
    print_header()
    
    while True:
        print("\nSelect calculator type:")
        print("1. Concept Evaluation")
        print("2. Quality Review")
        print("3. Custom Weighted Scoring")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            concept_evaluation_calculator()
        elif choice == '2':
            quality_review_calculator()
        elif choice == '3':
            custom_weight_calculator()
        elif choice == '4':
            print("\nThank you for using the Template Weight Calculator! 👋")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
        
        # Ask if user wants to continue
        if choice != '4':
            cont = input("\nPerform another calculation? (y/n): ").lower()
            if cont != 'y':
                print("\nThank you for using the Template Weight Calculator! 👋")
                break

if __name__ == "__main__":
    main()
