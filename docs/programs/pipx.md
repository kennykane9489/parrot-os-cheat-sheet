# pipx

[All programs](README.md) · [Repository home](../../README.md)

Install Python command-line applications into separate environments while exposing their commands on your PATH.

## Install and verify

```bash
sudo apt update
apt policy pipx
sudo apt install pipx
pipx --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK, WRITE. Use pipx for applications, not libraries imported by another project.

```bash
pipx ensurepath
pipx list
```

Open a new terminal after ensurepath. It may update shell startup configuration. Do not use sudo for your normal pipx environment.

### Install a CLI and check it

```bash
pipx install httpie
http --version
http GET http://127.0.0.1:8000/
```

HTTPie is an example trusted CLI; the request needs a running local web server. pipx supplies isolation; HTTPie performs the request. A missing executable after installation usually indicates PATH needs reloading.

### Maintain or remove it

```bash
pipx list
pipx upgrade httpie
pipx uninstall httpie
```

Upgrade acts on this pipx application, not an APT-installed program of the same name. Use `command -v http` to see which executable runs. Do not install multiple competing copies without tracking them.

**Troubleshooting:** libraries generally have no entry-point executable and are unsuitable for pipx. A package build failure may require supported Python and build dependencies; inspect upstream requirements. Cleanup with pipx uninstall removes the application's environment; it may leave user settings outside it.

**Cleanup:** pipx uninstall httpie removes the example application environment; review any separate user settings before deleting them.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run pipx` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://pipx.pypa.io/stable/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
