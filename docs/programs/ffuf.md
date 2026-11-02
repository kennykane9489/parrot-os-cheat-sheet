# ffuf

[All programs](README.md) · [Repository home](../../README.md)

Replace a FUZZ marker in HTTP requests with wordlist entries, with calibration, rate limits and structured output.

## Install and verify

```bash
sudo apt update
apt policy ffuf
sudo apt install ffuf
ffuf -V
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK and WRITE. With the local HTTP lab running:

```bash
printf '%s\n' hello.txt missing.txt robots.txt > lab-paths.txt
ffuf -u http://127.0.0.1:8000/FUZZ -w lab-paths.txt -t 2 -rate 5 -ac -of json -o ffuf-lab.json
```

`FUZZ` is substituted once per word. `-t` controls concurrent workers; `-rate` limits requests per second. `-ac` calibrates filtering; `-of json` chooses format and `-o` saves a report.

### Examine positives

```bash
jq '.results[] | {url, status, length}' ffuf-lab.json
curl -i http://127.0.0.1:8000/hello.txt
```

Validate responses independently; calibration can hide useful results. `jq` is optional and separately installed. `-mc` chooses matching status codes and `-fc` excludes codes; decide based on the application's real negative response.

### Test a query parameter

```bash
ffuf -u 'http://127.0.0.1:8000/search?q=FUZZ' -w terms.txt -t 2 -rate 5
```

This needs a real local application implementing `/search` and a short terms.txt. The static Python file server does not implement search. Quote URLs so the shell does not interpret query delimiters.

**Troubleshooting:** inspect a known valid and a known invalid request before tuning filters. Login redirects, CSRF state and expiring cookies can invalidate results. Never publish real tokens inside saved commands.

**Cleanup:** stop the run, close the test server when finished, and redact/archive results as appropriate.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run ffuf` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/ffuf/ffuf). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
