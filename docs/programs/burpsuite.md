# Burp Suite Community

[All programs](README.md) · [Repository home](../../README.md)

Intercept, inspect and replay HTTP requests in a dedicated browser testing workflow. Community is free; Professional is a separate licensed product.

## Install and verify

```bash
sudo apt update
apt policy burpsuite
sudo apt install burpsuite
burpsuite --help
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK and WRITE; intercepted requests can change application state.

### Start and connect

```bash
burpsuite
```

If the repository package is unavailable, download the Linux installer from PortSwigger's official download page. Verify its origin, select the build for your architecture and follow the installer; do not use keygens or cracked installers. GUI launchers may not implement `--help`; the installed app's About page shows its version.

1. Create a temporary project if prompted and use the default configuration for your first lab.
2. Open Proxy's built-in browser. Browse your own lab URL, such as the local HTTP server.
3. Inspect Proxy → HTTP history. Keep Intercept off when you want requests to continue normally; turn it on only when ready to forward/drop paused requests.

### Replay one request

Send the `GET /hello.txt` request to Repeater. Send it unchanged and inspect 200/body, then change the path to `/missing.txt` and send again. Compare the 404 result. The built-in browser is already configured; external browsers require a dedicated proxy profile and the Burp CA for HTTPS interception.

### Save evidence

Save the relevant raw HTTP request, not just the response HTML. Redact cookies/tokens before committing files. A raw request includes method/path, Host header, headers, blank line and optional body. Adding `url=file://...` is only a parameter; it does not create a file-read capability without a vulnerable application.

**Troubleshooting:** a “hanging” browser often has an intercepted request waiting. Port conflicts require changing proxy settings and browser configuration together. HTTPS errors in an external profile may require correct CA trust.

**Cleanup:** close the test browser, stop proxy listeners and restore any external browser proxy/CA changes. Keep interception CAs limited to test profiles.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run burpsuite` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://portswigger.net/burp/documentation/desktop/getting-started/download-and-install). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
