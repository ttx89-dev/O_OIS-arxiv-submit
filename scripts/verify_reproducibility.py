#!/usr/bin/env python3
"""
Verify reproducibility: run test suites twice, ensure diff == 0.
Run: python3 scripts/verify_reproducibility.py
"""

import subprocess
import sys
import os
import re

PROJECTS = [
    ('POINTS', '/var/home/ryan/Documents/projects/POINTS', ['python3', '-m', 'pytest', 'suite/tests/', '-q']),
    ('MSCA_gates', '/var/home/ryan/Documents/projects/MSCA', ['python3', '-m', 'msca.gates']),
]

# Wall-clock timings are hardware noise, not structural output: normalise
# "2.37s"-style floats before diffing so run-twice compares structure.
def _norm(s):
    return re.sub(r'\d+\.\d+s', '<t>', s)

def run_twice(name, cwd, cmd):
    print(f'\n=== {name}: Run 1 ===')
    r1 = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=300)
    out1 = _norm(r1.stdout + r1.stderr)
    code1 = r1.returncode

    print(f'=== {name}: Run 2 ===')
    r2 = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=300)
    out2 = _norm(r2.stdout + r2.stderr)
    code2 = r2.returncode

    same = (out1 == out2) and (code1 == code2)
    print(f'  Run 1 exit: {code1}, Run 2 exit: {code2}, Outputs identical: {same}')

    if not same:
        print('  *** DIFFERENCE DETECTED ***')
        # Show first difference
        for i, (l1, l2) in enumerate(zip(out1.splitlines(), out2.splitlines())):
            if l1 != l2:
                print(f'  Line {i}: "{l1}" vs "{l2}"')
                break
        return False

    if code1 != 0:
        print(f'  *** NON-ZERO EXIT ({code1}) ***')
        return False

    return True

def main():
    all_ok = True
    for name, cwd, cmd in PROJECTS:
        if not os.path.isdir(cwd):
            print(f'*** {name}: directory not found: {cwd} ***')
            all_ok = False
            continue
        try:
            ok = run_twice(name, cwd, cmd)
            all_ok = all_ok and ok
        except subprocess.TimeoutExpired:
            print(f'  *** TIMEOUT ***')
            all_ok = False
        except Exception as e:
            print(f'  *** ERROR: {e} ***')
            all_ok = False

    print(f'\n=== RESULT: {"ALL PASS" if all_ok else "SOME FAILED"} ===')
    sys.exit(0 if all_ok else 1)

if __name__ == '__main__':
    main()