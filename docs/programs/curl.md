# curl

[All programs](README.md) · [Repository home](../../README.md)

Send HTTP requests and inspect responses without a browser.

## Install and verify

```bash
sudo apt update
apt policy curl
sudo apt install curl
curl --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK and optional WRITE. Start the local HTTP lab first.

```bash
curl -i http://127.0.0.1:8000/hello.txt
curl -I http://127.0.0.1:8000/hello.txt
curl -o saved-hello.txt http://127.0.0.1:8000/hello.txt
```

`-i` includes response headers; `-I` sends HEAD, which some servers handle differently; `-o` writes the body to a file and overwrites that path.

### Bounded request and structured body

```bash
curl --connect-timeout 5 --max-time 15 -L --max-redirs 3 http://127.0.0.1:8000/
curl -i -H 'Content-Type: application/json' --data '{"message":"hello"}' http://127.0.0.1:8000/api
```

The second example demonstrates JSON POST formatting; the simple Python file server does not implement this API and should reject POST. Use your own app implementing `/api` to test success. `-L` follows redirects; avoid forwarding secrets to unrelated destinations.

### Exit status versus HTTP status

```bash
curl --fail-with-body -sS http://127.0.0.1:8000/missing.txt
```

By default curl can exit successfully even for HTTP errors. `--fail-with-body` makes HTTP 400+ produce a failure status while retaining the body; older builds may need `--fail` instead.

**Troubleshooting:** error 6 is resolution, 7 connection failure, and certificate errors need fixing trust/hostname/time. Do not routinely use `-k`.

**Cleanup:** delete only response files you created, and protect requests containing credentials.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run curl` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://curl.se/docs/manpage.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
