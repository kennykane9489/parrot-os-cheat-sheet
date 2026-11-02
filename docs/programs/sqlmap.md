# sqlmap

[All programs](README.md) · [Repository home](../../README.md)

Validate suspected SQL injection in your own test application using a captured raw request and a single chosen parameter.

## Install and verify

```bash
sudo apt update
apt policy sqlmap
sudo apt install sqlmap
sqlmap --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK; active tests can modify application state or burden a database. Prerequisites: a disposable authorized app/database and a raw HTTP request for a real database-backed input. A static Python file server is not an SQL-injection lab.

### Prepare a request

Capture the intended application request in Burp, save the raw request including headers/blank line/body to `search.req`, and protect cookies/tokens. Identify the parameter name you actually intend to test.

```bash
sqlmap -r search.req -p q --level=1 --risk=1 --threads=1
```

Replace q with the selected parameter. `-r` supplies request bytes; `-p` narrows parameter selection; risk/level limit certain tests but do not make the operation passive. Leave prompts interactive while learning.

### Proxy and HTTPS context

```bash
sqlmap -r search.req -p q --level=1 --risk=1 --threads=1 --proxy=http://127.0.0.1:8080
```

This needs Burp or another proxy actually listening there. Use `--force-ssl` only when the captured request should use HTTPS. `--force-ssl461` is invalid. Do not use `--batch` to skip decisions before understanding them.

### Interpret results

A suspected injection needs reproducible evidence and application/database context. Session expiry, WAF responses and unstable pages can distort testing. Review logs and compare a baseline before claiming a finding. No data-dump/OS-shell step is required to document an injection.

**Troubleshooting:** re-capture stale requests, verify Host/content type/CSRF state and test a single input. Use a fresh disposable database when repeatability matters.

**Cleanup:** stop the tool and remove or redact saved request/session data; restore the disposable database from its snapshot if changed.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run sqlmap` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/sqlmapproject/sqlmap/wiki/Usage). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
