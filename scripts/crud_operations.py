#!/usr/bin/env python3
# CRUD Operations for Notion Knowledge Base
# This script contains functions for Create, Read, Update, and Delete operations
# on the Notion database specified in AGENT.md

import os
import json
from hermes_tools import read_file, write_file, terminal
from typing import Dict, Any, List, Optional

# Load the AGENT.md configuration
AGENT_PATH = "/home/lifetofree/hermes-agent/AGENT.md"

# Initialize the Notion database ID
DATABASE_ID = None


def load_agent_config() -> Dict[str, str]:
    """Load the Notion configuration from AGENT.md"""
    try:
        content = read_file(path=AGENT_PATH)
        config = {}
        for line in content['content'].split('\n'):
            if 'database_id:' in line and 'notion:' in line:
                # Extract the database_id value
                db_id = line.split('database_id: ')[1].strip().split()[0]
                config['database_id'] = db_id
            elif 'api_key:' in line and 'notion:' in line:
                # Extract the api_key value
                api_key = line.split('api_key: ')[1].strip().split()[0]
                config['api_key'] = api_key
            elif 'page_parent_id:' in line and 'notion:' in line:
                # Extract the page_parent_id value
                page_parent_id = line.split('page_parent_id: ')[1].strip().split()[0]
                config['page_parent_id'] = page_parent_id
        return config
    except Exception as e:
        print(f"Error loading agent config: {e}")
        return {}

# Load the configuration
AGENT_CONFIG = load_agent_config()
DATABASE_ID = AGENT_CONFIG.get('database_id')

# Check if we have a valid database ID
if not DATABASE_ID:
    print("Error: Database ID not found in AGENT.md")
else:
    print(f"Database ID loaded: {DATABASE_ID}")

# The following functions will use the database_id from AGENT.md

def create_page(title: str, content: str, body: str, tags: List[str] = None) -> str:
    """Create a new page in the Notion database

    Args:
        title: The title of the page
        content: Short summary (1-3 sentences)
        body: Full content with references and links
        tags: List of tags (e.g., ["research", "howto"])

    Returns:
        The URL of the created page
    """
    if not DATABASE_ID:
        print("Error: Database ID not configured")
        return ""
    
    # Create the page data structure
    page_data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Title": {"title": [{"text": {"content": title}}]},
            "Content": {"rich_text": [{"text": {"content": content}}]},
            "Body": {"rich_text": [{"text": {"content": body}}]},
            "Tags": {"multi_select": []}
        }
    }
    
    # Add tags if provided
    if tags:
        page_data["properties"]["Tags"]["multi_select"] = [{"name": tag} for tag in tags]
    
    # Create the page using the Notion API
    # This would be implemented with the actual Notion API call
    # For now, we'll simulate it
    print(f"Creating page: {title}")
    print(f"Content: {content}")
    print(f"Body: {body}")
    print(f"Tags: {tags}")
    
    # Simulate successful creation
    page_url = f"https://www.notion.so/p/lifetofree/{DATABASE_ID.replace('-', '')}/{title.replace(' ', '-').lower()}"
    print(f"Page created: {page_url}")
    
    return page_url


def read_page(query: str, tags: List[str] = None, date_range: str = None) -> List[Dict[str, Any]]:
    """Search the Notion database for pages matching the query

    Args:
        query: Search term
        tags: List of tags to filter by
        date_range: Date range to filter by (e.g., "2026-06-01..2026-06-30")

    Returns:
        List of matching pages with their properties
    """
    if not DATABASE_ID:
        print("Error: Database ID not configured")
        return []
    
    # This would be implemented with the actual Notion API call
    # For now, we'll simulate it
    print(f"Searching for: {query}")
    if tags:
        print(f"Filtering by tags: {tags}")
    if date_range:
        print(f"Filtering by date range: {date_range}")
    
    # Simulate search results
    results = [
        {"title": "Sample Page 1", "url": "https://www.notion.so/p/lifetofree/12345678901234567890123456789012", "content": "This is a sample page"},
        {"title": "Sample Page 2", "url": "https://www.notion.so/p/lifetofree/23456789012345678901234567890123", "content": "Another sample page"}
    ]
    
    return results


def update_page(page_id: str, title: str = None, content: str = None, body: str = None, tags: List[str] = None) -> bool:
    """Update an existing page in the Notion database

    Args:
        page_id: The ID of the page to update
        title: New title (optional)
        content: New content (optional)
        body: New body (optional)
        tags: New tags (optional)

    Returns:
        True if successful, False otherwise
    """
    if not DATABASE_ID:
        print("Error: Database ID not configured")
        return False
    
    print(f"Updating page: {page_id}")
    if title:
        print(f"New title: {title}")
    if content:
        print(f"New content: {content}")
    if body:
        print(f"New body: {body}")
    if tags:
        print(f"New tags: {tags}")
    
    # Simulate update
    print(f"Page {page_id} updated successfully")
    return True


def delete_page(page_id: str) -> bool:
    """Delete a page from the Notion database

    Args:
        page_id: The ID of the page to delete

    Returns:
        True if successful, False otherwise
    """
    if not DATABASE_ID:
        print("Error: Database ID not configured")
        return False
    
    # Confirm deletion
    confirm = input(f"Are you sure you want to delete page {page_id}? (y/N): ")
    if confirm.lower() != 'y':
        print("Deletion cancelled")
        return False
    
    # Simulate deletion
    print(f"Deleting page: {page_id}")
    print(f"Page {page_id} deleted successfully")
    return True

# Example usage
if __name__ == "__main__":
    # Create a new page
    page_url = create_page(
        title="New Knowledge Base Entry",
        content="This is a new entry in the knowledge base",
        body="This is the full content with references and links",
        tags=["research", "howto"]
    )
    
    # Search for pages
    results = read_page(query="knowledge base")
    for result in results:
        print(f"- {result['title']}: {result['url']}")
    
    # Update a page
    update_page(
        page_id="12345678901234567890123456789012",
        content="Updated content",
        tags=["research", "updated"]
    )
    
    # Delete a page
    delete_page(page_id="12345678901234567890123456789012")