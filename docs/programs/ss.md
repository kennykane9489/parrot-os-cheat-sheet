# ss

[All programs](README.md) · [Repository home](../../README.md)

Identify listening ports, active sockets and the processes that own them. Part of iproute2.

## Install and verify

```bash
sudo apt update
apt policy iproute2
sudo apt install iproute2
ss -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT. Use process visibility only when needed; sudo can reveal other users' sockets.

```bash
ss -tuln
sudo ss -tulpn
ss -tn state established
```

`t` TCP; `u` UDP; `l` listening; `n` numeric addresses; `p` processes. UDP does not perform TCP-style listening handshakes even though it appears in combined output.

### Find the local HTTP server

```bash
ss -ltn 'sport = :8000'
```

After starting the HTTP lab, expect a listener at `127.0.0.1:8000`. A listener at `0.0.0.0:8000` accepts on all IPv4 interfaces, subject to firewall/routing. `127.0.0.1` is loopback-only. IPv6 `::` binding behavior can depend on system socket settings.

### Determine a port conflict

```bash
sudo ss -ltnp 'sport = :8000'
```

Read the PID/process before deciding whether to stop it. Do not kill a random service merely because it occupies your desired lab port; choosing another port is often easier.

**Troubleshooting:** no listener may mean the server exited or bound another address/port. A listener proves only local socket state, not remote reachability or authentication. Process details may be hidden without privileges.

**Cleanup:** inspection leaves sockets unchanged. Stop only your own lab server in its terminal.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run iproute2` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://man7.org/linux/man-pages/man8/ss.8.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
