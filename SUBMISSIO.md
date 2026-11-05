# SUBMISSION — arXiv admission sheet (v1)

**Status: nothing submitted.** Every remaining action on this sheet is
owner-side (account, endorsement, license, final submit). This sheet records
what to upload, the form metadata, and the decisions still open. Version
facts live in `VERSIONS.md`; package layout in `README.md`.

## Upload list (single zip, folder structure preserved)

Exactly the 27 files of `v1_manifest.sha256`:

- `main.tex`
- `main.bbl` — required; the compiled bibliography makes arXiv's build
  independent of `bibtex` runs
- `bibliography.bib` — optional when `main.bbl` is included (harmless to add)
- `sections/` — 10 `.tex` files (`01_introduction` … `10_conclusion`)
- `figures/` — 6 `.pdf` figures (arXiv requires figures; they are referenced
  by the text)
- `supplements/` — `o_ois_ebnf.tex`, `reproducibility.tex`,
  `raw_data.csv` (cited in the paper by the reproducibility appendix:
  `python scripts/export_raw_data.py > supplements/raw_data.csv`)
- `scripts/` — 4 `.py` files (the appendix names these as the reproduction
  entry points, so they ship with the source)

## Do NOT upload

- `main.pdf` — arXiv compiles its own preview from the LaTeX source
- Derived artifacts: `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, `.blg`
- `tables/` — empty; referenced by nothing
- Admin docs — `README.md`, `VERSIONS.md`, this file

## Upload package — READY (machine-verified)

- Artifact: `arxiv_v1_upload.zip` — 272,413 bytes, **27 entries, all
  byte-identical** to `v1_manifest.sha256` (round-trip hash-verified at
  build time), folder layout preserved, `main.tex` at the zip root,
  deterministic entry timestamps (2026-11-05 10:50:59).
- Clean-room compile of exactly the upload set, inside the frozen toolchain
  container (`fedora-toolbox-43`, TeX Live 2023): latexmk **exit 0**,
  0 hard errors, no missing-file notices, **31 pages**, 472,358 bytes;
  `pdftotext` text layer **byte-identical** to the frozen v1 PDF. The fresh
  build's sha256 `7459c95144f36f03cf7a23c5aef602fa4f0de41a731123b9ded4023e83843d30`
  differs from the frozen `58528aeb…e5fa` in the embedded creation timestamp
  only (10:50:59 → 15:31:17 SAST; file sizes equal).
- Staging retained at `/tmp/opencode/upload_pkg` (build log `build_stdout.log`,
  nothing deleted). Original freeze re-verified after packaging: 27 OK / 0 non-OK.

## Form metadata (verbatim from `main.tex`)

| Field | Value |
|---|---|
| Title | Maximum Semantic Capacity via the Ontology of Optimal Information Structure: A Unified Framework Across Visual Encoding and Agent Calibration |
| Author | Ryan St Dare |
| Primary subject | cs.AI |
| Cross-list | cs.CL, cs.IT |
| Keywords | ontology, semantic capacity, knowledge graph encoding, visual glyph, Reed-Solomon, agent calibration, tiered context loading, reproducibility |
| Suggested Comment field | "31 pages, 6 figures. Reproducibility: run-twice-diff-zero checks ship in scripts/verify_reproducibility.py." — a suggestion only; owner edits or drops it |

Preview reference point: the frozen v1 PDF is 31 pages, 472,358 bytes.
ArXiv builds with its own TeX Live release, so minor layout drift in their
preview is possible; content must match.

## Decision flags (owner, before final submit)

1. **Private-repo citations.** The bibliography points to
   `github.com/ttx89-dev/{POINTS, 65536, MSCA}`. Decision history:
   (2026-11-05, earlier) kept private for now — superseded same day —
   (2026-11-05, later) **owner ordered the repositories public — done and
   verified**: API `private=false` × 3, unauthenticated HTTP 200 × 3, after
   a pre-public secret sweep (0 pattern hits across tracked files and git
   history; the flagged `msca/tokens.py` is text tokenization, not auth).
   `65536-backup` deliberately stays private (not cited). The cited URLs
   now resolve; no change to `.bib`/`.bbl` — v1 stands, no v2 required.
2. **Distribution license.** Skeleton intent: paper text CC-BY-4.0 (code
   MIT OR Apache-2.0). The arXiv form asks for a distribution license:
   default non-exclusive vs CC BY 4.0. Owner chooses on the form; this is
   form metadata only and does not alter the frozen source.

## Owner checklist (first-time submitter)

Machine-side steps are complete (upload package built, hash-verified,
clean-room compile-verified — see "Upload package" above). The steps below
require the owner: account creation needs email verification, and
endorsement needs another person.

1. Create an arXiv account and verify email (arxiv.org → Register).
2. Get endorsement in the **primary category cs.AI** (Dashboard →
   endorsement request) — required for first-time submitters.
3. Decide flags 1 and 2 above.
4. Zip the upload list with folder layout preserved (`main.tex` at the zip
   root), submit via Submit an Article: upload → metadata per the table
   above → review arXiv's compiled preview against the frozen facts in
   `VERSIONS.md`.
5. Approval queue → identifier issued. Append the identifier to the v1
   entry in `VERSIONS.md` (additive).
6. Any later correction = **new version (v2, v3, …)** under the same
   identifier — never an edit of v1. Apply peer-feedback revisions as v2 per
   the timeline in `ARXIV_SKELETON.md`.

## Non-submission reminders

- The package is published as its own public repository
  (`O_OIS-arxiv-submit`, 2026-11-05, owner order "have it all out there
  regardless" while cs.AI endorsement is pending). The arXiv submission
  itself is still pending — nothing submitted.
- All numbers on this sheet trace to in-session measured output of
  2026-11-05; see `VERSIONS.md` for the full verification record.
