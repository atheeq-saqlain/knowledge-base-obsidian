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

## Slug = published indicator

**Slugs are auto-generated** when you create a concept or question in Knowledge Tracker (from name / statement if not supplied).

In Obsidian frontmatter, leave `slug` **empty** while drafting. After you add the item in the app, **copy the generated slug back** into the note. A filled `slug` means that item exists in the database.

Do not change slugs in the app after publish.

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

1. Draft in Obsidian (`slug` empty); check graph view for links.
2. Add **concepts** in Knowledge Tracker → copy returned slug into the concept note.
3. Add **questions** in the tracker → copy slug into the question note.
4. Run graph validate after a batch: `POST /knowledge/graph/validate`.

## Templates

Enable **Templates** in Obsidian (folder: `Templates`). See [[Templates/Concept]] and [[Templates/Question]].

## Before adding to the tracker

- [ ] Prerequisites form a DAG (no cycles)
- [ ] Every checklist row links to at least one concept; same mapping in ChecklistEditor
- [ ] Checklist labels are observable and specific

## Related

- **knowledge-tracker-server** — API, graph validation (`docs/ARCHITECTURE.md`, `M1.md`)
- **knowledge-tracker-web-client** — ConceptForm, QuestionForm, ChecklistEditor
