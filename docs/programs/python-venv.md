# Python virtual environments

[All programs](README.md) · [Repository home](../../README.md)

Keep project dependencies separate from Parrot’s system Python.

## Install and verify

```bash
sudo apt update
apt policy python3-venv
sudo apt install python3-venv
python3 --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** WRITE. Work in your own project directory. A venv is an environment, not a virtual machine or security sandbox.

```bash
mkdir -p ~/labs/python-demo
cd ~/labs/python-demo
python3 -m venv .venv
source .venv/bin/activate
python -c 'import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)'
python -m pip --version
```

The executable/pip should be under this `.venv`; the Boolean should be `True`. Activation affects the current shell. You can instead use `.venv/bin/python` explicitly without activation.

### Run and record a project

```bash
python -c 'print("isolated Python works")'
python -m pip list
python -m pip freeze > requirements.txt
deactivate
```

Freeze writes installed versions for later review; it is not a complete cross-platform dependency lock. A project with no third-party packages can have an empty requirements file.

**Troubleshooting:** missing ensurepip/venv support usually requires the matching Parrot `python3-venv` package. An “externally managed” pip error means you are probably using system Python; verify executable paths. Do not solve it with `sudo pip`.

**Cleanup:** deactivate first. Inspect the exact project's `.venv` path and remove only that generated environment if no longer needed. Keep source files and requirements. Virtual environments can be recreated and should not be committed to Git.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run python3-venv` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://docs.python.org/3/library/venv.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
