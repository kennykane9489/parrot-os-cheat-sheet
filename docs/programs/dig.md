# dig

[All programs](README.md) · [Repository home](../../README.md)

Query DNS records and inspect resolver answers. Both tools are supplied by BIND utilities on typical Debian-based installations.

## Install and verify

```bash
sudo apt update
apt policy dnsutils
sudo apt install dnsutils
dig -version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK. Query the configured resolver:

```bash
dig example.com A
dig example.com AAAA +short
dig example.com MX
dig -x 127.0.0.1
```

Read the response status, ANSWER section and queried SERVER. `+short` hides diagnostic context; use full output for failures. A and AAAA are IPv4/IPv6 addresses; MX describes mail routing. Reverse lookup may return no name.

### Compare a specific resolver

```bash
dig @192.168.56.1 lab.test A
```

Only use a resolver you control or are authorized to query. The example lab zone must exist there. `NXDOMAIN` means that resolver reports the name absent; `SERVFAIL` indicates a resolution failure, not necessarily absence. A timeout can be network or service trouble.

**Troubleshooting:** dig queries DNS directly and may differ from applications using hosts files or other name services. Compare with `getent hosts NAME`. Avoid assuming a CDN answer is the origin server.

**Cleanup:** no local settings changed. Queries can be logged by your resolver.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run dnsutils` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://bind9.readthedocs.io/en/latest/manpages.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
