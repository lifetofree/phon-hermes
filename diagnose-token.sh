#!/bin/bash
# Script to diagnose Notion API token issue

# Use the full path to the .env file
ENV_FILE="/home/lifetofree/hermes-agent/.env"

# Check if .env file exists
if [ -f "$ENV_FILE" ]; then
  echo "Loading environment variables from $ENV_FILE..."
  source "$ENV_FILE"
  if [ $? -eq 0 ]; then
    echo "Environment variables loaded successfully"
  else
    echo "Failed to load environment variables"
    exit 1
  fi
else
  echo "Error: .env file not found at $ENV_FILE"
  exit 1
fi

# Check if NOTION_TOKEN is set
if [ -z "$NOTION_TOKEN" ]; then
  echo "Error: NOTION_TOKEN environment variable is not set."
  exit 1
fi

# Check if PARENT_PAGE_ID is set
if [ -z "$PARENT_PAGE_ID" ]; then
  echo "Error: PARENT_PAGE_ID environment variable is not set."
  exit 1
fi

# Print the first 10 characters of the token for verification
echo "First 10 characters of NOTION_TOKEN: ${NOTION_TOKEN:0:10}"

# Check if the token starts with the expected prefix
if [[ "$NOTION_TOKEN" == "ntn_*" ]]; then
  echo "Token starts with 'ntn_' - this is correct for Notion integration"
else
  echo "Token does not start with 'ntn_' - this may be incorrect"
fi

# Test the token using a simple API call to get user info
echo "Testing API token with a simple call to get user info..."

# Make a simple API call to check the token
curl -s -X GET "https://api.notion.com/v1/users" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json"