#!/bin/bash
# Script to force read the .env file

# Use the full path to the .env file
ENV_FILE="/home/lifetofree/hermes-agent/.env"

# Check if .env file exists
if [ -f "$ENV_FILE" ]; then
  echo "Loading environment variables from $ENV_FILE..."
  # Use cat to read the file directly
  cat "$ENV_FILE"
else
  echo "Error: .env file not found at $ENV_FILE"
  exit 1
fi