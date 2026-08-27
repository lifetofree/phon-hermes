#!/bin/bash
# Script to create a Notion database for knowledge base

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

# Check if required environment variables are set
if [ -z "$NOTION_TOKEN" ]; then
  echo "Error: NOTION_TOKEN environment variable is not set."
  echo "Please set it in your .env file."
  exit 1
fi

# Check if the parent page ID is provided
if [ -z "$PARENT_PAGE_ID" ]; then
  echo "Error: PARENT_PAGE_ID environment variable is not set."
  echo "Please set it in your .env file."
  exit 1
fi

# Create the database using the Notion API
# This uses the curl command as described in the Notion skill documentation

# First, create the database
create_database() {
  echo "Creating database with parent page ID: $PARENT_PAGE_ID"
  echo "Request body:"
  echo "{
    "parent": {"page_id": "$PARENT_PAGE_ID"},
    "title": [{"text": {"content": "Knowledge Base"}}],
    "properties": {
      "Title": {"title": {}},
      "Category": {"select": {"options": [{"name": "Concept"}, {"name": "Tutorial"}, {"name": "Reference"}, {"name": "Tips"}]}},
      "Tags": {"multi_select": {"options": []}},
      "Status": {"select": {"options": [{"name": "Draft"}, {"name": "Review"}, {"name": "Published"}]}},
      "Created": {"date": {}},
      "Updated": {"date": {}},
      "URL": {"url": {}}
    }
  }"

  curl -s -X POST "https://api.notion.com/v1/data_sources" \
    -H "Authorization: Bearer $NOTION_TOKEN" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    -d '{
      "parent": {"page_id": "$PARENT_PAGE_ID"},
      "title": [{"text": {"content": "Knowledge Base"}}],
      "properties": {
        "Title": {"title": {}},
        "Category": {"select": {"options": [{"name": "Concept"}, {"name": "Tutorial"}, {"name": "Reference"}, {"name": "Tips"}]}},
        "Tags": {"multi_select": {"options": []}},
        "Status": {"select": {"options": [{"name": "Draft"}, {"name": "Review"}, {"name": "Published"}]}},
        "Created": {"date": {}},
        "Updated": {"date": {}},
        "URL": {"url": {}}
      }
    }'
}

# Create the database
echo "Creating Notion database..."
create_database

# Check if the command succeeded
if [ $? -eq 0 ]; then
  echo "Database created successfully!"
else
  echo "Failed to create database."
fi

# Make the script executable
chmod +x /home/lifetofree/hermes-agent/create-notion-database.sh

# Create a sample database with additional properties
create_knowledge_base_database() {
  echo "Creating enhanced knowledge base database..."
  echo "Request body:"
  echo "{
    "parent": {"page_id": "$PARENT_PAGE_ID"},
    "title": [{"text": {"content": "Knowledge Base"}}],
      "properties": {
      "Title": {"title": {}},
      "Category": {"select": {"options": [{"name": "Concept"}, {"name": "Tutorial"}, {"name": "Reference"}, {"name": "Tips"}]}},
      "Tags": {"multi_select": {"options": []}},
      "Status": {"select": {"options": [{"name": "Draft"}, {"name": "Review"}, {"name": "Published"}]}},
      "Created": {"date": {}},
      "Updated": {"date": {}},
      "URL": {"url": {}}
    }
  }"

  curl -s -X POST "https://api.notion.com/v1/data_sources" \
    -H "Authorization: Bearer $NOTION_TOKEN" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    -d '{
      "parent": {"page_id": "$PARENT_PAGE_ID"},
      "title": [{"text": {"content": "Knowledge Base"}}],
      "properties": {
        "Title": {"title": {}},
        "Category": {"select": {"options": [{"name": "Concept"}, {"name": "Tutorial"}, {"name": "Reference"}, {"name": "Tips"}]}},
        "Tags": {"multi_select": {"options": []}},
        "Status": {"select": {"options": [{"name": "Draft"}, {"name": "Review"}, {"name": "Published"}]}},
        "Created": {"date": {}},
        "Updated": {"date": {}},
        "URL": {"url": {}}
      }
    }'
}

# Create the enhanced database
echo "Creating enhanced knowledge base database..."
create_knowledge_base_database

# Check if the command succeeded
if [ $? -eq 0 ]; then
  echo "Enhanced database created successfully!"
else
  echo "Failed to create enhanced database."
fi