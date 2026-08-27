#!/bin/bash
# Script to check environment variables

# Check if NOTION_TOKEN is set
if [ -z "$NOTION_TOKEN" ]; then
  echo "NOTION_TOKEN is not set"
else
  echo "NOTION_TOKEN is set"
fi

# Check if PARENT_PAGE_ID is set
if [ -z "$PARENT_PAGE_ID" ]; then
  echo "PARENT_PAGE_ID is not set"
else
  echo "PARENT_PAGE_ID is set"
fi

# Check if the .env file exists
if [ -f ".env" ]; then
  echo ".env file exists"
else
  echo ".env file does not exist"
fi

# Check if we can source the .env file
if [ -f ".env" ]; then
  echo "Attempting to source .env file..."
  source .env
  if [ $? -eq 0 ]; then
    echo "Successfully sourced .env file"
    echo "NOTION_TOKEN: $NOTION_TOKEN"
    echo "PARENT_PAGE_ID: $PARENT_PAGE_ID"
  else
    echo "Failed to source .env file"
  fi
else
  echo ".env file does not exist"
fi