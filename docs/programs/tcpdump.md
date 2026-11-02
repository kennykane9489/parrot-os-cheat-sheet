# tcpdump

[All programs](README.md) · [Repository home](../../README.md)

Capture a narrowly filtered packet trace from a specific interface for diagnosis.

## Install and verify

```bash
sudo apt update
apt policy tcpdump
sudo apt install tcpdump
tcpdump --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** CAPTURE and WRITE. Keep the example on loopback and a known test port.

```bash
sudo tcpdump -D
sudo tcpdump -i lo -nn -c 10 'tcp port 8000'
```

`-D` lists interfaces; `-i lo` selects loopback; `-nn` avoids name/port-name lookups; `-c 10` stops after ten matching packets. If not enough packets arrive, Ctrl+C stops the capture. Generate requests in the HTTP lab from another terminal.

### Save then inspect

```bash
sudo tcpdump -i lo -nn -c 10 -w /tmp/parrot-http.pcap 'tcp port 8000'
tcpdump -nn -r /tmp/parrot-http.pcap
```

Choose a fresh output path; the example can overwrite an existing file of that name. Root-owned captures may require a deliberate ownership/permission adjustment or a privileged read under local policy. Do not make them world-readable just for convenience.

### Interpret carefully

Packet flags, endpoints and sequence numbers help identify handshake/retransmission behavior. A capture only reflects packets visible at that point, not every event on the network. `-A` prints payload bytes and can expose secrets; avoid broad unfiltered payload dumps.

**Troubleshooting:** wrong interface, filter or privilege often explains an empty capture. Check that traffic is actually generated after capture starts. A checksum-offload warning may not represent on-wire corruption.

**Cleanup:** stop the capture, confirm no background process remains, and remove only your known lab pcap when no longer needed.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run tcpdump` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.tcpdump.org/manpages/tcpdump.1.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
