# Networking, DNS and VM connections

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** INSPECT; DNS commands send NETWORK requests.

### ip, ss and NetworkManager — modern network basics

```bash
ip -br address                 # Interfaces and addresses
ip route                       # IPv4 routes/default gateway
ip -6 route                    # IPv6 routes
ip route get 10.10.10.10        # Which route/interface would reach this lab target?
ip neigh                       # Neighbor cache
ss -tuln                       # Listening TCP/UDP sockets, numeric addresses
sudo ss -tulpn                 # Include owning processes where permitted
nmcli device status            # NetworkManager device state
nmcli connection show --active # Active connections
```

Prefer `ip`/`ss` over legacy `ifconfig`, `route` and `netstat` for routine Linux administration. Interface names are not always `eth0` or `wlan0`.

### dig / nslookup — query DNS

Package commonly named `dnsutils`; verify availability first.

```bash
dig example.com A +short
dig example.com AAAA +short
dig example.com MX
nslookup example.com
getent hosts example.com       # Uses system name-service configuration, including hosts file
```

DNS answers can include multiple addresses or a CDN; they do not prove server ownership or testing permission.

| VM network | Behavior | Practical use |
|---|---|---|
| NAT | Guest outbound connections usually share host-side connectivity; inbound access typically needs forwarding. | Updates, browsing, VPN labs. |
| Bridged | Guest appears on the physical LAN with its own network identity. | When explicitly needing LAN access. |
| Host-only | Private network shared by host and attached guests; no Internet by default. | Controlled local labs. |
| Internal network / LAN segment | Attached guests communicate; host is usually excluded. | Isolated target networks. |
| Custom | Hypervisor-specific network selection/configuration. | Read that hypervisor's settings. |

An isolated target with a second NAT adapter can regain outside access. Check every adapter.
