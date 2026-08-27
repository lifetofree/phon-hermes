#!/bin/bash
# Script to check file permissions

# Check if .env file exists
if [ -f ".env" ]; then
  echo ".env file exists"
  # Check permissions
  ls -la .env
else
  echo ".env file does not exist"
fi

# Check if we can read the file
if [ -r ".env" ]; then
  echo "We have read permission for .env file"
else
  echo "We do not have read permission for .env file"
fi

# Check if we can write to the file
if [ -w ".env" ]; then
  echo "We have write permission for .env file"
else
  echo "We do not have write permission for .env file"
fi

# Check if we can execute the file
if [ -x ".env" ]; then
  echo "We have execute permission for .env file"
else
  echo "We do not have execute permission for .env file"
fi