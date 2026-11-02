# Nmap

[All programs](README.md) · [Repository home](../../README.md)

Discover hosts, inspect ports and identify services within an explicitly authorized scope.

## Install and verify

```bash
sudo apt update
apt policy nmap
sudo apt install nmap
nmap --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK; some probes/scripts can affect services. Begin with the local HTTP practice lab.

```bash
nmap -sT -p 8000 127.0.0.1
nmap -sV -p 8000 127.0.0.1
```

`-sT` completes TCP connections; `-sV` sends identification probes. An open port means a service accepted connections; a service label may just be a database guess.

### Inventory a single lab host

```bash
mkdir -p results
nmap -sT --top-ports 20 -oA results/initial 192.168.56.20
nmap -sV -p 22,80,443 -oN results/services.txt 192.168.56.20
```

Choose ports from observed results rather than assuming the example host has them. `-oA` creates three formats. `-p-` covers TCP 1–65535; UDP needs `-sU` and generally privileges. Large scans cost time/traffic.

### Discovery and scripts

```bash
nmap -sn 192.168.56.0/24
nmap --script-help http-title
nmap --script http-title -p 80,443 192.168.56.20
```

Only scan an authorized subnet. `-sn` skips port scanning; `-Pn` instead skips host discovery and treats targets as up. Inspect scripts before running; `--script vuln` is not a comprehensive safe audit.

**Troubleshooting:** filtered is uncertainty, not closed. Wrong VPN routes, target state and firewall behavior affect results. Raw SYN/OS scans need appropriate privileges. `-p` takes ports, not IP ranges.

**Cleanup:** stop unfinished scans with Ctrl+C and retain only appropriately protected/redacted results.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run nmap` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://nmap.org/book/man.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
