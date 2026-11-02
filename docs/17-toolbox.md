# Useful additions

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** Mixed; inspect each command. Capture tools observe traffic and may require privileges.

| Program | Install/check | Start here | Why use it |
|---|---|---|---|
| Wireshark | `apt policy wireshark` | Open GUI, choose lab interface, start/stop capture. | Inspect DNS, TCP and HTTP traffic visually; avoid running the entire GUI as root. |
| tcpdump | `sudo apt install tcpdump` | `sudo tcpdump -i lo -nn -c 20 'tcp port 8000'` | Capture 20 matching loopback packets; change interface intentionally. |
| tshark | `apt policy tshark` | `tshark -r capture.pcapng -Y dns` | Read saved captures with a Wireshark display filter. |
| jq | `sudo apt install jq` | `jq . results.json` | Format/inspect JSON. |
| ripgrep | `sudo apt install ripgrep` | `rg -n 'ERROR' logs/` | Fast text search; binary/hidden files are skipped by default. |
| tmux | `sudo apt install tmux` | `tmux new -s lab` | Keep terminal sessions; Ctrl+B then D detaches, `tmux attach -t lab` resumes. |
| btop | `apt policy btop` | `btop` | Interactive resource monitoring; q quits. |
| OpenSSL | `apt policy openssl` | `openssl x509 -in certificate.pem -noout -dates -subject -issuer` | Inspect a saved PEM certificate without making a network request. |
| OWASP ZAP | Use official installation instructions below. | Start with manual proxy browsing of a lab. | Web-testing proxy; passive observations differ from active scans. |
| ShellCheck | `sudo apt install shellcheck` | `shellcheck script.sh` | Catch common shell-script mistakes before running a script. |

`tcpdump` capture filters and Wireshark/tshark display filters are different languages. Packet files, saved HTTP requests and output logs may contain credentials; limit access and redact before sharing.
