# Wireshark

[All programs](README.md) · [Repository home](../../README.md)

Inspect network packets visually with display filters and protocol detail panes.

## Install and verify

```bash
sudo apt update
apt policy wireshark
sudo apt install wireshark
wireshark --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** CAPTURE/WRITE, potentially sensitive traffic. Limit exercises to your own loopback traffic. Run the GUI as a normal user, not as root.

### Capture setup

If the installer asks whether non-superusers may capture, choose according to your machine's access policy. On Debian-style packaging, `sudo dpkg-reconfigure wireshark-common` can revisit capture permissions; only authorized users should join the wireshark group. Log out/in after group changes. Reading an existing capture does not require live-capture privilege.

### Practical local capture

1. Start the local Python HTTP lab.
2. Open Wireshark and select loopback (`lo`) if capture permission is configured.
3. Set capture filter `tcp port 8000` before starting.
4. Make one request with curl, then stop capture promptly.
5. Apply display filter `http` or `tcp.port == 8000` and select a packet to inspect headers and bytes.

Capture filters and display filters use different syntax. A plaintext HTTP body can be visible; encrypted HTTPS payloads normally are not readable merely by capturing them.

### Save/read

Save as a new pcapng file, then reopen it to verify it contains the intended traffic. Use Follow TCP Stream only on traffic you are authorized to inspect; it can expose complete application exchanges.

**Troubleshooting:** no packets may mean wrong interface/filter, no generated traffic or missing permissions. Do not use sudo on the entire GUI as the routine fix.

**Cleanup:** stop capture, close your test server, and restrict/delete captures containing sensitive data before sharing.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run wireshark` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.wireshark.org/docs/wsug_html_chunked/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
