# SMB: smbclient, CIFS, SMBMap and NetExec

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** NETWORK, MOUNT and possible WRITE; see each tool’s notes.

### smbclient — browse SMB shares interactively

Install: `sudo apt install smbclient`.

```bash
smbclient -L 192.168.56.20 -U labuser
smbclient //192.168.56.20/Data -U labuser
```

Passwords are prompted. Inside smbclient use `help`, `ls`, `cd folder`, `get example.txt`, `lcd /tmp`, and `quit`. `put` uploads and changes the server. Listing shares does not enumerate user accounts. `-N` suppresses the password prompt for a deliberately configured guest/anonymous lab test; it does not bypass authentication.

### CIFS mount — access a share as a local directory

Install: `sudo apt install cifs-utils`.

```bash
sudo mkdir -p /mnt/lab-data
sudo mount -t cifs //192.168.56.20/Data /mnt/lab-data -o username=labuser,ro
find /mnt/lab-data -type f -ls
sudo umount /mnt/lab-data
```

The example requests a read-only mount and prompts for the password. Avoid passwords in shell history. Negotiate modern SMB; do not force SMB1 to make an obsolete server work. A persistent credentials file must have restrictive permissions.

### SMBMap — summarize share permissions

Check/install package `smbmap`, then:

```bash
smbmap --help
smbmap -H 192.168.56.20
```

An unauthenticated attempt may return nothing. For authenticated use, follow your installed version's credential options. Permission checks can make test writes unless disabled by supported options; inspect help before treating the tool as strictly read-only.

### NetExec — maintained successor in the CrackMapExec lineage

Prefer NetExec for new workflows. Check `apt policy netexec`; otherwise use the official isolated-install instructions. Do not assume Kali installation instructions prove Parrot package availability.

```bash
nxc --help
nxc smb --help
nxc smb 192.168.56.20
```

Used for protocol discovery and authorized assessments of Windows/AD environments. Authenticated flags such as `--shares` and `--pass-pol` depend on server permissions and protocol support; use a designated lab account and the credential method supported by your build. Random usernames/passwords are not a reliable substitute for guest authentication. No scanner is guaranteed to evade endpoint protection.

### Impacket — network-protocol toolkit

Contains Python protocol libraries and example utilities. Package and command names vary. Check `apt policy python3-impacket impacket-scripts` and package contents before installation. Prefer distribution packages or the upstream isolated-install instructions. Begin with utility help and protocol documentation rather than assuming every example command is installed under the same name.
