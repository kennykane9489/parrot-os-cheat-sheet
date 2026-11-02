# less

[All programs](README.md) · [Repository home](../../README.md)

Read long files without loading an editor; search and navigate logs interactively.

## Install and verify

```bash
sudo apt update
apt policy less
sudo apt install less
less --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT. Open a text file you own:

```bash
less -N notes.txt
```

`-N` shows line numbers. Press Space/PageDown for the next screen, `b` for the previous screen, `g` for the beginning, `G` for the end and `q` to quit.

### Find an error

Type `/ERROR` then Enter. Press `n` for the next match and `N` for the previous. Search is generally case-sensitive; `-i` makes searches without uppercase letters case-insensitive.

```bash
less -i app.log
```

### Follow a growing log

```bash
less +F app.log
```

Follow mode waits for appended data. Press Ctrl+C to return to normal navigation, then `q` to exit. For systemd services, journalctl can select the relevant logs before reading them.

**Troubleshooting:** a missing file is a path problem; check pwd and ls. Long lines can be horizontally navigated with arrow keys when using `-S`. Avoid `-r` on untrusted logs because raw control characters may affect your terminal. `less` is a reader, not a sandbox.

**Cleanup:** quit the viewer. It does not edit the file, although search/history preferences may be stored in your account.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run less` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.greenwoodsoftware.com/less/faq.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
