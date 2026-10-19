---
name: fix-catalog-review
description: >-
  Fixes flagged Knowledge Tracker catalog notes from a moderator export prompt.
  Use when the user pastes a catalog-review export, asks to process flagged
  questions/concepts, or run fix-catalog-review on review markdown.
---

# Fix catalog review

## When to use

User provides a catalog review export (markdown/JSON) or asks to fix flagged vault notes by `code`.

## Steps

1. Read each flagged item: `targetCode`, path, issue types, comments.
2. Open the vault note (`Concepts/` or `Questions/`). Find by path or by frontmatter `code`.
3. Apply minimal edits that address the comments. Preserve `code`.
4. Keep note structure aligned with Templates and README (sections, checklist table).
5. Set frontmatter `status: ai_fixed` (never `approved`).
6. Reply with: code, path, what changed, any remaining risks.

## Do not

- Set `status: approved`
- Change `code` or rename only to “fix” links
- Add board/grade into `Concepts/` or `Questions/` paths
- Modify MongoDB or sync scripts unless asked

## Status cycle

`flagged` → (you fix) → `ai_fixed` → moderator approves or flags again in the web app.
