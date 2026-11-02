# GNOME Tweaks and extensions

[All programs](README.md) · [Repository home](../../README.md)

Adjust GNOME desktop preferences beyond the standard Settings app. GNOME extensions require GNOME Shell; they do not apply to MATE/KDE.

## Install and verify

```bash
sudo apt update
apt policy gnome-tweaks
sudo apt install gnome-tweaks
gnome-tweaks --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** CHANGE to your desktop preferences. Check your environment before installing:

```bash
printf '%s\n' "$XDG_CURRENT_DESKTOP"
gnome-tweaks
```

If you are not running GNOME, use your desktop’s settings instead. Installing Tweaks does not switch you to GNOME.

### Practical workflow

1. Open Tweaks as your normal user, never with sudo.
2. Record the current setting you intend to change.
3. Change a single option such as the interface font or window-titlebar behavior.
4. Check usability and restore the recorded setting if the result is undesirable.

Available panels vary by GNOME release. Extension management may be in the separate Extensions app. Use the official GNOME extensions site, check shell-version compatibility and review each extension's permissions/source before enabling it.

**Troubleshooting:** an empty or missing option may be a desktop/version mismatch. Disable a newly added extension if the shell becomes unstable. Do not install Ubuntu desktop meta-packages to “fix” Parrot. Logout/login can apply some desktop changes; save work first.

**Cleanup:** disable/remove the specific test extension and restore changed settings. Removing Tweaks does not necessarily undo the preferences you changed.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run gnome-tweaks` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://extensions.gnome.org/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
