# tmux

[All programs](README.md) · [Repository home](../../README.md)

Keep related terminal windows and panes in a session that survives client detachment.

## Install and verify

```bash
sudo apt update
apt policy tmux
sudo apt install tmux
tmux -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** starts processes/sessions; commands inside panes have their own effects.

```bash
tmux new -s parrot-lab
```

Inside tmux the default prefix is Ctrl+B. Release it, then press `%` to split left/right or `"` to split top/bottom. Prefix then an arrow selects a pane. Prefix then `c` creates a window; prefix then `n`/`p` changes windows.

### Detach and resume

Press Ctrl+B then `d` to detach without stopping the programs. In a normal terminal:

```bash
tmux ls
tmux attach -t parrot-lab
```

Detaching is not a cleanup step: an HTTP server, VPN or scanner can continue running in the session. Check what's running before leaving it unattended.

### Practical arrangement

Put the local HTTP server in one pane and curl/ss in the other. This makes request and server logs visible together. Avoid displaying real passwords in either pane or screenshot.

### End deliberately

Stop foreground programs with their own graceful shutdown (often Ctrl+C), then type exit in shells. After confirming nothing important remains, `tmux kill-session -t parrot-lab` terminates that named session and its programs. Do not use kill-server as a routine cleanup because it affects all sessions.

**Troubleshooting:** “no server running” usually means no session exists. A different user/root account has a separate tmux context. If nested sessions confuse prefixes, detach and attach from a normal shell.

**Cleanup:** stop your own tasks gracefully before closing their shells or killing the specifically named disposable session.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run tmux` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/tmux/tmux/wiki/Getting-Started). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
