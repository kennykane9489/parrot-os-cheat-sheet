# ripgrep / rg

[All programs](README.md) · [Repository home](../../README.md)

Search file contents quickly with useful line numbers, file filters and explicit hidden-file handling.

## Install and verify

```bash
sudo apt update
apt policy ripgrep
sudo apt install ripgrep
rg --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT; output can reveal secrets. Start inside your project, not the entire filesystem.

```bash
rg -n 'ERROR' logs/
rg -n -i 'openvpn' docs/
rg -n -F '127.0.0.1' .
rg --files -g '*.md'
```

`-n` prints line numbers; `-i` ignores case; `-F` treats the pattern literally instead of as regex. `--files` lists searchable filenames and `-g` constrains a glob.

### Search hidden configuration deliberately

```bash
rg --hidden -n 'timeout' .github/
```

By default rg respects ignore rules and skips hidden/binary files. `--hidden` includes hidden files but does not automatically disable every ignore rule. Use `--no-ignore` only when needed and keep the path narrow to avoid secrets/vendor output.

### Interpret exit codes

0 normally means a match, 1 means no match, and 2 indicates an error. A no-match result is not necessarily a failed tool installation. In scripts, distinguish these conditions instead of treating every nonzero exit as a crash.

**Troubleshooting:** a missing result may be case, regex syntax, ignore rules, binary classification or the wrong working directory. Start with a known file and literal pattern. Do not copy sensitive matches into public issue reports.

**Cleanup:** these commands do not edit files; only remove a redirected report if you created one.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run ripgrep` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
