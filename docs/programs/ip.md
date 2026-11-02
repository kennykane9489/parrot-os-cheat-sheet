# ip

[All programs](README.md) · [Repository home](../../README.md)

Inspect addresses, links, neighbors and routes using the modern iproute2 suite.

## Install and verify

```bash
sudo apt update
apt policy iproute2
sudo apt install iproute2
ip -Version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT in this guide. Other ip commands can disconnect the machine or alter routing.

```bash
ip -br address
ip link show
ip route
ip -6 route
ip neigh
```

Brief address output associates interfaces with addresses. Link state does not prove Internet access. IPv4 and IPv6 have separate routing tables; a default route points to the gateway used when no more-specific route matches.

### Troubleshoot a VPN target

```bash
ip route get 10.10.10.10
```

Replace the address with your lab target. Read the selected `dev`, source address and optional gateway. A VPN-lab target should normally route through the expected tunnel. This is a route lookup, not a reachability probe.

### Inspect one actual interface

```bash
ip address show dev lo
ip -s link show dev lo
```

`lo` exists on normal Linux systems. Use the name from your own output for physical/tunnel interfaces. `-s` shows packet counters; drops/errors can guide further diagnosis.

**Troubleshooting:** names such as enp0s3, wlp2s0 and tun0 vary. An IP route command failing with “network unreachable” identifies a local routing problem. Do not add arbitrary default routes while a remote session depends on the connection.

**Cleanup:** read-only commands require none.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run iproute2` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://man7.org/linux/man-pages/man8/ip.8.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
