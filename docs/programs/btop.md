# btop

[All programs](README.md) · [Repository home](../../README.md)

Monitor CPU, memory, disks, network rates and processes interactively.

## Install and verify

```bash
sudo apt update
apt policy btop
sudo apt install btop
btop --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT during viewing; process controls can terminate programs. Run as your normal user first.

```bash
btop
```

Use the on-screen help/menu for keys supported by your build. `q` quits. CPU percentages and memory figures need context: cached memory is not automatically wasted, and a momentary spike does not prove a fault.

### Practical diagnosis

1. Note idle CPU/memory before starting your local lab tool.
2. Run a known benign task and watch its process and resource changes.
3. Compare sustained behavior rather than judging one refresh.
4. Quit btop and inspect application logs if resource use stays unexpectedly high.

A process may use multiple CPU cores, so percentages must be interpreted using the interface's selected normalization. Network rate graphs reflect local interface counters, not application attribution by themselves.

### Avoid accidental termination

If selecting a process exposes signal/kill controls, read its PID/name and save work before taking action. Prefer stopping your own foreground tool from its original terminal rather than force-killing it in a monitor.

**Troubleshooting:** display issues can reflect unsupported terminal color/Unicode settings, limited window size or permissions for optional sensors. Open the menu/help and choose a compatible theme; installing a new GPU driver is not a generic fix.

**Cleanup:** q exits monitoring; it does not stop the processes you were observing. Close any lab process separately.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run btop` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/aristocratos/btop). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
