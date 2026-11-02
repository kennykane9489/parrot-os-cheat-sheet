# Metasploit Framework — module-based lab testing

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** CHANGE and NETWORK; service/database setup changes the local machine.

Framework is distinct from paid Metasploit Pro; a Framework install does not imply a web service at port 3790. Check `apt policy metasploit-framework` before installation.

```bash
sudo systemctl start postgresql
command -v msfdb
# If supplied by your package and documented for this installation:
sudo msfdb init
msfconsole
```

Run `msfdb init` for initial setup, not every launch. Database setup depends on packaging; if the helper is absent, use the package/upstream instructions. Inside msfconsole:

```text
db_status
workspace -a training
search type:auxiliary name:http_version
use auxiliary/scanner/http/http_version
info
show options
set RHOSTS 192.168.56.20
set RPORT 8000
run
back
sessions
help
exit
```

`db_status` is a console command, not a Linux shell command. Use `info` and `show options` for every module; `check` exists only for modules supporting it and may still send active probes.

### Payload and session terminology

- `RHOSTS`: target host(s), where the chosen module provides that option.
- `RPORT`: target service port.
- `LHOST`: callback/listener address for applicable reverse payloads; must be reachable from the lab target.
- `LPORT`: callback/listener port. A reverse handler generally does not need `RHOST`.
- Reverse connection: target connects to listener. Bind connection: operator connects to a listening target. Firewall/NAT changes reachability.

```bash
msfvenom --help
msfvenom -l payloads
msfvenom -l formats
```

The old bare `msfvenom -l` listing is incomplete. Payload names and architectures vary; select from the installed list. Encoding is not encryption and does not guarantee antivirus evasion. `pbcopy`/`pbpaste` are macOS utilities, not standard Parrot commands. Running a file alone does not guarantee a session: matching listener, routing and compatible payload all matter. Distribution of disguised backdoors is not part of this reference.

### Meterpreter — existing authorized lab session reference

Commands depend on target platform, loaded extensions and session type. Run `help` in the actual session instead of relying on a frozen full command dump.

| Command | Purpose |
|---|---|
| `help` | Available commands for this session. |
| `sysinfo` | Target OS/system information. |
| `getuid` | Session's current user identity. |
| `pwd`, `ls`, `cd` | Remote filesystem navigation. |
| `lpwd`, `lls`, `lcd` | Local filesystem navigation. |
| `ps` | List remote processes. |
| `ipconfig` | Show network information when supported. |
| `background` | Return to console while keeping the session. |
| `exit` | End the current session. |

In msfconsole, use `sessions -l` and `sessions -i ID` to list or interact. Credential dumping, keylogging, webcam access, log clearing and timestamp alteration are not routine inventory steps and are omitted from the quick workflow.
