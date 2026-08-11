# Knowledge Base (Obsidian)

Visual workspace for designing the **Knowledge Tracker** catalog. Draft concepts and questions here, explore relationships in graph/backlinks, then sync into MongoDB by **slug**.

Obsidian is the authoring / visualization layer. The DB is the runtime source of truth for learning. Sync is **one-way**: vault → MongoDB (upsert by slug).

## What you're modeling

- **Concepts** — reusable knowledge units, linked by prerequisites (DAG), with an optional cognitive **`kind`**
- **Questions** — assessable items with a checklist; each row maps to concepts
- **Syllabi** — ordered learning paths (usually list **schemas**, not every foundation)

### Concept kinds

| `kind` | Meaning | DSA examples |
|--------|---------|--------------|
| `fact` | Declarative knowledge | Rare in Blind 75; optional |
| `representation` | Data shape / mental model | Array, Hashmap, String, Binary Tree |
| `operation` | Small executable move | Recursion |
| `schema` | Reusable “when I see X, do Y” pattern — **prefer as question `coreConcept`** | Complement Lookup, Sliding Window, DFS |
| `principle` | Why / when / tradeoffs | Pair-sum Complement Reduction, Window Validity Invariant |

Frontmatter:

```yaml
---
slug: dsa-sliding-window
kind: schema
---
```

BKT and frontier treat all kinds equally. Kinds are for authoring filters and progress labeling.

## Layout

```text
Concepts/          # one note per concept (human-readable file name = display name)
Questions/         # one note per question
Syllabi/           # learning paths (ordered chapters → sections → concepts/questions)
Templates/
  Concept.md
  Question.md
  Syllabus.md
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

| Section / field | Purpose |
| --------------- | ------- |
| **Note title**  | Human-readable name → `Concept.name` |
| **`kind`**      | See table above → `Concept.kind` |
| **Definition**  | Precise, generic statement. Prefer standalone; add `[[wikilinks]]` only when another concept is **required**. Those links become `preRequisitConcepts` on sync |
| **Description** | Elaboration and examples — **no wikilinks** |

## Question notes

| Section                  | Purpose                                        |
| ------------------------ | ---------------------------------------------- |
| **Note title**           | Human-readable title                           |
| **Statement**            | What the learner sees                          |
| **Description**          | Examples, constraints, context (optional)      |
| **Correct Answer**       | Reference solution (optional)                  |
| **Core Concept**         | Single `[[wikilink]]` → prefer a **schema**    |
| **Assessment Checklist** | Table: `label`, `weight`, `required`, `role`   |

Embed concepts in checklist **labels** with `[[wikilinks]]`. On sync, links become `assessmentChecklist[].concepts`; labels are stored as plain text (wikilinks stripped). `referredConcepts` is derived from checklist concepts minus core.

**Checklist options:** `weight` 1 · 2 · 3 · `required` true · false · `role` primary · supporting

Primary items should map mainly to the schema; representations/operations/principles as supporting when useful.

## Syllabus notes

Institutional learning paths (board/grade ordering). Not part of the knowledge catalog graph — they order existing concepts and questions for enrollment / next-question ranking.

| Section / field | Purpose                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------- |
| **Note title**  | → `Syllabus.name`                                                                               |
| **slug**        | Stable join key (e.g. `dsa-blind-75`)                                                           |
| **label**       | Short code                                                                                      |
| **grade**       | Grade / audience label                                                                          |
| **status**      | `draft` \| `active`                                                                             |
| **Summary**     | Description of the path                                                                         |
| **Chapters**    | `### Chapter` → `#### Section` → optional **Concepts** / **Questions** lists of `[[wikilinks]]` |

Order within each section is learning order. Prerequisites still come from the concept graph. List **schemas** (and selected principles) under section Concepts; foundations show under progress → “Show foundations”.

## Sync to Knowledge Tracker

From `knowledge-tracker-server`:

```bash
# .env
OBSIDIAN_VAULT_PATH=D:/obsidian/knowledge-base-obsidian
DATABASE_URL=...

npm run sync-obsidian
```

Optional one-shot retag helper (already applied for Blind 75): `node scripts/retag-blind75-kinds.js`
