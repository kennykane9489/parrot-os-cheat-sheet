# nmcli / NetworkManager

[All programs](README.md) · [Repository home](../../README.md)

Inspect and manage connections controlled by NetworkManager. Distinguish a device from its saved connection profile.

## Install and verify

```bash
sudo apt update
apt policy network-manager
sudo apt install network-manager
nmcli --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT initially; activation/deactivation CHANGES connectivity. NetworkManager is often installed already. Installing/restarting it during a remote session can disrupt access.

```bash
nmcli device status
nmcli connection show --active
nmcli connection show
```

A profile can exist while inactive. Device state and profile names help identify what is actually connected.

### Connect to your own Wi-Fi

```bash
nmcli device wifi list
nmcli --ask device wifi connect 'YOUR_SSID'
```

Replace the SSID; `--ask` prompts for secrets instead of putting a password in history. Listing may initiate a wireless scan. Enterprise authentication can need a more detailed profile; use the appropriate GUI or documented enterprise settings.

### Reactivate a saved profile

```bash
nmcli connection up 'YOUR_PROFILE_NAME'
```

Use the exact name from your output. This can interrupt a current connection. To deliberately disconnect a specific device use `nmcli device disconnect DEVICE` only with a recovery path.

**Troubleshooting:** “NetworkManager is not running” requires checking service status; “unmanaged” can mean another service/config owns the device. Do not start competing managers. After wireless monitor mode, restore managed mode before reconnecting.

**Cleanup:** reconnect your original profile if you changed it. Do not delete profiles unless you intend to lose their saved settings.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run network-manager` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://networkmanager.dev/docs/api/latest/nmcli.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
