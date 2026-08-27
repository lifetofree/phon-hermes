#!/bin/bash

# Create a Notion database
# This script creates a database in your Notion workspace

# Set the parent page ID (from your Notion URL)
PARENT_PAGE_ID="3c7df8d88d8c801c87f9e845700178af"

# Use the existing NOTION_API_KEY from environment
export NOTION_TOKEN="$NOTION_API_KEY"

# Create the database using the Notion API
curl -s https://api.notion.com/v1/databases \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": { "page_id": "'$PARENT_PAGE_ID'" },
    "title": [{ "text": { "content": "UDO Knowledge Base" } }],
    "is_inline": true,
    "properties": {
      "Name": { "title": {} },
      "Content": { "rich_text": {} },
      "Tags": { "multi_select": { "options": [
        { "name": "research",  "color": "blue" },
        { "name": "howto",     "color": "green" },
        { "name": "reference", "color": "purple" },
        { "name": "note",      "color": "gray" }
      ]}},
      "Type": { "select": { "options": [
        { "name": "article", "color": "blue" },
        { "name": "snippet", "color": "orange" },
        { "name": "task",    "color": "red" }
      ]}},
      "Date": { "date": {} }
    }
  }' | python3 -m json.tool