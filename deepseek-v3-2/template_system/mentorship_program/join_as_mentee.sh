#!/usr/bin/env bash
set -euo pipefail

prompt() {
  local label="$1" input=""
  while [[ -z "$input" ]]; do
    read -r -p "$label: " input
  done
  printf '%s' "$input"
}

echo "Welcome! Let's create your mentee profile."

name=$(prompt "Your name")
role=$(prompt "Current role or focus area")
goals=$(prompt "Top 2-3 goals for mentorship")
timeline=$(prompt "Timeline or cadence you prefer (e.g., weekly, bi-weekly)")
learning_style=$(prompt "Learning style (e.g., examples, pairing, async notes)")
topics=$(prompt "Topics you want to cover first")
communication=$(prompt "Preferred communication channels (e.g., Slack, email, video)")
timezone=$(prompt "Your timezone")
contact=$(prompt "Contact handle for mentors")
ready=$(prompt "Ready for matching now? (yes/no)")

output_file="mentee_profile.md"
cat > "$output_file" <<EOF
# Mentee Profile

- **Name:** $name
- **Current Role/Focus:** $role
- **Top Goals:** $goals
- **Preferred Timeline/Cadence:** $timeline
- **Learning Style:** $learning_style
- **Topics to Cover First:** $topics
- **Communication Channels:** $communication
- **Timezone:** $timezone
- **Contact for Mentors:** $contact
- **Ready for Matching:** $ready
- **Last Updated:** $(date -u +"%Y-%m-%d %H:%M UTC")

---
Share this file in chat so mentors know your goals and availability.
EOF

echo "Mentee profile saved to $output_file"
