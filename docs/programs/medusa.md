# Medusa

[All programs](README.md) · [Repository home](../../README.md)

Perform module-specific authentication checks in a bounded training environment. Use it as an alternative to Hydra, not a redundant extra run.

## Install and verify

```bash
sudo apt update
apt policy medusa
sudo apt install medusa
medusa -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK; can lock accounts. Prerequisites: a disposable local SSH service/account and a verified small attempt budget.

```bash
medusa -d
medusa -M ssh -q
```

`-d` lists the modules actually compiled into your installation. `-M ssh -q` documents the selected module. The available modules vary by build; a copied static list is unreliable.

### One known test credential

```bash
read -r -s -p 'Disposable lab password: ' lab_password
printf '\n'
medusa -h 127.0.0.1 -u labuser -p "$lab_password" -M ssh -t 1 -f
unset lab_password
```

Use only a disposable password: expanded arguments may be visible in the local process list despite not appearing literally in shell history. `-h` is one host; `-u` one username; `-p` one password; `-M` the module; `-t 1` one login worker; `-f` stops this host after a valid credential. This confirms a known account rather than guessing a large list.

### Input files

`-H`, `-U` and `-P` take host, user and password files. Inspect attempt counts before combining files. A generic HTTP module may not implement your application’s form/CSRF flow; inspect `medusa -M http -q` and any separate web-form module actually present.

**Troubleshooting:** module absence requires a supported build or another appropriate tool, not a guessed module name. Read network errors and account policy before interpreting authentication failures.

**Cleanup:** close the test session and reset/remove designated lab credentials. Keep audit output private and redact before sharing.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run medusa` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](http://foofus.net/goons/jmk/medusa/medusa.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
