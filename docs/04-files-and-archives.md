# Files, archives and terminal essentials

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** INSPECT, WRITE and EXTRACT. Archive extraction writes files.

```bash
pwd                         # Current directory
ls -lah                     # Files including hidden files, sizes and permissions
mkdir -p ~/labs/example/results
cd ~/labs/example
find . -type f -ls           # Find regular files and list details
rg -n 'pattern' .            # Search file contents; install package ripgrep
less notes.txt              # Read a large file; q quits
sha256sum downloaded.iso     # Compute checksum; compare with trusted publisher value
```

### tar — inspect, extract and create archives

```bash
tar -tf archive.tar.gz                  # List members before extracting
mkdir -p extracted
tar -xzf archive.tar.gz -C extracted    # Extract gzip-compressed tar archive
tar -xf archive.tar.xz -C extracted     # GNU tar auto-detects common compression
tar -czf backup.tar.gz notes/           # Create gzip-compressed archive
```

`-x` extracts, `-c` creates, `-t` lists, `-z` selects gzip, `-f` takes the archive filename. `-f` need not be the final option; its argument must be supplied correctly. Extract untrusted archives as a regular user into a new directory, not with `sudo` into the system.
