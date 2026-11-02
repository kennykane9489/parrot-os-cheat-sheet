# systemctl

[All programs](README.md) · [Repository home](../../README.md)

Inspect and control systemd units. Starting now and enabling at boot are separate operations.

## Install and verify

```bash
sudo apt update
apt policy systemd
sudo apt install systemd
systemctl --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT for status; CHANGE/DISCONNECT for service control. systemd is normally part of Parrot; do not remove it as lab cleanup.

```bash
systemctl status NetworkManager --no-pager
systemctl is-active NetworkManager
systemctl is-enabled NetworkManager
systemctl --failed
```

Status includes recent logs. is-active checks current runtime state; is-enabled checks boot/unit wiring, not current health. Some units are static and are not enabled like ordinary services.

### Optional PostgreSQL lab service

```bash
sudo systemctl start postgresql
systemctl status postgresql --no-pager
```

Use only if installed and needed. Start does not automatically configure every application that will use the service. Debian's meta-service may delegate to versioned clusters.

### Deliberate control

`stop` halts a service now; `restart` stops/starts it and interrupts users. `enable` changes automatic activation; `disable` does not necessarily stop a running service. Do not restart networking over your sole remote connection.

**Troubleshooting:** “unit not found” means wrong unit name or missing package; list units/unit-files and consult the package. “System has not been booted with systemd” can be a container or different init environment. `daemon-reload` reloads unit definitions after edits; it is not an application-config reload.

**Cleanup:** stop only services you started for the lab and only if nothing else needs them. Restore any deliberate boot-setting changes to the recorded baseline.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run systemd` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
