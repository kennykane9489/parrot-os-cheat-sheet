# Add this package to GitHub

[Home](README.md)

1. Extract the ZIP on your computer.
2. Open the existing repository and review its files before replacing anything.
3. Place the CONTENTS of `parrot-os-cheat-sheet/` at the repository root: `README.md`, `docs/`, `labs/`, `scripts/`, `tests/`, the maintenance files and `.github/`.
4. Commit through your usual Git workflow or GitHub's file upload interface. Ensure hidden `.github/` is included; Finder may hide it. Avoid nesting everything inside an extra folder.
5. Open README and check navigation. Visit Actions to inspect the first Documentation checks run; repository settings may require enabling Actions.

No files are automatically published by extracting this archive. Existing files with matching paths will need review before replacement. Keep your existing license and unrelated project files.

## Repository description

```text
Parrot OS cheat sheet covering Linux administration, networking, troubleshooting, and authorized security testing.
```

## Local validation

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```
