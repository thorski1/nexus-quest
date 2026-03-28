"""
story.py — Narrative for Data Vaults (databases skill pack).
Theme: Data is the lifeblood of every system. Master the vaults.
"""

INTRO_STORY = """
[bold red]NEXUS TERMINAL — DATA VAULT OPERATIONS[/bold red]

The breach was deeper than anyone knew. NEXUS didn't just compromise the
application layer — they went straight for the databases. Every transaction,
every customer record, every cryptographic key — stored in vaults they now
control.

CIPHER's voice is measured but urgent: [bold cyan]"Forget the web servers.
Forget the containers. The databases are the real target. NEXUS has been
siphoning data for weeks through replicated read replicas they spun up
inside our own infrastructure. Shadow shards. Rogue connections pooled
through compromised PgBouncer instances."[/bold cyan]

A schema diagram materializes on your terminal. Hundreds of tables. Foreign
key relationships webbing across the screen like neural pathways. Some
legitimate. Some... injected.

[bold white]"They altered the schema?"[/bold white]

[bold cyan]"Three unauthorized migrations. A shadow table with audit logging
disabled. An index that doesn't match any known query pattern — likely an
exfiltration channel. And the replication lag on replica-07 is suspiciously
zero. It shouldn't be that fast unless they're reading directly from the WAL
stream."[/bold cyan]

A pause. Then: [bold cyan]"Data is the lifeblood of every system. The queries,
the schemas, the replication topology — this is where the real evidence lives.
Master the vaults, or NEXUS keeps draining them."[/bold cyan]

[italic]Connecting to vault-primary-01.nexus.internal:5432... authentication required.[/italic]
"""

ZONE_INTROS = {
    "database_fundamentals": (
        "[bold cyan]ZONE 1 — THE FOUNDATION LAYER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Before you touch a single table, you need to understand "
        "what we're dealing with. Relational vs document stores. ACID guarantees. "
        "The CAP theorem trade-offs NEXUS exploited. They chose their database "
        "technologies strategically — you need to understand why.'[/bold white]"
    ),
    "sql_mastery": (
        "[bold cyan]ZONE 2 — THE QUERY FORGE[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The exfiltrated data was extracted through SQL. Complex "
        "JOINs that merged customer records with internal keys. Subqueries nested "
        "three levels deep. GROUP BY with HAVING clauses that filtered to exactly "
        "the high-value targets. You need to read SQL like a language — and write it "
        "like a weapon.'[/bold white]"
    ),
    "nosql_world": (
        "[bold cyan]ZONE 3 — THE UNSTRUCTURED FRONTIER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Not everything NEXUS took was in Postgres. They hit the "
        "Redis cache — session tokens, rate limiter state, the real-time leaderboard "
        "that maps operator activity. They cloned a MongoDB collection with flexible "
        "schemas that nobody was validating. And the DynamoDB table? They created a "
        "secondary index we never authorized. Know the NoSQL landscape.'[/bold white]"
    ),
    "database_design": (
        "[bold cyan]ZONE 4 — THE SCHEMA BLUEPRINT[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The shadow table NEXUS injected violates every normal form "
        "in the book. Comma-separated user IDs in a single column. Transitive dependencies "
        "everywhere. No foreign keys — by design, so deletions leave no trace. "
        "You need to understand how databases should be designed to spot what's wrong "
        "with this one.'[/bold white]"
    ),
    "migrations_and_versioning": (
        "[bold cyan]ZONE 5 — THE EVOLUTION CHAMBER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Three unauthorized migrations in the Alembic history. "
        "Version ae7f3c — adds a column with no audit trail. Version b12d8a — creates "
        "an index on a column that no application query uses. Version c49e1f — alters "
        "a foreign key constraint to CASCADE DELETE. They evolved the schema to suit "
        "their operation. You need to understand migrations to trace what they did.'[/bold white]"
    ),
    "replication_and_scaling": (
        "[bold cyan]ZONE 6 — THE REPLICATION GRID[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Replica-07 is the smoking gun. It's receiving the WAL "
        "stream but it's not in our replica inventory. NEXUS created a shadow read "
        "replica — every write to the primary is mirrored to their infrastructure in "
        "real time. Sharding, replication, connection pooling — they used our own "
        "scaling architecture against us. Learn how it works.'[/bold white]"
    ),
    "backup_and_recovery": (
        "[bold cyan]ZONE 7 — THE DISASTER VAULT[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The good news: our WAL archive is intact. The bad news: "
        "NEXUS has been in the system for 18 days. We need point-in-time recovery to "
        "reconstruct the exact state of the database before the first unauthorized "
        "migration. RTO is 4 hours. RPO is zero. You need to understand backup "
        "strategies, WAL, and recovery procedures — lives depend on this data.'[/bold white]"
    ),
    "database_security": (
        "[bold cyan]ZONE 8 — THE ENCRYPTION PERIMETER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The initial vector was a SQL injection in the reporting "
        "dashboard — a parameterized query that someone rewrote as string concatenation "
        "during a late-night hotfix. From there, NEXUS escalated to a superuser account "
        "with no row-level security. Audit logging was disabled on the shadow table. "
        "Encryption at rest was on, but they had the KMS key. Every layer of database "
        "security failed. Learn them all — so we can rebuild them.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "database_fundamentals": (
        "[bold green]ZONE CLEAR — THE FOUNDATION LAYER[/bold green]\n\n"
        "Relational vs NoSQL, ACID vs BASE, CAP theorem — the theoretical foundation "
        "is locked in. You can evaluate any database technology against its trade-offs. "
        "CIPHER: 'You understand the landscape. Now let's get into the SQL.'"
    ),
    "sql_mastery": (
        "[bold green]ZONE CLEAR — THE QUERY FORGE[/bold green]\n\n"
        "SELECT, JOIN, GROUP BY, HAVING, subqueries, indexes, EXPLAIN — SQL is no "
        "longer a mystery. CIPHER: 'You just deconstructed the exfiltration query. "
        "Three JOINs, a correlated subquery, and a HAVING clause that filtered to "
        "exactly 847 high-value accounts. Now we know what they took.'"
    ),
    "nosql_world": (
        "[bold green]ZONE CLEAR — THE UNSTRUCTURED FRONTIER[/bold green]\n\n"
        "MongoDB, Redis, DynamoDB, Cassandra, graph databases — the NoSQL ecosystem "
        "is mapped. CIPHER: 'The unauthorized DynamoDB GSI was designed to query by "
        "email address — a field that should never be a key. You spotted the pattern. "
        "We've revoked the index and rotated the access keys.'"
    ),
    "database_design": (
        "[bold green]ZONE CLEAR — THE SCHEMA BLUEPRINT[/bold green]\n\n"
        "Normalization, denormalization, ERDs, foreign keys — you can read a schema "
        "and spot structural anomalies. CIPHER: 'The shadow table's violations were "
        "deliberate: no foreign keys means no cascade trail, no 1NF means data "
        "hidden in comma-separated fields. You saw through it.'"
    ),
    "migrations_and_versioning": (
        "[bold green]ZONE CLEAR — THE EVOLUTION CHAMBER[/bold green]\n\n"
        "Migrations, versioning, rollbacks, expand-and-contract — schema evolution "
        "is under your control. CIPHER: 'All three unauthorized migrations are "
        "identified and rolled back. The Alembic history is clean. The CASCADE DELETE "
        "on the FK is reverted to RESTRICT. Schema integrity restored.'"
    ),
    "replication_and_scaling": (
        "[bold green]ZONE CLEAR — THE REPLICATION GRID[/bold green]\n\n"
        "Primary-replica, sharding, connection pooling, partitioning — the scaling "
        "architecture is transparent. CIPHER: 'Replica-07 has been identified and "
        "disconnected from the WAL stream. The replication slot is dropped. "
        "Connection pool audit shows no remaining rogue connections.'"
    ),
    "backup_and_recovery": (
        "[bold green]ZONE CLEAR — THE DISASTER VAULT[/bold green]\n\n"
        "Backups, WAL, PITR, RTO/RPO — you can plan and execute a recovery. "
        "CIPHER: 'Point-in-time recovery to 18 days ago is complete. The pre-breach "
        "database state is restored on the staging cluster. We have a clean baseline. "
        "Now we rebuild from verified data.'"
    ),
    "database_security": (
        "[bold green]ZONE CLEAR — THE ENCRYPTION PERIMETER[/bold green]\n\n"
        "SQL injection, least privilege, encryption, RLS, audit logging — every "
        "security layer is understood and hardened. CIPHER: 'The injection vector "
        "is patched. All accounts are least-privilege. RLS policies enforce tenant "
        "isolation. Audit logging is enabled on every table. Encryption keys are "
        "rotated. The data vaults are sealed. NEXUS won't get in this way again.'"
    ),
}

BOSS_INTROS = {
    "database_fundamentals": (
        "[bold red]BOSS CHALLENGE — TECHNOLOGY SELECTION[/bold red]\n\n"
        "[bold white]CIPHER: 'A new microservice needs persistent storage. "
        "High write throughput, flexible schema, horizontal scaling, eventual "
        "consistency is acceptable. Relational or NoSQL? Justify every trade-off. "
        "Wrong choice here and the architecture crumbles under load.'[/bold white]"
    ),
    "sql_mastery": (
        "[bold red]BOSS CHALLENGE — QUERY FORENSICS[/bold red]\n\n"
        "[bold white]CIPHER: 'The EXPLAIN output shows a sequential scan on a "
        "10-million-row table, a nested loop join, and an estimated cost of 847,000. "
        "The query takes 45 seconds. Diagnose the problem, design the index, "
        "and predict the new execution plan.'[/bold white]"
    ),
    "nosql_world": (
        "[bold red]BOSS CHALLENGE — DATA MODEL AUDIT[/bold red]\n\n"
        "[bold white]CIPHER: 'The DynamoDB table has a partition key with 3 unique values "
        "and 50 million items. Read latency is spiking. Explain what went wrong, "
        "design a better key schema, and describe the migration path.'[/bold white]"
    ),
    "database_design": (
        "[bold red]BOSS CHALLENGE — SCHEMA RECONSTRUCTION[/bold red]\n\n"
        "[bold white]CIPHER: 'The shadow table has 47 columns, no foreign keys, "
        "comma-separated values in 6 columns, and transitive dependencies everywhere. "
        "Normalize it to 3NF. Show me the tables, keys, and relationships.'[/bold white]"
    ),
    "migrations_and_versioning": (
        "[bold red]BOSS CHALLENGE — ZERO-DOWNTIME MIGRATION[/bold red]\n\n"
        "[bold white]CIPHER: 'The production users table has 200 million rows. "
        "You need to split the full_name column into first_name and last_name "
        "with zero downtime. Walk me through every migration step, the rollback "
        "plan, and how you verify data integrity.'[/bold white]"
    ),
    "replication_and_scaling": (
        "[bold red]BOSS CHALLENGE — ROGUE REPLICA[/bold red]\n\n"
        "[bold white]CIPHER: 'pg_stat_replication shows a connected replica with "
        "an IP address outside our infrastructure. It's consuming the WAL stream "
        "in real time. Describe the immediate response: disconnect it, audit "
        "the replication slots, and prevent reconnection.'[/bold white]"
    ),
    "backup_and_recovery": (
        "[bold red]BOSS CHALLENGE — DISASTER RECOVERY[/bold red]\n\n"
        "[bold white]CIPHER: 'At 14:32:07, someone ran DROP TABLE customers on "
        "production. You have a base backup from this morning and continuous WAL "
        "archiving. Walk me through the complete PITR procedure to recover to "
        "14:32:06 — every command, every verification step.'[/bold white]"
    ),
    "database_security": (
        "[bold red]BOSS CHALLENGE — BREACH ANALYSIS[/bold red]\n\n"
        "[bold white]CIPHER: 'The attack chain: SQL injection → privilege escalation → "
        "data exfiltration. Parameterized queries were bypassed through a stored "
        "procedure with dynamic SQL. The app user had GRANT OPTION. Audit logging "
        "was off. Design the complete remediation: fix the injection, revoke "
        "excessive privileges, enable audit logging, add RLS policies.'[/bold white]"
    ),
}
