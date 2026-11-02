# smbclient

[All programs](README.md) · [Repository home](../../README.md)

Browse authorized Windows/Samba shares with an interactive client and prompted credentials.

## Install and verify

```bash
sudo apt update
apt policy smbclient
sudo apt install smbclient
smbclient --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK; downloads WRITE locally, uploads WRITE remotely. Prerequisites: an actual lab SMB server, a named share and a permitted test account.

```bash
smbclient -L 192.168.56.20 -U labuser
smbclient //192.168.56.20/Data -U labuser
```

Replace host, account and Data share with values provided by your lab. Enter the password at the prompt. Listing shares is not user enumeration. For a deliberately guest-enabled lab, `-N` skips the password prompt; it does not bypass authentication.

### Inside the SMB prompt

```text
help
ls
cd documents
lcd /tmp
get example.txt
quit
```

Use only a folder/file that actually exists. `cd` changes the remote location; `lcd` changes the local download directory. `get` copies a remote file locally; `put` uploads and changes the server. A read-only exercise needs no upload.

### Domain account

```bash
smbclient -L 192.168.56.20 -U 'LAB/labuser'
```

Your server determines accepted domain/workgroup naming. Prefer a prompted password rather than embedding it in the account string.

**Troubleshooting:** access denied can reflect credentials or share/filesystem permissions. A visible share may still be unreadable. Check server policy rather than forcing SMB1 or weakening authentication.

**Cleanup:** quit the client and remove only the authorized test downloads you no longer need; do not delete remote files as local cleanup.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run smbclient` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
