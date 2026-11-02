# Read this first

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** INSPECT; examples also create local working folders.

- Run commands one at a time. Replace example addresses, usernames, filenames and interfaces before running them.
- `$` and `#` prompt markers are not part of a command. Code blocks omit them.
- `sudo` elevates privileges. Read-only queries usually do not need it.
- `&&` runs the next command only if the previous command succeeds.
- `>` overwrites a file; `>>` appends. Quote paths containing spaces and URLs containing `&` or `?`.
- Stop foreground commands with Ctrl+C. Never paste a whole reference as a shell script.
- Check instructions with `man PROGRAM`, `PROGRAM --help`, or a tool's own help command.

```bash
cat /etc/os-release          # Distribution/release
uname -r                    # Running kernel
dpkg --print-architecture   # Package architecture
printf '%s\n' "$XDG_CURRENT_DESKTOP"
command -v nmap             # Locate installed executable
apt policy nmap             # Installed/candidate package versions
```
