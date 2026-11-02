# Hydra

[All programs](README.md) · [Repository home](../../README.md)

Test a small, agreed set of login attempts against a designated training account. Different protocols require different modules.

## Install and verify

```bash
sudo apt update
apt policy hydra
sudo apt install hydra
hydra -h
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** NETWORK; can trigger lockouts/audit events. Use a disposable local SSH service with a labuser account you created for training and an agreed three-attempt allowance. Do not use your daily account.

```bash
hydra -U ssh
printf '%s\n' wrong-demo-1 wrong-demo-2 LAB_ONLY_CHANGE_ME > lab-passwords.txt
hydra -l labuser -P lab-passwords.txt -t 1 -f ssh://127.0.0.1
```

The example does not create an SSH server/account. Replace the final dummy candidate with the known disposable lab password only in your private test file. `-l` is one user; `-P` is a password file; `-t 1` limits workers; `-f` stops after success on the host. A service may enforce lockouts after even fewer attempts; confirm first.

### HTML form preparation

```bash
hydra -U http-post-form
```

Before writing a form test, capture the actual action path, POST fields, cookies/CSRF handling and reliable failure/success marker. Placeholders are case-sensitive `^USER^` and `^PASS^`; `^user^` is incorrect. HTTP Basic Auth and an HTML form are different protocols/workflows. Do not substitute a generic form string into a live service.

**Troubleshooting:** zero successes can reflect protocol mismatch, account lockout, dynamic CSRF or incorrect markers rather than wrong candidates. A reported hit needs a single manual confirmation using the designated account.

**Cleanup:** remove private lab candidate/result files, end the dedicated SSH test service if you started it, and remove/reset the disposable account according to your lab setup. Do not retain a known-password file in Git.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run hydra` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://github.com/vanhauser-thc/thc-hydra). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
