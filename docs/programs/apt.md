# APT and parrot-upgrade

[All programs](README.md) · [Repository home](../../README.md)

Manage Debian-format packages and dependencies. Use `apt` interactively; use `apt-get`/`apt-cache` for stable scripting interfaces.

## Install and verify

```bash
sudo apt update
apt policy apt
sudo apt install apt
apt --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK, CHANGE; upgrades may REMOVE dependencies. APT is already part of Parrot. Do not reinstall it merely to verify the command.

### Update the system

```bash
sudo apt update
apt list --upgradable
sudo parrot-upgrade
```

`update` refreshes indexes without upgrading installed software. Parrot’s wrapper handles rolling system upgrades. Review removals; reboot when needed to load a new kernel.

### Find and install one tool

```bash
apt search ripgrep
apt show ripgrep
apt policy ripgrep
sudo apt install ripgrep
```

Search finds packages; show describes them; policy identifies candidates/origins. Install fetches dependencies. A specific package can also be upgraded by `sudo apt install --only-upgrade ripgrep`.

### Preview cleanup

```bash
sudo apt autoremove --dry-run
sudo apt clean
```

Autoremove's preview lists unused automatic dependencies. Clean deletes downloaded archives, not installed tools. Remove keeps many settings; purge also deletes package-managed configuration, not necessarily files in your home.

**Troubleshooting:** wait for a running updater rather than deleting lock files. DNS errors require a working resolver; missing candidates require checking indexes/release/repositories. After an interrupted transaction, use `sudo dpkg --configure -a` only after other package processes finish. Do not run an unattended chain of upgrade/removal commands.

**Cleanup:** package operations create no disposable lab folder. Use clean for cached downloads only when needed; review autoremove before performing it.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run apt` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://parrotsec.org/docs/configuration/parrot-software-management/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
