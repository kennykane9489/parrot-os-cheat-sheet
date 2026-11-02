# Parrot OS Cheat Sheet

Practical Linux commands, explanations, and small security labs for Parrot OS.

**Updated:** November 2, 2026 · **Status:** documentation reviewed; Parrot runtime testing pending

## Start here

- [Quick reference](docs/quick-reference.md): everyday commands with impact labels.
- [Troubleshooting](docs/troubleshooting.md): symptom → check → fix.
- [Example output](docs/example-output.md): interpret results and common errors.
- [Practice labs](labs/README.md): complete local exercises with cleanup.
- [Compatibility record](COMPATIBILITY.md): what has and has not been tested.

## Guides

| Topic | Guide |
|---|---|
| 01 | [Read this first](docs/01-start-here.md) |
| 02 | [Updates and APT](docs/02-apt-and-updates.md) |
| 03 | [First setup and Python tools](docs/03-setup-and-python.md) |
| 04 | [Files, archives and terminal essentials](docs/04-files-and-archives.md) |
| 05 | [Networking, DNS and VM connections](docs/05-networking-and-vms.md) |
| 06 | [OpenVPN and HTB troubleshooting](docs/06-vpn-troubleshooting.md) |
| 07 | [Nmap — host discovery, ports and services](docs/07-nmap.md) |
| 08 | [curl and Burp Suite — understand HTTP](docs/08-http-and-burp.md) |
| 09 | [Content discovery: Gobuster, ffuf, Wfuzz, Nikto](docs/09-web-discovery.md) |
| 10 | [SMB: smbclient, CIFS, SMBMap and NetExec](docs/10-smb-and-netexec.md) |
| 11 | [SQLmap — test suspected SQL injection](docs/11-sqlmap.md) |
| 12 | [Metasploit Framework — module-based lab testing](docs/12-metasploit.md) |
| 13 | [RouterSploit — optional embedded-device lab framework](docs/13-routersploit.md) |
| 14 | [Password-audit tools: Crunch, Hydra and Medusa](docs/14-password-auditing.md) |
| 15 | [Netcat, SSH and temporary file sharing](docs/15-file-transfers.md) |
| 16 | [Wireless monitor mode](docs/16-wireless.md) |
| 17 | [Useful additions](docs/17-toolbox.md) |
| 18 | [A sensible lab workflow](docs/18-lab-workflow.md) |
| 19 | [Primary documentation and verification links](docs/19-sources.md) |

## Command impact labels

| Label | Meaning |
|---|---|
| INSPECT | Read state or show help. Some output contains sensitive information. |
| NETWORK | Send traffic to the specified destination. |
| WRITE | Create or overwrite local files. |
| CHANGE | Install software or modify settings/state. |
| REMOVE | Delete files or packages. |
| LISTEN | Open a server/listener; exposure depends on bind address. |
| MOUNT | Attach a filesystem; remote access may generate traffic. |
| DISCONNECT | Can interrupt networking or an active connection. |

A command can have several effects. Read the nearby notes, replace example values, and run one command at a time. Use security-testing commands on your own systems or explicitly authorized labs. Private IPs are examples, not authorization.

## Checks and maintenance

Requires Python 3.10+ and Bash. From the repository root:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

Checks validate basic Markdown structure, local links/anchors and Bash syntax. They do not execute command examples, scan systems, check external website availability, or prove a command works on Parrot. GitHub Actions runs the same checks on pushes and pull requests.

Read [Contributing](CONTRIBUTING.md), [Changes](CHANGELOG.md), and [Upload instructions](UPLOAD.md).
