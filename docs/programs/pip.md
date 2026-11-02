# pip

[All programs](README.md) · [Repository home](../../README.md)

Install Python libraries inside a project environment. Use `python -m pip` to select the pip belonging to that interpreter.

## Install and verify

```bash
sudo apt update
apt policy python3-pip
sudo apt install python3-pip
python3 -m pip --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK, WRITE; package installs can execute build code. First create/activate a venv with `python3 -m venv .venv` and `source .venv/bin/activate`.

### Install, inspect, and validate a library

```bash
python -m pip install requests
python -m pip show requests
python -m pip check
python -c 'import requests; print(requests.__version__)'
```

This example obtains the Requests HTTP library from your configured package index. Review package identity and trust before installing. Show reports metadata/location; check detects incompatible installed dependency requirements.

### Recreate a known project

```bash
python -m pip install -r requirements.txt
python -m pip list
python -m pip freeze > installed-versions.txt
```

Use only a trusted requirements file; it may reference source repositories or other indexes. Freeze records what is present; it does not review vulnerabilities or guarantee reproducibility across operating systems.

### Remove a project dependency

```bash
python -m pip uninstall requests
```

Uninstall prompts and does not automatically remove all dependencies. Deactivate when finished. For disposable experiments, remove the inspected project venv instead of changing system Python.

**Troubleshooting:** verify `sys.executable` and pip location when imports fail. Build failures may need development headers compatible with the project. Do not globally bypass Parrot's externally managed environment protection.

**Cleanup:** deactivate the environment and remove only a confirmed disposable project venv if it is no longer needed. Keep source and requirements files.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run python3-pip` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://pip.pypa.io/en/stable/user_guide/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
