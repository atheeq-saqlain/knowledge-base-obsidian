# Knowledge Base (Obsidian)

Visual workspace for designing the **Knowledge Tracker** catalog. Draft concepts and questions here, explore relationships in graph/backlinks, then sync into MongoDB by **slug**.

Obsidian is the authoring / visualization layer. The DB is the runtime source of truth for learning. Sync is **one-way**: vault → MongoDB (upsert by slug).

## What you're modeling

- **Concepts** — reusable skills, linked by prerequisites (DAG)
- **Questions** — assessable items with a checklist; each row maps to concepts

## Layout

```text
Concepts/          # one note per concept (human-readable file name = display name)
Questions/         # one note per question
Templates/
  Concept.md
  Question.md
```

## Slugs

Every concept and question note has a **slug** in frontmatter. Set it when you create the note (manually or via an AI agent). Slugs are the join key for sync.

**Generation logic** (for agents or manual authoring):

1. Start from the **file name** (without `.md`) — e.g. `Contains Duplicates` → `contains-duplicates`
2. Optionally prefix with a **folder / domain** segment — e.g. under `Concepts/DSA/` → `dsa-contains-duplicates`
3. Use lowercase kebab-case: trim, lowercase, replace spaces/underscores with `-`, strip punctuation
4. Prefer uniqueness across the vault; if a collision exists, append a short disambiguator
5. Keep the slug **stable** after sync — do not rename it later

## Concept notes

| Section | Purpose |
|---------|---------|
| **Note title** | Human-readable name → `Concept.name` |
| **Definition** | Precise, generic statement. Prefer standalone; add `[[wikilinks]]` only when another concept is **required**. Those links become `preRequisitConcepts` on sync |
| **Description** | Elaboration and examples — **no wikilinks** |

## Question notes

| Section | Purpose |
|---------|---------|
| **Note title** | Human-readable title |
| **Statement** | What the learner sees |
| **Description** | Examples, constraints, context (optional) |
| **Correct Answer** | Reference solution (optional) |
| **Core Concept** | Single `[[wikilink]]` → `Question.coreConcept` |
| **Assessment Checklist** | Table: `label`, `weight`, `required`, `role` |

Embed concepts in checklist **labels** with `[[wikilinks]]`. On sync, links become `assessmentChecklist[].concepts`; labels are stored as plain text (wikilinks stripped). `referredConcepts` is derived from checklist concepts minus core.

**Checklist options:** `weight` 1 · 2 · 3 · `required` true · false · `role` primary · supporting

## Sync to Knowledge Tracker

From `knowledge-tracker-server`:

```bash
# .env
OBSIDIAN_VAULT_PATH=D:/obsidian/knowledge-base-obsidian

npm run sync-obsidian:dry   # preview
npm run sync-obsidian       # upsert concepts + questions by slug
```

Or:

```bash
node scripts/sync-obsidian-vault.js --vault "D:/obsidian/knowledge-base-obsidian"
```

**What sync does:**

1. Upsert all `Concepts/**/*.md` by `slug` (name, definition, description)
2. Convert Markdown sections → **HTML** for RichTextEditor (`definition`, `description`, `statement`, `correctAnswer`)
3. Set `preRequisitConcepts` from `[[wikilinks]]` in Definition
4. Upsert all `Questions/**/*.md` by `slug` (statement, description, correctAnswer, coreConcept, checklist)
5. Run graph validation

Checklist labels stay plain text (wikilinks stripped) for ChecklistEditor. Rich fields use the same Markdown→HTML path as pasting into the editor.

## Templates

Enable **Templates** in Obsidian (folder: `Templates`). See [[Templates/Concept]] and [[Templates/Question]].

## Before syncing

- [ ] Slug is set and unique on every note
- [ ] Prerequisites form a DAG (no cycles)
- [ ] Every checklist row links to at least one concept
- [ ] Checklist labels are observable and specific

## Related

- **knowledge-tracker-server** — `scripts/sync-obsidian-vault.js`, graph validation
- **knowledge-tracker-web-client** — ConceptForm, QuestionForm, ChecklistEditor
