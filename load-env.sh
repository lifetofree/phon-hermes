#!/bin/bash
# Script to load environment variables from .env file

# Check if .env file exists
if [ -f ".env" ]; then
  echo "Loading environment variables from .env file..."
  source .env
  if [ $? -eq 0 ]; then
    echo "Environment variables loaded successfully"
  else
    echo "Failed to load environment variables"
    exit 1
  fi
else
  echo "Error: .env file not found"
  exit 1
fi

# Check if NOTION_TOKEN is set
if [ -z "$NOTION_TOKEN" ]; then
  echo "Error: NOTION_TOKEN environment variable is not set"
  exit 1
fi

# Check if PARENT_PAGE_ID is set
if [ -z "$PARENT_PAGE_ID" ]; then
  echo "Error: PARENT_PAGE_ID environment variable is not set"
  exit 1
fi

# Print the values
echo "NOTION_TOKEN: $NOTION_TOKEN"
echo "PARENT_PAGE_ID: $PARENT_PAGE_ID"