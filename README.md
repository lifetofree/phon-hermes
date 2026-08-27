# Notion Database Creation Scripts

This directory contains scripts and configuration files for creating a Notion database for your knowledge base.

## Files

- `create-notion-database.sh` - Bash script to create a Notion database
- `notion-config.json` - Configuration file for the database properties
- `README.md` - This file

## Prerequisites

1. Install the `ntn` CLI (Notion's official CLI):
   ```bash
   curl -fsSL https://ntn.dev | bash
   ```

2. Set the required environment variables in your `~/.hermes/.env` file:
   ```bash
   NOTION_TOKEN=ntn_your_key_here
   PARENT_PAGE_ID=your_parent_page_id
   ```

## Usage

1. Make the script executable:
   ```bash
   chmod +x create-notion-database.sh
   ```

2. Run the script:
   ```bash
   ./create-notion-database.sh
   ```

The script will create a Notion database with the properties defined in the configuration file. You can modify the `notion-config.json` file to customize the database structure.

## Customization

You can modify the `notion-config.json` file to change the database properties, add new fields, or change the default values. The script will use these settings when creating the database.

## Troubleshooting

If you encounter any issues, check the following:

1. Ensure that the `NOTION_TOKEN` environment variable is set correctly
2. Verify that the `PARENT_PAGE_ID` points to a valid Notion page
3. Make sure you have the necessary permissions to create a database in the target page
4. Check the Notion API documentation for any changes to the endpoint structure

For more information about the Notion API, visit: https://developers.notion.com
