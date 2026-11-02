# A sensible lab workflow

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** Workflow guidance; apply each linked tool’s impact notes.

1. Confirm scope, target address and network isolation. Create a working folder and `results/` directory.
2. Verify your IP, route and VPN if used. Identify a few ports with Nmap.
3. Enumerate only observed services: HTTP with curl/Burp, SMB with smbclient.
4. Run focused discovery with a small list, then inspect individual results.
5. Record evidence, tool version, exact command and limitations. Confirm findings before assigning a vulnerability label.
6. Stop listeners, unmount shares, restore wireless mode and close the VPN when finished.
