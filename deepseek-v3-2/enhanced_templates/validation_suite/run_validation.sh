#!/bin/bash

# Run template validation
echo "🚀 Starting Enhanced Template Validation Suite"
echo "📅 Date: $(date)"
echo "================================================"

# Check Python availability
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3."
    exit 1
fi

# Run the validation script
python3 validate_template_consistency.py

# Check exit code
validation_result=$?
echo "================================================"
echo "Validation completed with exit code: $validation_result"

if [ $validation_result -eq 0 ]; then
    echo "✅ All templates validated successfully!"
else
    echo "❌ Template validation failed. Please check the issues above."
fi

exit $validation_result
