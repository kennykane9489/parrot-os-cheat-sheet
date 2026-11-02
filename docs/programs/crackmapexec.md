# CrackMapExec migration

[All programs](README.md) · [Repository home](../../README.md)

Understand older CME notes and move new workflows to NetExec without assuming command-line flags are identical.

## Install and verify

For new Parrot installations, use the [NetExec installation guide](netexec.md). This migration page intentionally does not recommend a fresh legacy CME installation. Query an existing command with `command -v crackmapexec` before deciding whether to retain it.

## Use it in practice

**Impact:** INSPECT for migration preparation; legacy commands can perform NETWORK actions.

### Identify what is installed

```bash
command -v crackmapexec
command -v nxc
apt policy crackmapexec netexec
```

A missing command simply means it is not on PATH. Do not install an unmaintained fork merely to reproduce an old cheat-sheet line.

### Migration example

Old notes often contain `crackmapexec smb HOST`. For a new setup, install NetExec using its dedicated guide and start with:

```bash
nxc smb --help
nxc smb 192.168.56.20
```

For authenticated share or policy enumeration, use a designated lab account and validate current flags. Re-check output format, workspace behavior and credential handling before converting scripts. A filename change alone is not a tested migration.

**Troubleshooting:** both tools on PATH can lead to testing one build while reading another's documentation. Record exact executables and versions. Preserve old reports before removing a legacy installation and avoid automatic conversion of post-exploitation commands.

**Cleanup:** retire the old tool only through the manager that installed it after you no longer need its data. The new workflow is documented in [NetExec](netexec.md).

## Updates and removal

Update through the same manager or upstream method used for installation. Avoid mixing distribution and source installations of the same executable. Follow the cleanup steps above before removing any files.

## Reference and compatibility

[Upstream documentation](https://github.com/Pennyw0rth/NetExec). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
