# OpenSSL

[All programs](README.md) · [Repository home](../../README.md)

Inspect certificates and create local test cryptographic material without assuming that an arbitrary certificate is trusted.

## Install and verify

```bash
sudo apt update
apt policy openssl
sudo apt install openssl
openssl version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT for reads; key/certificate creation WRITES sensitive files.

```bash
openssl x509 -in certificate.pem -noout -subject -issuer -dates -fingerprint -sha256
```

Use an actual PEM certificate. These fields describe identity claims/validity dates and a fingerprint, not a complete trust decision. A certificate can be well-formed and still be untrusted or for the wrong host.

### Create a loopback-only test certificate

```bash
umask 077
openssl req -x509 -newkey rsa:2048 -sha256 -days 1 -keyout lab-key.pem -out lab-cert.pem -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost,IP:127.0.0.1'
```

The command prompts for a private-key passphrase. Keep it private; a self-signed certificate is not automatically trusted by browsers. `umask 077` restricts new-file permissions in this shell; it remains in effect afterward. Use a separate test terminal if you do not want to change the original shell's mask.

### Inspect your generated certificate

```bash
openssl x509 -in lab-cert.pem -noout -text
openssl verify -CAfile lab-cert.pem lab-cert.pem
```

The verification trusts that file explicitly for this command; it does not install a system CA or establish external identity.

**Troubleshooting:** PEM parse failures may mean wrong file type or an HTML error page. TLS client failures also depend on chain, hostname and system time; do not disable validation globally.

**Cleanup:** remove only the lab certificate/private key after ensuring no test server needs them. Never commit private keys.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run openssl` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://docs.openssl.org/master/man1/openssl/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
