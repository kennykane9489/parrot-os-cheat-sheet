# Wget

[All programs](README.md) · [Repository home](../../README.md)

Download a resource to a local file with clear filename and timeout controls.

## Install and verify

```bash
sudo apt update
apt policy wget
sudo apt install wget
wget --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK and WRITE. Run the local HTTP lab and download its harmless text file:

```bash
wget --timeout=15 --tries=1 -O wget-hello.txt http://127.0.0.1:8000/hello.txt
cat wget-hello.txt
```

`-O` sets the destination and can truncate/overwrite it; do not point it at an important file. Check that the body is expected before executing or trusting any download.

### Inspect server response

```bash
wget --server-response --spider http://127.0.0.1:8000/hello.txt
```

Spider checks availability without deliberately saving the resource as a normal download. Server behavior varies; read the method/status output. A successful download does not authenticate a publisher by itself.

### Resume a large known download

`wget -c URL` attempts continuation when the server supports it. Use this only for the same resource; if the remote file changed, verify the final checksum. Do not run recursive mirroring against a site without considering scope, traffic and ownership.

**Troubleshooting:** a downloaded HTML error page is not the expected executable/archive. Check status, filename and publisher checksum. Certificate errors should be fixed through trust/time/name configuration, not bypassed globally.

**Cleanup:** remove `wget-hello.txt` if it was generated solely for this example.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run wget` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.gnu.org/software/wget/manual/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
