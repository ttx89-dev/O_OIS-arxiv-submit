#!/usr/bin/env python3
"""
Extract EBNF from O_OIS_EBNF.md and format as LaTeX appendix.
Run: python3 scripts/extract_ebnf.py > supplements/o_ois_ebnf.tex
"""

import re
import sys
from pathlib import Path

EBNF_PATH = Path(__file__).parent.parent.parent / 'O_OIS_EBNF.md'

def main():
    with open(EBNF_PATH) as f:
        content = f.read()

    # Extract code blocks (EBNF)
    code_blocks = re.findall(r'```(?:ebnf|bnf|text)?\n(.*?)\n```', content, re.DOTALL)

    # Extract tables
    tables = re.findall(r'\|.*?\n\|[-|:]+\n(?:.*?\n)*', content)

    # Output LaTeX
    print(r'% O-OIS EBNF Appendix (auto-generated from O_OIS_EBNF.md)')
    print(r'\section*{Appendix: Full O-OIS EBNF Grammar}')
    print(r'\addcontentsline{toc}{section}{Appendix: Full O-OIS EBNF Grammar}')
    print()

    # Split by sections and format
    sections = re.split(r'^##?\s+', content, flags=re.MULTILINE)
    for sec in sections:
        if not sec.strip():
            continue
        lines = sec.strip().split('\n')
        title = lines[0].strip()
        body = '\n'.join(lines[1:])

        if title.startswith('3.') or title.startswith('Transport') or title.startswith('Core Graph') or title.startswith('Relation') or title.startswith('Epistemic') or title.startswith('Tiered') or title.startswith('Encoding') or title.startswith('Semantic') or title.startswith('Optimality') or title.startswith('Disclosure'):
            # Subsection
            print(rf'\subsection*{{{title}}}')
            print()

        # Format code blocks in body
        body = re.sub(r'```(?:ebnf|bnf|text)?\n(.*?)\n```', lambda m: r'\begin{verbatim}\n' + m.group(1) + r'\n\end{verbatim}', body, flags=re.DOTALL)
        body = re.sub(r'`([^`]+)`', r'\\texttt{\1}', body)
        body = body.replace('&', '\\&').replace('%', '\\%').replace('#', '\\#').replace('_', '\\_')

        print(body)
        print()

if __name__ == '__main__':
    main()