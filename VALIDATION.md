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
