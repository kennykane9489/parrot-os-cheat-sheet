# SQLmap — test suspected SQL injection

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** NETWORK; active SQL injection testing can affect application behavior.

Install if available: `sudo apt install sqlmap`. Supply a raw request captured from your test app, not an HTML response.

```bash
sqlmap -h
sqlmap -r search.req -p q --level=1 --risk=1 --threads=1
```

Replace `q` with the exact parameter under test. Use `--force-ssl` only when the request must use HTTPS; `--force-ssl461` is invalid. Interactive prompts help you review behavior; `--batch` automatically selects default answers. Lowest risk settings are still active tests and do not guarantee no side effects. This starting workflow validates a suspected issue without requesting database dumps or OS access.
