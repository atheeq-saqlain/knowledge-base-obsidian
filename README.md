# Knowledge Base (Obsidian)

Visual workspace for designing the **Knowledge Tracker** catalog. Draft concepts and questions here, explore relationships in graph/backlinks, then **enter content manually** in the moderator UI.

**There is no automated sync** between this vault and the application database. Obsidian is for authoring and visualization only; the DB is the runtime source of truth for learning.

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

Every concept and question note has a **slug** in frontmatter. Set it when you create the note (manually or via an AI agent).

**Generation logic** (for agents or manual authoring):

1. Start from the **file name** (without `.md`) — e.g. `Contains Duplicates` → `contains-duplicates`
2. Optionally prefix with a **folder / domain** segment — e.g. under `Concepts/Software/` → `software-contains-duplicates` only if you use domain prefixes; otherwise keep the name-based slug
3. Use lowercase kebab-case: trim, lowercase, replace spaces/underscores with `-`, strip punctuation
4. Prefer uniqueness across the vault; if a collision exists, append a short disambiguator from content (e.g. `-2`, or a distinguishing word from the definition/statement)
5. Keep the slug **stable** after the note is published to Knowledge Tracker — do not rename it later

Copy the same slug into the app when you create the concept or question so Obsidian and the DB stay aligned.

## Concept notes

| Section | Purpose |
|---------|---------|
| **Note title** | Human-readable name → `Concept.name` in tracker |
| **Definition** | One precise, generic statement of what the concept *is*. Prefer standalone; add `[[wikilinks]]` only when another concept is **required** to state the definition. Use those links when picking `preRequisitConcepts` in the app |
| **Description** | Elaboration, examples, contexts — **no wikilinks** |

Set any remaining **prerequisites** in Knowledge Tracker when publishing if they are not already linked in the definition.

## Question notes

| Section | Purpose |
|---------|---------|
| **Note title** | Human-readable title |
| **Statement** | What the learner sees |
| **Description** | Examples, constraints, context (optional) |
| **Correct Answer** | Reference solution (optional) |
| **Core Concept** | Single `[[wikilink]]` → `Question.coreConcept` in tracker |
| **Assessment Checklist** | Table: `label`, `weight`, `required`, `role` |

Embed concepts in checklist **labels** with `[[wikilinks]]` for the graph view. In the app, use **plain-text labels** and map concepts in ChecklistEditor to match.

**Checklist options:** `weight` 1 · 2 · 3 · `required` true · false · `role` primary · supporting

## Manual publish workflow

1. Create notes in Obsidian with a **slug** already set; check graph view for links.
2. Add **concepts** in Knowledge Tracker using the same slug, name, definition, description, and prerequisites.
3. Add **questions** using the same slug, statement, core concept, and checklist mappings.
4. Run graph validate after a batch: `POST /knowledge/graph/validate`.

## Templates

Enable **Templates** in Obsidian (folder: `Templates`). See [[Templates/Concept]] and [[Templates/Question]].

## Before adding to the tracker

- [ ] Slug is set and unique
- [ ] Prerequisites form a DAG (no cycles)
- [ ] Every checklist row links to at least one concept; same mapping in ChecklistEditor
- [ ] Checklist labels are observable and specific

## Related

- **knowledge-tracker-server** — API, graph validation (`docs/ARCHITECTURE.md`, `M1.md`)
- **knowledge-tracker-web-client** — ConceptForm, QuestionForm, ChecklistEditor
