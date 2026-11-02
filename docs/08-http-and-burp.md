# curl and Burp Suite — understand HTTP

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** NETWORK and WRITE; saving responses writes local files.

### curl — requests without a GUI

Install: `sudo apt install curl`.

```bash
curl -I http://127.0.0.1:8000/             # HEAD request; some servers handle it differently from GET
curl -i http://127.0.0.1:8000/             # GET with response headers
curl -L --max-redirs 5 http://127.0.0.1:8000/ # Follow redirects with a limit
curl -o response.html http://127.0.0.1:8000/ # Save body
```

Keep TLS validation enabled. `-k` bypasses certificate validation; it does not fix trust or TLS configuration.

### Burp Suite Community — intercept and replay browser requests

Use the official Community installer or the repository package if available (`apt policy burpsuite`). Professional requires a legitimate license. The old cracked installer/keygen link is removed.

1. Launch Burp, create a temporary project if prompted, and open Proxy's built-in browser.
2. Browse your lab application. Proxy → HTTP history records requests. Intercept toggles whether requests pause.
3. Send a relevant request to Repeater. Change one input, send it and compare status, body and timing.
4. To test with sqlmap, save/copy the actual raw HTTP request to a text file, including request line, Host header, headers, blank line and body.
5. If using an external browser, configure its proxy and install Burp's CA only in a dedicated test profile. Burp's built-in browser reduces setup work.

Adding `url=file:///etc/passwd` does not make Burp read a remote file. It only sends a parameter. A server would need a vulnerable file-handling/SSRF behavior, appropriate scheme support and permissions. A POST body also needs correct content type and request framing. Use a lab's harmless marker file to validate behavior.
