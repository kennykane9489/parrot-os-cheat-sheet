# Program user guides

[Repository home](../../README.md) · [Quick reference](../quick-reference.md)

Each guide includes installation, practical workflows, interpretation, troubleshooting, cleanup and an upstream reference. Examples require the stated prerequisites; private addresses are placeholders, not authorization.

## Files

| Program | Purpose |
|---|---|
| [find](find.md) | Locate filesystem entries by name, type, size and other metadata. It searches paths, not file contents. |
| [less](less.md) | Read long files without loading an editor; search and navigate logs interactively. |
| [sha256sum](sha256sum.md) | Calculate SHA-256 digests to compare file bytes or verify against a trusted publisher checksum. |
| [tar](tar.md) | Create, list and extract archives; compression and archiving are separate steps combined by convenient options. |

## Network testing

| Program | Purpose |
|---|---|
| [Metasploit Framework](metasploit.md) | Organize authorized testing modules and evidence in workspaces. Framework is distinct from licensed Metasploit Pro. |
| [Meterpreter sessions](meterpreter.md) | Interact with an existing authorized lab session using platform-supported commands. Meterpreter is a payload/session type, not an independent desktop package. |
| [msfvenom](msfvenom.md) | Inspect Framework payload metadata and supported output formats. Installed with Metasploit Framework. |
| [Nmap](nmap.md) | Discover hosts, inspect ports and identify services within an explicitly authorized scope. |
| [RouterSploit](routersploit.md) | Explore embedded-device module metadata in an isolated, firmware-specific lab. Historical dependencies may not support a modern Parrot release. |

## Networking

| Program | Purpose |
|---|---|
| [dig](dig.md) | Query DNS records and inspect resolver answers. Both tools are supplied by BIND utilities on typical Debian-based installations. |
| [getent](getent.md) | Query the system name-service configuration, including hosts files and DNS where configured. |
| [ip](ip.md) | Inspect addresses, links, neighbors and routes using the modern iproute2 suite. |
| [Netcat / nc](netcat.md) | Open simple TCP clients/listeners for local protocol and connection exercises. This guide targets netcat-openbsd, not every nc implementation. |
| [nmcli / NetworkManager](nmcli.md) | Inspect and manage connections controlled by NetworkManager. Distinguish a device from its saved connection profile. |
| [nslookup](nslookup.md) | Query DNS records and inspect resolver answers. Both tools are supplied by BIND utilities on typical Debian-based installations. |
| [OpenSSH / ssh and scp](openssh.md) | Log in and copy files over encrypted authenticated connections. Client installation does not install an SSH server. |
| [OpenVPN](openvpn.md) | Connect to a trusted VPN provider or lab using its issued profile and credentials. |
| [Python HTTP server](python-http-server.md) | Temporarily serve a dedicated folder for local file inspection and download exercises. Not a production server. |
| [ss](ss.md) | Identify listening ports, active sockets and the processes that own them. Part of iproute2. |
| [sysctl](sysctl.md) | Inspect and deliberately change kernel runtime parameters. Most network failures do not require changing these settings. |

## Password labs

| Program | Purpose |
|---|---|
| [Crunch](crunch.md) | Generate candidate strings from an explicit character set for small controlled exercises. It does not authenticate or crack anything by itself. |
| [Hydra](hydra.md) | Test a small, agreed set of login attempts against a designated training account. Different protocols require different modules. |
| [Medusa](medusa.md) | Perform module-specific authentication checks in a bounded training environment. Use it as an alternative to Hydra, not a redundant extra run. |

## SMB and AD

| Program | Purpose |
|---|---|
| [CIFS mounts / cifs-utils](cifs-utils.md) | Mount an SMB share into the local filesystem with explicit permissions and a clear unmount step. |
| [CrackMapExec migration](crackmapexec.md) | Understand older CME notes and move new workflows to NetExec without assuming command-line flags are identical. |
| [Impacket](impacket.md) | Python protocol libraries and example clients for Windows/SMB and related network protocols. |
| [NetExec](netexec.md) | Assess protocol configuration and permitted account access in Windows/AD labs. The primary CLI is commonly nxc; verify installed entry points. |
| [smbclient](smbclient.md) | Browse authorized Windows/Samba shares with an interactive client and prompted credentials. |
| [SMBMap](smbmap.md) | Summarize SMB shares and effective permissions for an authorized account. |

## System

| Program | Purpose |
|---|---|
| [APT and parrot-upgrade](apt.md) | Manage Debian-format packages and dependencies. Use `apt` interactively; use `apt-get`/`apt-cache` for stable scripting interfaces. |
| [Bash and core shell commands](bash.md) | Navigate folders, create files and understand shell operators before combining tool commands. cd is a shell builtin; many file utilities come from coreutils. |
| [dpkg](dpkg.md) | Inspect and manage individual .deb packages and their installed file lists. APT sits above dpkg and resolves downloads/dependencies. |
| [Git](git.md) | Track file history, inspect changes, and collaborate with a remote repository. |
| [GNOME Tweaks and extensions](gnome-tweaks.md) | Adjust GNOME desktop preferences beyond the standard Settings app. GNOME extensions require GNOME Shell; they do not apply to MATE/KDE. |
| [journalctl](journalctl.md) | Read systemd journal entries by service, boot and time to diagnose the exact failure. |
| [pip](pip.md) | Install Python libraries inside a project environment. Use `python -m pip` to select the pip belonging to that interpreter. |
| [pipx](pipx.md) | Install Python command-line applications into separate environments while exposing their commands on your PATH. |
| [PostgreSQL service for labs](postgresql.md) | Provide the optional database used by Metasploit workspaces. Service installation and database initialization are separate actions. |
| [Python virtual environments](python-venv.md) | Keep project dependencies separate from Parrot’s system Python. |
| [systemctl](systemctl.md) | Inspect and control systemd units. Starting now and enabling at boot are separate operations. |

## Traffic analysis

| Program | Purpose |
|---|---|
| [tcpdump](tcpdump.md) | Capture a narrowly filtered packet trace from a specific interface for diagnosis. |
| [TShark](tshark.md) | Use Wireshark protocol analysis from the terminal, especially for reading saved captures and extracting fields. |
| [Wireshark](wireshark.md) | Inspect network packets visually with display filters and protocol detail panes. |

## Utilities

| Program | Purpose |
|---|---|
| [btop](btop.md) | Monitor CPU, memory, disks, network rates and processes interactively. |
| [jq](jq.md) | Read, transform and validate JSON using composable filters. |
| [OpenSSL](openssl.md) | Inspect certificates and create local test cryptographic material without assuming that an arbitrary certificate is trusted. |
| [ripgrep / rg](ripgrep.md) | Search file contents quickly with useful line numbers, file filters and explicit hidden-file handling. |
| [ShellCheck](shellcheck.md) | Analyze shell scripts for common quoting, portability and logic mistakes without executing them. |
| [tmux](tmux.md) | Keep related terminal windows and panes in a session that survives client detachment. |

## Web testing

| Program | Purpose |
|---|---|
| [Burp Suite Community](burpsuite.md) | Intercept, inspect and replay HTTP requests in a dedicated browser testing workflow. Community is free; Professional is a separate licensed product. |
| [curl](curl.md) | Send HTTP requests and inspect responses without a browser. |
| [ffuf](ffuf.md) | Replace a FUZZ marker in HTTP requests with wordlist entries, with calibration, rate limits and structured output. |
| [Gobuster](gobuster.md) | Enumerate web paths, DNS names or virtual hosts with explicit mode-specific options. |
| [Nikto](nikto.md) | Check web servers for known risky files, outdated components and configuration clues. Findings need manual validation. |
| [OWASP ZAP](zap.md) | Inspect HTTP traffic and assess your own web application with a scoped proxy workflow. Passive analysis and active scans have different effects. |
| [SecLists](seclists.md) | A collection of test wordlists for discovery and security exercises. It is data, not an executable scanner. |
| [sqlmap](sqlmap.md) | Validate suspected SQL injection in your own test application using a captured raw request and a single chosen parameter. |
| [Wfuzz](wfuzz.md) | Fuzz paths or request parameters with payload generators and filters based on response properties. |
| [Wget](wget.md) | Download a resource to a local file with clear filename and timeout controls. |

## Wireless

| Program | Purpose |
|---|---|
| [airmon-ng](airmon-ng.md) | Manage monitor-mode interfaces for supported Aircrack-ng hardware in an authorized wireless lab. |
| [iw](iw.md) | Inspect modern Linux wireless interfaces, driver capabilities and connection state. |

