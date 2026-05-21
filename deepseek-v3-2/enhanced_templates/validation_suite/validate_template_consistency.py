#!/usr/bin/env python3
"""
Template Consistency Validation Script
Validates that templates follow consistent structure and standards
"""

import os
import sys
import yaml
import re
from pathlib import Path

class TemplateValidator:
    def __init__(self, templates_dir):
        self.templates_dir = Path(templates_dir)
        self.validation_results = []
        self.required_sections = {
            'concept_evaluation': ['title', 'description', 'evaluation_criteria', 'scoring_scale', 'decision_thresholds'],
            'script_development': ['title', 'hook', 'problem_statement', 'concept_explanation', 'key_takeaways', 'call_to_action'],
            'visual_specifications': ['title', 'scene_breakdown', 'visual_requirements', 'color_palette', 'technical_specs'],
            'collaboration_coordination': ['title', 'phase_structure', 'responsibilities', 'communication_protocol', 'timeline'],
            'quality_review': ['title', 'review_categories', 'scoring_system', 'decision_criteria', 'improvement_guidance'],
            'performance_tracking': ['title', 'metrics_framework', 'tracking_templates', 'analysis_methods', 'optimization_guidelines']
        }
    
    def validate_all_templates(self):
        """Validate all templates in the templates directory"""
        print("🔍 Starting template validation...")
        print(f"📁 Templates directory: {self.templates_dir}")
        
        # Check if templates directory exists
        if not self.templates_dir.exists():
            print(f"❌ Templates directory not found: {self.templates_dir}")
            return False
        
        # Get all template files
        template_files = list(self.templates_dir.glob("*.md")) + list(self.templates_dir.glob("*.sh"))
        
        if not template_files:
            print("❌ No template files found")
            return False
        
        print(f"📄 Found {len(template_files)} template files")
        
        # Validate each template
        all_valid = True
        for template_file in template_files:
            is_valid = self.validate_template(template_file)
            if not is_valid:
                all_valid = False
        
        # Print summary
        self.print_validation_summary()
        
        return all_valid
    
    def validate_template(self, template_file):
        """Validate a single template file"""
        filename = template_file.name
        print(f"\n📋 Validating: {filename}")
        
        validations = []
        
        # Check file exists
        validations.append(self.check_file_exists(template_file))
        
        # Check file size
        validations.append(self.check_file_size(template_file))
        
        # Check file extension
        validations.append(self.check_file_extension(template_file))
        
        # Check content based on template type
        template_type = self.determine_template_type(filename)
        if template_type:
            validations.append(self.check_required_sections(template_file, template_type))
            validations.append(self.check_template_structure(template_file, template_type))
        
        # Check for YAML frontmatter if Markdown
        if filename.endswith('.md'):
            validations.append(self.check_yaml_frontmatter(template_file))
        
        # Check for shebang if shell script
        if filename.endswith('.sh'):
            validations.append(self.check_shebang(template_file))
        
        # Determine overall validity
        is_valid = all(v['status'] == 'PASS' for v in validations)
        
        # Store results
        self.validation_results.append({
            'filename': filename,
            'valid': is_valid,
            'validations': validations
        })
        
        return is_valid
    
    def check_file_exists(self, file_path):
        """Check if file exists"""
        result = {
            'check': 'file_exists',
            'status': 'PASS' if file_path.exists() else 'FAIL',
            'message': 'File exists' if file_path.exists() else 'File not found'
        }
        return result
    
    def check_file_size(self, file_path):
        """Check if file has reasonable size"""
        file_size = file_path.stat().st_size
        min_size = 100  # 100 bytes minimum
        max_size = 50000  # 50KB maximum for templates
        
        if file_size < min_size:
            status = 'FAIL'
            message = f'File too small: {file_size} bytes (minimum: {min_size})'
        elif file_size > max_size:
            status = 'WARNING'
            message = f'File large: {file_size} bytes (maximum recommended: {max_size})'
        else:
            status = 'PASS'
            message = f'File size OK: {file_size} bytes'
        
        return {'check': 'file_size', 'status': status, 'message': message}
    
    def check_file_extension(self, file_path):
        """Check if file has valid extension"""
        valid_extensions = ['.md', '.sh', '.yaml', '.yml', '.json']
        ext = file_path.suffix
        
        if ext in valid_extensions:
            status = 'PASS'
            message = f'Valid extension: {ext}'
        else:
            status = 'WARNING'
            message = f'Non-standard extension: {ext} (expected: {valid_extensions})'
        
        return {'check': 'file_extension', 'status': status, 'message': message}
    
    def determine_template_type(self, filename):
        """Determine template type based on filename"""
        filename_lower = filename.lower()
        
        if 'concept' in filename_lower and 'evaluation' in filename_lower:
            return 'concept_evaluation'
        elif 'script' in filename_lower and 'development' in filename_lower:
            return 'script_development'
        elif 'visual' in filename_lower and 'specification' in filename_lower:
            return 'visual_specifications'
        elif 'collaboration' in filename_lower and 'coordination' in filename_lower:
            return 'collaboration_coordination'
        elif 'quality' in filename_lower and 'review' in filename_lower:
            return 'quality_review'
        elif 'performance' in filename_lower and 'tracking' in filename_lower:
            return 'performance_tracking'
        else:
            print(f"   ⚠️  Could not determine template type from filename: {filename}")
            return None
    
    def check_required_sections(self, file_path, template_type):
        """Check if template contains required sections"""
        if template_type not in self.required_sections:
            return {'check': 'required_sections', 'status': 'SKIP', 'message': f'No section requirements defined for {template_type}'}
        
        required = self.required_sections[template_type]
        content = file_path.read_text(encoding='utf-8').lower()
        
        missing_sections = []
        for section in required:
            # Look for section in various formats
            section_patterns = [
                f'#.*{section}',  # Markdown header with section
                f'\\*{section}\\*',  # Bold/italic section
                f'{section}:',  # Label with colon
                f'\\[{section}\\]',  # Bracketed section
            ]
            
            found = any(re.search(pattern, content) for pattern in section_patterns)
            if not found:
                missing_sections.append(section)
        
        if missing_sections:
            status = 'FAIL'
            message = f'Missing sections: {", ".join(missing_sections)}'
        else:
            status = 'PASS'
            message = f'All required sections present: {", ".join(required)}'
        
        return {'check': 'required_sections', 'status': status, 'message': message}
    
    def check_template_structure(self, file_path, template_type):
        """Check basic template structure"""
        content = file_path.read_text(encoding='utf-8')
        
        # Check for title/header
        has_title = bool(re.search(r'^#\s+.+', content, re.MULTILINE))
        
        # Check for some structure (at least 3 sections)
        sections = re.findall(r'^#{1,3}\s+.+', content, re.MULTILINE)
        
        if not has_title:
            status = 'FAIL'
            message = 'Missing main title/header'
        elif len(sections) < 3:
            status = 'WARNING'
            message = f'Only {len(sections)} sections found (minimum 3 recommended)'
        else:
            status = 'PASS'
            message = f'Good structure with {len(sections)} sections'
        
        return {'check': 'template_structure', 'status': status, 'message': message}
    
    def check_yaml_frontmatter(self, file_path):
        """Check for YAML frontmatter in Markdown files"""
        content = file_path.read_text(encoding='utf-8')
        
        # Check for YAML frontmatter pattern
        yaml_pattern = r'^---\s*\n.*?\n---\s*\n'
        has_yaml = bool(re.search(yaml_pattern, content, re.DOTALL | re.MULTILINE))
        
        if has_yaml:
            status = 'PASS'
            message = 'YAML frontmatter found'
        else:
            status = 'INFO'
            message = 'No YAML frontmatter (optional for templates)'
        
        return {'check': 'yaml_frontmatter', 'status': status, 'message': message}
    
    def check_shebang(self, file_path):
        """Check for shebang in shell scripts"""
        content = file_path.read_text(encoding='utf-8')
        
        has_shebang = content.startswith('#!/')
        
        if has_shebang:
            status = 'PASS'
            message = 'Shebang found'
        else:
            status = 'WARNING'
            message = 'No shebang in shell script'
        
        return {'check': 'shebang', 'status': status, 'message': message}
    
    def print_validation_summary(self):
        """Print summary of validation results"""
        print("\n" + "="*60)
        print("VALIDATION SUMMARY")
        print("="*60)
        
        total_templates = len(self.validation_results)
        valid_templates = sum(1 for r in self.validation_results if r['valid'])
        invalid_templates = total_templates - valid_templates
        
        print(f"📊 Total Templates: {total_templates}")
        print(f"✅ Valid Templates: {valid_templates}")
        print(f"❌ Invalid Templates: {invalid_templates}")
        
        if invalid_templates > 0:
            print("\n🔧 Issues Found:")
            for result in self.validation_results:
                if not result['valid']:
                    print(f"\n  📄 {result['filename']}:")
                    for validation in result['validations']:
                        if validation['status'] != 'PASS':
                            status_icon = '❌' if validation['status'] == 'FAIL' else '⚠️' 
                            print(f"    {status_icon} {validation['check']}: {validation['message']}")
        else:
            print("\n🎉 All templates are valid!")
        
        print("\n" + "="*60)

def main():
    # Get templates directory from command line or use default
    if len(sys.argv) > 1:
        templates_dir = sys.argv[1]
    else:
        # Default: templates directory in same parent as script
        script_dir = Path(__file__).parent
        templates_dir = script_dir.parent / 'templates'
    
    # Validate templates
    validator = TemplateValidator(templates_dir)
    is_valid = validator.validate_all_templates()
    
    # Return exit code based on validation result
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()
