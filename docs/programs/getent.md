# getent

[All programs](README.md) · [Repository home](../../README.md)

Query the system name-service configuration, including hosts files and DNS where configured.

## Install and verify

```bash
sudo apt update
apt policy libc-bin
sudo apt install libc-bin
getent --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT and possible NETWORK. libc-bin is a shared system package; getent normally exists already.

```bash
getent hosts localhost
getent ahosts example.com
getent passwd "$USER"
```

Hosts uses system NSS configuration; ahosts returns address-family-aware results. The passwd query prints the current user's account record, not password contents. Do not publish full account records unnecessarily.

### Compare system and DNS resolution

```bash
getent hosts app.test
dig app.test A
```

A lab name in `/etc/hosts` may resolve through getent while dig reports no DNS record. That difference is expected because the tools consult different sources. Do not assume it means a tool is broken.

**Troubleshooting:** inspect the relevant line in `/etc/hosts` and the `hosts:` configuration in `/etc/nsswitch.conf` if you administer the machine. A missing result has a nonzero exit status; it can reflect absent records or service failures. Avoid dumping unrelated identity databases.

**Cleanup:** these commands make no configuration changes. Local hosts entries you deliberately added for another lab should be removed individually when no longer required.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run libc-bin` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://manpages.debian.org/stable/manpages/getent.1.en.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
