# Password-audit tools: Crunch, Hydra and Medusa

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** WRITE for Crunch; Hydra/Medusa help commands only INSPECT. Actual audits send NETWORK requests.

Use designated test accounts in a lab with an agreed attempt limit; authentication tests can lock accounts. Prefer one tool appropriate to the actual protocol rather than running several redundant tools.

### Crunch — generate candidate strings

Check/install `crunch` from APT if available.

```bash
mkdir -p ~/labs/wordlists
crunch 4 4 012345abcdef -o ~/labs/wordlists/demo.txt
wc -l ~/labs/wordlists/demo.txt
```

Produces every length-4 combination from the 12 supplied characters: 12^4 = 20,736 lines. It does not recover a password by itself. Output grows exponentially; calculate space before increasing lengths.

### Hydra — network authentication auditing

Prefer the repository package (`apt policy hydra`, then `sudo apt install hydra`) over untracked `make install`.

```bash
hydra -h
hydra -U http-post-form
hydra -U ssh
```

Module help explains supported fields and syntax. In form templates the placeholders are case-sensitive `^USER^` and `^PASS^`; the original `^user^` is wrong. `-l`/`-p` supply one username/password, whereas `-L`/`-P` name files. SSH tests must select SSH. HTTP form paths, body parameters, CSRF state, cookies and failure/success markers must match the actual app. A login page URL alone is insufficient. The old public-IP examples and `-t 64` default are removed.

### Medusa — modular parallel authentication auditor

Check/install package `medusa` if available.

```bash
medusa -d
medusa -M http -q
medusa -M ssh -q
```

`-d` lists compiled modules; `-M MODULE -q` shows module usage. `-h`/`-H` select one host/a host file; `-u`/`-U` one username/a username file; `-p`/`-P` one password/a password file. `-t` and `-T` control concurrency; `-n` selects a port. Installed modules vary, so the old static module list is replaced with live help. Do not assume generic HTTP authentication and an HTML form use the same module configuration.
