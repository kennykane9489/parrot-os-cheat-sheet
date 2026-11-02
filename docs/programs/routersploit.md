# RouterSploit

[All programs](README.md) · [Repository home](../../README.md)

Explore embedded-device module metadata in an isolated, firmware-specific lab. Historical dependencies may not support a modern Parrot release.

## Install and verify

Use a separate user-owned checkout and inspect upstream requirements first:

```bash
sudo apt install git python3-venv
mkdir -p ~/tools
git clone https://github.com/threat9/routersploit.git ~/tools/routersploit
cd ~/tools/routersploit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python rsf.py
```

An existing destination must be inspected rather than overwritten. Dependency installation can execute build code. Upstream compatibility must be checked; no claim is made that all dependencies work on current Parrot. Python 2 packages such as python-pip/python-dev are not a valid modern setup.

## Use it in practice

**Impact:** NETWORK/WRITE during installation; selected modules may change or destabilize devices.

### Launch in its isolated environment

```bash
cd ~/tools/routersploit
source .venv/bin/activate
python rsf.py
```

Inside the framework, start with `help`. Use tab completion and the installed module descriptions instead of an old fixed list. Do not assume a scanner or a check is passive; read the module implementation/documentation before running it.

### Practical identification workflow

1. On your own router, read its administration page or label for exact model/hardware revision and firmware version.
2. Compare that version to the vendor's advisory and RouterSploit module description.
3. Use module `show options`/help as provided by the current shell to understand target fields. Do not run an exploit against a merely similar device name.
4. Prefer updating and validating vendor firmware in a disposable spare-device lab before any intrusive validation.

**Troubleshooting:** modern Python/build dependency failures may mean the project needs an older supported isolated environment. Use an upstream-documented disposable VM/container; do not downgrade Parrot's system Python. A module not present is a version difference, not permission to choose a random exploit.

**Cleanup:** exit the framework, deactivate the venv, stop lab services and restore your spare device's known-good configuration/firmware as appropriate. Preserve source commit/version with notes.

## Updates and removal

Update through the same manager or upstream method used for installation. Avoid mixing distribution and source installations of the same executable. Follow the cleanup steps above before removing any files.

## Reference and compatibility

[Upstream documentation](https://github.com/threat9/routersploit). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
