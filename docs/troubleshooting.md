# Troubleshooting

[Home](../README.md) · [Output examples](example-output.md)

Work from the exact error. Stop after a check identifies the cause; avoid applying every fix.

| Symptom | Possible cause | Check | Next step |
|---|---|---|---|
| APT cannot resolve repository hostname | DNS or network issue | `ip route`; `getent hosts deb.parrot.sh` | Fix the active connection/resolver; retry `sudo apt update`. Do not replace repositories randomly. |
| APT lock is held | Another package transaction | `ps -ef` and running updater windows | Let the other transaction finish. Do not delete locks or kill a healthy updater. |
| dpkg says interrupted | Incomplete configuration | Read the exact package-manager error | Once no package manager is running, use `sudo dpkg --configure -a`; then review `sudo apt --fix-broken install` if required. |
| No installation candidate | Package name/repository/release mismatch | `apt policy PACKAGE`; `cat /etc/os-release` | Refresh indexes and check Parrot/upstream instructions. Do not add Kali or Ubuntu repositories. |
| Externally managed Python environment | Attempted system-level pip install | Check whether a virtual environment is active | Use a project venv or pipx. See [Python](03-setup-and-python.md). |
| VPN says connected, lab unreachable | Wrong lab region, stopped target, missing/overlapping route | `ip route get 10.10.10.10`; provider target status | Verify target IP and tunnel route; close duplicate tunnels and use the correct provider config. |
| Ping fails but web app works | ICMP filtered | Test the known web-service URL | Treat ping as one signal; do not change VPN settings based only on ping. |
| Local HTTP connection refused | No listener or wrong address/port | `ss -tuln`; server terminal | Start the lab server on the intended bind address/port. |
| HTTP port already in use | Another listener occupies port | `sudo ss -tulpn` | Stop only the process you recognize, or choose a different free port and update both commands. |
| TLS certificate error | Wrong name, clock, CA trust or deliberate lab certificate | `date -Is`; inspect hostname/certificate | Correct trust/name/time. Bypassing verification is not a general fix. |
| Gobuster finds every path | Wildcard/custom error responses | Request a random nonexistent path with curl | Compare status, length and content; configure supported filters and manually verify findings. |
| SMB authentication fails | Wrong account/domain, policy or permissions | `smbclient -L HOST -U USER`; read server-side logs if yours | Verify credentials and access with the administrator; do not force SMB1. |
| No wireless interface in a VM | Only virtual Ethernet exposed | `ip -br link`; `iw dev` | Pass through a compatible USB Wi-Fi adapter; check driver support. |
| Wi-Fi stops after monitor mode | Monitor interface or stopped NetworkManager | `iw dev`; `nmcli device status` | Stop the actual monitor interface, then restart NetworkManager. This interrupts connections. |
| Permission denied | File ownership, service privilege or access policy | `ls -l PATH`; `id` | Correct the specific permission/ownership. Avoid blanket `chmod 777` or running every tool as root. |

## Collect evidence before asking for help

Record OS/release, tool version, exact command, complete relevant error, and expected result. Redact passwords, session cookies, VPN keys and personal data. Network and service logs can contain sensitive information.
