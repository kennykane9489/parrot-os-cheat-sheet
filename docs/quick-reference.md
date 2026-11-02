# Quick reference

[Home](../README.md) · [Impact labels](../README.md#command-impact-labels)

Examples are independent commands, not an installation script. Use the guide for prerequisites and interpretation.

| Task | Command | Impact | Details |
|---|---|---|---|
| Identify release | `cat /etc/os-release` | INSPECT | [Setup](01-start-here.md) |
| Refresh package index | `sudo apt update` | NETWORK, CHANGE | [APT](02-apt-and-updates.md) |
| Upgrade Parrot | `sudo parrot-upgrade` | NETWORK, CHANGE, possible REMOVE | [APT](02-apt-and-updates.md) |
| Find package | `apt search KEYWORD` | INSPECT | [APT](02-apt-and-updates.md) |
| Check package version | `apt policy nmap` | INSPECT | [Compatibility](../COMPATIBILITY.md) |
| Preview orphan removal | `sudo apt autoremove --dry-run` | INSPECT | [APT](02-apt-and-updates.md) |
| Show interfaces | `ip -br address` | INSPECT | [Networking](05-networking-and-vms.md) |
| Show routes | `ip route` | INSPECT | [Networking](05-networking-and-vms.md) |
| Show listeners | `ss -tuln` | INSPECT | [Networking](05-networking-and-vms.md) |
| Resolve a name | `getent hosts example.com` | INSPECT, possible NETWORK | [DNS](05-networking-and-vms.md) |
| Check local HTTP | `curl -i http://127.0.0.1:8000/` | NETWORK | [HTTP lab](../labs/01-local-http.md) |
| Scan local HTTP port | `nmap -sT -p 8000 127.0.0.1` | NETWORK | [Nmap](07-nmap.md) |
| Search files | `rg -n 'ERROR' logs/` | INSPECT | [Files](04-files-and-archives.md) |
| Inspect archive | `tar -tf archive.tar.gz` | INSPECT | [Archives](04-files-and-archives.md) |
| Hash file | `sha256sum example.txt` | INSPECT | [Archive lab](../labs/02-archive-integrity.md) |
| Read service log | `journalctl -u NetworkManager -b -n 50 --no-pager` | INSPECT | [Troubleshooting](troubleshooting.md) |
| See tool help | `gobuster dir --help` | INSPECT | [Discovery](09-web-discovery.md) |

Do not use a one-line automatic upgrade/removal chain. Review proposed package removals. For destructive commands, preview or back up first.
