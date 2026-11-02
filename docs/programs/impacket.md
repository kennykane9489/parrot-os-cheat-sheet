# Impacket

[All programs](README.md) · [Repository home](../../README.md)

Python protocol libraries and example clients for Windows/SMB and related network protocols.

## Install and verify

```bash
sudo apt update
apt policy python3-impacket impacket-scripts
sudo apt install python3-impacket impacket-scripts
dpkg -L impacket-scripts
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK for clients, WRITE for installs/downloads. Package splits and entry-point names vary; check APT candidates individually before installation.

### Upstream isolated fallback

```bash
sudo apt install pipx
pipx install impacket
pipx list
```

Do this only when deliberately choosing upstream instead of the distribution copy. The upstream example may be `smbclient.py`, while a distro wrapper may be `impacket-smbclient`.

### Locate and run a permitted client

```bash
command -v impacket-smbclient
command -v smbclient.py
```

If your installed wrapper is impacket-smbclient, use:

```bash
impacket-smbclient -h
impacket-smbclient 'LAB/labuser@192.168.56.20'
```

Enter the password when prompted rather than placing it in the target string. In the client, use `help`, `shares`, `use Data`, `ls` and `exit` with actual authorized share names. This is a protocol-learning workflow, not remote execution.

### Verify the result

Compare a known share/file listing with Samba smbclient. Differences can reflect negotiation/authentication details, not necessarily a vulnerability.

**Troubleshooting:** “command not found” often reflects the packaging prefix or pipx PATH. Kerberos needs appropriate DNS/time/realm configuration; do not switch to credential-dumping examples to diagnose a file listing.

**Cleanup:** exit the client and remove only authorized local downloads. Update/remove through the selected manager, preserving any needed test reports.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run python3-impacket impacket-scripts` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/fortra/impacket). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
