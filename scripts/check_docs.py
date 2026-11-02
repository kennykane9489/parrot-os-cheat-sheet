#!/usr/bin/env python3
"""Offline Markdown structure, local link and Bash syntax checks; never runs examples."""
import argparse
from collections import Counter
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlsplit


def parse(text):
    prose, blocks, errors, anchors = [], [], [], set()
    counts = Counter()
    opened, body = None, []
    for number, line in enumerate(text.splitlines(), 1):
        fence = re.match(r'^\s*(`{3,}|~{3,})(.*)$', line)
        if opened:
            if fence and fence[1][0] == opened[0] and len(fence[1]) >= opened[1] and not fence[2].strip():
                if opened[2] in ('bash', 'sh'):
                    blocks.append((opened[3], '\n'.join(body)))
                opened, body = None, []
            else:
                body.append(line)
            continue
        if fence:
            opened = (fence[1][0], len(fence[1]), fence[2].strip(), number)
            continue
        prose.append(line)
        heading = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if heading:
            slug = re.sub(r'[^\w\- ]', '', heading[1].lower()).replace(' ', '-')
            count = counts[slug]
            counts[slug] += 1
            anchors.add(slug if count == 0 else f'{slug}-{count}')
        anchors.update(re.findall(r'<a\s+id="([^"]+)"', line))
    if opened:
        errors.append('unclosed code fence')
    text = '\n'.join(prose)
    if len(re.findall(r'<details(?:\s[^>]*)?>', text)) != text.count('</details>'):
        errors.append('unbalanced details tags')
    if not re.search(r'^#\s+\S', text, re.M):
        errors.append('missing page title')
    return text, anchors, blocks, errors


def check(root):
    root = root.resolve()
    errors, parsed, block_count = [], {}, 0
    files = sorted(p for p in root.rglob('*.md') if not {'.git', 'node_modules', '.venv', '__pycache__'}.intersection(p.parts))
    bash = shutil.which('bash')
    if not bash:
        return ['Bash is required'], 0, 0
    if not files:
        return ['no Markdown files found'], 0, 0
    for path in files:
        if not path.resolve().is_relative_to(root):
            errors.append(f'{path}: file escapes repository')
            continue
        try:
            prose, anchors, blocks, issues = parse(path.read_text(encoding='utf-8'))
        except (OSError, UnicodeError) as exc:
            errors.append(f'{path}: cannot read: {exc}')
            continue
        parsed[path.resolve()] = (prose, anchors)
        errors.extend(f'{path.relative_to(root)}: {issue}' for issue in issues)
        for line, body in blocks:
            block_count += 1
            try:
                result = subprocess.run([bash, '--noprofile', '--norc', '-n'], input=body,
                                        text=True, capture_output=True, timeout=5,
                                        env={'PATH': '/usr/bin:/bin', 'LC_ALL': 'C'})
                if result.returncode:
                    errors.append(f'{path.relative_to(root)}:{line}: invalid Bash syntax: {result.stderr.strip()}')
            except (OSError, subprocess.TimeoutExpired) as exc:
                errors.append(f'{path}: Bash check failed: {exc}')
    for path, (prose, _) in parsed.items():
        for target in re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)', prose):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            linked = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not linked.is_relative_to(root):
                errors.append(f'{path.relative_to(root)}: link escapes repository: {target}')
            elif not linked.exists():
                errors.append(f'{path.relative_to(root)}: missing local target: {target}')
            elif url.fragment and linked.suffix == '.md':
                if linked not in parsed or unquote(url.fragment) not in parsed[linked][1]:
                    errors.append(f'{path.relative_to(root)}: missing anchor: {target}')
    return errors, len(files), block_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error('--root must be an existing directory')
    errors, files, blocks = check(args.root)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {files} Markdown files; {blocks} Bash examples; local links and basic structure checked.')
    print('Examples parsed only. External URLs not requested.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
