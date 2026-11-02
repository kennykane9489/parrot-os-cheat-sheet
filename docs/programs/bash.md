# Bash and core shell commands

[All programs](README.md) · [Repository home](../../README.md)

Navigate folders, create files and understand shell operators before combining tool commands. cd is a shell builtin; many file utilities come from coreutils.

## Install and verify

```bash
sudo apt update
apt policy bash coreutils
sudo apt install bash coreutils
bash --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT, WRITE or REMOVE depending on command. Run in a fresh temporary directory for practice, not your home root.

```bash
shell_lab=$(mktemp -d /tmp/parrot-shell.XXXXXX)
cd "$shell_lab"
pwd
mkdir notes
printf 'hello\n' > notes/example.txt
ls -lah notes
cat notes/example.txt
```

pwd prints the current directory. ls lists entries; `-a` includes hidden entries. mkdir creates a directory. printf writes text and `>` overwrites the destination. `>>` appends. Quoting variable expansions preserves spaces and prevents unintended globbing.

### Operators and paths

`&&` runs the right command only after success; a pipe `|` sends output into another program. `~` expands to your home in suitable shell contexts. Relative paths depend on pwd. A leading `#` begins a comment outside quoted strings; prompt markers in tutorials are not commands.

### Inspect permissions

```bash
id
ls -l notes/example.txt
```

Owner/group/mode govern local access alongside ACLs and other policy. sudo elevates privileges; it is not a generic fix for every error. Do not use chmod 777 as a default repair.

### Cleanup in the same terminal

```bash
rm -- notes/example.txt
rmdir notes
cd ~
rmdir -- "$shell_lab"
unset shell_lab
```

rm deletes files; rmdir removes empty directories. `--` ends option parsing. Avoid recursive deletion until you have inspected the exact target and consequences.

**Troubleshooting:** check pwd before relative paths, quote expansions, and read the exact permission/path error. Do not retry a mistaken deletion with sudo.

**Cleanup:** the commands above remove only the known file and empty temporary directories.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run bash coreutils` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.gnu.org/software/bash/manual/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
