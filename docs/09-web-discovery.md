# Content discovery: Gobuster, ffuf, Wfuzz, Nikto

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** NETWORK and WRITE; discovery sends many requests and saves results.

These tools send requests. Use small lists and conservative concurrency first. A 200 response may be a custom error page; verify a random nonexistent path as a baseline.

### Wordlists / SecLists

SecLists supplies curated testing lists, not a scanning engine. Check `apt policy seclists`; inspect installed paths with `dpkg -L seclists`. Paths vary; do not assume `/opt/SecLists` exists.

For a reproducible tiny local test list:

```bash
printf '%s\n' admin login robots.txt > paths.txt
```

### Gobuster — discover paths, DNS names and virtual hosts

Install if available: `sudo apt install gobuster`. Modern releases use subcommands, not old `-m dir` syntax.

```bash
gobuster dir --help
gobuster dir -u http://127.0.0.1:8000 -w paths.txt -t 5 -o gobuster.txt
gobuster vhost --help
gobuster vhost -u http://app.test --append-domain -w subdomains.txt -t 5
```

The vhost example needs a lab hostname resolving to your server and a list containing labels such as `dev`, not full domains when `--append-domain` is used. DNS mode flags changed across versions: inspect `gobuster dns --help` before choosing `-d` or `--domain`/`-do`. `-x php,txt` adds extensions in directory mode. Status/length filtering is version-specific; don't copy an obsolete global option table.

### ffuf — flexible HTTP fuzzing

Install if available: `sudo apt install ffuf`.

```bash
ffuf -u http://127.0.0.1:8000/FUZZ -w paths.txt -t 5 -rate 10 -ac -of json -o ffuf.json
```

`FUZZ` is replaced by each word; `-t` controls concurrent workers, `-rate` caps requests per second, `-ac` attempts automatic filtering. Verify filtered results manually; calibration can hide useful responses.

### Wfuzz — substitute payloads in HTTP requests

Install if available: `sudo apt install wfuzz`.

```bash
wfuzz -w paths.txt 'http://127.0.0.1:8000/FUZZ'
wfuzz -z range,0-10 'http://127.0.0.1:8000/item?id=FUZZ'
```

Use `--hc 404` only when 404 is a reliable negative signal. `--hl N` hides responses with N lines; an old hardcoded `--hl 97` is not universal. HTTPS support can depend on the packaged PycURL build.

### Nikto — web-server checks

Install if available: `sudo apt install nikto`.

```bash
nikto -Help
nikto -h http://127.0.0.1:8000 -o nikto.txt -Format txt
```

Checks potentially dangerous files, known server issues and configuration clues. It is noisy and findings need confirmation. Nikto is not a general operating-system detection tool. Launching a packaged executable avoids assuming `nikto.pl` is in your current directory.
