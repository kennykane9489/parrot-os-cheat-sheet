# Netcat, SSH and temporary file sharing

[Home](../README.md) · [Quick reference](quick-reference.md) · [Troubleshooting](troubleshooting.md)

**Impact:** LISTEN, NETWORK and WRITE. SSH key generation creates private key material.

### OpenBSD Netcat — simple TCP diagnostics

Check `nc -h`; implementations differ. For the commands below install/select `netcat-openbsd` and confirm its help.

Terminal A:

```bash
nc -l 127.0.0.1 2222
```

Terminal B:

```bash
nc 127.0.0.1 2222
```

Typed lines appear at the other end. This loopback example stays local. For lab-host transfers, the receiver can run:

```bash
nc -l 192.168.56.10 2222 > received.txt
```

Sender:

```bash
nc -N 192.168.56.10 2222 < original.txt
```

`-N` closes the network write side after stdin EOF in OpenBSD nc. Verify `sha256sum` on each side. Netcat has no built-in authentication or encryption; prefer SSH for private files. The original `< filename >` trailing redirection is a syntax error. `-k` keeps a listener serving connections; it does not define transfer boundaries or verify files.

### SSH / scp — encrypted administration and copying

```bash
ssh labuser@192.168.56.20
scp ./notes.txt labuser@192.168.56.20:~/
ssh-keygen -t ed25519
```

Install client package `openssh-client` if needed. Verify server host-key fingerprints through a trusted channel. Key generation can prompt before overwriting an existing key; choose a new filename if necessary and protect it with a passphrase. Server installation is separate and exposes a service.

### Python HTTP server — temporary downloads

Share only a dedicated directory:

```bash
mkdir -p ~/lab-share
python3 -m http.server 8000 --bind 127.0.0.1 --directory ~/lab-share
```

Browse `http://127.0.0.1:8000/`. For another authorized lab machine, bind explicitly to your lab-interface IP. Stop with Ctrl+C. This is unencrypted, unauthenticated file serving; directory contents may be listed. Port 8000 avoids root privileges. Do not serve your entire home directory.
