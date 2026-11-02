# Nmap — host discovery, ports and services

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** NETWORK; host/port probes contact the selected systems.

Install: `sudo apt install nmap`. A port state is an observation, not proof of a vulnerability. Start with a single authorized lab host.

```bash
nmap 10.10.10.10                          # Default TCP scan: common 1,000 ports
nmap -sT -p 22,80,443 10.10.10.10          # TCP connect scan; no raw-socket privilege needed
nmap -sV -p 22,80,443 10.10.10.10          # Probe service versions on selected ports
sudo nmap -sS -p- 10.10.10.10              # SYN scan, TCP ports 1–65535
sudo nmap -sU --top-ports 20 10.10.10.10   # Small UDP scan; can be slow/ambiguous
nmap --top-ports 20 10.10.10.10            # 20 common TCP ports
nmap -sn 192.168.56.0/24                  # Host discovery; no subsequent port scan
nmap 192.168.56.10,11,12                  # Address-list syntax
nmap 192.168.56.10-14                     # Last-octet range
nmap -sn 192.168.56.0/24 --exclude 192.168.56.1
nmap -iL targets.txt -oA results/inventory # Read scoped targets; save normal/XML/grepable output
nmap -n -sV -p 80,443 10.10.10.10          # Skip reverse-DNS lookups
nmap -Pn -p 443 10.10.10.10               # Skip host discovery; still scan the port
nmap --script-help http-title             # Read script documentation first
nmap -p 80,443 --script http-title 10.10.10.10
```

Create `results/` first. `-p` takes PORTS, not target addresses. A `/28` contains 16 addresses; do not describe it as 14 address ranges. IPv4 octets end at 255, never 256. `-A` enables OS detection, version detection, default scripts and traceroute; `-T4` changes timing and can be unsuitable on fragile/slow networks. `--script vuln` is not a complete vulnerability audit; some scripts are intrusive. Inspect individual scripts before running them.
