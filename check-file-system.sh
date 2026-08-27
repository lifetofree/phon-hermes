#!/bin/bash
# Script to check file system for .env file

# Check if .env file exists in current directory
if [ -f ".env" ]; then
  echo ".env file exists in current directory"
else
  echo ".env file does not exist in current directory"
fi

# Check if .env file exists in hermes-agent directory
if [ -f "~/hermes-agent/.env" ]; then
  echo ".env file exists in ~/hermes-agent directory"
else
  echo ".env file does not exist in ~/hermes-agent directory"
fi

# Check if .env file exists in ~/.hermes directory
if [ -f "~/.hermes/.env" ]; then
  echo ".env file exists in ~/.hermes directory"
else
  echo ".env file does not exist in ~/.hermes directory"
fi

# List all .env files in the system
find /home/lifetofree -name ".env" -type f