# OWASP ZAP

[All programs](README.md) · [Repository home](../../README.md)

Inspect HTTP traffic and assess your own web application with a scoped proxy workflow. Passive analysis and active scans have different effects.

## Install and verify

Check whether your Parrot repositories provide a supported build:

```bash
apt policy zaproxy
```

If a candidate exists, install with `sudo apt install zaproxy` and launch `zaproxy`. Otherwise obtain the appropriate Linux package/installer from the [official ZAP download page](https://www.zaproxy.org/download/), verify its origin and follow that format's current Java/runtime instructions. Do not add another distribution's repository or assume every Linux installer bundles Java. Use the app's About dialog for its exact version.

## Use it in practice

**Impact:** NETWORK and WRITE; active scans can change application state. Use your local disposable app.

### Launch and browse

Launch ZAP from the installed desktop shortcut or its documented startup script. Choose a temporary/non-persisted session if appropriate for a first exercise. Use Manual Explore / the browser-launch workflow for your version rather than guessing proxy/CA settings.

1. Browse the local HTTP lab and request hello.txt and missing.txt.
2. Inspect the Sites tree and History to compare 200/404 responses.
3. Review passive alerts as observations requiring context; missing headers in a toy file server do not prove a broadly exploitable defect.
4. Add your own app to a named context/scope before any active testing.

### First active test

Use only an intentionally disposable application/database with explicit permission. Review scope, authentication/session handling and scan policy before launching an active scan. Do not start with an unscoped “attack everything” action or a third-party production site.

### Evidence

Save a report/session only if needed, knowing it may include requests, cookies and sensitive responses. Redact before sharing. A passing scan does not prove absence of vulnerabilities; automated coverage depends on explored routes and app state.

**Troubleshooting:** an unreachable browser may be waiting for proxy setup or an HTTPS CA configuration. Java/build requirements vary with distribution format; read the chosen official installer requirements.

**Cleanup:** stop scans, close proxy listeners/test browser and remove any external browser proxy/CA changes. Restore the disposable app/database as necessary.

## Updates and removal

Update through the same manager or upstream method used for installation. Avoid mixing distribution and source installations of the same executable. Follow the cleanup steps above before removing any files.

## Reference and compatibility

[Upstream documentation](https://www.zaproxy.org/getting-started/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
