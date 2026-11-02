# Gobuster

[All programs](README.md) · [Repository home](../../README.md)

Enumerate web paths, DNS names or virtual hosts with explicit mode-specific options.

## Install and verify

```bash
sudo apt update
apt policy gobuster
sudo apt install gobuster
gobuster --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK and WRITE. Begin with the local HTTP lab and a three-entry wordlist.

```bash
printf '%s\n' hello.txt missing.txt robots.txt > lab-paths.txt
gobuster dir -u http://127.0.0.1:8000 -w lab-paths.txt -t 2 -o gobuster-lab.txt
```

`dir` selects path enumeration; `-u` is the base URL; `-w` supplies candidates; `-t` limits concurrent workers. Expect hello.txt to exist; independently verify results with curl. `-o` writes results.

### File extensions and lab virtual hosts

```bash
gobuster dir --help
gobuster dir -u http://127.0.0.1:8000 -w names.txt -x txt,html -t 2
gobuster vhost -u http://app.test --append-domain -w labels.txt -t 2
```

Create `names.txt` with bare stems such as `hello`; do not reuse `hello.txt` when appending `.txt`. The vhost example needs app.test resolving to your lab web server and labels.txt containing short labels such as dev. It tests HTTP Host routing, not DNS existence. `--append-domain` builds full hostnames from labels.

### DNS mode

Read `gobuster dns --help` for the installed build: domain flag names changed across versions. Do not copy the old global `-m dir` interface.

**Troubleshooting:** a wildcard/custom error page may match every word. Request a random nonexistent path, compare response length/status and set only filters supported by your release. Follow redirects intentionally. TLS bypass does not repair certificates.

**Cleanup:** Ctrl+C stops requests; remove generated test files/results only after reviewing evidence.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run gobuster` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/OJ/gobuster). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
