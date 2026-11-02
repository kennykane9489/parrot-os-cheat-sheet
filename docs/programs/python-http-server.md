# Python HTTP server

[All programs](README.md) · [Repository home](../../README.md)

Temporarily serve a dedicated folder for local file inspection and download exercises. Not a production server.

## Install and verify

```bash
sudo apt update
apt policy python3
sudo apt install python3
python3 --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** WRITE and LISTEN; downloads are NETWORK. The server provides no built-in authentication or transport encryption in this basic workflow.

```bash
share_dir=$(mktemp -d /tmp/parrot-share.XXXXXX)
printf 'hello from lab\n' > "$share_dir/hello.txt"
python3 -m http.server 8000 --bind 127.0.0.1 --directory "$share_dir"
```

Keep this terminal open. The explicit bind confines access to loopback. The dedicated directory avoids serving your entire home, including private files. Directory contents may be listed.

### Verify in another terminal

```bash
curl -i http://127.0.0.1:8000/hello.txt
curl -i http://127.0.0.1:8000/missing.txt
```

Expect 200 with your text, and 404 for the missing path. This server serves files; it does not implement an API, upload handler or database application.

### Deliberate lab LAN sharing

Only when another authorized lab computer needs access, replace the bind address with your actual lab-interface IP and consider its firewall/routing. Do not use `0.0.0.0` casually on an untrusted network. Ports above 1023 avoid root privileges.

**Troubleshooting:** address-in-use means another listener occupies the port; choose a free port and update requests. Connection refused may mean the server stopped. A 404 means an HTTP response occurred but the path is absent.

**Cleanup:** Ctrl+C in the original terminal, then `rm -- "$share_dir/hello.txt"`, `rmdir -- "$share_dir"`, and `unset share_dir` there. Remove only this known temporary data.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run python3` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://docs.python.org/3/library/http.server.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
