# Wfuzz

[All programs](README.md) · [Repository home](../../README.md)

Fuzz paths or request parameters with payload generators and filters based on response properties.

## Install and verify

```bash
sudo apt update
apt policy wfuzz
sudo apt install wfuzz
wfuzz --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK. Use a short list against the local HTTP lab.

```bash
printf '%s\n' hello.txt missing.txt robots.txt > lab-paths.txt
wfuzz -w lab-paths.txt 'http://127.0.0.1:8000/FUZZ'
wfuzz --hc 404 -w lab-paths.txt 'http://127.0.0.1:8000/FUZZ'
```

The first pass establishes actual responses. The second hides HTTP 404 only after that status has been confirmed as a reliable negative. `FUZZ` marks substitution; `-w` chooses the list.

### Numeric parameter example

```bash
wfuzz -z range,0-3 'http://127.0.0.1:8000/item?id=FUZZ'
```

A local application must implement this endpoint for meaningful results. `-z range,0-3` generates four candidate values. The static file-server lab does not have an item database.

### Understand filtering

`--hc` hides status codes, `--hl` hides line counts and `--hw` hides word counts. Derive values from your app; a copied `--hl 97` can conceal real content or do nothing. Run `wfuzz --help` to see your installed build's thread/output options before increasing traffic.

**Troubleshooting:** a custom 200 error page needs body/size-based analysis. HTTPS support can depend on PycURL's SSL backend; use the supported package environment rather than breaking system Python to repair it.

**Cleanup:** stop with Ctrl+C. If you saved output, remove secrets before sharing. No listener is created by these examples.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run wfuzz` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://wfuzz.readthedocs.io/en/latest/user/basicusage.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
