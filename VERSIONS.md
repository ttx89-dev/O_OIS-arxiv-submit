# VERSIONS — paper version ledger (additive)

One entry per paper version. Frozen bytes are never edited: any content change
is a rebuild and therefore a NEW version, published here with its own identity
block, hashes, freshness gate and manifest reference. The admin docs
(`README.md`, `SUBMISSION.md`) are records, not paper content — editing them
never touches a frozen version.

---

## v1 — established 2026-11-05

**Status:** frozen, verified, **not yet submitted** (owner-side actions: `SUBMISSION.md`).

### Identity

| Field | Value | Source |
|---|---|---|
| Title | Maximum Semantic Capacity via the Ontology of Optimal Information Structure: A Unified Framework Across Visual Encoding and Agent Calibration | `main.tex` `\title` (lines 45–47); verified on PDF page 1 |
| Author | Ryan St Dare | `main.tex` `\author`; `pdfauthor`; PDF page 1 |
| Title-page date | November 5, 2026 | `\date{\today}` rendered at build |
| Subject classes | cs.AI (primary), cs.CL, cs.IT (cross-list) | `pdfsubject`; skeleton target venue (line 3) |
| Keywords | ontology, semantic capacity, knowledge graph encoding, visual glyph, Reed-Solomon, agent calibration, tiered context loading, reproducibility | `pdfkeywords` (line 24) |

### Build facts (measured)

- Artifact: `main.pdf` — 472,358 bytes, 31 pages.
- Created: Thu Nov 5 10:50:59 2026 SAST (`pdfinfo` CreationDate).
- Engine: pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023), format preloaded
  `pdflatex 2026.11.3` (`main.log` banner, 5 NOV 2026 10:50).
- Toolchain location: distrobox container `fedora-toolbox-43`
  (registry.fedoraproject.org/fedora-toolbox:43). Verified inside the
  container: `/usr/bin/pdflatex`, `/usr/bin/latexmk`, `/usr/bin/bibtex` —
  `pdflatex --version` reports pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023),
  matching `main.log` exactly. The host shell has no TeX binaries. Distrobox
  shares the home directory, so the build path is identical inside the container.
- Build command: `make pdf` (Makefile → `latexmk -pdf -interaction=nonstopmode
  -halt-on-error -file-line-error main.tex`).

### Identity hashes

- sha256: `58528aeb3c2f45ce495f2b17a4ec39e72292fc2a86863bf62c272f01e869e5fa`
- md5: `4cea3d98f175051f624dd4b2dc5617bc`

### Verification record — 2026-11-05, all from live in-session output

1. **Freshness gate PASS** — `main.pdf` (10:50:59) is newer than the newest
   source edit measured among `main.tex`, `sections/*.tex`, `bibliography.bib`
   (newest: `main.tex` at 10:50:51). The PDF matches the current source tree.
2. **Reproducibility ALL PASS** —
   `python3 scripts/verify_reproducibility.py`: POINTS run twice, exit 0 × 2,
   outputs identical; MSCA gates run twice, exit 0 × 2, outputs identical;
   `RESULT: ALL PASS`.
3. **Stale-token sweep nil** — `pdftotext main.pdf`: **0** hits for `mcsa`;
   **0** hits for `vexl-points` / `624 tok` (no pre-rename residue anywhere in
   the compiled paper).
4. **Appendix truth** — reproducibility appendix cites the current engines:
   `python -m msca.gates`; `--capacity --verify` → MATCHES code; `--summary` →
   resident 621 tokens / budget 640; POINTS 94 tests + 42 subtests, golden
   corpus 7 entries, 14 red-team patterns.
5. **Source freeze** — `v1_manifest.sha256`: 27 files (main.tex, main.bbl,
   bibliography.bib, Makefile; sections 10; figures 6; supplements 2 tex +
   1 csv; scripts 4). Verified twice today: **27 OK / 0 non-OK**. Excluded by
   design: derived build artifacts (`.aux .log .out .fls .fdb_latexmk .blg`,
   and `main.pdf` itself — it is pinned by the identity block above, not the
   manifest) and the admin docs in this directory. `tables/` is empty and
   inert (`main.tex` references no table file).
   Re-verify at any time: `sha256sum -c v1_manifest.sha256`.

### Submission packaging — 2026-11-05 (post-freeze, additive)

- Owner decision recorded: the repositories cited in the bibliography stay
  **private for now** ("do not yet make public") — `.bib`/`main.bbl`
  untouched, v1 stands, no v2 required.
- Upload package: `arxiv_v1_upload.zip` — 272,413 bytes, 27 entries,
  byte-identical round-trip against `v1_manifest.sha256`, deterministic
  entry timestamps, `main.tex` at the zip root.
- Clean-room compile of exactly the upload set inside the frozen toolchain
  container (`fedora-toolbox-43`, TeX Live 2023): latexmk exit 0, 0 hard
  errors, 31 pages, 472,358 bytes; `pdftotext` text layer **byte-identical**
  to the frozen v1. Fresh-build sha256
  `7459c95144f36f03cf7a23c5aef602fa4f0de41a731123b9ded4023e83843d30`
  (md5 `bb756efaaf256c8ef9614c48773937eb`) — equal to the frozen build in
  everything but the embedded creation timestamp (10:50:59 → 15:31:17 SAST).
- Original freeze re-verified after packaging: 27 OK / 0 non-OK. Staging
  material retained (never-delete rule).
- Decision superseded same day (later): owner ordered the cited repositories
  public. Executed and verified — API `private=false` × 3, unauthenticated
  HTTP 200 × 3 — after a pre-public secret sweep (0 pattern hits in tracked
  files and git history). Not a source change: `.bib`/`.bbl` untouched, so
  v1 stands with no v2 required. Only flag 1 of `SUBMISSION.md` remains
  resolved; flag 2 (license) is still an owner at-form choice.
- Publication (2026-11-05, owner order "have it all out there regardless",
  cs.AI endorsement pending): the package became its own public repository
  `O_OIS-arxiv-submit` — frozen v1 sources, admin docs, upload zip; committed
  in place (`arxiv_submission/`), pushed to
  https://github.com/ttx89-dev/O_OIS-arxiv-submit and verified
  unauthenticated. The git boundary truth: this directory is the repo; the
  projects-root repo does not track it.

### Update policy

1. Frozen bytes of v1 are never edited in place.
2. Any content change → rebuild → **NEW version** → new entry in this file
   with: identity block, sha256 + md5, freshness gate (PDF newer than newest
   measured source), manifest reference (amended or new file), verification
   record. A rebuild reproduces content, not bytes — `CreationDate` and tool
   release lines differ — so byte identity of the artifact is not expected
   across toolchains; the identity block pins the delivered bytes, the
   manifest pins the sources.
3. Post-submission, arXiv performs no in-place PDF updates: corrections ship
   as **new versions (v2, v3, …)** under the same identifier. v1 is permanent;
   arXiv displays the newest version. Peer-feedback revisions are applied as
   v2 per the timeline in `ARXIV_SKELETON.md` (the doc that also governs the
   original timeline).
4. After any submission event, append the arXiv identifier and status line to
   this v1 entry (and to future entries). Additive only.
