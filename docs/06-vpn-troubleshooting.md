# OpenVPN and HTB troubleshooting

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** NETWORK and CHANGE; VPN changes routing. Diagnostics are INSPECT.

OpenVPN establishes a tunnel using a provider-issued configuration. Treat `.ovpn` files as trusted configuration, since they can reference credentials or scripts.

```bash
sudo apt install openvpn
sudo openvpn --config ~/Downloads/lab.ovpn
```

Keep that terminal open. Look for `Initialization Sequence Completed`; in another terminal check:

```bash
ip -br address
ip route get 10.10.10.10
ping -c 3 10.10.10.10
```

A target may block ping; a failed ping alone does not prove the tunnel is broken. Check the target is running, the correct lab/VPN region is selected, and the target route uses the tunnel. Avoid overlapping VPN sessions and local subnets. Capture the specific error rather than applying unrelated fixes.

The old sysctl recipe is not a general HTB repair. `disable_ipv6=0` ENABLES IPv6; it does not disable it. Inspect current state if logs mention IPv6:

```bash
sysctl net.ipv6.conf.all.disable_ipv6
sysctl net.ipv6.conf.default.disable_ipv6
sysctl net.ipv6.conf.lo.disable_ipv6
```

Do not change global IPv6 settings without an error that justifies it. For persistent, deliberate sysctl changes, use a named file under `/etc/sysctl.d/` and document how to undo it.
