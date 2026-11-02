# dpkg

[All programs](README.md) · [Repository home](../../README.md)

Inspect and manage individual .deb packages and their installed file lists. APT sits above dpkg and resolves downloads/dependencies.

## Install and verify

```bash
sudo apt update
apt policy dpkg
sudo apt install dpkg
dpkg --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT for queries; CHANGE for installs/configuration. Already installed on Parrot.

### Inspect before installing

```bash
dpkg --print-architecture
dpkg-deb --info ./file.deb
dpkg-deb --contents ./file.deb
```

Replace `file.deb` with a trusted local package. Compare architecture and package details with your system. Inspection does not establish publisher authenticity.

### Install and find package files

```bash
sudo apt install ./file.deb
dpkg -l nmap
dpkg -L nmap
dpkg -S /usr/bin/nmap
```

APT is preferable for a local .deb because it can fetch dependencies. `dpkg -i` alone cannot fetch them. `-l` queries package status; `-L` lists files; `-S` finds the owning package. Files installed outside the package manager may have no owner.

### Recover an interrupted setup

```bash
sudo dpkg --configure -a
sudo apt --fix-broken install
```

Use recovery only when package errors call for it, after other package transactions stop. Review the dependency repair proposal.

**Troubleshooting:** an architecture mismatch requires the correct build, not force flags. If a dependency cannot be satisfied, use a compatible package/release. Do not force overwrites to conceal conflicts. Cleanup of a test package belongs in APT, after reviewing a dry run.

**Cleanup:** if you intentionally installed a disposable test package, preview its removal through APT before removing it. Do not remove dpkg itself.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run dpkg` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://manpages.debian.org/stable/dpkg/dpkg.1.en.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
