# SecLists

[All programs](README.md) · [Repository home](../../README.md)

A collection of test wordlists for discovery and security exercises. It is data, not an executable scanner.

## Install and verify

```bash
sudo apt update
apt policy seclists
sudo apt install seclists
dpkg -L seclists
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT for list selection; copying/writing lists is WRITE. Installation may require significant disk space; read APT's size estimate.

```bash
dpkg -L seclists | less
find /usr/share/seclists -type f -iname '*common*'
```

The `/usr/share/seclists` path is a common location, not guaranteed. Use the path actually reported by dpkg. If your repositories do not package it, clone the official danielmiessler/SecLists repository into your own tools directory and record its commit.

### Inspect and select a list

```bash
head -n 20 /path/to/chosen-list.txt
wc -l /path/to/chosen-list.txt
```

Replace the placeholder path. A short technology-appropriate list is a better starting point than an enormous catch-all. Review content and encoding before feeding a tool.

### Small self-contained practice list

```bash
printf '%s\n' hello.txt missing.txt robots.txt > lab-paths.txt
```

Use this with ffuf/Gobuster against the local HTTP lab. It gives predictable positive and negative results without needing a large package.

**Troubleshooting:** a missing `/opt/SecLists` folder is a path assumption, not a broken scanner. Full-domain lists and label-only subdomain lists need different vhost settings. A list can contain comments or unusual characters; know your tool's parsing behavior.

**Cleanup:** remove only your lab-generated list. Do not store real users' secrets in shared wordlists.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run seclists` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/danielmiessler/SecLists). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
