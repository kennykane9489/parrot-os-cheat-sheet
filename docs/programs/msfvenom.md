# msfvenom

[All programs](README.md) · [Repository home](../../README.md)

Inspect Framework payload metadata and supported output formats. Installed with Metasploit Framework.

## Install and verify

```bash
sudo apt update
apt policy metasploit-framework
sudo apt install metasploit-framework
msfvenom --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT for the examples below. Payload generation can create executable artifacts; real payload behavior depends on selected options, architecture and target.

```bash
msfvenom -l payloads
msfvenom -l formats
msfvenom -l encoders
```

The listing type after `-l` is required; the old bare `-l` is incomplete. Use listings to identify actual names from your installed Framework rather than copying architecture-specific names from an old sheet.

### Inspect an example payload's requirements

```bash
msfvenom -p windows/meterpreter/reverse_tcp --list-options
```

This prints metadata/options instead of generating an executable. Confirm the name exists in your installed list. LHOST must be a callback address reachable from the authorized lab target; it is not always your default LAN IP. LPORT is the chosen callback/listener port. Reverse and bind payloads use opposite connection directions.

### Plan a controlled experiment

Match target OS/architecture, payload options, listener type and routing before following an authorized course lab. A file extension does not change architecture. Staged and stageless payload names differ. Encoding is not encryption and does not guarantee antivirus evasion. Never distribute a disguised backdoor as a file-sharing example.

**Troubleshooting:** a nonexistent payload is a version/name mismatch. Connectivity failures may be routing/NAT/firewall rather than payload generation. An executable opening does not guarantee a session.

**Cleanup:** these inspection commands create no payload. Delete only your own confirmed lab artifacts after stopping matching sessions/listeners, or restore the disposable VM snapshot.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run metasploit-framework` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
