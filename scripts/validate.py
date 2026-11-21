#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate.py - repo structure validator (fleet standard, exit 0 pass / 1 error / 2 warning).

Checks:
  E* (exit 1): SKILL.md missing or frontmatter without name/description
  W* (exit 2): README.md / LICENSE missing; references/ or scripts/ missing
Usage:
  python scripts/validate.py              # validate repo root
  python scripts/validate.py <file>       # validate a SKILL.md-format file
"""
import io, os, re, sys

def check_skill_md(text):
    errors, warnings = [], []
    parts = text.split('---')
    if len(parts) < 3 or parts[0].strip():
        errors.append('E1: SKILL.md frontmatter missing or malformed (must start with --- block)')
        return errors, warnings
    head = parts[1]
    if not re.search(r'(?m)^name:\s*\S', head):
        errors.append('E2: frontmatter missing name')
    if not re.search(r'(?m)^description:\s*\S', head):
        errors.append('E2: frontmatter missing description')
    return errors, warnings

def main():
    args = [a for a in sys.argv[1:]]
    file_mode = bool(args)
    if args:
        errors, warnings = check_skill_md(io.open(args[0], encoding='utf-8').read())
    else:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        errors, warnings = [], []
        skill = os.path.join(root, 'SKILL.md')
        if not os.path.exists(skill):
            errors.append('E1: SKILL.md missing at repo root')
        else:
            e, w = check_skill_md(io.open(skill, encoding='utf-8').read())
            errors += e
            warnings += w
        for req in ('README.md', 'LICENSE'):
            if not os.path.exists(os.path.join(root, req)):
                warnings.append('W1: %s missing' % req)
        if not os.path.isdir(os.path.join(root, 'references')) and not os.path.isdir(os.path.join(root, 'scripts')):
            warnings.append('W2: references/ and scripts/ both missing')
    if errors:
        print('FAIL ' + '; '.join(errors))
        return 1
    if warnings:
        print('WARN ' + '; '.join(warnings))
        return 2
    print('PASS: frontmatter ok' + ('' if file_mode else '; README/LICENSE present; structure complete'))
    return 0

if __name__ == '__main__':
    sys.exit(main())
