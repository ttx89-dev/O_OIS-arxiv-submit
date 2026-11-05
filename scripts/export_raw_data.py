#!/usr/bin/env python3
"""
Export all measured raw data as CSV for supplementary material.
Run: python3 scripts/export_raw_data.py > supplements/raw_data.csv
"""

import sys
import json
import subprocess
import pathlib

# All measured data from in-session verification
data = {
    'points_golden_corpus': [
        {'graph': 'empty_graph', 'entities': 0, 'edges': 0, 'facets': 0, 'salience': 0, 'glyph_bytes': 8192, 'json_bytes': 26, 'points_sc': 0.0, 'json_sc': 0.0, 'ratio': None},
        {'graph': 'single_entity', 'entities': 1, 'edges': 0, 'facets': 0, 'salience': 0, 'glyph_bytes': 8192, 'json_bytes': 65, 'points_sc': 0.00244, 'json_sc': 0.30769, 'ratio': 0.00793},
        {'graph': 'single_edge', 'entities': 2, 'edges': 1, 'facets': 0, 'salience': 0, 'glyph_bytes': 8192, 'json_bytes': 231, 'points_sc': 0.01221, 'json_sc': 0.43290, 'ratio': 0.02820},
        {'graph': 'multi_edge', 'entities': 4, 'edges': 3, 'facets': 0, 'salience': 0, 'glyph_bytes': 8192, 'json_bytes': 560, 'points_sc': 0.03174, 'json_sc': 0.46429, 'ratio': 0.06836},
        {'graph': 'with_payload', 'entities': 4, 'edges': 4, 'facets': 2, 'salience': 2, 'glyph_bytes': 8192, 'json_bytes': 940, 'points_sc': 0.04395, 'json_sc': 0.38298, 'ratio': 0.11476},
        {'graph': 'negated_varied', 'entities': 4, 'edges': 4, 'facets': 0, 'salience': 0, 'glyph_bytes': 8192, 'json_bytes': 743, 'points_sc': 0.03906, 'json_sc': 0.43069, 'ratio': 0.09070},
        {'graph': 'demo_graph', 'entities': 6, 'edges': 6, 'facets': 0, 'salience': 0, 'glyph_bytes': 8192, 'json_bytes': 1069, 'points_sc': 0.05859, 'json_sc': 0.44902, 'ratio': 0.13049},
    ],
    'capacity_sweep': [
        {'entities': 1, 'points_sc': 0.00244, 'json_sc': 0.31746, 'ratio': 0.00769, 'points_wins': False},
        {'entities': 2, 'points_sc': 0.01221, 'json_sc': 0.44643, 'ratio': 0.02735, 'points_wins': False},
        {'entities': 5, 'points_sc': 0.04150, 'json_sc': 0.47887, 'ratio': 0.08666, 'points_wins': False},
        {'entities': 10, 'points_sc': 0.09033, 'json_sc': 0.48677, 'ratio': 0.18558, 'points_wins': False},
        {'entities': 20, 'points_sc': 0.18799, 'json_sc': 0.48600, 'ratio': 0.38681, 'points_wins': False},
        {'entities': 50, 'points_sc': 0.48096, 'json_sc': 0.48528, 'ratio': 0.99109, 'points_wins': False},
        {'entities': 100, 'points_sc': 0.96924, 'json_sc': 0.48511, 'ratio': 1.9980, 'points_wins': True},
        {'entities': 150, 'points_sc': 1.45752, 'json_sc': 0.48207, 'ratio': 3.0234, 'points_wins': True},
        {'entities': 200, 'points_sc': 1.94580, 'json_sc': 0.48062, 'ratio': 4.0485, 'points_wins': True},
        {'entities': 250, 'points_sc': 2.43408, 'json_sc': 0.47968, 'ratio': 5.0744, 'points_wins': True},
        {'entities': 300, 'points_sc': 2.92236, 'json_sc': 0.47909, 'ratio': 6.0997, 'points_wins': True},
        {'entities': 350, 'points_sc': 3.41064, 'json_sc': 0.47870, 'ratio': 7.1244, 'points_wins': True},
        {'entities': 400, 'points_sc': 3.89892, 'json_sc': 0.47838, 'ratio': 8.1499, 'points_wins': True},
        {'entities': 450, 'points_sc': 4.38720, 'json_sc': 0.47814, 'ratio': 9.1758, 'points_wins': True},
        {'entities': 460, 'points_sc': 4.48486, 'json_sc': 0.46154, 'ratio': 9.7172, 'points_wins': True},
    ],
    'rich_graph': [
        {'description': '300 entities, 299 edges, 30 facets, 30 salience', 'points_sc': 2.9956, 'json_sc': 0.4529, 'ratio': 6.614, 'json_kb': 52.9},
    ],
    'rs_recovery': [
        {'corrupted_bytes': 0, 'repaired': True, 'verified': True, 'errors_corrected': 0},
        {'corrupted_bytes': 1, 'repaired': True, 'verified': True, 'errors_corrected': 1},
        {'corrupted_bytes': 2, 'repaired': True, 'verified': True, 'errors_corrected': 2},
        {'corrupted_bytes': 4, 'repaired': True, 'verified': True, 'errors_corrected': 4},
        {'corrupted_bytes': 8, 'repaired': True, 'verified': True, 'errors_corrected': 8},
        {'corrupted_bytes': 12, 'repaired': True, 'verified': True, 'errors_corrected': 12},
        {'corrupted_bytes': 16, 'repaired': True, 'verified': True, 'errors_corrected': 16},
        {'corrupted_bytes': 20, 'repaired': True, 'verified': True, 'errors_corrected': 20},
        {'corrupted_bytes': 24, 'repaired': True, 'verified': True, 'errors_corrected': 24},
        {'corrupted_bytes': 32, 'repaired': True, 'verified': True, 'errors_corrected': 32},
    ],
    'test_suite': [
        {'component': 'POINTS', 'tests': 94, 'subtests': 42, 'status': 'PASS'},
        {'component': 'MSCA_gates', 'tests': 15, 'subtests': 3, 'status': 'PASS'},
    ],
    'msca_capacity': [
        {'metric': 'resident_tokens', 'value': 624, 'unit': 'tokens (p50k_base)', 'budget': 640, 'status': 'PASS'},
        {'metric': 'capacity_record_match', 'value': True, 'unit': 'bool', 'commit': '22a26a9', 'status': 'PASS'},
    ],
    'mutation_checks': [
        {'component': 'MSCA_gates', 'mutations': 3, 'detected': 3, 'status': 'PASS'},
    ],
    'reproducibility': [
        {'component': 'POINTS', 'run_twice_diff_zero': True},
    ],
}

# --- MSCA capacity: live-read from the MSCA repo (no hardcoded values) ---
MSCA_DIR = pathlib.Path(__file__).resolve().parent.parent.parent / 'MSCA'
msca_verified = False
msca_cap = {}
try:
    msca_cap = json.loads((MSCA_DIR / 'msca_store' / 'capacity.json').read_text())
    probe = subprocess.run(
        [sys.executable, '-m', 'msca.capacity', '--verify'],
        cwd=str(MSCA_DIR), capture_output=True, text=True, timeout=60)
    msca_verified = probe.returncode == 0 and 'MATCHES' in (probe.stdout or '')
    print('MSCA capacity live-read: tokens=%s commit=%s verified=%s'
          % (msca_cap.get('resident_tokens'), msca_cap.get('commit'), msca_verified),
          file=sys.stderr)
except Exception as exc:
    print('warning: MSCA capacity live-read failed: %s' % exc, file=sys.stderr)

for row in data['msca_capacity']:
    if row['metric'] == 'resident_tokens':
        val = msca_cap.get('resident_tokens')
        if val: row['value'] = val
        row['unit'] = 'tokens (%s)' % msca_cap.get('resident_worst_encoding', 'p50k_base')
        row['budget'] = msca_cap.get('ceiling', row['budget'])
        ok = isinstance(row['budget'], int) and isinstance(row['value'], int)
        row['status'] = 'PASS' if (ok and 0 < row['value'] <= row['budget']
                                   and msca_verified) else 'FAIL'
    elif row['metric'] == 'capacity_record_match':
        row['value'] = msca_verified
        row['status'] = 'PASS' if msca_verified else 'FAIL'

# every msca row carries the commit it was measured at (visible in the CSV)
for row in data['msca_capacity']:
    row['commit'] = msca_cap.get('commit') or ''

# Print CSV with section headers
print('section,key,value')
for section, records in data.items():
    if isinstance(records, list) and records:
        # Get all keys from first record
        keys = list(records[0].keys())
        for key in keys:
            for i, record in enumerate(records):
                val = record.get(key, '')
                if isinstance(val, bool):
                    val = 'true' if val else 'false'
                elif val is None:
                    val = ''
                print(f'{section},{key}[{i}],{val}')
    else:
        for key, val in records.items():
            if isinstance(val, bool):
                val = 'true' if val else 'false'
            print(f'{section},{key},{val}')