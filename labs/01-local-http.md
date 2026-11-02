# Lab 1: Local HTTP inspection

[Lab index](README.md) · [Troubleshooting](../docs/troubleshooting.md)

**Goal:** explain a listener, request, HTTP status and port state. **Impact:** WRITE, LISTEN and NETWORK, all on loopback. No sudo required. Requires Python 3 and curl; Nmap is optional. Confirm with `python3 --version` and `curl --version`.

## 1. Setup and serve — terminal A

```bash
lab_dir=$(mktemp -d /tmp/parrot-http.XXXXXX)
printf 'hello from lab
' > "$lab_dir/hello.txt"
printf 'Lab directory: %s
' "$lab_dir"
python3 -m http.server 8000 --bind 127.0.0.1 --directory "$lab_dir"
```

Keep terminal A open. If port 8000 is occupied, choose 8001 in this server command and all requests below. Loopback binding keeps this server off your LAN.

## 2. Inspect — terminal B

```bash
curl -i http://127.0.0.1:8000/hello.txt
curl -i http://127.0.0.1:8000/missing.txt
ss -tuln
```

Expected: the first response is `200` with `hello from lab`; the second is `404`. `ss` should include a listener at `127.0.0.1:8000`. Headers/version strings vary. Optional:

```bash
nmap -sT -p 8000 127.0.0.1
```

Expected: TCP port 8000 is open while the server runs. A port label alone does not identify the actual software.

## 3. Cleanup — terminal A

Press Ctrl+C to stop the server. Then, in the same terminal where `lab_dir` was set:

```bash
rm -- "$lab_dir/hello.txt"
rmdir -- "$lab_dir"
unset lab_dir
```

Cleanup removes only the known file and empty temporary directory. If you closed terminal A, use its printed directory path after verifying its contents; do not guess it. Repeating curl should now fail unless another process starts a listener on that port.

## Check your understanding

1. Why bind to 127.0.0.1? 2. Does a 404 mean the server is offline? 3. Why can an open port's service label be misleading?

<details>
<summary>Answers</summary>

1. It restricts listening to this machine's loopback interface.
2. No. The server answered but did not find that resource.
3. Nmap can label the port from its database without identifying the running application.

</details>
