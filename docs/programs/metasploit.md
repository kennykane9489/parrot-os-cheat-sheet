# Metasploit Framework

[All programs](README.md) · [Repository home](../../README.md)

Organize authorized testing modules and evidence in workspaces. Framework is distinct from licensed Metasploit Pro.

## Install and verify

```bash
sudo apt update
apt policy metasploit-framework
sudo apt install metasploit-framework
msfconsole --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** CHANGE for database setup, NETWORK for module execution. Work against a disposable lab.

```bash
sudo systemctl start postgresql
command -v msfdb
sudo msfdb init
msfconsole
```

Run initialization only if this package supplies msfdb and its instructions call for it. Missing helpers require the package/upstream database setup, not guessed commands. Database support is optional for some Framework tasks.

### Inside msfconsole

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

### Session and option terminology

RHOSTS is the module's target selection; RPORT is its service port. LHOST/LPORT describe listener/callback settings for payloads that use them. A database workspace organizes evidence; it does not isolate network traffic.

**Troubleshooting:** disconnected database status requires checking the exact install's DB configuration. Empty hosts/services can reflect no DB connection or no recorded scan. Framework does not imply a Pro web interface on port 3790.

**Cleanup:** use `jobs` and `sessions -l` to identify your active tasks, stop only your lab tasks, and `exit` the console. Stop the optional database only if nothing else needs it.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run metasploit-framework` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://docs.metasploit.com/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
