# Netcat / nc

[All programs](README.md) · [Repository home](../../README.md)

Open simple TCP clients/listeners for local protocol and connection exercises. This guide targets netcat-openbsd, not every nc implementation.

## Install and verify

```bash
sudo apt update
apt policy netcat-openbsd
sudo apt install netcat-openbsd
nc -h
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** LISTEN, NETWORK and WRITE. Netcat traffic here is unauthenticated and unencrypted. Prefer SSH for private remote files.

### Two-terminal conversation

Terminal A:

```bash
nc -l 127.0.0.1 2222
```

Terminal B:

```bash
nc 127.0.0.1 2222
```

Type a line in either terminal; it appears at the other endpoint. Loopback confines the exercise to this computer. Ctrl+C closes the run.

### Transfer a small local file

Receiver, terminal A:

```bash
nc -l 127.0.0.1 2222 > received.txt
```

Sender, terminal B:

```bash
printf 'transfer example\n' > original.txt
nc -N 127.0.0.1 2222 < original.txt
sha256sum original.txt
```

After the receiver exits, run `sha256sum received.txt` there and compare. `-N` closes the write side after stdin EOF in OpenBSD nc. `>` overwrites an existing destination. The old `< filename >` trailing operator is invalid shell syntax.

### Port check

```bash
nc -vz -w 3 127.0.0.1 8000
```

This attempts a connection to one local port. A successful TCP connection does not prove the application is healthy.

**Troubleshooting:** `-N` not supported suggests a different nc implementation. Check local help instead of assuming flags. `-k` keeps listeners serving; it does not provide framing or checksums.

**Cleanup:** close all lab listeners and delete only original.txt/received.txt if created for the exercise.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run netcat-openbsd` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://manpages.debian.org/stable/netcat-openbsd/nc.1.en.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
