# iw

[All programs](README.md) · [Repository home](../../README.md)

Inspect modern Linux wireless interfaces, driver capabilities and connection state.

## Install and verify

```bash
sudo apt update
apt policy iw
sudo apt install iw
iw --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT here; a scan sends/receives wireless traffic and can affect connectivity. Requires actual supported wireless hardware, not a VM's virtual Ethernet adapter.

```bash
iw dev
iw list
iw reg get
```

`iw dev` shows current wireless devices/interfaces. `iw list` shows PHY capabilities including supported modes. Regulatory information is not permission to transmit on every listed channel; obey the actual local rules.

### Inspect your connection

```bash
iw dev wlan0 link
```

Replace wlan0 with a name from iw dev. It reports association details where supported. “Not connected” is a state, not necessarily a driver failure.

### Scan only when needed

```bash
sudo iw dev wlan0 scan
```

This asks for a scan on the specified interface; availability depends on driver/state/permissions. Use NetworkManager's normal connection workflow instead of manually competing with its control.

**Troubleshooting:** no wireless devices in a VM usually means the compatible USB adapter has not been passed through. Monitor mode requires driver/hardware support. A soft/hard block may require checking rfkill or a physical switch; do not assume a missing interface is fixed by changing its name.

**Cleanup:** these inspection commands require none. For mode changes, follow the dedicated airmon-ng guide's restoration steps using the actual resulting interface name.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run iw` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
