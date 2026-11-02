# NetExec

[All programs](README.md) · [Repository home](../../README.md)

Assess protocol configuration and permitted account access in Windows/AD labs. The primary CLI is commonly nxc; verify installed entry points.

## Install and verify

```bash
sudo apt update
apt policy netexec
sudo apt install netexec
nxc --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK; authenticated enumeration can produce audit events. APT availability depends on Parrot release.

### Isolated upstream fallback

If no Parrot package candidate exists, use a user-level pipx install instead of mixing distributions:

```bash
sudo apt install pipx git
pipx ensurepath
pipx install git+https://github.com/Pennyw0rth/NetExec
```

Open a new terminal. Read the upstream supported Python/build requirements if dependencies fail; some builds require Python headers or Rust. Record the source commit/version.

### Discover one lab SMB endpoint

```bash
nxc smb 192.168.56.20
nxc smb --help
```

This reports available SMB/OS/domain clues where the server permits them; unauthenticated metadata is not proof of compromise.

### Inspect shares with a designated account

```bash
read -r -s -p 'Disposable lab password: ' lab_password
printf '\n'
nxc smb 192.168.56.20 -u labuser -p "$lab_password" --shares
unset lab_password
```

Use only the credentials supplied for the lab. Passwords expanded on the command line can be visible to local process observers even if not in shell history. `--pass-pol` queries policy where supported/authorized. Do not supply random passwords as a substitute for guest access.

**Troubleshooting:** domain names, target resolution, time synchronization and SMB policy affect authentication. An “admin” marker is a tool interpretation to validate, not a guarantee that every action succeeds. No “stealth” claim guarantees evasion.

**Cleanup:** close the tool and protect its workspace/database. Update a pipx install with pipx, and an APT install with APT; do not maintain both unknowingly.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run netexec` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.netexec.wiki/getting-started/installation/installation-on-unix). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
