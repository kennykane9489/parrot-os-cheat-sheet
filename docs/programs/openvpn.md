# OpenVPN

[All programs](README.md) · [Repository home](../../README.md)

Connect to a trusted VPN provider or lab using its issued profile and credentials.

## Install and verify

```bash
sudo apt update
apt policy openvpn
sudo apt install openvpn
openvpn --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK and CHANGE to routing/DNS integration. Use a fresh configuration for the correct lab/region.

```bash
sudo openvpn --config ~/Downloads/lab.ovpn
```

Keep the terminal open. A successful initialization message indicates the tunnel initialized; it does not guarantee the target is running. Configuration files can reference scripts, keys and credentials, so obtain them from the provider and do not share them publicly.

### Verify the route in another terminal

```bash
ip -br address
ip route get 10.10.10.10
ping -c 3 10.10.10.10
```

Replace the IP with your authorized target. Read which interface the route selects. Ping may be blocked; also test the known service. Avoid simultaneous duplicate VPNs and overlapping host-only/NAT subnets.

### When it fails

Authentication errors need valid provider credentials/profile. Route conflicts require inspecting both VPN and local subnet routes. DNS failures need checking the provider's supported resolver integration; OpenVPN itself does not always apply all DNS settings on every Linux setup. If logs specifically mention IPv6, diagnose that error rather than applying a blanket sysctl recipe.

**Cleanup:** Ctrl+C in the OpenVPN terminal closes this session; verify routes/connection state afterward. Remove unneeded profiles securely according to your provider’s credential handling. Do not publish configuration or logs containing keys/tokens.

**Troubleshooting:** distinguish authentication, route and resolver failures from the actual logs; initialization alone does not prove the target is reachable.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run openvpn` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
