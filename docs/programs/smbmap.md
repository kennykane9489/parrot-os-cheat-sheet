# SMBMap

[All programs](README.md) · [Repository home](../../README.md)

Summarize SMB shares and effective permissions for an authorized account.

## Install and verify

```bash
sudo apt update
apt policy smbmap
sudo apt install smbmap
smbmap --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK; permission checks may WRITE test files unless disabled. Read help for your installed release before assessing a production share.

```bash
smbmap -H 192.168.56.20 --no-write-check
```

`-H` selects one host. Current upstream supports `--no-write-check`; confirm it in local help. This example attempts unauthenticated access and may show no shares. It does not bypass permissions.

### Authenticated lab inventory

```bash
read -r -s -p 'Disposable lab password: ' lab_password
printf '\n'
smbmap -H 192.168.56.20 -u labuser -p "$lab_password" --no-write-check
unset lab_password
```

The shell prompt avoids storing the literal password in history, but the expanded password can still appear in process arguments. Use only disposable lab credentials for this example, and prefer a supported secure credential method in real assessments. Review READ/WRITE claims in context; skipping write checks limits what can be confirmed.

### Validate a result

Connect to a reported share with smbclient and list a known harmless folder. Share access and nested file permissions may differ.

**Troubleshooting:** blank output can be failed/guest authentication, filtering or no permitted shares. Domain settings and SMB support matter. Do not enable arbitrary execution or automatic downloads merely to list permissions.

**Cleanup:** stop the tool and protect results. If you intentionally enabled write checks, verify any test artifacts were removed according to the installed version's behavior.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run smbmap` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/ShawnDEvans/smbmap). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
