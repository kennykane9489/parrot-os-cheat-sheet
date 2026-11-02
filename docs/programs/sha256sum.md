# sha256sum

[All programs](README.md) · [Repository home](../../README.md)

Calculate SHA-256 digests to compare file bytes or verify against a trusted publisher checksum.

## Install and verify

```bash
sudo apt update
apt policy coreutils
sudo apt install coreutils
sha256sum --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT; creating checksum lists WRITES files. Coreutils is a shared base package; do not remove it after this exercise.

```bash
sha256sum downloaded.iso
```

Compare all hexadecimal characters with the checksum obtained from the publisher over a trusted channel. A checksum copied from the same untrusted source as the file does not establish authenticity.

### Verify a small file later

```bash
printf 'lab notes\n' > checksum-demo.txt
sha256sum checksum-demo.txt > checksum-demo.sha256
sha256sum -c checksum-demo.sha256
```

Expected: `checksum-demo.txt: OK` before any modifications. Changing even one byte will usually yield FAILED with a nonzero exit status. Keep checksum manifests out of directories where an attacker can silently modify both files if you need security assurance.

### Compare two copies

```bash
sha256sum original.txt copied.txt
```

Matching digests are strong evidence of matching bytes, not origin or safety. For direct local comparison use `cmp original.txt copied.txt`.

**Troubleshooting:** `-c` resolves manifest filenames relative to the working directory. Run it from the expected folder and check names before assuming corruption. Line-ending conversion can legitimately change a digest.

**Cleanup:** remove only `checksum-demo.txt` and `checksum-demo.sha256` if you created them for this exercise.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run coreutils` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.gnu.org/software/coreutils/manual/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
