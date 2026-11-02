# PostgreSQL service for labs

[All programs](README.md) · [Repository home](../../README.md)

Provide the optional database used by Metasploit workspaces. Service installation and database initialization are separate actions.

## Install and verify

```bash
sudo apt update
apt policy postgresql
sudo apt install postgresql
psql --version
```

Run the install only if APT shows a candidate from your configured Parrot repositories. Read the proposed changes. If no candidate exists, follow the upstream installation reference instead of adding Kali/Ubuntu repositories. Installation changes your system; version/help checks inspect it.

## Use it in practice

**Impact:** CHANGE; service starts may expose a listener according to its configuration. Install only if you need a local database. Do not reuse production data for security-tool experiments.

```bash
sudo systemctl start postgresql
systemctl status postgresql --no-pager
pg_lsclusters
```

Debian-family packaging can have a meta-service and versioned clusters. A successful meta-service status alone does not prove a cluster is accepting connections; inspect actual cluster state.

### Local readiness and identity

```bash
pg_isready
sudo -u postgres psql -c 'SELECT version();'
```

The second command uses the local postgres service account with packaging-default local access assumptions. It prints a version query and does not create a database. Do not weaken pg_hba.conf or expose the database publicly merely to make local tools work.

### Metasploit integration

Use the Metasploit package's supported `msfdb init` helper when supplied. This creates the dedicated database/role it needs. `db_status` is then run inside msfconsole, not the Linux shell.

**Troubleshooting:** verify the correct cluster, socket/port and authentication rules. On installations with an existing cluster, preserve databases and configuration; never delete the data directory as a first fix.

**Cleanup:** if no other applications need the lab service, `sudo systemctl stop postgresql` stops it. Stopping does not delete databases. Remove only a confirmed disposable database through documented PostgreSQL administration after backup.

## Updates and removal

For an APT installation, use Parrot’s normal `sudo parrot-upgrade` workflow. Preview removal with `sudo apt remove --dry-run postgresql` and review dependencies before proceeding. Removing packages may leave user-created files. Do not remove shared base-system packages simply to finish a lab.

## Reference and compatibility

[Upstream documentation](https://www.postgresql.org/docs/current/tutorial-start.html). Examples are documentation-reviewed starting workflows; Parrot runtime verification is pending unless recorded in the compatibility log. Inspect local help when flags differ. Output descriptions are expected behavior, not captured results from your machine.
