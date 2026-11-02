# sysctl

[All programs](README.md) · [Repository home](../../README.md)

Inspect and deliberately change kernel runtime parameters. Most network failures do not require changing these settings.

## Install and verify

```bash
sudo apt update
apt policy procps
sudo apt install procps
sysctl --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT for reads; CHANGE for writes. procps is commonly installed already.

```bash
sysctl net.ipv4.ip_forward
sysctl net.ipv6.conf.all.disable_ipv6
sysctl net.ipv6.conf.default.disable_ipv6
```

`ip_forward=0` disables IPv4 forwarding; `disable_ipv6=0` enables IPv6. Be precise about the name's negative wording.

### Save a baseline before any justified change

```bash
sysctl net.ipv4.ip_forward > forwarding-baseline.txt
```

This writes a note, not a restorable backup script. If a documented lab requires forwarding, first understand its routing/firewall implications. A temporary write uses `sudo sysctl -w KEY=VALUE` with a real key/value; restore the recorded value when finished.

### Persistent settings

For a deliberate persistent change, put only the intended key/value in a named file under `/etc/sysctl.d/`, then load that file with `sudo sysctl -p /etc/sysctl.d/FILENAME.conf`. Do not paste placeholder paths. `sysctl --system` loads many configuration files, so it can apply unrelated changes.

**Troubleshooting:** a missing key can mean unsupported kernel functionality. Permission denied usually indicates the write requires privileges or is restricted in a container. Do not turn IPv6 off/on globally as a universal VPN repair.

**Cleanup:** restore changed runtime values and remove only your own persistent configuration entry. Keep the baseline until restoration is confirmed.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run procps` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://manpages.debian.org/stable/procps/sysctl.8.en.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
