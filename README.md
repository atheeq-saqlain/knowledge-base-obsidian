# Knowledge Base (Obsidian)

Visual workspace for designing the **Knowledge Tracker** catalog. Draft concepts and questions here, explore relationships in graph/backlinks, then sync into MongoDB by **slug**.

Obsidian is the authoring / visualization layer. The DB is the runtime source of truth for learning. Sync is **one-way**: vault → MongoDB (upsert by slug).

## What you're modeling

- **Concepts** — reusable knowledge units, linked by prerequisites (DAG), with an optional cognitive **`kind`**
- **Questions** — assessable items with a checklist; each row maps to concepts
- **Syllabi** — board/grade learning paths that *order* existing concepts and questions

Concepts and questions are **shared across syllabi**. A Class 10 KSEEB path and a CBSE path both wikilink `[[nth Term of an AP]]`; they do not get separate copies of the note.

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
Concepts/<Subject>/<Domain>/<optional Subdomain>/<Note>.md
Questions/<Subject>/<Domain>/<optional Subdomain>/<Note>.md
Syllabi/            # institutional paths (board × grade × subject)
Templates/
  Concept.md
  Question.md
  Syllabus.md
```

`<Subject>` is the discipline (`Maths`, `Physics`, `Chemistry`, `Biology`, `DSA`, `Networking`, …). The same rules apply to every subject.

### Folder rules (all subjects)

Folders describe **where the knowledge sits in the discipline**, not which textbook, board, or grade taught it.

1. **Subject / Domain / Subdomain** — at most three levels under `Concepts/` or `Questions/`. Do not add a fourth.
2. **Name domains in the language of the subject**, not a syllabus unit title. Prefer `Algebra`, `Mechanics`, `Organic Chemistry`, `Cell Biology` over “Chapter 3” or a single board’s heading.
3. **Never put board, grade, or exam names in the path** (`KSEEB`, `CBSE`, `Grade 10`, `NEET`, `JEE`, `GCSE`). Those belong only in `Syllabi/`.
4. **One note, many syllabi.** If two courses teach the same idea, they link the same file.
5. **Questions follow the core concept.** A question lives in the same `<Subject>/<Domain>/…` folder as the concept in its **Core Concept** wikilink — even if the wording comes from one particular textbook.
6. **Create a subdomain only when a domain is a mixed pile** (about 15+ concepts, or two clearly different clusters). Do not pre-create empty “future chapter” folders.
7. **Home a note by what it is about**, not the chapter that introduced it. A construction of tangents lives under geometry of circles; an area-of-a-sector formula lives under measurement.
8. **Filenames stay unique vault-wide** so `[[Note Title]]` wikilinks keep working. The `#` heading matches the file name.

### When to add a subdomain

| Level | Question it answers | Examples |
| ----- | ------------------- | -------- |
| Subject | Which discipline? | `Maths`, `Physics`, `Chemistry`, `Biology`, `DSA` |
| Domain | Which strand of that discipline? | `Algebra`, `Mechanics`, `Organic Chemistry` |
| Subdomain | Which cluster inside a large strand? | `Algebra/Sequences and Series`, `Mechanics/Kinematics` |

Stop at subdomain. Education level is never a folder.

### Examples

```text
Concepts/Maths/Algebra/Sequences and Series/nth Term of an AP.md
Concepts/Maths/Geometry/Circles/Tangent to a Circle.md
Concepts/Physics/Mechanics/Kinematics/Displacement.md
Concepts/Chemistry/Physical Chemistry/Stoichiometry/Mole Concept.md
Concepts/Biology/Cell Biology/Cell Structure/Mitochondrion.md
Concepts/DSA/Sliding Window.md
```

Suggested Maths domains (add others when the first note needs them): `Number`, `Algebra`, `Geometry`, `Measurement`, `Analytic Geometry`, `Trigonometry`, `Calculus`, `Statistics`, `Probability`, `Discrete Mathematics`, `Linear Algebra`.

Suggested peers for other subjects (illustrative, not mandatory): Physics — `Mechanics`, `Waves`, `Electricity and Magnetism`, `Thermal Physics`, `Modern Physics`; Chemistry — `Physical Chemistry`, `Inorganic Chemistry`, `Organic Chemistry`; Biology — `Cell Biology`, `Genetics`, `Physiology`, `Ecology`, `Evolution`.

DSA may stay flat under `Concepts/DSA/` until a cluster (for example graphs vs DP) is large enough to split.

## Slugs

Every concept and question note has a **slug** in frontmatter. Set it when you create the note. Slugs are the join key for sync.

**Generation logic** (for agents or manual authoring):

1. Take the path under `Concepts/` or `Questions/`, without the extension.
2. Slugify **each** segment (lowercase kebab-case: trim, replace spaces with `-`, strip punctuation).
3. Join segments with `-`.

```text
Concepts/Maths/Algebra/Sequences and Series/nth Term of an AP.md
→ maths-algebra-sequences-and-series-nth-term-of-an-ap

Questions/Physics/Mechanics/Kinematics/SUVAT Horizontal Throw.md
→ physics-mechanics-kinematics-suvat-horizontal-throw

Concepts/DSA/Sliding Window.md
→ dsa-sliding-window
```

4. Prefer uniqueness across the vault; if a collision exists, append a short disambiguator.
5. If you **move** a note to a new folder, update the slug to match the new path. Sync can still match an existing DB concept by **name** (and a question by **statement**) so a slug rename does not create a duplicate — but matching by slug is the steady state, so keep path and slug aligned.
6. Do not encode board or grade in the slug (`maths-kseeb-10-ap` is wrong).

Syllabus slugs stay independent of the catalog tree (e.g. `karnataka-10-maths`, `dsa-blind-75`).

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

Place the question file next to its core concept’s topic folder.

## Syllabus notes

Institutional learning paths (board, grade, exam, course). This is the **only** layer that encodes “who learns this, in what order.” It is not part of the knowledge-catalog graph.

| Section / field | Purpose                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------- |
| **Note title**  | → `Syllabus.name`                                                                               |
| **`slug`**      | Stable join key (e.g. `dsa-blind-75`, `karnataka-10-maths`)                                     |
| **`label`**     | Short code                                                                                      |
| **`grade`**     | Grade / audience label                                                                          |
| **`status`**    | `draft` \| `active`                                                                             |
| **Summary**     | Description of the path                                                                         |
| **Chapters**    | `### Chapter` → `#### Section` → optional **Concepts** / **Questions** lists of `[[wikilinks]]` |

Order within each section is learning order. Prerequisites still come from the concept graph. List **schemas** (and selected principles) under section Concepts; foundations show under progress → “Show foundations”.

Multiple syllabus notes may link the same catalog files. Add a new board or grade by adding a syllabus, not by copying concepts into a new folder.

## Sync to Knowledge Tracker

From `knowledge-tracker-server`:

```bash
# .env
OBSIDIAN_VAULT_PATH=D:/obsidian/knowledge-base-obsidian
DATABASE_URL=...

npm run sync-obsidian
```

If a note has no `slug` in frontmatter, sync derives one from its path under `Concepts/` or `Questions/`. Prefer setting the slug explicitly so it stays stable.

Optional one-shot retag helper (already applied for Blind 75): `node scripts/retag-blind75-kinds.js`
