#!/bin/bash

# Pivot Pilot - Email Updater
# This script fetches recent emails using Himalaya and updates data.json

ACCOUNT="autumparra"
MAX_EMAILS=5

echo "📬 Fetching latest emails from $ACCOUNT..."

# Get recent emails (correct modern syntax)
EMAILS=$(himalaya envelope list --account "$ACCOUNT" after:1d --max "$MAX_EMAILS" --output json 2>/dev/null)

if [ -z "$EMAILS" ]; then
    echo "⚠️  Could not fetch emails. Make sure Himalaya is configured."
    exit 1
fi

# Count unread emails (basic approach)
UNREAD_COUNT=$(echo "$EMAILS" | grep -o '"status":"unread"' | wc -l | tr -d ' ')

# Create a simple email summary for the dashboard
EMAIL_SUMMARY=$(cat <<EOF
[
  {
    "emoji": "🔥",
    "text": "$UNREAD_COUNT new/unread emails"
  },
  {
    "emoji": "📧",
    "text": "Last checked: $(date '+%H:%M')"
  }
]
EOF
)

# Update data.json with new email summary
# This uses a simple approach - replace the emailSummary section
TEMP_FILE=$(mktemp)

jq --argjson summary "$EMAIL_SUMMARY" '.emailSummary = $summary' data.json > "$TEMP_FILE" && mv "$TEMP_FILE" data.json

echo "✅ Updated data.json with latest emails!"
echo "Open pivot-pilot.html to see the changes."