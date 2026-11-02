# find

[All programs](README.md) · [Repository home](../../README.md)

Locate filesystem entries by name, type, size and other metadata. It searches paths, not file contents.

## Install and verify

```bash
sudo apt update
apt policy findutils
sudo apt install findutils
find --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT for these examples. Start with a narrow directory.

```bash
find ~/Documents -type f -name '*.pdf'
find ~/Documents -type f -size +10M -ls
find . -type f -mtime -7 -print
```

Quote globs so find receives the pattern rather than the shell expanding it. `-type f` selects regular files; `+10M` selects larger files; `-mtime -7` uses find's day-based modification-age semantics, not a calendar-week boundary.

### Safely process files with spaces

```bash
find . -type f -name '*.txt' -exec wc -l -- {} +
```

Find supplies filenames as separate arguments. `+` batches arguments for fewer executions; it must terminate the `-exec` expression. Do not parse `find` output with whitespace splitting.

### Verify a result

```bash
find . -type f -name 'notes.txt' -ls
```

`-ls` prints metadata; it does not read the document. Use ripgrep for content search.

**Troubleshooting:** permission errors may be normal outside your directories. Narrow the search rather than running all searches as root. `-delete` and `-exec rm` are destructive and unnecessary for locating a file. Preview exact matches before adding any action.

**Cleanup:** these examples do not change files, so there is nothing to undo.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run findutils` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.gnu.org/software/findutils/manual/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
