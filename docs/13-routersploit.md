# RouterSploit — optional embedded-device lab framework

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** CHANGE; dependency installation executes package build/install code. Modules may send NETWORK traffic.

The original Python 2 dependencies (`python-dev`, `python-pip`) are obsolete. The upstream project is `threat9/routersploit`; verify current compatibility and module applicability before investing in it.

```bash
git clone https://github.com/threat9/routersploit.git
cd routersploit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python rsf.py
```

If dependencies fail on modern Parrot, use the upstream documented supported environment or an isolated disposable VM; do not downgrade system Python. Inside the framework start with `help`. Module categories and vulnerability checks can change or be intrusive. Old device exploit names are not generic router repair commands, and results require matching model/firmware validation.
