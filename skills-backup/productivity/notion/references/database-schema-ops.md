# Database schema operations (Notion API)

When to use: the owner asks to create a database, change a property's type, wire a relation with a back-reference, add per-row aggregates (rollups), or remove/rename columns — anything past simply adding new properties.

Class recipe for reshaping a Notion database via API: create a DB, add/rename/remove properties, relations with a synced reverse, rollups. Examples use the 2022-06-28 family (`PATCH /v1/databases/{database_id}`, relation config carries `database_id`); on 2025-09-03 the same shapes apply to `PATCH /v1/data_sources/{data_source_id}` with `data_source_id` in relation configs (see SKILL.md API Version section for the version split).

## Create a database
- `POST /v1/databases` with `parent: {"page_id": "<full id>"}` — page ids in owner-sent links are shortened; resolve the full id first (search or GET the parent).
- Property `type: "status"` cannot be created via API — use `select` instead (Kanban groups by select equally well).
- Views (Board/Calendar) are UI-only: hand the owner the one-time click (Layout → Board → Group by).
- Seed one example row and say it is deletable — the owner immediately sees the fill pattern and which fields are theirs to complete.

## Property types are IMMUTABLE
A PATCH on a property changes only `name` and `description`. "Turn Client (rich text) into a relation" has no direct API call — migrate:
1. Read every row's old values (query the DB first — after removal they are gone).
2. Create the NEW property via `PATCH properties`.
3. PATCH each row to set the new property from the old value.
4. Remove the old property: `PATCH /v1/databases/{id}` with `"properties": {"Client": null}` — setting a property to null DELETES it and its data, so migrate first.
- Before removing, grep all consumers (cron scripts, bot prompts, watcher rules) for the property name.

## Relations
- `single_property` is ONE-SIDED: it creates no property on the destination database, so any destination-side rollup referencing the relation fails later. Use `dual_property` when the destination needs a back-reference or rollup:
  `{"relation": {"database_id": "<dest>", "type": "dual_property", "dual_property": {"synced_property_name": "งาน"}}}`
- The synced reverse property appears on the destination automatically; RENAME it (e.g. to "งาน") in a SEPARATE PATCH afterwards — bundling rename + rollup creation in one PATCH fails validation while the name is mid-flight.
- Rollups are added in their own PATCH only AFTER the synced reverse exists; sequence dependent PATCHes with a short sleep and verify each.
- 2025-09-03: relations additionally require the integration to READ the destination data source (see SKILL.md).

## Rollups
- `rollup_property_name` is REQUIRED even for `count_values` (which ignores it): `{"rollup": {"relation_property_name": "งาน", "rollup_property_name": "Price", "function": "count_values"}}` — omitting it fails with "rollup_property_name should be defined, instead was `undefined`".
- The rolled property must exist on the DESTINATION database (e.g. Price lives on Job Desk when a customer-level rollup sums jobs' prices).

## Verify after schema surgery
- A 400 in a multi-property PATCH aborts the WHOLE body — none of it lands. Sequence dependent steps individually and re-GET both databases at the end, diffing the property list against intent before reporting done.
- Read each row's post-migration property values (not just schema) when migrating data — a relation PATCH that returns 200 can still point at the wrong row id.
