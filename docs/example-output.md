# Reading command output

[Home](../README.md) · [Troubleshooting](troubleshooting.md)

All output on this page is **illustrative**, not a captured result from your device. Exact text changes by release, locale and tool version.

## Interface state

Command: `ip -br address` (INSPECT)

```text
lo               UNKNOWN        127.0.0.1/8 ::1/128
eth0             UP             192.168.56.10/24
```

`lo` is loopback. `UP` indicates interface state, not guaranteed Internet access. An IPv4 address is not proof of a correct default route. `UNKNOWN` on loopback is common.

## Port state

Command: `nmap -sT -p 8000 127.0.0.1` (NETWORK)

```text
PORT     STATE SERVICE
8000/tcp open  http-alt
```

`open` means a TCP connection was accepted. The service column may come from a port-name database; it does not establish the running software. Use appropriate version probes or inspect the listener. `closed` means no service accepted that probe. `filtered` means Nmap could not establish open/closed due to filtering or missing responses.

## HTTP response

Command: `curl -i http://127.0.0.1:8000/hello.txt` (NETWORK)

```text
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.x
Content-type: text/plain
Content-Length: 15

hello from lab
```

The lab file is 15 bytes including a newline. `200` indicates HTTP success, not security. A missing path commonly returns `404`; some applications use custom error pages with `200`. A server header can be changed or misleading.

## Connection refused

```text
curl: (7) Failed to connect to 127.0.0.1 port 8000
```

Check for the listener and the correct port. This differs from a timeout, where traffic may be dropped or a host may not respond.

## DNS lookup failure

```text
curl: (6) Could not resolve host: example.com
```

Name resolution failed before an HTTP connection could be established. Test resolver/network settings; changing HTTP headers will not repair DNS.

## Checksums

Two identical `sha256sum` values are strong evidence that two files have the same bytes. They do not establish whether a download is trustworthy; compare against an authenticated publisher checksum/signature when authenticity matters.
