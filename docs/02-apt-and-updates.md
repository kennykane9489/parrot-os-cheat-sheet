# Updates and APT

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** CHANGE and possible REMOVE. Review package proposals before confirming.

APT resolves package dependencies, downloads packages from configured repositories and coordinates installation through dpkg. `apt` is an interactive interface sharing functionality with `apt-get` and `apt-cache`, not simply a subset. Prefer `apt-get`/`apt-cache` for scripts with stable interfaces.

### Recommended Parrot system update

Back up important files or take a VM snapshot first. Parrot recommends its rolling-update wrapper:

```bash
sudo apt update
sudo parrot-upgrade
```

Review proposed removals. Reboot after kernel updates when convenient to load the new kernel. Do not add Kali or Ubuntu repositories to fix a missing Parrot package. If `parrot-upgrade` is missing, check the official instructions for your installed release before a distribution upgrade.

| Command | Meaning |
|---|---|
| `sudo apt update` | Refresh available-package indexes; installs no updates. |
| `apt list --upgradable` | Show available package upgrades. |
| `sudo apt upgrade` | Upgrade packages; may add dependencies, but does not remove installed packages. |
| `sudo apt full-upgrade` | Allow dependency changes including removals; inspect the proposal. |
| `sudo apt install PACKAGE` | Install a named package and dependencies. |
| `sudo apt remove PACKAGE` | Remove the package, generally retaining system configuration. |
| `sudo apt purge PACKAGE` | Also remove package-managed configuration; home-directory settings can remain. |
| `sudo apt autoremove --dry-run` | Preview removal of automatically installed dependencies no longer required. |
| `sudo apt autoremove` | Perform that removal after reviewing the list. |
| `apt search KEYWORD` | Search package names/descriptions. |
| `apt show PACKAGE` | Read package details. |
| `apt list --installed` | List installed packages. |
| `sudo apt clean` | Clear cached downloaded package archives. |
| `sudo apt autoclean` | Clear cached archives that can no longer be downloaded. |
| `sudo apt edit-sources` | Edit repository configuration; avoid changing repositories casually. |
| `apt policy PACKAGE` | Check package version and repository origin. |

Do not chain `upgrade`, `full-upgrade` and automatic removals with `-y` as routine maintenance. The upgrade steps overlap, and automatic approval hides important review points.

### Broken/interrupted installs

Wait for any other package manager to finish. Do not delete lock files as a first fix.

```bash
sudo dpkg --configure -a     # Complete interrupted package configuration
sudo apt --fix-broken install  # Resolve broken dependencies; review changes
```

These commands address package-state problems, not arbitrary network or repository errors.

### Install a downloaded .deb

Only use trusted packages built for your distribution and architecture.

```bash
cd ~/Downloads
sudo apt install ./file.deb
```

The `./` identifies a local file. APT can resolve dependencies from your repositories. `sudo dpkg -i ./file.deb` installs a local package but does not fetch missing dependencies itself. A `.deb` is a package, not a “dpkg.”
