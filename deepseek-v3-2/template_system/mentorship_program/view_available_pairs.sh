#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

clean_field() {
  local file="$1" label="$2"
  grep -m1 -i "^$label:" "$file" | cut -d':' -f2- | sed 's/^ *//'
}

show_ready_profiles() {
  local kind="$1" pattern="$2" header="$3" fields=("${@:4}")
  local files=( $pattern )

  echo "=== $header ==="
  if [[ ${#files[@]} -eq 0 ]]; then
    echo "No $kind profiles found."
    echo
    return
  fi

  local any=0
  for file in "${files[@]}"; do
    if grep -qi "^Ready for Matching: *yes" "$file"; then
      ((any++))
      echo "- File: $file"
      for field in "${fields[@]}"; do
        value=$(clean_field "$file" "$field")
        echo "  $field: ${value:-Not provided}"
      done
      echo
    fi
  done

  if [[ $any -eq 0 ]]; then
    echo "No $kind are currently ready for matching."
    echo
  fi
}

echo "People ready to connect:"
show_ready_profiles "mentors" "mentor_profile*.md" "Mentors" \
  "Name" "Expertise" "Availability" "Communication Channels" "Timezone" "Contact for Mentees"
show_ready_profiles "mentees" "mentee_profile*.md" "Mentees" \
  "Name" "Top Goals" "Preferred Timeline/Cadence" "Communication Channels" "Timezone" "Contact for Mentors"
echo "Update a profile script to change readiness, then rerun this viewer."
