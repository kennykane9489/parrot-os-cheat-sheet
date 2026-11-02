# ShellCheck

[All programs](README.md) · [Repository home](../../README.md)

Analyze shell scripts for common quoting, portability and logic mistakes without executing them.

## Install and verify

```bash
sudo apt update
apt policy shellcheck
sudo apt install shellcheck
shellcheck --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** INSPECT. ShellCheck complements Bash syntax checking; neither proves that a script is safe to execute.

### Create a deliberately flawed fixture

```bash
printf '%s\n' '#!/bin/bash' 'name="lab notes"' 'printf "%s\n" $name' > shellcheck-demo.sh
shellcheck shellcheck-demo.sh
bash -n shellcheck-demo.sh
```

ShellCheck should report unquoted expansion in this example. Bash -n can accept it because it is syntactically valid. Do not run the flawed script merely to check its syntax.

### Fix quoting and recheck

```bash
printf '%s\n' '#!/bin/bash' 'name="lab notes"' 'printf "%s\n" "$name"' > shellcheck-demo.sh
shellcheck shellcheck-demo.sh
```

Quoting preserves a single argument instead of unintended splitting/globbing. A clean report means no issue was found by that analysis, not complete correctness or harmless behavior.

### Work on a real script

Set the correct shebang or `shellcheck -s bash script.sh` when appropriate. Read warning explanations before suppression. Use a narrow documented suppression only when you understand the invariant; do not disable all warnings to get a green check.

**Troubleshooting:** an unsupported shell/extension needs the correct parser assumption. External sourced files may need explicitly scoped analysis; avoid following untrusted source paths indiscriminately.

**Cleanup:** remove only shellcheck-demo.sh if created for the exercise.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run shellcheck` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.shellcheck.net/). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
