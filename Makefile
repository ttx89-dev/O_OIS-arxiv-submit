# ============================================================
# Makefile for ONE ArXiv Submission
# ============================================================

.PHONY: all pdf clean figures supplements check help

# Default target
all: pdf

# Main PDF target
pdf: main.pdf

main.pdf: main.tex sections/*.tex figures/*.pdf supplements/o_ois_ebnf.tex supplements/reproducibility.tex bibliography.bib
	@echo "Building PDF with latexmk..."
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
	@echo "PDF built: main.pdf"

# Generate all figures
figures:
	@echo "Generating figures..."
	python3 scripts/generate_figures.py

# Generate supplements (EBNF appendix is hand-written; raw data CSV is generated)
supplements:
	@echo "Generating supplements (raw data only)..."
	python3 scripts/export_raw_data.py > supplements/raw_data.csv
	@echo "o_ois_ebnf.tex is hand-written and will NOT be overwritten."
	@echo "Re-run extract_ebnf.py manually if you need the old generated appendix."

# Verify reproducibility (run-twice-diff-zero on all repos)
check:
	@echo "Verifying reproducibility..."
	python3 scripts/verify_reproducibility.py

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	latexmk -C
	rm -f *.aux *.bbl *.blg *.fdb_latexmk *.fls *.log *.out *.toc *.synctex.gz *.run.xml
	rm -f supplements/raw_data.csv

# Clean everything including generated figures
clean-all: clean
	rm -f figures/*.pdf

# Quick build (skip figure/supplement generation if they exist)
quick: figures supplements pdf

# View PDF (macOS)
view: pdf
	open main.pdf

# View PDF (Linux)
view-linux: pdf
	xdg-open main.pdf

# Help
help:
	@echo "ONE ArXiv Submission Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  all / pdf       - Build main.pdf (default)"
	@echo "  figures         - Generate all figures (scripts/generate_figures.py)"
	@echo "  supplements     - Generate EBNF appendix and raw data CSV"
	@echo "  check           - Verify reproducibility (run-twice-diff-zero)"
	@echo "  clean           - Remove LaTeX build artifacts"
	@echo "  clean-all       - Remove everything including generated figures"
	@echo "  quick           - Generate figures/supplements then build PDF"
	@echo "  view            - Open PDF (macOS)"
	@echo "  view-linux      - Open PDF (Linux)"
	@echo "  help            - Show this help"
	@echo ""
	@echo "Prerequisites:"
	@echo "  - TeX Live (latexmk, pdflatex)"
	@echo "  - Python 3.9+ with matplotlib, numpy"
	@echo "  - Source repos cloned at expected paths (see scripts/verify_reproducibility.py)"

main.pdf: figures