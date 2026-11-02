# Contributing

[Home](README.md)

Keep examples small, explain each flag that matters, state prerequisites and impact, and include expected results and cleanup for labs. Use loopback or explicitly marked lab placeholders. Do not add live third-party scan targets, cracked installers, secrets or unverified success claims.

## Change checklist

- Confirm syntax against the installed tool's help and a primary source.
- Record actual Parrot/tool versions when runtime-tested; otherwise say pending.
- Label example output as illustrative unless it was actually captured.
- Add a changelog entry and keep internal links current.
- Run the checks from the repository root:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

The checker supports this repository's simple inline links and fenced examples. It is not a complete Markdown parser. Keep reference-style links and complicated inline link syntax out of new pages unless the checker is extended and tested. External links are intentionally not requested by the offline checker.

## Licensing

No new license is selected by this package. Preserve any existing repository license and attribution. The repository owner should choose terms deliberately before inviting reuse; do not assume that a public repository grants a license to every included work.
