# journalctl

[All programs](README.md) · [Repository home](../../README.md)

Read systemd journal entries by service, boot and time to diagnose the exact failure.

## Install and verify

```bash
sudo apt update
apt policy systemd
sudo apt install systemd
journalctl --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT; redirected logs WRITE files and can reveal sensitive data. Start with a narrow selection.

```bash
journalctl -u NetworkManager -b -n 50 --no-pager
journalctl -b -p warning --no-pager
journalctl --since '30 minutes ago' --no-pager
```

`-u` selects a unit, `-b` the current boot, `-n` the most recent count, and `--no-pager` prints directly. Priority warning includes warning and more severe entries. A service name must match the actual unit.

### Follow a specific lab service

```bash
journalctl -u postgresql -f
```

`-f` follows new entries; Ctrl+C ends viewing, not the service. Versioned PostgreSQL cluster units can have their own logs. Compare timestamps with the exact moment of your failing operation.

### Previous boot

```bash
journalctl --list-boots
journalctl -b -1 -n 50 --no-pager
```

A previous boot is available only if the journal retained it. Missing historical logs do not prove no event occurred.

**Troubleshooting:** limited access may require a legitimate journal-reading group or sudo under your machine policy. An empty query may use the wrong unit/time range. Avoid clearing/vacuuming logs as a diagnostic step; it removes evidence and can affect retention policy.

**Cleanup:** Ctrl+C or q exits the viewer. Redact usernames, network identifiers and tokens before posting excerpts.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run systemd` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
