#!/usr/bin/env bash
set -euo pipefail

prompt() {
  local label="$1" input=""
  while [[ -z "$input" ]]; do
    read -r -p "$label: " input
  done
  printf '%s' "$input"
}

echo "Welcome! Let's set up your mentor profile."

name=$(prompt "Your name")
role=$(prompt "Primary expertise or role (e.g., Backend Engineer, PM)")
years=$(prompt "Years of experience")
bio=$(prompt "Short bio (1-2 sentences)")
availability=$(prompt "Weekly availability (hours or time windows)")
style=$(prompt "Preferred mentorship style (e.g., hands-on pairing, async feedback)")
communication=$(prompt "Preferred communication channels (e.g., Slack, email, video)")
timezone=$(prompt "Your timezone")
contact=$(prompt "Contact handle for mentees")
ready=$(prompt "Ready for matching now? (yes/no)")

output_file="mentor_profile.md"
cat > "$output_file" <<EOF
# Mentor Profile

- **Name:** $name
- **Expertise:** $role
- **Years of Experience:** $years
- **Short Bio:** $bio
- **Availability:** $availability
- **Mentorship Style:** $style
- **Communication Channels:** $communication
- **Timezone:** $timezone
- **Contact for Mentees:** $contact
- **Ready for Matching:** $ready
- **Last Updated:** $(date -u +"%Y-%m-%d %H:%M UTC")

---
Share this file in chat to help mentees know your focus and availability.
EOF

echo "Mentor profile saved to $output_file"
