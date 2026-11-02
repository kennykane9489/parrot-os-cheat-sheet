# Git

[All programs](README.md) · [Repository home](../../README.md)

Track file history, inspect changes, and collaborate with a remote repository.

## Install and verify

```bash
sudo apt update
apt policy git
sudo apt install git
git --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** WRITE locally; NETWORK on clone/fetch/push. Start in a new directory rather than an unrelated project.

### Clone this reference

```bash
git clone https://github.com/kennykane9489/parrot-os-cheat-sheet.git
cd parrot-os-cheat-sheet
git status
git log -5 --oneline
```

Clone creates a directory. Status identifies uncommitted changes; log shows recent commits. A clone downloads code; it does not make that code trustworthy to execute.

### Make a small documentation change

```bash
git switch -c docs/my-notes
git diff
git add docs/quick-reference.md
git diff --cached
git commit -m "Clarify quick reference"
```

Edit the file before staging. `--cached` reviews exactly what will be committed. Configure a commit name/email if prompted, using values you are comfortable exposing in public history.

### Update without hiding conflicts

```bash
git fetch origin
git status
git diff HEAD..origin/main
```

Fetch updates remote-tracking data without merging it. Review before choosing a merge/rebase. Publishing your branch with `git push -u origin docs/my-notes` needs authenticated write access.

**Troubleshooting:** authentication failures need a credential helper, SSH key or supported token method; never put tokens in a public URL. Preserve local changes before updating. Avoid `reset --hard` or forced pushes as routine fixes. To leave a branch, use `git switch main`; keep your work committed or safely saved first.

**Cleanup:** return to main only after committing/saving work. Remove a local test branch only after confirming its changes are preserved; deleting a working directory is not required.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run git` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://git-scm.com/docs/gittutorial). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
