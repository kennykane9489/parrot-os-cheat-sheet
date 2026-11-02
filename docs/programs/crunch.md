# Crunch

[All programs](README.md) · [Repository home](../../README.md)

Generate candidate strings from an explicit character set for small controlled exercises. It does not authenticate or crack anything by itself.

## Install and verify

```bash
sudo apt update
apt policy crunch
sudo apt install crunch
crunch --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** WRITE; output can grow exponentially. Some builds show usage with no arguments rather than --help; inspect local usage.

```bash
crunch 2 2 ab12 -o crunch-demo.txt
wc -l crunch-demo.txt
head crunch-demo.txt
```

Two positions over four characters produce 4^2 = 16 lines. The first two numbers are minimum and maximum lengths. Review the output before using it in any other tool.

### Reproduce the original example accurately

```bash
crunch 4 4 012345abcdef -o crunch-four.txt
wc -l crunch-four.txt
```

There are 12 characters, producing 12^4 = 20,736 candidates. Each fixed-width line also has a newline; disk use grows with both length and candidate count. Increasing to long ranges can fill storage quickly.

### Decide whether generation helps

For a training service with a known small candidate set, an explicit three-line test file is usually enough. Generating every possible password is not an efficient general recovery method. Respect account lockouts when any list is used for authentication.

**Troubleshooting:** output-path errors need a writable directory; huge estimates call for reducing the range rather than blindly continuing. Stop with Ctrl+C if the generated size is unexpected.

**Cleanup:** delete only the two lab-generated files after reviewing them. Do not publish wordlists containing private personal details or actual secrets.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run crunch` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://sourceforge.net/projects/crunch-wordlist/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
