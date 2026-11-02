# nslookup

[All programs](README.md) · [Repository home](../../README.md)

Query DNS records and inspect resolver answers. Both tools are supplied by BIND utilities on typical Debian-based installations.

## Install and verify

```bash
sudo apt update
apt policy dnsutils
sudo apt install dnsutils
nslookup -version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK. Start with a single name:

```bash
nslookup example.com
nslookup -type=MX example.com
nslookup example.com 192.168.56.1
```

The last command chooses the example lab resolver; replace it with one you use legitimately. Read which server answered and whether the result is authoritative. “Non-authoritative” commonly means a recursive resolver answered from cached/forwarded data, not that the result is invalid.

### Interactive session

```text
nslookup
> set type=AAAA
> example.com
> exit
```

Run `nslookup` in your terminal, then enter only the text after each `>` prompt. It switches query type for subsequent requests.

**Troubleshooting:** NXDOMAIN, SERVFAIL and timeouts are different conditions. Compare a working name, the configured resolver and system resolution through getent. Do not replace system DNS just because one record type has no answer.

**Cleanup:** exit the interactive shell. These queries do not alter resolver configuration.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run dnsutils` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://bind9.readthedocs.io/en/latest/manpages.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
