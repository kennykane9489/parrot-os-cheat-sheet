# Nikto

[All programs](README.md) · [Repository home](../../README.md)

Check web servers for known risky files, outdated components and configuration clues. Findings need manual validation.

## Install and verify

```bash
sudo apt update
apt policy nikto
sudo apt install nikto
nikto -Version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK and WRITE; active checks can be noisy. Use your isolated web lab.

```bash
nikto -Help
nikto -h http://127.0.0.1:8000 -o nikto-lab.txt -Format txt
```

`-h` sets the target URL, `-o` writes findings and `-Format` selects an output formatter. Read any scan errors, not just finding counts. The simple Python server may produce little meaningful vulnerability coverage; a deliberately configured lab web app is a richer exercise.

### Investigate one finding

1. Read its exact URL, method and evidence.
2. Request that resource manually through curl or Burp within scope.
3. Check the response body instead of treating a status code alone as proof.
4. Compare the installed server's actual version/configuration with vendor guidance before declaring it vulnerable.

Nikto is a web-server scanner, not a general OS-identification tool. Proxy/user-agent options do not make a test invisible or authorized. Package-provided launchers avoid assuming nikto.pl lives in the current folder.

**Troubleshooting:** connection refusal means no service accepted that address/port. A reverse proxy, authentication gateway or custom errors can distort findings. Limit the target/scope and use the installed help for options controlling duration/plugins.

**Cleanup:** Ctrl+C stops the scan; protect the report because paths/version details can be sensitive. Update the installed package through its original manager rather than mixing untracked source updates into APT files.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run nikto` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/sullo/nikto/wiki). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
