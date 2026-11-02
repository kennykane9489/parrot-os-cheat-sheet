# Validation record

[Home](README.md) · [Compatibility](COMPATIBILITY.md)

Prepared November 2, 2026. These checks ran in the preparation environment using Python 3.12.14 and Bash, not on a Parrot OS installation.

| Check | Result |
|---|---|
| Offline documentation checker | Passed: basic page structure, balanced fences/details, local target/anchor links and Bash syntax. |
| Checker regression suite | 9 tests passed: valid input, missing files/anchors, unclosed fences, invalid Bash, non-execution, out-of-root links, duplicate headings and unmatched details. |
| Archive lab | Documented Bash blocks executed successfully; extracted bytes matched via SHA-256 and cmp; cleanup completed. |
| Python venv lab | Documented Bash blocks executed successfully; isolated interpreter/pip verified; cleanup completed. |
| HTTP lab smoke test | Python server launched on loopback with an ephemeral port; 200/body, missing-path 404 and curl verified; server stopped and temporary files cleaned. |
| Parrot security-tool runtime checks | Not performed; pending a real Parrot test environment. |
| Optional Nmap step in HTTP lab | Not run during preparation. |
| GitHub-hosted workflow | Not run during preparation; provided for the first repository push/PR. |

The HTTP smoke test used an ephemeral port to avoid colliding with existing services; the teaching example uses 8000 with instructions to change it if occupied. Output in the separate example-output guide remains illustrative. No remote security targets were scanned.

The offline checker handles the repository's simple Markdown conventions. It is not full Markdown linting, does not fetch external links, and does not verify command semantics, package availability or upstream vulnerability claims.

## Full-guide and single-page revision — November 2, 2026

- 61 program guides added, with all instructions also present in a continuous README and HTML reader in the original topic order.
- Documentation validation passed for 97 Markdown files and 447 Bash examples. Repeated examples in source guides and the continuous README are counted separately.
- 17 Python tests passed, including static page structure, unique anchors, original order, complete guide sections, local runtime assets and normal-text contrast ratios.
- Node tests passed for the jump selector/focus, successful copying, manual clipboard fallback and an invalid jump target. These use a small DOM test double, not a browser.
- Static HTML production build completed with Marked 17.0.5 and the installed Node runtime. Runtime page assets are all local; opening the already-built page needs no package install.
- A fresh offline npm dependency resolution could not complete because registry metadata was not cached; the build used the same pinned package already installed in the preparation runtime. A fresh npm installation was not verified.
- No browser/screenshot QA or execution of the new security-tool examples was performed. Existing local lab smoke results above remain limited to their stated environment.
- GitHub-hosted checks for this revision will run after the commit. Existing earlier success does not establish this revision's result.
