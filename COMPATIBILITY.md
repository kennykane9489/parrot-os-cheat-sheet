# Compatibility and verification

[Home](README.md)

## Current status

| Area | Status | Limitation |
|---|---|---|
| Intended platform | Parrot OS, with Debian-style package management | No exact Parrot release claimed as tested. |
| Documentation checker | Python 3.10+ and Bash | Uses the standard library; check actual local interpreter in validation notes. |
| Local links, Markdown structure and Bash syntax | Checked during package preparation | Syntax is not runtime correctness or full Markdown linting. |
| Local HTTP and archive lab behavior | Smoke checks recorded in validation notes | Preparation environment is not Parrot. |
| Security tools on Parrot | Pending runtime verification | Upstream references and local help must be compared with installed versions. |
| GitHub Actions | Workflow provided | First hosted run happens after upload; not run on GitHub during preparation. |
| External source links | Reference list provided | No automatic availability check; sites may block automated clients. |

See [validation notes](VALIDATION.md) for actual completed checks.

## Record a real Parrot test

Create a report with release, architecture, tool package version, date, exact command, expected/actual result and cleanup. Never mark a version tested from a web page or a passing syntax check.

```bash
cat /etc/os-release
uname -r
dpkg --print-architecture
apt policy nmap gobuster ffuf sqlmap
python3 --version
bash --version
```

These inspect local state and cached package metadata. Redact sensitive host/user details before publishing. Use [the report template](.github/ISSUE_TEMPLATE/command-problem.md) for problems.
