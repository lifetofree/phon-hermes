#!/bin/bash
# อ่าน properties + children ของการ์ด Idea e-book Rakazo (ผ่าน env NOTION_TOKEN)
CARD="41bdf8d8-8d8c-813f-914c-dd2711a99b4e"
AUTH="Authorization: Bearer ${NOTION_TOKEN}"
H="Notion-Version: 2022-06-28"
echo "=== PROPERTIES ==="
curl -s "https://api.notion.com/v1/pages/${CARD}" -H "$AUTH" -H "$H" | jq -r '.properties | to_entries[] | "\(.key) [\(.value.type)]: \(if .value.type=="select" then .value.select.name elif .value.type=="status" then .value.status.name elif .value.type=="title" or .value.type=="rich_text" then (.value|(.title // .rich_text)|map(.plain_text)|join("")) elif .value.type=="date" then .value.date.start else "?" end)"'
echo "=== CHILDREN ==="
curl -s "https://api.notion.com/v1/blocks/${CARD}/children?page_size=100" -H "$AUTH" -H "$H" | jq -r '.results[] | select(.has_children == false or true) | [.type, ((.paragraph.rich_text // .toggle.rich_text // .quote.rich_text // .callout.rich_text // .bulleted_list_item.rich_text // .numbered_list_item.rich_text // .to_do.rich_text // .heading_2.rich_text // .heading_3.rich_text // []) | map(.plain_text) | join(""))] | join(" :: ")'
