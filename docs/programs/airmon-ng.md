# airmon-ng

[All programs](README.md) · [Repository home](../../README.md)

Manage monitor-mode interfaces for supported Aircrack-ng hardware in an authorized wireless lab.

## Install and verify

```bash
sudo apt update
apt policy aircrack-ng
sudo apt install aircrack-ng
airmon-ng --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** CHANGE and DISCONNECT. Never do this over the only connection you need for remote access. Have a local recovery path.

```bash
iw dev
iw list
sudo airmon-ng check
sudo airmon-ng start wlan0
iw dev
```

Replace wlan0 with your actual adapter. Check supported interface modes first. Read the created monitor interface name; it is not guaranteed to be wlan0mon. `check` reports conflicting processes; it does not automatically kill them.

### Conflicts

`sudo airmon-ng check kill` stops interfering processes and may disconnect networking. Use it only if the conflict is understood and you can recover locally. A monitor interface does not imply injection support or permission to capture other people's traffic.

### Restore normal networking

```bash
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
nmcli device status
```

Use the actual monitor name. Reconnect your saved profile if necessary. Restarting NetworkManager can affect other active network connections.

**Troubleshooting:** a VM needs compatible USB wireless hardware passed through. An unsupported driver cannot be fixed by merely using legacy iwconfig commands. Do not change regulatory settings to evade hardware/channel restrictions.

**Cleanup:** stop the monitor interface, restore your original connection and verify managed state. Keep any permitted capture files protected and delete unneeded captures according to the lab's scope.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run aircrack-ng` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.aircrack-ng.org/doku.php?id=airmon-ng). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
