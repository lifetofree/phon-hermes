# Notion API transport pitfalls (adduckivity workspace, API-Version 2022-06-28)

## Pagination — route by endpoint, not by habit

- True-GET list endpoints — `GET /v1/blocks/{page_id}/children`, `/v1/users`, `/v1/search` — take `page_size`/`start_cursor` ONLY as query-string params. Attaching a JSON body converts the request into POST; for blocks/children, POST means APPEND-blocks, which rejects pagination keys with a 400. A request helper that always attaches a body silently converts GETs into POSTs — branch on endpoint before paginating.
- `POST /v1/databases/{id}/query` is the mirror: in this workspace it has 400'd on `page_size` in BOTH the body and the query string — send body `{}`; when the database holds ≤100 rows the default response returns everything, so pagination keys are not needed at all.
- Loop shape for read-backs: keep fetching while `has_more` is true, passing `start_cursor = next_cursor` — query string for the GET endpoints, body for POST endpoints that accept it. Never send a body and still expect GET semantics.
