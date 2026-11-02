# TShark

[All programs](README.md) · [Repository home](../../README.md)

Use Wireshark protocol analysis from the terminal, especially for reading saved captures and extracting fields.

## Install and verify

```bash
sudo apt update
apt policy tshark
sudo apt install tshark
tshark --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT for saved files; live capture CAPTURES/WRITES traffic. Use the packet file from your own lab.

```bash
tshark -r /tmp/parrot-http.pcap
tshark -r /tmp/parrot-http.pcap -Y http.request
```

`-r` reads an existing capture. `-Y` is a display filter, evaluated after protocol decoding. HTTP requests may not be decoded if the chosen port/protocol isn't recognized or if traffic is encrypted/incomplete.

### Extract useful columns

```bash
tshark -r /tmp/parrot-http.pcap -Y http.request -T fields -e frame.number -e ip.src -e http.request.method -e http.request.uri
```

`-T fields` produces selected fields rather than the default packet summary. Multiple values/escaping require care before importing into a spreadsheet; this output is not automatically a robust CSV for every use.

### Limited live capture

```bash
tshark -i lo -f 'tcp port 8000' -c 10
```

Use configured capture privileges, not a root GUI. `-f` is a capture filter; `-Y` is a display filter. Ctrl+C stops an idle capture if ten matching packets never arrive.

**Troubleshooting:** file-permission errors need proper ownership/access, not weakening all permissions. For nonstandard HTTP ports you can investigate Decode As options documented for your build. Do not equate absence under a filter with absence in the original file.

**Cleanup:** stop live capture and protect/delete lab packet files as appropriate.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run tshark` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.wireshark.org/docs/man-pages/tshark.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
