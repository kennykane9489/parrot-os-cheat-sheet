![Matte black Parrot OS Cheat Sheet](assets/banner.svg)

# Parrot OS Cheat Sheet

One continuous reference for installing and using your tools. Each program has its setup, commands, practical examples and troubleshooting together. Updated November 2, 2026.

**Find a tool:** use Ctrl+F (Cmd+F on Mac) or the jump links below. [Open the matte-black version](index.html) after downloading the repository, or serve it with the command below. GitHub renders this Markdown using its own theme; the styled version is index.html.

## Jump to a program

[APT and parrot-upgrade](#program-apt) · [Bash and core shell commands](#program-bash) · [GNOME Tweaks and extensions](#program-gnome-tweaks) · [Git](#program-git) · [Python virtual environments](#program-python-venv) · [pip](#program-pip) · [pipx](#program-pipx)

[dpkg](#program-dpkg) · [OpenVPN](#program-openvpn) · [ip](#program-ip) · [ss](#program-ss) · [nmcli / NetworkManager](#program-nmcli) · [dig](#program-dig) · [nslookup](#program-nslookup)

[getent](#program-getent) · [sysctl](#program-sysctl) · [Burp Suite Community](#program-burpsuite) · [tar](#program-tar) · [RouterSploit](#program-routersploit) · [CrackMapExec migration](#program-crackmapexec) · [NetExec](#program-netexec)

[smbclient](#program-smbclient) · [CIFS mounts / cifs-utils](#program-cifs-utils) · [SMBMap](#program-smbmap) · [Impacket](#program-impacket) · [Nmap](#program-nmap) · [curl](#program-curl) · [Wget](#program-wget)

[Gobuster](#program-gobuster) · [SecLists](#program-seclists) · [Nikto](#program-nikto) · [Wfuzz](#program-wfuzz) · [ffuf](#program-ffuf) · [PostgreSQL service for labs](#program-postgresql) · [Metasploit Framework](#program-metasploit)

[Meterpreter sessions](#program-meterpreter) · [msfvenom](#program-msfvenom) · [Netcat / nc](#program-netcat) · [OpenSSH / ssh and scp](#program-openssh) · [Python HTTP server](#program-python-http-server) · [Crunch](#program-crunch) · [Hydra](#program-hydra)

[Medusa](#program-medusa) · [sqlmap](#program-sqlmap) · [iw](#program-iw) · [airmon-ng](#program-airmon-ng) · [Wireshark](#program-wireshark) · [tcpdump](#program-tcpdump) · [TShark](#program-tshark)

[find](#program-find) · [less](#program-less) · [sha256sum](#program-sha256sum) · [jq](#program-jq) · [ripgrep / rg](#program-ripgrep) · [tmux](#program-tmux) · [btop](#program-btop)

[OpenSSL](#program-openssl) · [OWASP ZAP](#program-zap) · [ShellCheck](#program-shellcheck) · [systemctl](#program-systemctl) · [journalctl](#program-journalctl)

---

## Before you start

Run commands one at a time. Replace example paths, interfaces, accounts and addresses. Network-testing examples are for your own systems or explicitly authorized labs; private addresses alone are not authorization. Examples are documentation-reviewed; Parrot runtime checks remain pending. “Expected” describes behavior, not a captured result from your computer.

Installation sections use Parrot APT packages where available. Read `apt policy PACKAGE` and the proposed changes first; do not add Kali or Ubuntu repositories. A shared base package such as coreutils, systemd or libc-bin normally exists already and should not be removed as lab cleanup. Update APT-installed tools through Parrot's upgrade workflow; update pipx/source installs through the manager that installed them.

`sudo` changes privileges. `>` overwrites files; `>>` appends. Quote variable/path expansions. `&&` runs the next command only after success. Ctrl+C usually stops a foreground tool. For exact options, use local help/man pages for your installed build.

**Practice setup:** many HTTP examples refer to a local server on 127.0.0.1:8000. Start it with the [Python HTTP server section](#program-python-http-server), then stop it when finished. A static file server is not an SQL-injection, authentication or API lab. Those exercises need the explicitly described test service.

### Command impact labels

| Label | Meaning |
|---|---|
| INSPECT | Read state/help; output can contain private information. |
| NETWORK | Send requests or probes to the specified service. |
| WRITE / CHANGE | Create files, install packages or change settings. |
| REMOVE | Delete data or packages. |
| LISTEN / MOUNT | Open a listener or attach a filesystem. |
| CAPTURE | Observe packet data; scope and permissions matter. |
| DISCONNECT | Can interrupt an active network connection. |

### VM network types

| Type | What it does |
|---|---|
| NAT | Usually gives the guest outbound connectivity through the host; inbound connections may need forwarding. |
| Bridged | Places the guest on the physical LAN with its own network identity. |
| Host-only | Private host/guest network; no Internet by default. |
| Internal network | Guest-to-guest segment; the host is usually excluded. |
| Custom | Hypervisor-specific configuration; inspect its actual adapters and routing. |

Check every adapter: an extra NAT/bridged interface can defeat an intended isolated lab.

---

<a id="program-apt"></a>

## APT and parrot-upgrade

Manage Debian-format packages and dependencies. Use `apt` interactively; use `apt-get`/`apt-cache` for stable scripting interfaces.

### Install and verify

```bash
sudo apt update
apt policy apt
sudo apt install apt
apt --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK, CHANGE; upgrades may REMOVE dependencies. APT is already part of Parrot. Do not reinstall it merely to verify the command.

#### Update the system

```bash
sudo apt update
apt list --upgradable
sudo parrot-upgrade
```

`update` refreshes indexes without upgrading installed software. Parrot’s wrapper handles rolling system upgrades. Review removals; reboot when needed to load a new kernel.

#### Find and install one tool

```bash
apt search ripgrep
apt show ripgrep
apt policy ripgrep
sudo apt install ripgrep
```

Search finds packages; show describes them; policy identifies candidates/origins. Install fetches dependencies. A specific package can also be upgraded by `sudo apt install --only-upgrade ripgrep`.

#### Preview cleanup

```bash
sudo apt autoremove --dry-run
sudo apt clean
```

Autoremove's preview lists unused automatic dependencies. Clean deletes downloaded archives, not installed tools. Remove keeps many settings; purge also deletes package-managed configuration, not necessarily files in your home.

**Troubleshooting:** wait for a running updater rather than deleting lock files. DNS errors require a working resolver; missing candidates require checking indexes/release/repositories. After an interrupted transaction, use `sudo dpkg --configure -a` only after other package processes finish. Do not run an unattended chain of upgrade/removal commands.

**Cleanup:** package operations create no disposable lab folder. Use clean for cached downloads only when needed; review autoremove before performing it.

**Reference:** [Official documentation](https://parrotsec.org/docs/configuration/parrot-software-management/).

[Back to top](#jump-to-a-program)

---

<a id="program-bash"></a>

## Bash and core shell commands

Navigate folders, create files and understand shell operators before combining tool commands. cd is a shell builtin; many file utilities come from coreutils.

### Install and verify

```bash
sudo apt update
apt policy bash coreutils
sudo apt install bash coreutils
bash --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT, WRITE or REMOVE depending on command. Run in a fresh temporary directory for practice, not your home root.

```bash
shell_lab=$(mktemp -d /tmp/parrot-shell.XXXXXX)
cd "$shell_lab"
pwd
mkdir notes
printf 'hello\n' > notes/example.txt
ls -lah notes
cat notes/example.txt
```

pwd prints the current directory. ls lists entries; `-a` includes hidden entries. mkdir creates a directory. printf writes text and `>` overwrites the destination. `>>` appends. Quoting variable expansions preserves spaces and prevents unintended globbing.

#### Operators and paths

`&&` runs the right command only after success; a pipe `|` sends output into another program. `~` expands to your home in suitable shell contexts. Relative paths depend on pwd. A leading `#` begins a comment outside quoted strings; prompt markers in tutorials are not commands.

#### Inspect permissions

```bash
id
ls -l notes/example.txt
```

Owner/group/mode govern local access alongside ACLs and other policy. sudo elevates privileges; it is not a generic fix for every error. Do not use chmod 777 as a default repair.

#### Cleanup in the same terminal

```bash
rm -- notes/example.txt
rmdir notes
cd ~
rmdir -- "$shell_lab"
unset shell_lab
```

rm deletes files; rmdir removes empty directories. `--` ends option parsing. Avoid recursive deletion until you have inspected the exact target and consequences.

**Troubleshooting:** check pwd before relative paths, quote expansions, and read the exact permission/path error. Do not retry a mistaken deletion with sudo.

**Cleanup:** the commands above remove only the known file and empty temporary directories.

**Reference:** [Official documentation](https://www.gnu.org/software/bash/manual/).

[Back to top](#jump-to-a-program)

---

<a id="program-gnome-tweaks"></a>

## GNOME Tweaks and extensions

Adjust GNOME desktop preferences beyond the standard Settings app. GNOME extensions require GNOME Shell; they do not apply to MATE/KDE.

### Install and verify

```bash
sudo apt update
apt policy gnome-tweaks
sudo apt install gnome-tweaks
gnome-tweaks --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** CHANGE to your desktop preferences. Check your environment before installing:

```bash
printf '%s\n' "$XDG_CURRENT_DESKTOP"
gnome-tweaks
```

If you are not running GNOME, use your desktop’s settings instead. Installing Tweaks does not switch you to GNOME.

#### Practical workflow

1. Open Tweaks as your normal user, never with sudo.
2. Record the current setting you intend to change.
3. Change a single option such as the interface font or window-titlebar behavior.
4. Check usability and restore the recorded setting if the result is undesirable.

Available panels vary by GNOME release. Extension management may be in the separate Extensions app. Use the official GNOME extensions site, check shell-version compatibility and review each extension's permissions/source before enabling it.

**Troubleshooting:** an empty or missing option may be a desktop/version mismatch. Disable a newly added extension if the shell becomes unstable. Do not install Ubuntu desktop meta-packages to “fix” Parrot. Logout/login can apply some desktop changes; save work first.

**Cleanup:** disable/remove the specific test extension and restore changed settings. Removing Tweaks does not necessarily undo the preferences you changed.

**Reference:** [Official documentation](https://extensions.gnome.org/).

[Back to top](#jump-to-a-program)

---

<a id="program-git"></a>

## Git

Track file history, inspect changes, and collaborate with a remote repository.

### Install and verify

```bash
sudo apt update
apt policy git
sudo apt install git
git --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** WRITE locally; NETWORK on clone/fetch/push. Start in a new directory rather than an unrelated project.

#### Clone this reference

```bash
git clone https://github.com/kennykane9489/parrot-os-cheat-sheet.git
cd parrot-os-cheat-sheet
git status
git log -5 --oneline
```

Clone creates a directory. Status identifies uncommitted changes; log shows recent commits. A clone downloads code; it does not make that code trustworthy to execute.

#### Make a small documentation change

```bash
git switch -c docs/my-notes
git diff
git add docs/quick-reference.md
git diff --cached
git commit -m "Clarify quick reference"
```

Edit the file before staging. `--cached` reviews exactly what will be committed. Configure a commit name/email if prompted, using values you are comfortable exposing in public history.

#### Update without hiding conflicts

```bash
git fetch origin
git status
git diff HEAD..origin/main
```

Fetch updates remote-tracking data without merging it. Review before choosing a merge/rebase. Publishing your branch with `git push -u origin docs/my-notes` needs authenticated write access.

**Troubleshooting:** authentication failures need a credential helper, SSH key or supported token method; never put tokens in a public URL. Preserve local changes before updating. Avoid `reset --hard` or forced pushes as routine fixes. To leave a branch, use `git switch main`; keep your work committed or safely saved first.

**Cleanup:** return to main only after committing/saving work. Remove a local test branch only after confirming its changes are preserved; deleting a working directory is not required.

**Reference:** [Official documentation](https://git-scm.com/docs/gittutorial).

[Back to top](#jump-to-a-program)

---

<a id="program-python-venv"></a>

## Python virtual environments

Keep project dependencies separate from Parrot’s system Python.

### Install and verify

```bash
sudo apt update
apt policy python3-venv
sudo apt install python3-venv
python3 --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** WRITE. Work in your own project directory. A venv is an environment, not a virtual machine or security sandbox.

```bash
mkdir -p ~/labs/python-demo
cd ~/labs/python-demo
python3 -m venv .venv
source .venv/bin/activate
python -c 'import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)'
python -m pip --version
```

The executable/pip should be under this `.venv`; the Boolean should be `True`. Activation affects the current shell. You can instead use `.venv/bin/python` explicitly without activation.

#### Run and record a project

```bash
python -c 'print("isolated Python works")'
python -m pip list
python -m pip freeze > requirements.txt
deactivate
```

Freeze writes installed versions for later review; it is not a complete cross-platform dependency lock. A project with no third-party packages can have an empty requirements file.

**Troubleshooting:** missing ensurepip/venv support usually requires the matching Parrot `python3-venv` package. An “externally managed” pip error means you are probably using system Python; verify executable paths. Do not solve it with `sudo pip`.

**Cleanup:** deactivate first. Inspect the exact project's `.venv` path and remove only that generated environment if no longer needed. Keep source files and requirements. Virtual environments can be recreated and should not be committed to Git.

**Reference:** [Official documentation](https://docs.python.org/3/library/venv.html).

[Back to top](#jump-to-a-program)

---

<a id="program-pip"></a>

## pip

Install Python libraries inside a project environment. Use `python -m pip` to select the pip belonging to that interpreter.

### Install and verify

```bash
sudo apt update
apt policy python3-pip
sudo apt install python3-pip
python3 -m pip --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK, WRITE; package installs can execute build code. First create/activate a venv with `python3 -m venv .venv` and `source .venv/bin/activate`.

#### Install, inspect, and validate a library

```bash
python -m pip install requests
python -m pip show requests
python -m pip check
python -c 'import requests; print(requests.__version__)'
```

This example obtains the Requests HTTP library from your configured package index. Review package identity and trust before installing. Show reports metadata/location; check detects incompatible installed dependency requirements.

#### Recreate a known project

```bash
python -m pip install -r requirements.txt
python -m pip list
python -m pip freeze > installed-versions.txt
```

Use only a trusted requirements file; it may reference source repositories or other indexes. Freeze records what is present; it does not review vulnerabilities or guarantee reproducibility across operating systems.

#### Remove a project dependency

```bash
python -m pip uninstall requests
```

Uninstall prompts and does not automatically remove all dependencies. Deactivate when finished. For disposable experiments, remove the inspected project venv instead of changing system Python.

**Troubleshooting:** verify `sys.executable` and pip location when imports fail. Build failures may need development headers compatible with the project. Do not globally bypass Parrot's externally managed environment protection.

**Cleanup:** deactivate the environment and remove only a confirmed disposable project venv if it is no longer needed. Keep source and requirements files.

**Reference:** [Official documentation](https://pip.pypa.io/en/stable/user_guide/).

[Back to top](#jump-to-a-program)

---

<a id="program-pipx"></a>

## pipx

Install Python command-line applications into separate environments while exposing their commands on your PATH.

### Install and verify

```bash
sudo apt update
apt policy pipx
sudo apt install pipx
pipx --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK, WRITE. Use pipx for applications, not libraries imported by another project.

```bash
pipx ensurepath
pipx list
```

Open a new terminal after ensurepath. It may update shell startup configuration. Do not use sudo for your normal pipx environment.

#### Install a CLI and check it

```bash
pipx install httpie
http --version
http GET http://127.0.0.1:8000/
```

HTTPie is an example trusted CLI; the request needs a running local web server. pipx supplies isolation; HTTPie performs the request. A missing executable after installation usually indicates PATH needs reloading.

#### Maintain or remove it

```bash
pipx list
pipx upgrade httpie
pipx uninstall httpie
```

Upgrade acts on this pipx application, not an APT-installed program of the same name. Use `command -v http` to see which executable runs. Do not install multiple competing copies without tracking them.

**Troubleshooting:** libraries generally have no entry-point executable and are unsuitable for pipx. A package build failure may require supported Python and build dependencies; inspect upstream requirements. Cleanup with pipx uninstall removes the application's environment; it may leave user settings outside it.

**Cleanup:** pipx uninstall httpie removes the example application environment; review any separate user settings before deleting them.

**Reference:** [Official documentation](https://pipx.pypa.io/stable/).

[Back to top](#jump-to-a-program)

---

<a id="program-dpkg"></a>

## dpkg

Inspect and manage individual .deb packages and their installed file lists. APT sits above dpkg and resolves downloads/dependencies.

### Install and verify

```bash
sudo apt update
apt policy dpkg
sudo apt install dpkg
dpkg --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT for queries; CHANGE for installs/configuration. Already installed on Parrot.

#### Inspect before installing

```bash
dpkg --print-architecture
dpkg-deb --info ./file.deb
dpkg-deb --contents ./file.deb
```

Replace `file.deb` with a trusted local package. Compare architecture and package details with your system. Inspection does not establish publisher authenticity.

#### Install and find package files

```bash
sudo apt install ./file.deb
dpkg -l nmap
dpkg -L nmap
dpkg -S /usr/bin/nmap
```

APT is preferable for a local .deb because it can fetch dependencies. `dpkg -i` alone cannot fetch them. `-l` queries package status; `-L` lists files; `-S` finds the owning package. Files installed outside the package manager may have no owner.

#### Recover an interrupted setup

```bash
sudo dpkg --configure -a
sudo apt --fix-broken install
```

Use recovery only when package errors call for it, after other package transactions stop. Review the dependency repair proposal.

**Troubleshooting:** an architecture mismatch requires the correct build, not force flags. If a dependency cannot be satisfied, use a compatible package/release. Do not force overwrites to conceal conflicts. Cleanup of a test package belongs in APT, after reviewing a dry run.

**Cleanup:** if you intentionally installed a disposable test package, preview its removal through APT before removing it. Do not remove dpkg itself.

**Reference:** [Official documentation](https://manpages.debian.org/stable/dpkg/dpkg.1.en.html).

[Back to top](#jump-to-a-program)

---

<a id="program-openvpn"></a>

## OpenVPN

Connect to a trusted VPN provider or lab using its issued profile and credentials.

### Install and verify

```bash
sudo apt update
apt policy openvpn
sudo apt install openvpn
openvpn --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK and CHANGE to routing/DNS integration. Use a fresh configuration for the correct lab/region.

```bash
sudo openvpn --config ~/Downloads/lab.ovpn
```

Keep the terminal open. A successful initialization message indicates the tunnel initialized; it does not guarantee the target is running. Configuration files can reference scripts, keys and credentials, so obtain them from the provider and do not share them publicly.

#### Verify the route in another terminal

```bash
ip -br address
ip route get 10.10.10.10
ping -c 3 10.10.10.10
```

Replace the IP with your authorized target. Read which interface the route selects. Ping may be blocked; also test the known service. Avoid simultaneous duplicate VPNs and overlapping host-only/NAT subnets.

#### When it fails

Authentication errors need valid provider credentials/profile. Route conflicts require inspecting both VPN and local subnet routes. DNS failures need checking the provider's supported resolver integration; OpenVPN itself does not always apply all DNS settings on every Linux setup. If logs specifically mention IPv6, diagnose that error rather than applying a blanket sysctl recipe.

**Cleanup:** Ctrl+C in the OpenVPN terminal closes this session; verify routes/connection state afterward. Remove unneeded profiles securely according to your provider’s credential handling. Do not publish configuration or logs containing keys/tokens.

**Troubleshooting:** distinguish authentication, route and resolver failures from the actual logs; initialization alone does not prove the target is reachable.

**Reference:** [Official documentation](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/).

[Back to top](#jump-to-a-program)

---

<a id="program-ip"></a>

## ip

Inspect addresses, links, neighbors and routes using the modern iproute2 suite.

### Install and verify

```bash
sudo apt update
apt policy iproute2
sudo apt install iproute2
ip -Version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT in this guide. Other ip commands can disconnect the machine or alter routing.

```bash
ip -br address
ip link show
ip route
ip -6 route
ip neigh
```

Brief address output associates interfaces with addresses. Link state does not prove Internet access. IPv4 and IPv6 have separate routing tables; a default route points to the gateway used when no more-specific route matches.

#### Troubleshoot a VPN target

```bash
ip route get 10.10.10.10
```

Replace the address with your lab target. Read the selected `dev`, source address and optional gateway. A VPN-lab target should normally route through the expected tunnel. This is a route lookup, not a reachability probe.

#### Inspect one actual interface

```bash
ip address show dev lo
ip -s link show dev lo
```

`lo` exists on normal Linux systems. Use the name from your own output for physical/tunnel interfaces. `-s` shows packet counters; drops/errors can guide further diagnosis.

**Troubleshooting:** names such as enp0s3, wlp2s0 and tun0 vary. An IP route command failing with “network unreachable” identifies a local routing problem. Do not add arbitrary default routes while a remote session depends on the connection.

**Cleanup:** read-only commands require none.

**Reference:** [Official documentation](https://man7.org/linux/man-pages/man8/ip.8.html).

[Back to top](#jump-to-a-program)

---

<a id="program-ss"></a>

## ss

Identify listening ports, active sockets and the processes that own them. Part of iproute2.

### Install and verify

```bash
sudo apt update
apt policy iproute2
sudo apt install iproute2
ss -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT. Use process visibility only when needed; sudo can reveal other users' sockets.

```bash
ss -tuln
sudo ss -tulpn
ss -tn state established
```

`t` TCP; `u` UDP; `l` listening; `n` numeric addresses; `p` processes. UDP does not perform TCP-style listening handshakes even though it appears in combined output.

#### Find the local HTTP server

```bash
ss -ltn 'sport = :8000'
```

After starting the HTTP lab, expect a listener at `127.0.0.1:8000`. A listener at `0.0.0.0:8000` accepts on all IPv4 interfaces, subject to firewall/routing. `127.0.0.1` is loopback-only. IPv6 `::` binding behavior can depend on system socket settings.

#### Determine a port conflict

```bash
sudo ss -ltnp 'sport = :8000'
```

Read the PID/process before deciding whether to stop it. Do not kill a random service merely because it occupies your desired lab port; choosing another port is often easier.

**Troubleshooting:** no listener may mean the server exited or bound another address/port. A listener proves only local socket state, not remote reachability or authentication. Process details may be hidden without privileges.

**Cleanup:** inspection leaves sockets unchanged. Stop only your own lab server in its terminal.

**Reference:** [Official documentation](https://man7.org/linux/man-pages/man8/ss.8.html).

[Back to top](#jump-to-a-program)

---

<a id="program-nmcli"></a>

## nmcli / NetworkManager

Inspect and manage connections controlled by NetworkManager. Distinguish a device from its saved connection profile.

### Install and verify

```bash
sudo apt update
apt policy network-manager
sudo apt install network-manager
nmcli --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT initially; activation/deactivation CHANGES connectivity. NetworkManager is often installed already. Installing/restarting it during a remote session can disrupt access.

```bash
nmcli device status
nmcli connection show --active
nmcli connection show
```

A profile can exist while inactive. Device state and profile names help identify what is actually connected.

#### Connect to your own Wi-Fi

```bash
nmcli device wifi list
nmcli --ask device wifi connect 'YOUR_SSID'
```

Replace the SSID; `--ask` prompts for secrets instead of putting a password in history. Listing may initiate a wireless scan. Enterprise authentication can need a more detailed profile; use the appropriate GUI or documented enterprise settings.

#### Reactivate a saved profile

```bash
nmcli connection up 'YOUR_PROFILE_NAME'
```

Use the exact name from your output. This can interrupt a current connection. To deliberately disconnect a specific device use `nmcli device disconnect DEVICE` only with a recovery path.

**Troubleshooting:** “NetworkManager is not running” requires checking service status; “unmanaged” can mean another service/config owns the device. Do not start competing managers. After wireless monitor mode, restore managed mode before reconnecting.

**Cleanup:** reconnect your original profile if you changed it. Do not delete profiles unless you intend to lose their saved settings.

**Reference:** [Official documentation](https://networkmanager.dev/docs/api/latest/nmcli.html).

[Back to top](#jump-to-a-program)

---

<a id="program-dig"></a>

## dig

Query DNS records and inspect resolver answers. Both tools are supplied by BIND utilities on typical Debian-based installations.

### Install and verify

```bash
sudo apt update
apt policy dnsutils
sudo apt install dnsutils
dig -version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK. Query the configured resolver:

```bash
dig example.com A
dig example.com AAAA +short
dig example.com MX
dig -x 127.0.0.1
```

Read the response status, ANSWER section and queried SERVER. `+short` hides diagnostic context; use full output for failures. A and AAAA are IPv4/IPv6 addresses; MX describes mail routing. Reverse lookup may return no name.

#### Compare a specific resolver

```bash
dig @192.168.56.1 lab.test A
```

Only use a resolver you control or are authorized to query. The example lab zone must exist there. `NXDOMAIN` means that resolver reports the name absent; `SERVFAIL` indicates a resolution failure, not necessarily absence. A timeout can be network or service trouble.

**Troubleshooting:** dig queries DNS directly and may differ from applications using hosts files or other name services. Compare with `getent hosts NAME`. Avoid assuming a CDN answer is the origin server.

**Cleanup:** no local settings changed. Queries can be logged by your resolver.

**Reference:** [Official documentation](https://bind9.readthedocs.io/en/latest/manpages.html).

[Back to top](#jump-to-a-program)

---

<a id="program-nslookup"></a>

## nslookup

Query DNS records and inspect resolver answers. Both tools are supplied by BIND utilities on typical Debian-based installations.

### Install and verify

```bash
sudo apt update
apt policy dnsutils
sudo apt install dnsutils
nslookup -version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK. Start with a single name:

```bash
nslookup example.com
nslookup -type=MX example.com
nslookup example.com 192.168.56.1
```

The last command chooses the example lab resolver; replace it with one you use legitimately. Read which server answered and whether the result is authoritative. “Non-authoritative” commonly means a recursive resolver answered from cached/forwarded data, not that the result is invalid.

#### Interactive session

```text
nslookup
> set type=AAAA
> example.com
> exit
```

Run `nslookup` in your terminal, then enter only the text after each `>` prompt. It switches query type for subsequent requests.

**Troubleshooting:** NXDOMAIN, SERVFAIL and timeouts are different conditions. Compare a working name, the configured resolver and system resolution through getent. Do not replace system DNS just because one record type has no answer.

**Cleanup:** exit the interactive shell. These queries do not alter resolver configuration.

**Reference:** [Official documentation](https://bind9.readthedocs.io/en/latest/manpages.html).

[Back to top](#jump-to-a-program)

---

<a id="program-getent"></a>

## getent

Query the system name-service configuration, including hosts files and DNS where configured.

### Install and verify

```bash
sudo apt update
apt policy libc-bin
sudo apt install libc-bin
getent --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT and possible NETWORK. libc-bin is a shared system package; getent normally exists already.

```bash
getent hosts localhost
getent ahosts example.com
getent passwd "$USER"
```

Hosts uses system NSS configuration; ahosts returns address-family-aware results. The passwd query prints the current user's account record, not password contents. Do not publish full account records unnecessarily.

#### Compare system and DNS resolution

```bash
getent hosts app.test
dig app.test A
```

A lab name in `/etc/hosts` may resolve through getent while dig reports no DNS record. That difference is expected because the tools consult different sources. Do not assume it means a tool is broken.

**Troubleshooting:** inspect the relevant line in `/etc/hosts` and the `hosts:` configuration in `/etc/nsswitch.conf` if you administer the machine. A missing result has a nonzero exit status; it can reflect absent records or service failures. Avoid dumping unrelated identity databases.

**Cleanup:** these commands make no configuration changes. Local hosts entries you deliberately added for another lab should be removed individually when no longer required.

**Reference:** [Official documentation](https://manpages.debian.org/stable/manpages/getent.1.en.html).

[Back to top](#jump-to-a-program)

---

<a id="program-sysctl"></a>

## sysctl

Inspect and deliberately change kernel runtime parameters. Most network failures do not require changing these settings.

### Install and verify

```bash
sudo apt update
apt policy procps
sudo apt install procps
sysctl --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT for reads; CHANGE for writes. procps is commonly installed already.

```bash
sysctl net.ipv4.ip_forward
sysctl net.ipv6.conf.all.disable_ipv6
sysctl net.ipv6.conf.default.disable_ipv6
```

`ip_forward=0` disables IPv4 forwarding; `disable_ipv6=0` enables IPv6. Be precise about the name's negative wording.

#### Save a baseline before any justified change

```bash
sysctl net.ipv4.ip_forward > forwarding-baseline.txt
```

This writes a note, not a restorable backup script. If a documented lab requires forwarding, first understand its routing/firewall implications. A temporary write uses `sudo sysctl -w KEY=VALUE` with a real key/value; restore the recorded value when finished.

#### Persistent settings

For a deliberate persistent change, put only the intended key/value in a named file under `/etc/sysctl.d/`, then load that file with `sudo sysctl -p /etc/sysctl.d/FILENAME.conf`. Do not paste placeholder paths. `sysctl --system` loads many configuration files, so it can apply unrelated changes.

**Troubleshooting:** a missing key can mean unsupported kernel functionality. Permission denied usually indicates the write requires privileges or is restricted in a container. Do not turn IPv6 off/on globally as a universal VPN repair.

**Cleanup:** restore changed runtime values and remove only your own persistent configuration entry. Keep the baseline until restoration is confirmed.

**Reference:** [Official documentation](https://manpages.debian.org/stable/procps/sysctl.8.en.html).

[Back to top](#jump-to-a-program)

---

<a id="program-burpsuite"></a>

## Burp Suite Community

Intercept, inspect and replay HTTP requests in a dedicated browser testing workflow. Community is free; Professional is a separate licensed product.

### Install and verify

```bash
sudo apt update
apt policy burpsuite
sudo apt install burpsuite
burpsuite --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK and WRITE; intercepted requests can change application state.

#### Start and connect

```bash
burpsuite
```

If the repository package is unavailable, download the Linux installer from PortSwigger's official download page. Verify its origin, select the build for your architecture and follow the installer; do not use keygens or cracked installers. GUI launchers may not implement `--help`; the installed app's About page shows its version.

1. Create a temporary project if prompted and use the default configuration for your first lab.
2. Open Proxy's built-in browser. Browse your own lab URL, such as the local HTTP server.
3. Inspect Proxy → HTTP history. Keep Intercept off when you want requests to continue normally; turn it on only when ready to forward/drop paused requests.

#### Replay one request

Send the `GET /hello.txt` request to Repeater. Send it unchanged and inspect 200/body, then change the path to `/missing.txt` and send again. Compare the 404 result. The built-in browser is already configured; external browsers require a dedicated proxy profile and the Burp CA for HTTPS interception.

#### Save evidence

Save the relevant raw HTTP request, not just the response HTML. Redact cookies/tokens before committing files. A raw request includes method/path, Host header, headers, blank line and optional body. Adding `url=file://...` is only a parameter; it does not create a file-read capability without a vulnerable application.

**Troubleshooting:** a “hanging” browser often has an intercepted request waiting. Port conflicts require changing proxy settings and browser configuration together. HTTPS errors in an external profile may require correct CA trust.

**Cleanup:** close the test browser, stop proxy listeners and restore any external browser proxy/CA changes. Keep interception CAs limited to test profiles.

**Reference:** [Official documentation](https://portswigger.net/burp/documentation/desktop/getting-started/download-and-install).

[Back to top](#jump-to-a-program)

---

<a id="program-tar"></a>

## tar

Create, list and extract archives; compression and archiving are separate steps combined by convenient options.

### Install and verify

```bash
sudo apt update
apt policy tar
sudo apt install tar
tar --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT or WRITE. Work in an empty destination and avoid sudo for ordinary extraction.

```bash
tar -tf archive.tar.gz
mkdir -p extracted
tar -xzf archive.tar.gz -C extracted
```

`-t` lists, `-x` extracts, `-z` handles gzip, `-f` supplies the archive file and `-C` changes extraction directory. The filename must follow `-f` correctly; `-f` is not required to be the final flag. GNU tar can auto-detect common compression when extracting with `tar -xf`.

#### Back up a folder and verify it

```bash
tar -czf notes-backup.tar.gz notes/
tar -tf notes-backup.tar.gz
```

`-c` creates a new archive. This overwrites an existing output archive, so choose a new backup filename. To restore, extract into a new directory rather than over the live files and compare contents.

**Troubleshooting:** “not in gzip format” can mean the suffix does not match the content or the download is an error page. Inspect before extraction. Absolute/traversal paths, links and decompression size can make unknown archives dangerous; avoid privileged extraction and inspect member names/size.

**Cleanup:** remove only your generated archive or known restored files after confirming the source remains intact. Follow the archive practice lab for exact temporary-file cleanup.

**Reference:** [Official documentation](https://www.gnu.org/software/tar/manual/).

[Back to top](#jump-to-a-program)

---

<a id="program-routersploit"></a>

## RouterSploit

Explore embedded-device module metadata in an isolated, firmware-specific lab. Historical dependencies may not support a modern Parrot release.

### Install and verify

Use a separate user-owned checkout and inspect upstream requirements first:

```bash
sudo apt install git python3-venv
mkdir -p ~/tools
git clone https://github.com/threat9/routersploit.git ~/tools/routersploit
cd ~/tools/routersploit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python rsf.py
```

An existing destination must be inspected rather than overwritten. Dependency installation can execute build code. Upstream compatibility must be checked; no claim is made that all dependencies work on current Parrot. Python 2 packages such as python-pip/python-dev are not a valid modern setup.

### Use it in practice

**Impact:** NETWORK/WRITE during installation; selected modules may change or destabilize devices.

#### Launch in its isolated environment

```bash
cd ~/tools/routersploit
source .venv/bin/activate
python rsf.py
```

Inside the framework, start with `help`. Use tab completion and the installed module descriptions instead of an old fixed list. Do not assume a scanner or a check is passive; read the module implementation/documentation before running it.

#### Practical identification workflow

1. On your own router, read its administration page or label for exact model/hardware revision and firmware version.
2. Compare that version to the vendor's advisory and RouterSploit module description.
3. Use module `show options`/help as provided by the current shell to understand target fields. Do not run an exploit against a merely similar device name.
4. Prefer updating and validating vendor firmware in a disposable spare-device lab before any intrusive validation.

**Troubleshooting:** modern Python/build dependency failures may mean the project needs an older supported isolated environment. Use an upstream-documented disposable VM/container; do not downgrade Parrot's system Python. A module not present is a version difference, not permission to choose a random exploit.

**Cleanup:** exit the framework, deactivate the venv, stop lab services and restore your spare device's known-good configuration/firmware as appropriate. Preserve source commit/version with notes.

**Reference:** [Official documentation](https://github.com/threat9/routersploit).

[Back to top](#jump-to-a-program)

---

<a id="program-crackmapexec"></a>

## CrackMapExec migration

Understand older CME notes and move new workflows to NetExec without assuming command-line flags are identical.

### Install and verify

For new Parrot installations, use the [NetExec installation guide](#program-netexec). This migration page intentionally does not recommend a fresh legacy CME installation. Query an existing command with `command -v crackmapexec` before deciding whether to retain it.

### Use it in practice

**Impact:** INSPECT for migration preparation; legacy commands can perform NETWORK actions.

#### Identify what is installed

```bash
command -v crackmapexec
command -v nxc
apt policy crackmapexec netexec
```

A missing command simply means it is not on PATH. Do not install an unmaintained fork merely to reproduce an old cheat-sheet line.

#### Migration example

Old notes often contain `crackmapexec smb HOST`. For a new setup, install NetExec using its dedicated guide and start with:

```bash
nxc smb --help
nxc smb 192.168.56.20
```

For authenticated share or policy enumeration, use a designated lab account and validate current flags. Re-check output format, workspace behavior and credential handling before converting scripts. A filename change alone is not a tested migration.

**Troubleshooting:** both tools on PATH can lead to testing one build while reading another's documentation. Record exact executables and versions. Preserve old reports before removing a legacy installation and avoid automatic conversion of post-exploitation commands.

**Cleanup:** retire the old tool only through the manager that installed it after you no longer need its data. The new workflow is documented in [NetExec](#program-netexec).

**Reference:** [Official documentation](https://github.com/Pennyw0rth/NetExec).

[Back to top](#jump-to-a-program)

---

<a id="program-netexec"></a>

## NetExec

Assess protocol configuration and permitted account access in Windows/AD labs. The primary CLI is commonly nxc; verify installed entry points.

### Install and verify

```bash
sudo apt update
apt policy netexec
sudo apt install netexec
nxc --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK; authenticated enumeration can produce audit events. APT availability depends on Parrot release.

#### Isolated upstream fallback

If no Parrot package candidate exists, use a user-level pipx install instead of mixing distributions:

```bash
sudo apt install pipx git
pipx ensurepath
pipx install git+https://github.com/Pennyw0rth/NetExec
```

Open a new terminal. Read the upstream supported Python/build requirements if dependencies fail; some builds require Python headers or Rust. Record the source commit/version.

#### Discover one lab SMB endpoint

```bash
nxc smb 192.168.56.20
nxc smb --help
```

This reports available SMB/OS/domain clues where the server permits them; unauthenticated metadata is not proof of compromise.

#### Inspect shares with a designated account

```bash
read -r -s -p 'Disposable lab password: ' lab_password
printf '\n'
nxc smb 192.168.56.20 -u labuser -p "$lab_password" --shares
unset lab_password
```

Use only the credentials supplied for the lab. Passwords expanded on the command line can be visible to local process observers even if not in shell history. `--pass-pol` queries policy where supported/authorized. Do not supply random passwords as a substitute for guest access.

**Troubleshooting:** domain names, target resolution, time synchronization and SMB policy affect authentication. An “admin” marker is a tool interpretation to validate, not a guarantee that every action succeeds. No “stealth” claim guarantees evasion.

**Cleanup:** close the tool and protect its workspace/database. Update a pipx install with pipx, and an APT install with APT; do not maintain both unknowingly.

**Reference:** [Official documentation](https://www.netexec.wiki/getting-started/installation/installation-on-unix).

[Back to top](#jump-to-a-program)

---

<a id="program-smbclient"></a>

## smbclient

Browse authorized Windows/Samba shares with an interactive client and prompted credentials.

### Install and verify

```bash
sudo apt update
apt policy smbclient
sudo apt install smbclient
smbclient --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK; downloads WRITE locally, uploads WRITE remotely. Prerequisites: an actual lab SMB server, a named share and a permitted test account.

```bash
smbclient -L 192.168.56.20 -U labuser
smbclient //192.168.56.20/Data -U labuser
```

Replace host, account and Data share with values provided by your lab. Enter the password at the prompt. Listing shares is not user enumeration. For a deliberately guest-enabled lab, `-N` skips the password prompt; it does not bypass authentication.

#### Inside the SMB prompt

```text
help
ls
cd documents
lcd /tmp
get example.txt
quit
```

Use only a folder/file that actually exists. `cd` changes the remote location; `lcd` changes the local download directory. `get` copies a remote file locally; `put` uploads and changes the server. A read-only exercise needs no upload.

#### Domain account

```bash
smbclient -L 192.168.56.20 -U 'LAB/labuser'
```

Your server determines accepted domain/workgroup naming. Prefer a prompted password rather than embedding it in the account string.

**Troubleshooting:** access denied can reflect credentials or share/filesystem permissions. A visible share may still be unreadable. Check server policy rather than forcing SMB1 or weakening authentication.

**Cleanup:** quit the client and remove only the authorized test downloads you no longer need; do not delete remote files as local cleanup.

**Reference:** [Official documentation](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html).

[Back to top](#jump-to-a-program)

---

<a id="program-cifs-utils"></a>

## CIFS mounts / cifs-utils

Mount an SMB share into the local filesystem with explicit permissions and a clear unmount step.

### Install and verify

```bash
sudo apt update
apt policy cifs-utils
sudo apt install cifs-utils
mount.cifs -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK and MOUNT; writable mounts can change remote files. Use a read-only mount first.

```bash
sudo mkdir -p /mnt/lab-data
sudo mount -t cifs //192.168.56.20/Data /mnt/lab-data -o username=labuser,ro
findmnt /mnt/lab-data
ls -la /mnt/lab-data
```

Substitute your server/share/account and enter the password at the prompt. `ro` requests read-only access from this mount. This does not change the underlying account's server-side permissions.

#### Inspect files

```bash
find /mnt/lab-data -maxdepth 2 -type f -ls
```

Restrict depth to avoid traversing a large share. Opening files can still generate network traffic and server audit events. Do not put passwords directly in command history. For persistent mounts, use a root-owned credentials file with restrictive permissions and the documented fstab options; do not improvise a public credentials path.

#### Unmount

```bash
cd ~
sudo umount /mnt/lab-data
sudo rmdir /mnt/lab-data
```

Only remove the empty mountpoint after successful unmount. Never recursively delete a mounted share to clean up the local directory.

**Troubleshooting:** “busy” means a process still uses the mount; close viewers/shells and retry normally. Permission errors require server/account checks. Protocol negotiation problems should be resolved with a supported server/client version, not routine SMB1 enablement.

**Cleanup:** unmount successfully before removing the empty mountpoint. Do not recursively delete a mounted remote share.

**Reference:** [Official documentation](https://manpages.debian.org/stable/cifs-utils/mount.cifs.8.en.html).

[Back to top](#jump-to-a-program)

---

<a id="program-smbmap"></a>

## SMBMap

Summarize SMB shares and effective permissions for an authorized account.

### Install and verify

```bash
sudo apt update
apt policy smbmap
sudo apt install smbmap
smbmap --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK; permission checks may WRITE test files unless disabled. Read help for your installed release before assessing a production share.

```bash
smbmap -H 192.168.56.20 --no-write-check
```

`-H` selects one host. Current upstream supports `--no-write-check`; confirm it in local help. This example attempts unauthenticated access and may show no shares. It does not bypass permissions.

#### Authenticated lab inventory

```bash
read -r -s -p 'Disposable lab password: ' lab_password
printf '\n'
smbmap -H 192.168.56.20 -u labuser -p "$lab_password" --no-write-check
unset lab_password
```

The shell prompt avoids storing the literal password in history, but the expanded password can still appear in process arguments. Use only disposable lab credentials for this example, and prefer a supported secure credential method in real assessments. Review READ/WRITE claims in context; skipping write checks limits what can be confirmed.

#### Validate a result

Connect to a reported share with smbclient and list a known harmless folder. Share access and nested file permissions may differ.

**Troubleshooting:** blank output can be failed/guest authentication, filtering or no permitted shares. Domain settings and SMB support matter. Do not enable arbitrary execution or automatic downloads merely to list permissions.

**Cleanup:** stop the tool and protect results. If you intentionally enabled write checks, verify any test artifacts were removed according to the installed version's behavior.

**Reference:** [Official documentation](https://github.com/ShawnDEvans/smbmap).

[Back to top](#jump-to-a-program)

---

<a id="program-impacket"></a>

## Impacket

Python protocol libraries and example clients for Windows/SMB and related network protocols.

### Install and verify

```bash
sudo apt update
apt policy python3-impacket impacket-scripts
sudo apt install python3-impacket impacket-scripts
dpkg -L impacket-scripts
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK for clients, WRITE for installs/downloads. Package splits and entry-point names vary; check APT candidates individually before installation.

#### Upstream isolated fallback

```bash
sudo apt install pipx
pipx install impacket
pipx list
```

Do this only when deliberately choosing upstream instead of the distribution copy. The upstream example may be `smbclient.py`, while a distro wrapper may be `impacket-smbclient`.

#### Locate and run a permitted client

```bash
command -v impacket-smbclient
command -v smbclient.py
```

If your installed wrapper is impacket-smbclient, use:

```bash
impacket-smbclient -h
impacket-smbclient 'LAB/labuser@192.168.56.20'
```

Enter the password when prompted rather than placing it in the target string. In the client, use `help`, `shares`, `use Data`, `ls` and `exit` with actual authorized share names. This is a protocol-learning workflow, not remote execution.

#### Verify the result

Compare a known share/file listing with Samba smbclient. Differences can reflect negotiation/authentication details, not necessarily a vulnerability.

**Troubleshooting:** “command not found” often reflects the packaging prefix or pipx PATH. Kerberos needs appropriate DNS/time/realm configuration; do not switch to credential-dumping examples to diagnose a file listing.

**Cleanup:** exit the client and remove only authorized local downloads. Update/remove through the selected manager, preserving any needed test reports.

**Reference:** [Official documentation](https://github.com/fortra/impacket).

[Back to top](#jump-to-a-program)

---

<a id="program-nmap"></a>

## Nmap

Discover hosts, inspect ports and identify services within an explicitly authorized scope.

### Install and verify

```bash
sudo apt update
apt policy nmap
sudo apt install nmap
nmap --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK; some probes/scripts can affect services. Begin with the local HTTP practice lab.

```bash
nmap -sT -p 8000 127.0.0.1
nmap -sV -p 8000 127.0.0.1
```

`-sT` completes TCP connections; `-sV` sends identification probes. An open port means a service accepted connections; a service label may just be a database guess.

#### Inventory a single lab host

```bash
mkdir -p results
nmap -sT --top-ports 20 -oA results/initial 192.168.56.20
nmap -sV -p 22,80,443 -oN results/services.txt 192.168.56.20
```

Choose ports from observed results rather than assuming the example host has them. `-oA` creates three formats. `-p-` covers TCP 1–65535; UDP needs `-sU` and generally privileges. Large scans cost time/traffic.

#### Discovery and scripts

```bash
nmap -sn 192.168.56.0/24
nmap --script-help http-title
nmap --script http-title -p 80,443 192.168.56.20
```

Only scan an authorized subnet. `-sn` skips port scanning; `-Pn` instead skips host discovery and treats targets as up. Inspect scripts before running; `--script vuln` is not a comprehensive safe audit.

**Troubleshooting:** filtered is uncertainty, not closed. Wrong VPN routes, target state and firewall behavior affect results. Raw SYN/OS scans need appropriate privileges. `-p` takes ports, not IP ranges.

**Cleanup:** stop unfinished scans with Ctrl+C and retain only appropriately protected/redacted results.

**Reference:** [Official documentation](https://nmap.org/book/man.html).

[Back to top](#jump-to-a-program)

---

<a id="program-curl"></a>

## curl

Send HTTP requests and inspect responses without a browser.

### Install and verify

```bash
sudo apt update
apt policy curl
sudo apt install curl
curl --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK and optional WRITE. Start the local HTTP lab first.

```bash
curl -i http://127.0.0.1:8000/hello.txt
curl -I http://127.0.0.1:8000/hello.txt
curl -o saved-hello.txt http://127.0.0.1:8000/hello.txt
```

`-i` includes response headers; `-I` sends HEAD, which some servers handle differently; `-o` writes the body to a file and overwrites that path.

#### Bounded request and structured body

```bash
curl --connect-timeout 5 --max-time 15 -L --max-redirs 3 http://127.0.0.1:8000/
curl -i -H 'Content-Type: application/json' --data '{"message":"hello"}' http://127.0.0.1:8000/api
```

The second example demonstrates JSON POST formatting; the simple Python file server does not implement this API and should reject POST. Use your own app implementing `/api` to test success. `-L` follows redirects; avoid forwarding secrets to unrelated destinations.

#### Exit status versus HTTP status

```bash
curl --fail-with-body -sS http://127.0.0.1:8000/missing.txt
```

By default curl can exit successfully even for HTTP errors. `--fail-with-body` makes HTTP 400+ produce a failure status while retaining the body; older builds may need `--fail` instead.

**Troubleshooting:** error 6 is resolution, 7 connection failure, and certificate errors need fixing trust/hostname/time. Do not routinely use `-k`.

**Cleanup:** delete only response files you created, and protect requests containing credentials.

**Reference:** [Official documentation](https://curl.se/docs/manpage.html).

[Back to top](#jump-to-a-program)

---

<a id="program-wget"></a>

## Wget

Download a resource to a local file with clear filename and timeout controls.

### Install and verify

```bash
sudo apt update
apt policy wget
sudo apt install wget
wget --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK and WRITE. Run the local HTTP lab and download its harmless text file:

```bash
wget --timeout=15 --tries=1 -O wget-hello.txt http://127.0.0.1:8000/hello.txt
cat wget-hello.txt
```

`-O` sets the destination and can truncate/overwrite it; do not point it at an important file. Check that the body is expected before executing or trusting any download.

#### Inspect server response

```bash
wget --server-response --spider http://127.0.0.1:8000/hello.txt
```

Spider checks availability without deliberately saving the resource as a normal download. Server behavior varies; read the method/status output. A successful download does not authenticate a publisher by itself.

#### Resume a large known download

`wget -c URL` attempts continuation when the server supports it. Use this only for the same resource; if the remote file changed, verify the final checksum. Do not run recursive mirroring against a site without considering scope, traffic and ownership.

**Troubleshooting:** a downloaded HTML error page is not the expected executable/archive. Check status, filename and publisher checksum. Certificate errors should be fixed through trust/time/name configuration, not bypassed globally.

**Cleanup:** remove `wget-hello.txt` if it was generated solely for this example.

**Reference:** [Official documentation](https://www.gnu.org/software/wget/manual/).

[Back to top](#jump-to-a-program)

---

<a id="program-gobuster"></a>

## Gobuster

Enumerate web paths, DNS names or virtual hosts with explicit mode-specific options.

### Install and verify

```bash
sudo apt update
apt policy gobuster
sudo apt install gobuster
gobuster --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK and WRITE. Begin with the local HTTP lab and a three-entry wordlist.

```bash
printf '%s\n' hello.txt missing.txt robots.txt > lab-paths.txt
gobuster dir -u http://127.0.0.1:8000 -w lab-paths.txt -t 2 -o gobuster-lab.txt
```

`dir` selects path enumeration; `-u` is the base URL; `-w` supplies candidates; `-t` limits concurrent workers. Expect hello.txt to exist; independently verify results with curl. `-o` writes results.

#### File extensions and lab virtual hosts

```bash
gobuster dir --help
gobuster dir -u http://127.0.0.1:8000 -w names.txt -x txt,html -t 2
gobuster vhost -u http://app.test --append-domain -w labels.txt -t 2
```

Create `names.txt` with bare stems such as `hello`; do not reuse `hello.txt` when appending `.txt`. The vhost example needs app.test resolving to your lab web server and labels.txt containing short labels such as dev. It tests HTTP Host routing, not DNS existence. `--append-domain` builds full hostnames from labels.

#### DNS mode

Read `gobuster dns --help` for the installed build: domain flag names changed across versions. Do not copy the old global `-m dir` interface.

**Troubleshooting:** a wildcard/custom error page may match every word. Request a random nonexistent path, compare response length/status and set only filters supported by your release. Follow redirects intentionally. TLS bypass does not repair certificates.

**Cleanup:** Ctrl+C stops requests; remove generated test files/results only after reviewing evidence.

**Reference:** [Official documentation](https://github.com/OJ/gobuster).

[Back to top](#jump-to-a-program)

---

<a id="program-seclists"></a>

## SecLists

A collection of test wordlists for discovery and security exercises. It is data, not an executable scanner.

### Install and verify

```bash
sudo apt update
apt policy seclists
sudo apt install seclists
dpkg -L seclists
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT for list selection; copying/writing lists is WRITE. Installation may require significant disk space; read APT's size estimate.

```bash
dpkg -L seclists | less
find /usr/share/seclists -type f -iname '*common*'
```

The `/usr/share/seclists` path is a common location, not guaranteed. Use the path actually reported by dpkg. If your repositories do not package it, clone the official danielmiessler/SecLists repository into your own tools directory and record its commit.

#### Inspect and select a list

```bash
head -n 20 /path/to/chosen-list.txt
wc -l /path/to/chosen-list.txt
```

Replace the placeholder path. A short technology-appropriate list is a better starting point than an enormous catch-all. Review content and encoding before feeding a tool.

#### Small self-contained practice list

```bash
printf '%s\n' hello.txt missing.txt robots.txt > lab-paths.txt
```

Use this with ffuf/Gobuster against the local HTTP lab. It gives predictable positive and negative results without needing a large package.

**Troubleshooting:** a missing `/opt/SecLists` folder is a path assumption, not a broken scanner. Full-domain lists and label-only subdomain lists need different vhost settings. A list can contain comments or unusual characters; know your tool's parsing behavior.

**Cleanup:** remove only your lab-generated list. Do not store real users' secrets in shared wordlists.

**Reference:** [Official documentation](https://github.com/danielmiessler/SecLists).

[Back to top](#jump-to-a-program)

---

<a id="program-nikto"></a>

## Nikto

Check web servers for known risky files, outdated components and configuration clues. Findings need manual validation.

### Install and verify

```bash
sudo apt update
apt policy nikto
sudo apt install nikto
nikto -Version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK and WRITE; active checks can be noisy. Use your isolated web lab.

```bash
nikto -Help
nikto -h http://127.0.0.1:8000 -o nikto-lab.txt -Format txt
```

`-h` sets the target URL, `-o` writes findings and `-Format` selects an output formatter. Read any scan errors, not just finding counts. The simple Python server may produce little meaningful vulnerability coverage; a deliberately configured lab web app is a richer exercise.

#### Investigate one finding

1. Read its exact URL, method and evidence.
2. Request that resource manually through curl or Burp within scope.
3. Check the response body instead of treating a status code alone as proof.
4. Compare the installed server's actual version/configuration with vendor guidance before declaring it vulnerable.

Nikto is a web-server scanner, not a general OS-identification tool. Proxy/user-agent options do not make a test invisible or authorized. Package-provided launchers avoid assuming nikto.pl lives in the current folder.

**Troubleshooting:** connection refusal means no service accepted that address/port. A reverse proxy, authentication gateway or custom errors can distort findings. Limit the target/scope and use the installed help for options controlling duration/plugins.

**Cleanup:** Ctrl+C stops the scan; protect the report because paths/version details can be sensitive. Update the installed package through its original manager rather than mixing untracked source updates into APT files.

**Reference:** [Official documentation](https://github.com/sullo/nikto/wiki).

[Back to top](#jump-to-a-program)

---

<a id="program-wfuzz"></a>

## Wfuzz

Fuzz paths or request parameters with payload generators and filters based on response properties.

### Install and verify

```bash
sudo apt update
apt policy wfuzz
sudo apt install wfuzz
wfuzz --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK. Use a short list against the local HTTP lab.

```bash
printf '%s\n' hello.txt missing.txt robots.txt > lab-paths.txt
wfuzz -w lab-paths.txt 'http://127.0.0.1:8000/FUZZ'
wfuzz --hc 404 -w lab-paths.txt 'http://127.0.0.1:8000/FUZZ'
```

The first pass establishes actual responses. The second hides HTTP 404 only after that status has been confirmed as a reliable negative. `FUZZ` marks substitution; `-w` chooses the list.

#### Numeric parameter example

```bash
wfuzz -z range,0-3 'http://127.0.0.1:8000/item?id=FUZZ'
```

A local application must implement this endpoint for meaningful results. `-z range,0-3` generates four candidate values. The static file-server lab does not have an item database.

#### Understand filtering

`--hc` hides status codes, `--hl` hides line counts and `--hw` hides word counts. Derive values from your app; a copied `--hl 97` can conceal real content or do nothing. Run `wfuzz --help` to see your installed build's thread/output options before increasing traffic.

**Troubleshooting:** a custom 200 error page needs body/size-based analysis. HTTPS support can depend on PycURL's SSL backend; use the supported package environment rather than breaking system Python to repair it.

**Cleanup:** stop with Ctrl+C. If you saved output, remove secrets before sharing. No listener is created by these examples.

**Reference:** [Official documentation](https://wfuzz.readthedocs.io/en/latest/user/basicusage.html).

[Back to top](#jump-to-a-program)

---

<a id="program-ffuf"></a>

## ffuf

Replace a FUZZ marker in HTTP requests with wordlist entries, with calibration, rate limits and structured output.

### Install and verify

```bash
sudo apt update
apt policy ffuf
sudo apt install ffuf
ffuf -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK and WRITE. With the local HTTP lab running:

```bash
printf '%s\n' hello.txt missing.txt robots.txt > lab-paths.txt
ffuf -u http://127.0.0.1:8000/FUZZ -w lab-paths.txt -t 2 -rate 5 -ac -of json -o ffuf-lab.json
```

`FUZZ` is substituted once per word. `-t` controls concurrent workers; `-rate` limits requests per second. `-ac` calibrates filtering; `-of json` chooses format and `-o` saves a report.

#### Examine positives

```bash
jq '.results[] | {url, status, length}' ffuf-lab.json
curl -i http://127.0.0.1:8000/hello.txt
```

Validate responses independently; calibration can hide useful results. `jq` is optional and separately installed. `-mc` chooses matching status codes and `-fc` excludes codes; decide based on the application's real negative response.

#### Test a query parameter

```bash
ffuf -u 'http://127.0.0.1:8000/search?q=FUZZ' -w terms.txt -t 2 -rate 5
```

This needs a real local application implementing `/search` and a short terms.txt. The static Python file server does not implement search. Quote URLs so the shell does not interpret query delimiters.

**Troubleshooting:** inspect a known valid and a known invalid request before tuning filters. Login redirects, CSRF state and expiring cookies can invalidate results. Never publish real tokens inside saved commands.

**Cleanup:** stop the run, close the test server when finished, and redact/archive results as appropriate.

**Reference:** [Official documentation](https://github.com/ffuf/ffuf).

[Back to top](#jump-to-a-program)

---

<a id="program-postgresql"></a>

## PostgreSQL service for labs

Provide the optional database used by Metasploit workspaces. Service installation and database initialization are separate actions.

### Install and verify

```bash
sudo apt update
apt policy postgresql
sudo apt install postgresql
psql --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** CHANGE; service starts may expose a listener according to its configuration. Install only if you need a local database. Do not reuse production data for security-tool experiments.

```bash
sudo systemctl start postgresql
systemctl status postgresql --no-pager
pg_lsclusters
```

Debian-family packaging can have a meta-service and versioned clusters. A successful meta-service status alone does not prove a cluster is accepting connections; inspect actual cluster state.

#### Local readiness and identity

```bash
pg_isready
sudo -u postgres psql -c 'SELECT version();'
```

The second command uses the local postgres service account with packaging-default local access assumptions. It prints a version query and does not create a database. Do not weaken pg_hba.conf or expose the database publicly merely to make local tools work.

#### Metasploit integration

Use the Metasploit package's supported `msfdb init` helper when supplied. This creates the dedicated database/role it needs. `db_status` is then run inside msfconsole, not the Linux shell.

**Troubleshooting:** verify the correct cluster, socket/port and authentication rules. On installations with an existing cluster, preserve databases and configuration; never delete the data directory as a first fix.

**Cleanup:** if no other applications need the lab service, `sudo systemctl stop postgresql` stops it. Stopping does not delete databases. Remove only a confirmed disposable database through documented PostgreSQL administration after backup.

**Reference:** [Official documentation](https://www.postgresql.org/docs/current/tutorial-start.html).

[Back to top](#jump-to-a-program)

---

<a id="program-metasploit"></a>

## Metasploit Framework

Organize authorized testing modules and evidence in workspaces. Framework is distinct from licensed Metasploit Pro.

### Install and verify

```bash
sudo apt update
apt policy metasploit-framework
sudo apt install metasploit-framework
msfconsole --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** CHANGE for database setup, NETWORK for module execution. Work against a disposable lab.

```bash
sudo systemctl start postgresql
command -v msfdb
sudo msfdb init
msfconsole
```

Run initialization only if this package supplies msfdb and its instructions call for it. Missing helpers require the package/upstream database setup, not guessed commands. Database support is optional for some Framework tasks.

#### Inside msfconsole

```text
db_status
workspace -a local-http
search type:auxiliary name:http_version
use auxiliary/scanner/http/http_version
info
show options
set RHOSTS 127.0.0.1
set RPORT 8000
run
back
hosts
services
```

Start the local HTTP lab first. The module inspects HTTP version clues; banners are not conclusive software evidence. `info` documents behavior and `show options` identifies required values. A module supporting `check` may still send active probes; not every module has it.

#### Session and option terminology

RHOSTS is the module's target selection; RPORT is its service port. LHOST/LPORT describe listener/callback settings for payloads that use them. A database workspace organizes evidence; it does not isolate network traffic.

**Troubleshooting:** disconnected database status requires checking the exact install's DB configuration. Empty hosts/services can reflect no DB connection or no recorded scan. Framework does not imply a Pro web interface on port 3790.

**Cleanup:** use `jobs` and `sessions -l` to identify your active tasks, stop only your lab tasks, and `exit` the console. Stop the optional database only if nothing else needs it.

**Reference:** [Official documentation](https://docs.metasploit.com/).

[Back to top](#jump-to-a-program)

---

<a id="program-meterpreter"></a>

## Meterpreter sessions

Interact with an existing authorized lab session using platform-supported commands. Meterpreter is a payload/session type, not an independent desktop package.

### Install and verify

```bash
sudo apt update
apt policy metasploit-framework
sudo apt install metasploit-framework
msfconsole --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT for inventory; other session commands can WRITE, capture data or change the target. Prerequisite: an existing session deliberately established in a controlled lab; this page does not assume an arbitrary target is accessible.

#### Select the session in msfconsole

```text
sessions -l
sessions -i 1
```

Replace 1 with the actual ID you are permitted to use. Inside the Meterpreter prompt:

```text
help
sysinfo
getuid
pwd
ls
ps
```

Commands depend on OS, extensions and session type. Help is authoritative for that session. sysinfo and getuid identify environment/current identity; they do not elevate privileges.

#### Understand local versus remote paths

```text
lpwd
lls
pwd
ls
background
```

`lpwd`/`lls` refer to the operator's machine; pwd/ls refer to the target. Background returns to msfconsole without terminating the session. To resume, use sessions -i with its ID.

#### End the session

```text
exit
```

Run exit in Meterpreter to end that session; confirm in msfconsole with sessions -l. Closing a client does not guarantee removal of arbitrary artifacts from a target; restore your disposable lab snapshot as needed.

**Troubleshooting:** missing commands reflect session/platform capabilities. An unexpected account or host means stop and verify the correct lab session. Avoid keylogging, webcam access, credential dumping, log clearing and timestamp alteration for ordinary inventory.

**Cleanup:** exit the intended lab session, confirm it is gone from sessions -l, and restore disposable target state if the wider lab created artifacts.

**Reference:** [Official documentation](https://docs.metasploit.com/docs/using-metasploit/advanced/meterpreter/meterpreter-basics.html).

[Back to top](#jump-to-a-program)

---

<a id="program-msfvenom"></a>

## msfvenom

Inspect Framework payload metadata and supported output formats. Installed with Metasploit Framework.

### Install and verify

```bash
sudo apt update
apt policy metasploit-framework
sudo apt install metasploit-framework
msfvenom --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT for the examples below. Payload generation can create executable artifacts; real payload behavior depends on selected options, architecture and target.

```bash
msfvenom -l payloads
msfvenom -l formats
msfvenom -l encoders
```

The listing type after `-l` is required; the old bare `-l` is incomplete. Use listings to identify actual names from your installed Framework rather than copying architecture-specific names from an old sheet.

#### Inspect an example payload's requirements

```bash
msfvenom -p windows/meterpreter/reverse_tcp --list-options
```

This prints metadata/options instead of generating an executable. Confirm the name exists in your installed list. LHOST must be a callback address reachable from the authorized lab target; it is not always your default LAN IP. LPORT is the chosen callback/listener port. Reverse and bind payloads use opposite connection directions.

#### Plan a controlled experiment

Match target OS/architecture, payload options, listener type and routing before following an authorized course lab. A file extension does not change architecture. Staged and stageless payload names differ. Encoding is not encryption and does not guarantee antivirus evasion. Never distribute a disguised backdoor as a file-sharing example.

**Troubleshooting:** a nonexistent payload is a version/name mismatch. Connectivity failures may be routing/NAT/firewall rather than payload generation. An executable opening does not guarantee a session.

**Cleanup:** these inspection commands create no payload. Delete only your own confirmed lab artifacts after stopping matching sessions/listeners, or restore the disposable VM snapshot.

**Reference:** [Official documentation](https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html).

[Back to top](#jump-to-a-program)

---

<a id="program-netcat"></a>

## Netcat / nc

Open simple TCP clients/listeners for local protocol and connection exercises. This guide targets netcat-openbsd, not every nc implementation.

### Install and verify

```bash
sudo apt update
apt policy netcat-openbsd
sudo apt install netcat-openbsd
nc -h
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** LISTEN, NETWORK and WRITE. Netcat traffic here is unauthenticated and unencrypted. Prefer SSH for private remote files.

#### Two-terminal conversation

Terminal A:

```bash
nc -l 127.0.0.1 2222
```

Terminal B:

```bash
nc 127.0.0.1 2222
```

Type a line in either terminal; it appears at the other endpoint. Loopback confines the exercise to this computer. Ctrl+C closes the run.

#### Transfer a small local file

Receiver, terminal A:

```bash
nc -l 127.0.0.1 2222 > received.txt
```

Sender, terminal B:

```bash
printf 'transfer example\n' > original.txt
nc -N 127.0.0.1 2222 < original.txt
sha256sum original.txt
```

After the receiver exits, run `sha256sum received.txt` there and compare. `-N` closes the write side after stdin EOF in OpenBSD nc. `>` overwrites an existing destination. The old `< filename >` trailing operator is invalid shell syntax.

#### Port check

```bash
nc -vz -w 3 127.0.0.1 8000
```

This attempts a connection to one local port. A successful TCP connection does not prove the application is healthy.

**Troubleshooting:** `-N` not supported suggests a different nc implementation. Check local help instead of assuming flags. `-k` keeps listeners serving; it does not provide framing or checksums.

**Cleanup:** close all lab listeners and delete only original.txt/received.txt if created for the exercise.

**Reference:** [Official documentation](https://manpages.debian.org/stable/netcat-openbsd/nc.1.en.html).

[Back to top](#jump-to-a-program)

---

<a id="program-openssh"></a>

## OpenSSH / ssh and scp

Log in and copy files over encrypted authenticated connections. Client installation does not install an SSH server.

### Install and verify

```bash
sudo apt update
apt policy openssh-client
sudo apt install openssh-client
ssh -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK; scp WRITES destination files. Prerequisites: an authorized lab SSH server/account and a trusted way to verify its host-key fingerprint.

```bash
ssh labuser@192.168.56.20
```

Verify the fingerprint before accepting a first connection. A changed host-key warning can indicate reinstall, wrong host or interception; investigate rather than deleting known_hosts blindly. Enter the account's password when requested.

#### Keys and copies

```bash
ssh-keygen -t ed25519 -f ~/.ssh/parrot_lab_ed25519
ssh -i ~/.ssh/parrot_lab_ed25519 labuser@192.168.56.20
scp ./notes.txt labuser@192.168.56.20:~/
scp labuser@192.168.56.20:~/example.txt ./example-copy.txt
```

Use a passphrase and decline overwriting existing keys. Public-key authentication requires provisioning the `.pub` key on the server first; key creation alone does not grant access. Never share/commit the private key. scp paths can overwrite files; choose fresh destinations.

#### Ports and diagnosis

```bash
ssh -p 2222 labuser@192.168.56.20
scp -P 2222 ./notes.txt labuser@192.168.56.20:~/
```

SSH uses lowercase `-p`; scp uses uppercase `-P` for ports. `ssh -v` provides diagnostics; redact before sharing.

**Troubleshooting:** refused means no listener/rejection; timeout suggests routing/filtering; permission denied concerns authentication/authorization. Starting a server is a separate explicit administration task.

**Cleanup:** use exit in the remote shell. Remove unused lab public keys from authorized_keys deliberately, then retire the corresponding private key after confirming it is no longer needed.

**Reference:** [Official documentation](https://man.openbsd.org/ssh).

[Back to top](#jump-to-a-program)

---

<a id="program-python-http-server"></a>

## Python HTTP server

Temporarily serve a dedicated folder for local file inspection and download exercises. Not a production server.

### Install and verify

```bash
sudo apt update
apt policy python3
sudo apt install python3
python3 --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** WRITE and LISTEN; downloads are NETWORK. The server provides no built-in authentication or transport encryption in this basic workflow.

```bash
share_dir=$(mktemp -d /tmp/parrot-share.XXXXXX)
printf 'hello from lab\n' > "$share_dir/hello.txt"
python3 -m http.server 8000 --bind 127.0.0.1 --directory "$share_dir"
```

Keep this terminal open. The explicit bind confines access to loopback. The dedicated directory avoids serving your entire home, including private files. Directory contents may be listed.

#### Verify in another terminal

```bash
curl -i http://127.0.0.1:8000/hello.txt
curl -i http://127.0.0.1:8000/missing.txt
```

Expect 200 with your text, and 404 for the missing path. This server serves files; it does not implement an API, upload handler or database application.

#### Deliberate lab LAN sharing

Only when another authorized lab computer needs access, replace the bind address with your actual lab-interface IP and consider its firewall/routing. Do not use `0.0.0.0` casually on an untrusted network. Ports above 1023 avoid root privileges.

**Troubleshooting:** address-in-use means another listener occupies the port; choose a free port and update requests. Connection refused may mean the server stopped. A 404 means an HTTP response occurred but the path is absent.

**Cleanup:** Ctrl+C in the original terminal, then `rm -- "$share_dir/hello.txt"`, `rmdir -- "$share_dir"`, and `unset share_dir` there. Remove only this known temporary data.

**Reference:** [Official documentation](https://docs.python.org/3/library/http.server.html).

[Back to top](#jump-to-a-program)

---

<a id="program-crunch"></a>

## Crunch

Generate candidate strings from an explicit character set for small controlled exercises. It does not authenticate or crack anything by itself.

### Install and verify

```bash
sudo apt update
apt policy crunch
sudo apt install crunch
crunch --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** WRITE; output can grow exponentially. Some builds show usage with no arguments rather than --help; inspect local usage.

```bash
crunch 2 2 ab12 -o crunch-demo.txt
wc -l crunch-demo.txt
head crunch-demo.txt
```

Two positions over four characters produce 4^2 = 16 lines. The first two numbers are minimum and maximum lengths. Review the output before using it in any other tool.

#### Reproduce the original example accurately

```bash
crunch 4 4 012345abcdef -o crunch-four.txt
wc -l crunch-four.txt
```

There are 12 characters, producing 12^4 = 20,736 candidates. Each fixed-width line also has a newline; disk use grows with both length and candidate count. Increasing to long ranges can fill storage quickly.

#### Decide whether generation helps

For a training service with a known small candidate set, an explicit three-line test file is usually enough. Generating every possible password is not an efficient general recovery method. Respect account lockouts when any list is used for authentication.

**Troubleshooting:** output-path errors need a writable directory; huge estimates call for reducing the range rather than blindly continuing. Stop with Ctrl+C if the generated size is unexpected.

**Cleanup:** delete only the two lab-generated files after reviewing them. Do not publish wordlists containing private personal details or actual secrets.

**Reference:** [Official documentation](https://sourceforge.net/projects/crunch-wordlist/).

[Back to top](#jump-to-a-program)

---

<a id="program-hydra"></a>

## Hydra

Test a small, agreed set of login attempts against a designated training account. Different protocols require different modules.

### Install and verify

```bash
sudo apt update
apt policy hydra
sudo apt install hydra
hydra -h
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK; can trigger lockouts/audit events. Use a disposable local SSH service with a labuser account you created for training and an agreed three-attempt allowance. Do not use your daily account.

```bash
hydra -U ssh
printf '%s\n' wrong-demo-1 wrong-demo-2 LAB_ONLY_CHANGE_ME > lab-passwords.txt
hydra -l labuser -P lab-passwords.txt -t 1 -f ssh://127.0.0.1
```

The example does not create an SSH server/account. Replace the final dummy candidate with the known disposable lab password only in your private test file. `-l` is one user; `-P` is a password file; `-t 1` limits workers; `-f` stops after success on the host. A service may enforce lockouts after even fewer attempts; confirm first.

#### HTML form preparation

```bash
hydra -U http-post-form
```

Before writing a form test, capture the actual action path, POST fields, cookies/CSRF handling and reliable failure/success marker. Placeholders are case-sensitive `^USER^` and `^PASS^`; `^user^` is incorrect. HTTP Basic Auth and an HTML form are different protocols/workflows. Do not substitute a generic form string into a live service.

**Troubleshooting:** zero successes can reflect protocol mismatch, account lockout, dynamic CSRF or incorrect markers rather than wrong candidates. A reported hit needs a single manual confirmation using the designated account.

**Cleanup:** remove private lab candidate/result files, end the dedicated SSH test service if you started it, and remove/reset the disposable account according to your lab setup. Do not retain a known-password file in Git.

**Reference:** [Official documentation](https://github.com/vanhauser-thc/thc-hydra).

[Back to top](#jump-to-a-program)

---

<a id="program-medusa"></a>

## Medusa

Perform module-specific authentication checks in a bounded training environment. Use it as an alternative to Hydra, not a redundant extra run.

### Install and verify

```bash
sudo apt update
apt policy medusa
sudo apt install medusa
medusa -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK; can lock accounts. Prerequisites: a disposable local SSH service/account and a verified small attempt budget.

```bash
medusa -d
medusa -M ssh -q
```

`-d` lists the modules actually compiled into your installation. `-M ssh -q` documents the selected module. The available modules vary by build; a copied static list is unreliable.

#### One known test credential

```bash
read -r -s -p 'Disposable lab password: ' lab_password
printf '\n'
medusa -h 127.0.0.1 -u labuser -p "$lab_password" -M ssh -t 1 -f
unset lab_password
```

Use only a disposable password: expanded arguments may be visible in the local process list despite not appearing literally in shell history. `-h` is one host; `-u` one username; `-p` one password; `-M` the module; `-t 1` one login worker; `-f` stops this host after a valid credential. This confirms a known account rather than guessing a large list.

#### Input files

`-H`, `-U` and `-P` take host, user and password files. Inspect attempt counts before combining files. A generic HTTP module may not implement your application’s form/CSRF flow; inspect `medusa -M http -q` and any separate web-form module actually present.

**Troubleshooting:** module absence requires a supported build or another appropriate tool, not a guessed module name. Read network errors and account policy before interpreting authentication failures.

**Cleanup:** close the test session and reset/remove designated lab credentials. Keep audit output private and redact before sharing.

**Reference:** [Official documentation](http://foofus.net/goons/jmk/medusa/medusa.html).

[Back to top](#jump-to-a-program)

---

<a id="program-sqlmap"></a>

## sqlmap

Validate suspected SQL injection in your own test application using a captured raw request and a single chosen parameter.

### Install and verify

```bash
sudo apt update
apt policy sqlmap
sudo apt install sqlmap
sqlmap --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** NETWORK; active tests can modify application state or burden a database. Prerequisites: a disposable authorized app/database and a raw HTTP request for a real database-backed input. A static Python file server is not an SQL-injection lab.

#### Prepare a request

Capture the intended application request in Burp, save the raw request including headers/blank line/body to `search.req`, and protect cookies/tokens. Identify the parameter name you actually intend to test.

```bash
sqlmap -r search.req -p q --level=1 --risk=1 --threads=1
```

Replace q with the selected parameter. `-r` supplies request bytes; `-p` narrows parameter selection; risk/level limit certain tests but do not make the operation passive. Leave prompts interactive while learning.

#### Proxy and HTTPS context

```bash
sqlmap -r search.req -p q --level=1 --risk=1 --threads=1 --proxy=http://127.0.0.1:8080
```

This needs Burp or another proxy actually listening there. Use `--force-ssl` only when the captured request should use HTTPS. `--force-ssl461` is invalid. Do not use `--batch` to skip decisions before understanding them.

#### Interpret results

A suspected injection needs reproducible evidence and application/database context. Session expiry, WAF responses and unstable pages can distort testing. Review logs and compare a baseline before claiming a finding. No data-dump/OS-shell step is required to document an injection.

**Troubleshooting:** re-capture stale requests, verify Host/content type/CSRF state and test a single input. Use a fresh disposable database when repeatability matters.

**Cleanup:** stop the tool and remove or redact saved request/session data; restore the disposable database from its snapshot if changed.

**Reference:** [Official documentation](https://github.com/sqlmapproject/sqlmap/wiki/Usage).

[Back to top](#jump-to-a-program)

---

<a id="program-iw"></a>

## iw

Inspect modern Linux wireless interfaces, driver capabilities and connection state.

### Install and verify

```bash
sudo apt update
apt policy iw
sudo apt install iw
iw --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT here; a scan sends/receives wireless traffic and can affect connectivity. Requires actual supported wireless hardware, not a VM's virtual Ethernet adapter.

```bash
iw dev
iw list
iw reg get
```

`iw dev` shows current wireless devices/interfaces. `iw list` shows PHY capabilities including supported modes. Regulatory information is not permission to transmit on every listed channel; obey the actual local rules.

#### Inspect your connection

```bash
iw dev wlan0 link
```

Replace wlan0 with a name from iw dev. It reports association details where supported. “Not connected” is a state, not necessarily a driver failure.

#### Scan only when needed

```bash
sudo iw dev wlan0 scan
```

This asks for a scan on the specified interface; availability depends on driver/state/permissions. Use NetworkManager's normal connection workflow instead of manually competing with its control.

**Troubleshooting:** no wireless devices in a VM usually means the compatible USB adapter has not been passed through. Monitor mode requires driver/hardware support. A soft/hard block may require checking rfkill or a physical switch; do not assume a missing interface is fixed by changing its name.

**Cleanup:** these inspection commands require none. For mode changes, follow the dedicated airmon-ng guide's restoration steps using the actual resulting interface name.

**Reference:** [Official documentation](https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html).

[Back to top](#jump-to-a-program)

---

<a id="program-airmon-ng"></a>

## airmon-ng

Manage monitor-mode interfaces for supported Aircrack-ng hardware in an authorized wireless lab.

### Install and verify

```bash
sudo apt update
apt policy aircrack-ng
sudo apt install aircrack-ng
airmon-ng --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** CHANGE and DISCONNECT. Never do this over the only connection you need for remote access. Have a local recovery path.

```bash
iw dev
iw list
sudo airmon-ng check
sudo airmon-ng start wlan0
iw dev
```

Replace wlan0 with your actual adapter. Check supported interface modes first. Read the created monitor interface name; it is not guaranteed to be wlan0mon. `check` reports conflicting processes; it does not automatically kill them.

#### Conflicts

`sudo airmon-ng check kill` stops interfering processes and may disconnect networking. Use it only if the conflict is understood and you can recover locally. A monitor interface does not imply injection support or permission to capture other people's traffic.

#### Restore normal networking

```bash
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
nmcli device status
```

Use the actual monitor name. Reconnect your saved profile if necessary. Restarting NetworkManager can affect other active network connections.

**Troubleshooting:** a VM needs compatible USB wireless hardware passed through. An unsupported driver cannot be fixed by merely using legacy iwconfig commands. Do not change regulatory settings to evade hardware/channel restrictions.

**Cleanup:** stop the monitor interface, restore your original connection and verify managed state. Keep any permitted capture files protected and delete unneeded captures according to the lab's scope.

**Reference:** [Official documentation](https://www.aircrack-ng.org/doku.php?id=airmon-ng).

[Back to top](#jump-to-a-program)

---

<a id="program-wireshark"></a>

## Wireshark

Inspect network packets visually with display filters and protocol detail panes.

### Install and verify

```bash
sudo apt update
apt policy wireshark
sudo apt install wireshark
wireshark --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** CAPTURE/WRITE, potentially sensitive traffic. Limit exercises to your own loopback traffic. Run the GUI as a normal user, not as root.

#### Capture setup

If the installer asks whether non-superusers may capture, choose according to your machine's access policy. On Debian-style packaging, `sudo dpkg-reconfigure wireshark-common` can revisit capture permissions; only authorized users should join the wireshark group. Log out/in after group changes. Reading an existing capture does not require live-capture privilege.

#### Practical local capture

1. Start the local Python HTTP lab.
2. Open Wireshark and select loopback (`lo`) if capture permission is configured.
3. Set capture filter `tcp port 8000` before starting.
4. Make one request with curl, then stop capture promptly.
5. Apply display filter `http` or `tcp.port == 8000` and select a packet to inspect headers and bytes.

Capture filters and display filters use different syntax. A plaintext HTTP body can be visible; encrypted HTTPS payloads normally are not readable merely by capturing them.

#### Save/read

Save as a new pcapng file, then reopen it to verify it contains the intended traffic. Use Follow TCP Stream only on traffic you are authorized to inspect; it can expose complete application exchanges.

**Troubleshooting:** no packets may mean wrong interface/filter, no generated traffic or missing permissions. Do not use sudo on the entire GUI as the routine fix.

**Cleanup:** stop capture, close your test server, and restrict/delete captures containing sensitive data before sharing.

**Reference:** [Official documentation](https://www.wireshark.org/docs/wsug_html_chunked/).

[Back to top](#jump-to-a-program)

---

<a id="program-tcpdump"></a>

## tcpdump

Capture a narrowly filtered packet trace from a specific interface for diagnosis.

### Install and verify

```bash
sudo apt update
apt policy tcpdump
sudo apt install tcpdump
tcpdump --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** CAPTURE and WRITE. Keep the example on loopback and a known test port.

```bash
sudo tcpdump -D
sudo tcpdump -i lo -nn -c 10 'tcp port 8000'
```

`-D` lists interfaces; `-i lo` selects loopback; `-nn` avoids name/port-name lookups; `-c 10` stops after ten matching packets. If not enough packets arrive, Ctrl+C stops the capture. Generate requests in the HTTP lab from another terminal.

#### Save then inspect

```bash
sudo tcpdump -i lo -nn -c 10 -w /tmp/parrot-http.pcap 'tcp port 8000'
tcpdump -nn -r /tmp/parrot-http.pcap
```

Choose a fresh output path; the example can overwrite an existing file of that name. Root-owned captures may require a deliberate ownership/permission adjustment or a privileged read under local policy. Do not make them world-readable just for convenience.

#### Interpret carefully

Packet flags, endpoints and sequence numbers help identify handshake/retransmission behavior. A capture only reflects packets visible at that point, not every event on the network. `-A` prints payload bytes and can expose secrets; avoid broad unfiltered payload dumps.

**Troubleshooting:** wrong interface, filter or privilege often explains an empty capture. Check that traffic is actually generated after capture starts. A checksum-offload warning may not represent on-wire corruption.

**Cleanup:** stop the capture, confirm no background process remains, and remove only your known lab pcap when no longer needed.

**Reference:** [Official documentation](https://www.tcpdump.org/manpages/tcpdump.1.html).

[Back to top](#jump-to-a-program)

---

<a id="program-tshark"></a>

## TShark

Use Wireshark protocol analysis from the terminal, especially for reading saved captures and extracting fields.

### Install and verify

```bash
sudo apt update
apt policy tshark
sudo apt install tshark
tshark --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT for saved files; live capture CAPTURES/WRITES traffic. Use the packet file from your own lab.

```bash
tshark -r /tmp/parrot-http.pcap
tshark -r /tmp/parrot-http.pcap -Y http.request
```

`-r` reads an existing capture. `-Y` is a display filter, evaluated after protocol decoding. HTTP requests may not be decoded if the chosen port/protocol isn't recognized or if traffic is encrypted/incomplete.

#### Extract useful columns

```bash
tshark -r /tmp/parrot-http.pcap -Y http.request -T fields -e frame.number -e ip.src -e http.request.method -e http.request.uri
```

`-T fields` produces selected fields rather than the default packet summary. Multiple values/escaping require care before importing into a spreadsheet; this output is not automatically a robust CSV for every use.

#### Limited live capture

```bash
tshark -i lo -f 'tcp port 8000' -c 10
```

Use configured capture privileges, not a root GUI. `-f` is a capture filter; `-Y` is a display filter. Ctrl+C stops an idle capture if ten matching packets never arrive.

**Troubleshooting:** file-permission errors need proper ownership/access, not weakening all permissions. For nonstandard HTTP ports you can investigate Decode As options documented for your build. Do not equate absence under a filter with absence in the original file.

**Cleanup:** stop live capture and protect/delete lab packet files as appropriate.

**Reference:** [Official documentation](https://www.wireshark.org/docs/man-pages/tshark.html).

[Back to top](#jump-to-a-program)

---

<a id="program-find"></a>

## find

Locate filesystem entries by name, type, size and other metadata. It searches paths, not file contents.

### Install and verify

```bash
sudo apt update
apt policy findutils
sudo apt install findutils
find --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT for these examples. Start with a narrow directory.

```bash
find ~/Documents -type f -name '*.pdf'
find ~/Documents -type f -size +10M -ls
find . -type f -mtime -7 -print
```

Quote globs so find receives the pattern rather than the shell expanding it. `-type f` selects regular files; `+10M` selects larger files; `-mtime -7` uses find's day-based modification-age semantics, not a calendar-week boundary.

#### Safely process files with spaces

```bash
find . -type f -name '*.txt' -exec wc -l -- {} +
```

Find supplies filenames as separate arguments. `+` batches arguments for fewer executions; it must terminate the `-exec` expression. Do not parse `find` output with whitespace splitting.

#### Verify a result

```bash
find . -type f -name 'notes.txt' -ls
```

`-ls` prints metadata; it does not read the document. Use ripgrep for content search.

**Troubleshooting:** permission errors may be normal outside your directories. Narrow the search rather than running all searches as root. `-delete` and `-exec rm` are destructive and unnecessary for locating a file. Preview exact matches before adding any action.

**Cleanup:** these examples do not change files, so there is nothing to undo.

**Reference:** [Official documentation](https://www.gnu.org/software/findutils/manual/).

[Back to top](#jump-to-a-program)

---

<a id="program-less"></a>

## less

Read long files without loading an editor; search and navigate logs interactively.

### Install and verify

```bash
sudo apt update
apt policy less
sudo apt install less
less --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT. Open a text file you own:

```bash
less -N notes.txt
```

`-N` shows line numbers. Press Space/PageDown for the next screen, `b` for the previous screen, `g` for the beginning, `G` for the end and `q` to quit.

#### Find an error

Type `/ERROR` then Enter. Press `n` for the next match and `N` for the previous. Search is generally case-sensitive; `-i` makes searches without uppercase letters case-insensitive.

```bash
less -i app.log
```

#### Follow a growing log

```bash
less +F app.log
```

Follow mode waits for appended data. Press Ctrl+C to return to normal navigation, then `q` to exit. For systemd services, journalctl can select the relevant logs before reading them.

**Troubleshooting:** a missing file is a path problem; check pwd and ls. Long lines can be horizontally navigated with arrow keys when using `-S`. Avoid `-r` on untrusted logs because raw control characters may affect your terminal. `less` is a reader, not a sandbox.

**Cleanup:** quit the viewer. It does not edit the file, although search/history preferences may be stored in your account.

**Reference:** [Official documentation](https://www.greenwoodsoftware.com/less/faq.html).

[Back to top](#jump-to-a-program)

---

<a id="program-sha256sum"></a>

## sha256sum

Calculate SHA-256 digests to compare file bytes or verify against a trusted publisher checksum.

### Install and verify

```bash
sudo apt update
apt policy coreutils
sudo apt install coreutils
sha256sum --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT; creating checksum lists WRITES files. Coreutils is a shared base package; do not remove it after this exercise.

```bash
sha256sum downloaded.iso
```

Compare all hexadecimal characters with the checksum obtained from the publisher over a trusted channel. A checksum copied from the same untrusted source as the file does not establish authenticity.

#### Verify a small file later

```bash
printf 'lab notes\n' > checksum-demo.txt
sha256sum checksum-demo.txt > checksum-demo.sha256
sha256sum -c checksum-demo.sha256
```

Expected: `checksum-demo.txt: OK` before any modifications. Changing even one byte will usually yield FAILED with a nonzero exit status. Keep checksum manifests out of directories where an attacker can silently modify both files if you need security assurance.

#### Compare two copies

```bash
sha256sum original.txt copied.txt
```

Matching digests are strong evidence of matching bytes, not origin or safety. For direct local comparison use `cmp original.txt copied.txt`.

**Troubleshooting:** `-c` resolves manifest filenames relative to the working directory. Run it from the expected folder and check names before assuming corruption. Line-ending conversion can legitimately change a digest.

**Cleanup:** remove only `checksum-demo.txt` and `checksum-demo.sha256` if you created them for this exercise.

**Reference:** [Official documentation](https://www.gnu.org/software/coreutils/manual/).

[Back to top](#jump-to-a-program)

---

<a id="program-jq"></a>

## jq

Read, transform and validate JSON using composable filters.

### Install and verify

```bash
sudo apt update
apt policy jq
sudo apt install jq
jq --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT and WRITE when redirecting output. Start with a known local fixture.

```bash
printf '%s\n' '{"tools":[{"name":"nmap","installed":true},{"name":"ffuf","installed":false}]}' > jq-demo.json
jq . jq-demo.json
jq -r '.tools[].name' jq-demo.json
jq '.tools[] | select(.installed == true)' jq-demo.json
```

`.` pretty-prints, `[]` iterates an array, `-r` emits raw strings, and select keeps matching objects. Quote filters so shell symbols are not interpreted.

#### Check a report and write a new file

```bash
jq -e '.tools | type == "array"' jq-demo.json
jq '[.tools[] | select(.installed == true)]' jq-demo.json > jq-installed.json
```

`-e` returns a useful success/failure exit status for Boolean/null results. Never redirect output to the input file directly; the shell truncates it before jq reads it. Write a new file, inspect it, then deliberately replace if needed.

**Troubleshooting:** parse errors can mean the input is HTML or newline-delimited JSON instead of the expected single document. A null result often means the field/path differs. Read a small fixture and confirm the schema.

**Cleanup:** remove the two demo JSON files if they are no longer needed; never publish reports containing tokens or personal data.

**Reference:** [Official documentation](https://jqlang.org/manual/).

[Back to top](#jump-to-a-program)

---

<a id="program-ripgrep"></a>

## ripgrep / rg

Search file contents quickly with useful line numbers, file filters and explicit hidden-file handling.

### Install and verify

```bash
sudo apt update
apt policy ripgrep
sudo apt install ripgrep
rg --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT; output can reveal secrets. Start inside your project, not the entire filesystem.

```bash
rg -n 'ERROR' logs/
rg -n -i 'openvpn' docs/
rg -n -F '127.0.0.1' .
rg --files -g '*.md'
```

`-n` prints line numbers; `-i` ignores case; `-F` treats the pattern literally instead of as regex. `--files` lists searchable filenames and `-g` constrains a glob.

#### Search hidden configuration deliberately

```bash
rg --hidden -n 'timeout' .github/
```

By default rg respects ignore rules and skips hidden/binary files. `--hidden` includes hidden files but does not automatically disable every ignore rule. Use `--no-ignore` only when needed and keep the path narrow to avoid secrets/vendor output.

#### Interpret exit codes

0 normally means a match, 1 means no match, and 2 indicates an error. A no-match result is not necessarily a failed tool installation. In scripts, distinguish these conditions instead of treating every nonzero exit as a crash.

**Troubleshooting:** a missing result may be case, regex syntax, ignore rules, binary classification or the wrong working directory. Start with a known file and literal pattern. Do not copy sensitive matches into public issue reports.

**Cleanup:** these commands do not edit files; only remove a redirected report if you created one.

**Reference:** [Official documentation](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md).

[Back to top](#jump-to-a-program)

---

<a id="program-tmux"></a>

## tmux

Keep related terminal windows and panes in a session that survives client detachment.

### Install and verify

```bash
sudo apt update
apt policy tmux
sudo apt install tmux
tmux -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** starts processes/sessions; commands inside panes have their own effects.

```bash
tmux new -s parrot-lab
```

Inside tmux the default prefix is Ctrl+B. Release it, then press `%` to split left/right or `"` to split top/bottom. Prefix then an arrow selects a pane. Prefix then `c` creates a window; prefix then `n`/`p` changes windows.

#### Detach and resume

Press Ctrl+B then `d` to detach without stopping the programs. In a normal terminal:

```bash
tmux ls
tmux attach -t parrot-lab
```

Detaching is not a cleanup step: an HTTP server, VPN or scanner can continue running in the session. Check what's running before leaving it unattended.

#### Practical arrangement

Put the local HTTP server in one pane and curl/ss in the other. This makes request and server logs visible together. Avoid displaying real passwords in either pane or screenshot.

#### End deliberately

Stop foreground programs with their own graceful shutdown (often Ctrl+C), then type exit in shells. After confirming nothing important remains, `tmux kill-session -t parrot-lab` terminates that named session and its programs. Do not use kill-server as a routine cleanup because it affects all sessions.

**Troubleshooting:** “no server running” usually means no session exists. A different user/root account has a separate tmux context. If nested sessions confuse prefixes, detach and attach from a normal shell.

**Cleanup:** stop your own tasks gracefully before closing their shells or killing the specifically named disposable session.

**Reference:** [Official documentation](https://github.com/tmux/tmux/wiki/Getting-Started).

[Back to top](#jump-to-a-program)

---

<a id="program-btop"></a>

## btop

Monitor CPU, memory, disks, network rates and processes interactively.

### Install and verify

```bash
sudo apt update
apt policy btop
sudo apt install btop
btop --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT during viewing; process controls can terminate programs. Run as your normal user first.

```bash
btop
```

Use the on-screen help/menu for keys supported by your build. `q` quits. CPU percentages and memory figures need context: cached memory is not automatically wasted, and a momentary spike does not prove a fault.

#### Practical diagnosis

1. Note idle CPU/memory before starting your local lab tool.
2. Run a known benign task and watch its process and resource changes.
3. Compare sustained behavior rather than judging one refresh.
4. Quit btop and inspect application logs if resource use stays unexpectedly high.

A process may use multiple CPU cores, so percentages must be interpreted using the interface's selected normalization. Network rate graphs reflect local interface counters, not application attribution by themselves.

#### Avoid accidental termination

If selecting a process exposes signal/kill controls, read its PID/name and save work before taking action. Prefer stopping your own foreground tool from its original terminal rather than force-killing it in a monitor.

**Troubleshooting:** display issues can reflect unsupported terminal color/Unicode settings, limited window size or permissions for optional sensors. Open the menu/help and choose a compatible theme; installing a new GPU driver is not a generic fix.

**Cleanup:** q exits monitoring; it does not stop the processes you were observing. Close any lab process separately.

**Reference:** [Official documentation](https://github.com/aristocratos/btop).

[Back to top](#jump-to-a-program)

---

<a id="program-openssl"></a>

## OpenSSL

Inspect certificates and create local test cryptographic material without assuming that an arbitrary certificate is trusted.

### Install and verify

```bash
sudo apt update
apt policy openssl
sudo apt install openssl
openssl version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT for reads; key/certificate creation WRITES sensitive files.

```bash
openssl x509 -in certificate.pem -noout -subject -issuer -dates -fingerprint -sha256
```

Use an actual PEM certificate. These fields describe identity claims/validity dates and a fingerprint, not a complete trust decision. A certificate can be well-formed and still be untrusted or for the wrong host.

#### Create a loopback-only test certificate

```bash
umask 077
openssl req -x509 -newkey rsa:2048 -sha256 -days 1 -keyout lab-key.pem -out lab-cert.pem -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost,IP:127.0.0.1'
```

The command prompts for a private-key passphrase. Keep it private; a self-signed certificate is not automatically trusted by browsers. `umask 077` restricts new-file permissions in this shell; it remains in effect afterward. Use a separate test terminal if you do not want to change the original shell's mask.

#### Inspect your generated certificate

```bash
openssl x509 -in lab-cert.pem -noout -text
openssl verify -CAfile lab-cert.pem lab-cert.pem
```

The verification trusts that file explicitly for this command; it does not install a system CA or establish external identity.

**Troubleshooting:** PEM parse failures may mean wrong file type or an HTML error page. TLS client failures also depend on chain, hostname and system time; do not disable validation globally.

**Cleanup:** remove only the lab certificate/private key after ensuring no test server needs them. Never commit private keys.

**Reference:** [Official documentation](https://docs.openssl.org/master/man1/openssl/).

[Back to top](#jump-to-a-program)

---

<a id="program-zap"></a>

## OWASP ZAP

Inspect HTTP traffic and assess your own web application with a scoped proxy workflow. Passive analysis and active scans have different effects.

### Install and verify

Check whether your Parrot repositories provide a supported build:

```bash
apt policy zaproxy
```

If a candidate exists, install with `sudo apt install zaproxy` and launch `zaproxy`. Otherwise obtain the appropriate Linux package/installer from the [official ZAP download page](https://www.zaproxy.org/download/), verify its origin and follow that format's current Java/runtime instructions. Do not add another distribution's repository or assume every Linux installer bundles Java. Use the app's About dialog for its exact version.

### Use it in practice

**Impact:** NETWORK and WRITE; active scans can change application state. Use your local disposable app.

#### Launch and browse

Launch ZAP from the installed desktop shortcut or its documented startup script. Choose a temporary/non-persisted session if appropriate for a first exercise. Use Manual Explore / the browser-launch workflow for your version rather than guessing proxy/CA settings.

1. Browse the local HTTP lab and request hello.txt and missing.txt.
2. Inspect the Sites tree and History to compare 200/404 responses.
3. Review passive alerts as observations requiring context; missing headers in a toy file server do not prove a broadly exploitable defect.
4. Add your own app to a named context/scope before any active testing.

#### First active test

Use only an intentionally disposable application/database with explicit permission. Review scope, authentication/session handling and scan policy before launching an active scan. Do not start with an unscoped “attack everything” action or a third-party production site.

#### Evidence

Save a report/session only if needed, knowing it may include requests, cookies and sensitive responses. Redact before sharing. A passing scan does not prove absence of vulnerabilities; automated coverage depends on explored routes and app state.

**Troubleshooting:** an unreachable browser may be waiting for proxy setup or an HTTPS CA configuration. Java/build requirements vary with distribution format; read the chosen official installer requirements.

**Cleanup:** stop scans, close proxy listeners/test browser and remove any external browser proxy/CA changes. Restore the disposable app/database as necessary.

**Reference:** [Official documentation](https://www.zaproxy.org/getting-started/).

[Back to top](#jump-to-a-program)

---

<a id="program-shellcheck"></a>

## ShellCheck

Analyze shell scripts for common quoting, portability and logic mistakes without executing them.

### Install and verify

```bash
sudo apt update
apt policy shellcheck
sudo apt install shellcheck
shellcheck --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT. ShellCheck complements Bash syntax checking; neither proves that a script is safe to execute.

#### Create a deliberately flawed fixture

```bash
printf '%s\n' '#!/bin/bash' 'name="lab notes"' 'printf "%s\n" $name' > shellcheck-demo.sh
shellcheck shellcheck-demo.sh
bash -n shellcheck-demo.sh
```

ShellCheck should report unquoted expansion in this example. Bash -n can accept it because it is syntactically valid. Do not run the flawed script merely to check its syntax.

#### Fix quoting and recheck

```bash
printf '%s\n' '#!/bin/bash' 'name="lab notes"' 'printf "%s\n" "$name"' > shellcheck-demo.sh
shellcheck shellcheck-demo.sh
```

Quoting preserves a single argument instead of unintended splitting/globbing. A clean report means no issue was found by that analysis, not complete correctness or harmless behavior.

#### Work on a real script

Set the correct shebang or `shellcheck -s bash script.sh` when appropriate. Read warning explanations before suppression. Use a narrow documented suppression only when you understand the invariant; do not disable all warnings to get a green check.

**Troubleshooting:** an unsupported shell/extension needs the correct parser assumption. External sourced files may need explicitly scoped analysis; avoid following untrusted source paths indiscriminately.

**Cleanup:** remove only shellcheck-demo.sh if created for the exercise.

**Reference:** [Official documentation](https://www.shellcheck.net/).

[Back to top](#jump-to-a-program)

---

<a id="program-systemctl"></a>

## systemctl

Inspect and control systemd units. Starting now and enabling at boot are separate operations.

### Install and verify

```bash
sudo apt update
apt policy systemd
sudo apt install systemd
systemctl --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT for status; CHANGE/DISCONNECT for service control. systemd is normally part of Parrot; do not remove it as lab cleanup.

```bash
systemctl status NetworkManager --no-pager
systemctl is-active NetworkManager
systemctl is-enabled NetworkManager
systemctl --failed
```

Status includes recent logs. is-active checks current runtime state; is-enabled checks boot/unit wiring, not current health. Some units are static and are not enabled like ordinary services.

#### Optional PostgreSQL lab service

```bash
sudo systemctl start postgresql
systemctl status postgresql --no-pager
```

Use only if installed and needed. Start does not automatically configure every application that will use the service. Debian's meta-service may delegate to versioned clusters.

#### Deliberate control

`stop` halts a service now; `restart` stops/starts it and interrupts users. `enable` changes automatic activation; `disable` does not necessarily stop a running service. Do not restart networking over your sole remote connection.

**Troubleshooting:** “unit not found” means wrong unit name or missing package; list units/unit-files and consult the package. “System has not been booted with systemd” can be a container or different init environment. `daemon-reload` reloads unit definitions after edits; it is not an application-config reload.

**Cleanup:** stop only services you started for the lab and only if nothing else needs them. Restore any deliberate boot-setting changes to the recorded baseline.

**Reference:** [Official documentation](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html).

[Back to top](#jump-to-a-program)

---

<a id="program-journalctl"></a>

## journalctl

Read systemd journal entries by service, boot and time to diagnose the exact failure.

### Install and verify

```bash
sudo apt update
apt policy systemd
sudo apt install systemd
journalctl --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

### Use it in practice

**Impact:** INSPECT; redirected logs WRITE files and can reveal sensitive data. Start with a narrow selection.

```bash
journalctl -u NetworkManager -b -n 50 --no-pager
journalctl -b -p warning --no-pager
journalctl --since '30 minutes ago' --no-pager
```

`-u` selects a unit, `-b` the current boot, `-n` the most recent count, and `--no-pager` prints directly. Priority warning includes warning and more severe entries. A service name must match the actual unit.

#### Follow a specific lab service

```bash
journalctl -u postgresql -f
```

`-f` follows new entries; Ctrl+C ends viewing, not the service. Versioned PostgreSQL cluster units can have their own logs. Compare timestamps with the exact moment of your failing operation.

#### Previous boot

```bash
journalctl --list-boots
journalctl -b -1 -n 50 --no-pager
```

A previous boot is available only if the journal retained it. Missing historical logs do not prove no event occurred.

**Troubleshooting:** limited access may require a legitimate journal-reading group or sudo under your machine policy. An empty query may use the wrong unit/time range. Avoid clearing/vacuuming logs as a diagnostic step; it removes evidence and can affect retention policy.

**Cleanup:** Ctrl+C or q exits the viewer. Redact usernames, network identifiers and tokens before posting excerpts.

**Reference:** [Official documentation](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html).

[Back to top](#jump-to-a-program)

---

## Local viewing and checks

Download/clone this repository, then open index.html directly for the styled version. It does not fetch external assets. Clipboard permissions vary for local files; when copying is unavailable it selects the command for manual copying.

To serve the styled page locally, run this from the repository folder and visit http://127.0.0.1:8000:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Stop with Ctrl+C. This shares the repository directory on loopback; do not start it from a folder containing private files.

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

Checks validate basic Markdown/link structure and shell syntax without executing the security examples. [Compatibility](COMPATIBILITY.md), [validation](VALIDATION.md), and [contribution notes](CONTRIBUTING.md) record the limits. All essential tool instructions are above; the docs folder retains source guides and supplementary notes.
