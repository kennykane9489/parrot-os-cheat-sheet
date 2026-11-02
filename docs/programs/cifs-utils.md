# CIFS mounts / cifs-utils

[All programs](README.md) · [Repository home](../../README.md)

Mount an SMB share into the local filesystem with explicit permissions and a clear unmount step.

## Install and verify

```bash
sudo apt update
apt policy cifs-utils
sudo apt install cifs-utils
mount.cifs -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK and MOUNT; writable mounts can change remote files. Use a read-only mount first.

```bash
sudo mkdir -p /mnt/lab-data
sudo mount -t cifs //192.168.56.20/Data /mnt/lab-data -o username=labuser,ro
findmnt /mnt/lab-data
ls -la /mnt/lab-data
```

Substitute your server/share/account and enter the password at the prompt. `ro` requests read-only access from this mount. This does not change the underlying account's server-side permissions.

### Inspect files

```bash
find /mnt/lab-data -maxdepth 2 -type f -ls
```

Restrict depth to avoid traversing a large share. Opening files can still generate network traffic and server audit events. Do not put passwords directly in command history. For persistent mounts, use a root-owned credentials file with restrictive permissions and the documented fstab options; do not improvise a public credentials path.

### Unmount

```bash
cd ~
sudo umount /mnt/lab-data
sudo rmdir /mnt/lab-data
```

Only remove the empty mountpoint after successful unmount. Never recursively delete a mounted share to clean up the local directory.

**Troubleshooting:** “busy” means a process still uses the mount; close viewers/shells and retry normally. Permission errors require server/account checks. Protocol negotiation problems should be resolved with a supported server/client version, not routine SMB1 enablement.

**Cleanup:** unmount successfully before removing the empty mountpoint. Do not recursively delete a mounted remote share.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run cifs-utils` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://manpages.debian.org/stable/cifs-utils/mount.cifs.8.en.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
