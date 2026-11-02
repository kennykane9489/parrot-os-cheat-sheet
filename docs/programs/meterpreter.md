# Meterpreter sessions

[All programs](README.md) · [Repository home](../../README.md)

Interact with an existing authorized lab session using platform-supported commands. Meterpreter is a payload/session type, not an independent desktop package.

## Install and verify

```bash
sudo apt update
apt policy metasploit-framework
sudo apt install metasploit-framework
msfconsole --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT for inventory; other session commands can WRITE, capture data or change the target. Prerequisite: an existing session deliberately established in a controlled lab; this page does not assume an arbitrary target is accessible.

### Select the session in msfconsole

```text
sessions -l
sessions -i 1
```

Replace 1 with the actual ID you are permitted to use. Inside the Meterpreter prompt:

```text
help
sysinfo
getuid
pwd
ls
ps
```

Commands depend on OS, extensions and session type. Help is authoritative for that session. sysinfo and getuid identify environment/current identity; they do not elevate privileges.

### Understand local versus remote paths

```text
lpwd
lls
pwd
ls
background
```

`lpwd`/`lls` refer to the operator's machine; pwd/ls refer to the target. Background returns to msfconsole without terminating the session. To resume, use sessions -i with its ID.

### End the session

```text
exit
```

Run exit in Meterpreter to end that session; confirm in msfconsole with sessions -l. Closing a client does not guarantee removal of arbitrary artifacts from a target; restore your disposable lab snapshot as needed.

**Troubleshooting:** missing commands reflect session/platform capabilities. An unexpected account or host means stop and verify the correct lab session. Avoid keylogging, webcam access, credential dumping, log clearing and timestamp alteration for ordinary inventory.

**Cleanup:** exit the intended lab session, confirm it is gone from sessions -l, and restore disposable target state if the wider lab created artifacts.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run metasploit-framework` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://docs.metasploit.com/docs/using-metasploit/advanced/meterpreter/meterpreter-basics.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
