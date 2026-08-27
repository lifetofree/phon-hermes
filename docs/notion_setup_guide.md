# Notion API Integration Setup Guide

## Step 1: Create a New Integration

1. Go to https://notion.so/my-integrations
2. Click on "Develop or Manage Integrations"
3. Click "New integration"
4. Enter a name for your integration (e.g., "Hermes Agent Integration")
5. Select the "Notion API" capability
6. Click "Create token"
7. Copy the generated API key (it starts with "ntn_" or "secret_")

## Step 2: Update Your .env File

1. Open your `.env` file:
   ```bash
   nano ~/.hermes/.env
   ```
2. Find the `NOTION_API_KEY` line
3. Replace the current value with your new API key
4. Save and close the file (Ctrl+X, then Y, then Enter)

## Step 3: Verify Your Setup

1. Check if the API key is set:
   ```bash
   env | grep NOTION_API_KEY
   ```
2. Try to create a database using the template:
   ```bash
   curl -s -X POST "https://api.notion.com/v1/data_sources" \
     -H "Authorization: Bearer $NOTION_API_KEY" \
     -H "Notion-Version: 2025-09-03" \
     -H "Content-Type: application/json" \
     -d @/home/lifetofree/database_template.json
   ```

## Step 4: Create Your Database

Once the API key is working, you can create your database. The database template is already in `/home/lifetofree/database_template.json`. After updating your API key, run the curl command above to create the database in your Notion workspace.

## Troubleshooting

If you still get an error:
- Make sure the integration has been shared with the target page in Notion
- Check that the page ID in the template is correct
- Verify that the API key has the necessary permissions

For more information, see the official Notion API documentation: https://developers.notion.com