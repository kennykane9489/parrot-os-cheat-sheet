# Wireless monitor mode

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** DISCONNECT and CHANGE; monitor-mode operations can interrupt Wi-Fi.

`iw` reports modern wireless capabilities; Aircrack-ng's `airmon-ng` manages compatible monitor interfaces. Monitor mode requires supporting hardware/driver, not merely an installed program. A VM commonly needs a compatible USB adapter passed through; its virtual Ethernet adapter cannot become Wi-Fi monitor mode.

```bash
iw dev
iw list                     # Look for monitor under supported interface modes
sudo airmon-ng check        # Inspect interfering processes first
sudo airmon-ng start wlan0  # Replace wlan0 with the real interface
iw dev                     # Read the resulting interface name/type
```

Starting monitor mode may disrupt connectivity. `airmon-ng check kill` stops conflicting processes and can disconnect networking; use only when needed with a recovery path. Restore using the actual monitor interface:

```bash
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
nmcli device status
```

`wlan0mon` is an example, not guaranteed. Legacy `iwconfig` commands can fail on modern drivers. Passive captures can include other people's traffic; keep captures scoped to the lab. This reference does not require deauthentication or packet injection.
