# Lab 2: Archives and integrity

[Lab index](README.md)

**Goal:** archive, extract and compare bytes. **Impact:** WRITE and REMOVE in a new temporary directory. Requires Bash, GNU tar, sha256sum and cmp. Run all steps in the same terminal.

## Setup

```bash
archive_lab=$(mktemp -d /tmp/parrot-archive.XXXXXX)
mkdir "$archive_lab/source" "$archive_lab/restored"
printf 'keep these bytes
' > "$archive_lab/source/note.txt"
```

## Create, inspect and extract

```bash
tar -czf "$archive_lab/notes.tar.gz" -C "$archive_lab" source
tar -tf "$archive_lab/notes.tar.gz"
tar -xzf "$archive_lab/notes.tar.gz" -C "$archive_lab/restored"
sha256sum "$archive_lab/source/note.txt" "$archive_lab/restored/source/note.txt"
cmp "$archive_lab/source/note.txt" "$archive_lab/restored/source/note.txt"
```

Expected: archive contains `source/` and `source/note.txt`; both digests match. Successful `cmp` prints nothing and exits 0. This verifies file bytes, not a publisher's identity. This archive is one you just created; inspect unknown archives before extraction.

## Cleanup

```bash
rm -- "$archive_lab/source/note.txt" "$archive_lab/restored/source/note.txt" "$archive_lab/notes.tar.gz"
rmdir -- "$archive_lab/source" "$archive_lab/restored/source" "$archive_lab/restored" "$archive_lab"
unset archive_lab
```

Question: will a checksum detect a changed byte? Yes, with overwhelming probability; it cannot tell you who made the change.
