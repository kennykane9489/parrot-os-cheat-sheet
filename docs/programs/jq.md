# jq

[All programs](README.md) · [Repository home](../../README.md)

Read, transform and validate JSON using composable filters.

## Install and verify

```bash
sudo apt update
apt policy jq
sudo apt install jq
jq --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT and WRITE when redirecting output. Start with a known local fixture.

```bash
printf '%s\n' '{"tools":[{"name":"nmap","installed":true},{"name":"ffuf","installed":false}]}' > jq-demo.json
jq . jq-demo.json
jq -r '.tools[].name' jq-demo.json
jq '.tools[] | select(.installed == true)' jq-demo.json
```

`.` pretty-prints, `[]` iterates an array, `-r` emits raw strings, and select keeps matching objects. Quote filters so shell symbols are not interpreted.

### Check a report and write a new file

```bash
jq -e '.tools | type == "array"' jq-demo.json
jq '[.tools[] | select(.installed == true)]' jq-demo.json > jq-installed.json
```

`-e` returns a useful success/failure exit status for Boolean/null results. Never redirect output to the input file directly; the shell truncates it before jq reads it. Write a new file, inspect it, then deliberately replace if needed.

**Troubleshooting:** parse errors can mean the input is HTML or newline-delimited JSON instead of the expected single document. A null result often means the field/path differs. Read a small fixture and confirm the schema.

**Cleanup:** remove the two demo JSON files if they are no longer needed; never publish reports containing tokens or personal data.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run jq` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://jqlang.org/manual/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
