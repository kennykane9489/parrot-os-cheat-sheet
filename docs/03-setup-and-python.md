# First setup and Python tools

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** CHANGE; downloads source code or dependencies.

```bash
sudo apt install git curl wget ca-certificates python3-venv python3-pip pipx
pipx ensurepath
```

Open a new terminal after changing PATH. Install tools in small groups after checking `apt policy PACKAGE`; not every edition has every security tool preinstalled.

### Git — track and obtain source code

```bash
git clone https://github.com/OWNER/PROJECT.git
cd PROJECT
git status
git log -5 --oneline
```

Replace the example repository. Inspect source and installation instructions before executing it. A successful clone does not establish trust.

### Python venv — isolate project dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
# Work inside this project's activated environment.
deactivate
```

Use this inside the intended project directory with a trusted requirements file. Avoid `sudo pip install` and routine `--break-system-packages`. For standalone Python applications, `pipx install PACKAGE` creates an isolated environment; do not install the same command through multiple managers without tracking which executable runs.

### Desktop environments

Check your actual desktop first. GNOME extensions apply to GNOME Shell, not MATE or KDE. On GNOME, the modern tweaks package is generally `gnome-tweaks`; check `apt policy gnome-tweaks` before installation. `Ubuntu-mate-desktop` is not a Parrot setup instruction. Use Parrot's documented desktop choices; adding several desktops changes login options, services and defaults.
