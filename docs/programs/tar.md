# tar

[All programs](README.md) · [Repository home](../../README.md)

Create, list and extract archives; compression and archiving are separate steps combined by convenient options.

## Install and verify

```bash
sudo apt update
apt policy tar
sudo apt install tar
tar --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT or WRITE. Work in an empty destination and avoid sudo for ordinary extraction.

```bash
tar -tf archive.tar.gz
mkdir -p extracted
tar -xzf archive.tar.gz -C extracted
```

`-t` lists, `-x` extracts, `-z` handles gzip, `-f` supplies the archive file and `-C` changes extraction directory. The filename must follow `-f` correctly; `-f` is not required to be the final flag. GNU tar can auto-detect common compression when extracting with `tar -xf`.

### Back up a folder and verify it

```bash
tar -czf notes-backup.tar.gz notes/
tar -tf notes-backup.tar.gz
```

`-c` creates a new archive. This overwrites an existing output archive, so choose a new backup filename. To restore, extract into a new directory rather than over the live files and compare contents.

**Troubleshooting:** “not in gzip format” can mean the suffix does not match the content or the download is an error page. Inspect before extraction. Absolute/traversal paths, links and decompression size can make unknown archives dangerous; avoid privileged extraction and inspect member names/size.

**Cleanup:** remove only your generated archive or known restored files after confirming the source remains intact. Follow the archive practice lab for exact temporary-file cleanup.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run tar` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.gnu.org/software/tar/manual/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
