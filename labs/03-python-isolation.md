# Lab 3: Python isolation without downloads

[Lab index](README.md) · [Python guide](../docs/03-setup-and-python.md)

**Goal:** verify that a venv uses a separate interpreter environment. **Impact:** WRITE and REMOVE in a fresh temporary directory. Needs Bash, Python 3 and venv support. If venv support is missing on Parrot, install `python3-venv` through APT first; this changes installed packages.

## Setup and inspect

```bash
venv_lab=$(mktemp -d /tmp/parrot-venv.XXXXXX)
python3 -m venv "$venv_lab/.venv"
source "$venv_lab/.venv/bin/activate"
python -c 'import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)'
python -m pip --version
deactivate
```

Expected: executable and pip paths point under your temporary `.venv`; the Boolean is `True`. No third-party package download is needed. If venv creation fails, stop and read the error before continuing.

## Cleanup

The following deletion is limited to the newly created, specifically named temporary directory. Keep the original terminal variable and run only after deactivation.

```bash
case "$venv_lab" in
  /tmp/parrot-venv.??????)
    rm -r -- "$venv_lab"
    ;;
  *) printf 'Unexpected lab path; inspect it manually.
' >&2 ;;
esac
unset venv_lab
```

Question: does activating a venv change the OS Python installation? No. It changes this shell's command lookup/environment to use the venv; deactivation restores it.
