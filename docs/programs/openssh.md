# OpenSSH / ssh and scp

[All programs](README.md) · [Repository home](../../README.md)

Log in and copy files over encrypted authenticated connections. Client installation does not install an SSH server.

## Install and verify

```bash
sudo apt update
apt policy openssh-client
sudo apt install openssh-client
ssh -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK; scp WRITES destination files. Prerequisites: an authorized lab SSH server/account and a trusted way to verify its host-key fingerprint.

```bash
ssh labuser@192.168.56.20
```

Verify the fingerprint before accepting a first connection. A changed host-key warning can indicate reinstall, wrong host or interception; investigate rather than deleting known_hosts blindly. Enter the account's password when requested.

### Keys and copies

```bash
ssh-keygen -t ed25519 -f ~/.ssh/parrot_lab_ed25519
ssh -i ~/.ssh/parrot_lab_ed25519 labuser@192.168.56.20
scp ./notes.txt labuser@192.168.56.20:~/
scp labuser@192.168.56.20:~/example.txt ./example-copy.txt
```

Use a passphrase and decline overwriting existing keys. Public-key authentication requires provisioning the `.pub` key on the server first; key creation alone does not grant access. Never share/commit the private key. scp paths can overwrite files; choose fresh destinations.

### Ports and diagnosis

```bash
ssh -p 2222 labuser@192.168.56.20
scp -P 2222 ./notes.txt labuser@192.168.56.20:~/
```

SSH uses lowercase `-p`; scp uses uppercase `-P` for ports. `ssh -v` provides diagnostics; redact before sharing.

**Troubleshooting:** refused means no listener/rejection; timeout suggests routing/filtering; permission denied concerns authentication/authorization. Starting a server is a separate explicit administration task.

**Cleanup:** use exit in the remote shell. Remove unused lab public keys from authorized_keys deliberately, then retire the corresponding private key after confirming it is no longer needed.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run openssh-client` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://man.openbsd.org/ssh). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
