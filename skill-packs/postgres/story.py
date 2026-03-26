"""
story.py - Narrative text for Postgres Quest
Cyberpunk/Stephensonian flavor — the Database as a corporate intelligence archive.
"""

INTRO_STORY = """
The database predates the company that owns it.

That's the thing nobody tells you about megacorp infrastructure: the acquisition trail goes
so deep that half their critical systems are running on technology that was old before
the founding partners were born. Mergers, buyouts, spin-offs, hostile takeovers — each one
leaving behind a sedimentary layer of data, slightly incompatible, never quite migrated,
accumulating like geological strata until the whole thing weighs a petabyte and nobody
alive fully understands its schema.

This one runs [bold cyan]PostgreSQL[/bold cyan]. Has for thirty years. Probably will for thirty more.

They call it [bold yellow]The Archive[/bold yellow]. Two hundred billion rows across eleven thousand tables.
The records of every transaction, every employee, every contract, every internal communication
that the corp has ever generated, going all the way back to the original company they
consumed in Year Zero of their expansion. Unindexed. Poorly normalized. Queried by a
generation of developers who learned SQL from a three-paragraph tutorial and never looked back.

Your client wants something specific out of it. Something that's been in there for years
without anyone knowing it's there. Finding it requires something the corp's own data team
doesn't have: [bold white]a real understanding of SQL[/bold white].

[bold white]You are a Data Archaeologist.[/bold white]

[bold magenta]Ghost-class. Freelance. Hired through seven layers of anonymization.[/bold magenta]
You don't break into systems. You don't need to.
They gave you read access weeks ago during the "independent audit" they paid for.
They just didn't realize the auditor was also the client's operative.

The database is open. The data is in there.

[bold cyan]All you have to do is know how to ask for it.[/bold cyan]
"""

ZONE_INTROS = {
    "surface_tables": """
[bold cyan]== THE SURFACE TABLES ==[/bold cyan]

First contact.

The database presents its outer layer — thousands of tables, each one a snapshot
of some corner of the corp's operations. The schema documentation is fifteen years
out of date. The table names are a mix of three different naming conventions because
three different consulting firms built three different parts of it over the years.

None of that matters right now. What matters is: you know [yellow]SELECT[/yellow].

The most fundamental operation in all of relational databases. Thirty years old.
Unchanged. The corp's $200M data warehouse layer is just SELECT statements all
the way down, wrapped in enough middleware to make the original engineers weep.

[italic]"The data was always there. You just have to ask for it in the language it understands."[/italic]
""",
    "filter_chambers": """
[bold cyan]== THE FILTER CHAMBERS ==[/bold cyan]

Two hundred billion rows.

You don't want two hundred billion rows. You want seventeen specific records that
match a pattern the corp's own analysts haven't thought to look for. The difference
between a data scientist and a data archaeologist is that the scientist works with
datasets. The archaeologist works with [bold white]needles[/bold white] — and knows exactly which
haystack to reach into.

[yellow]WHERE[/yellow] is the haystack remover.

Add a WHERE clause and the database stops showing you everything and starts showing
you only what satisfies a condition. Combine conditions with [yellow]AND[/yellow], [yellow]OR[/yellow],
[yellow]NOT[/yellow]. Check for nulls with [yellow]IS NULL[/yellow]. Specify ranges with [yellow]BETWEEN[/yellow].
Pattern-match strings with [yellow]LIKE[/yellow].

[italic]"The signal was always there. WHERE is how you tune out the noise."[/italic]
""",
    "aggregation_engine": """
[bold cyan]== THE AGGREGATION ENGINE ==[/bold cyan]

Individual rows are facts. Aggregations are [bold white]intelligence[/bold white].

Any analyst can pull a row. What the corp's security team is watching for is
pattern-of-life analysis — someone querying things that don't add up, generating
reports that don't fit the job description. But aggregations look like routine
business reporting. They look like dashboards. They look like nothing.

[yellow]COUNT[/yellow], [yellow]SUM[/yellow], [yellow]AVG[/yellow], [yellow]MIN[/yellow], [yellow]MAX[/yellow] —
the statistical summary layer. Combine with [yellow]GROUP BY[/yellow] to slice by category.
[yellow]HAVING[/yellow] to filter on those grouped results, the way WHERE filters individual rows.

[italic]"Totals don't look like espionage. That's the point."[/italic]
""",
    "junction_archive": """
[bold cyan]== THE JUNCTION ARCHIVE ==[/bold cyan]

The data you need isn't in one table.

It never is. Real-world data is [bold white]relational[/bold white] — spread across multiple tables
that connect to each other through foreign keys and reference fields, the same way
corporate org charts sprawl across divisions and subsidiaries and holding companies
designed specifically to make auditors' lives difficult.

Whoever designed this schema understood that concept deeply. The financial data is
in one table. The personnel data is in another. The contracts are in a third.
The connecting tissue between them is the [yellow]JOIN[/yellow].

[yellow]INNER JOIN[/yellow], [yellow]LEFT JOIN[/yellow], [yellow]RIGHT JOIN[/yellow] — the join operators.
Learn to read a schema and write a JOIN and the entire relational database opens up.
Data in one table becomes context for data in another.

[italic]"The interesting information is always at the intersection."[/italic]
""",
    "subquery_vaults": """
[bold cyan]== THE SUBQUERY VAULTS ==[/bold cyan]

You've mastered flat queries. Time to go deeper.

The data you're after requires a query that references the results of another query.
A question whose answer depends on first answering a different question. The corps'
compliance department runs queries like this every quarter — finding all employees
who accessed systems they shouldn't have, using a list of unauthorized systems that
is itself generated by a query.

They call this [bold white]subqueries[/bold white] and [bold white]CTEs[/bold white] — Common Table Expressions.
A CTE is a query you name and reference like a table. A subquery is a query embedded
inside another query's WHERE or FROM or SELECT clause.

[yellow]WITH cte AS (query)[/yellow] — the CTE syntax. Clean. Readable. The right tool.
Subqueries in WHERE and SELECT when you need them inline and small.

[italic]"The answer to the question you're asking might require answering a different question first."[/italic]
""",
    "schema_forge": """
[bold cyan]== THE SCHEMA FORGE ==[/bold cyan]

Reading is reconnaissance. Writing is [bold white]presence[/bold white].

You've been extracting data. Now you need to leave something behind — a staging
table for intermediate results, a temporary structure to hold data while you
process it, a record of what you've found in a format you control.

This is where SQL stops being a query language and starts being a
[bold white]data definition language[/bold white]. CREATE TABLE. ALTER TABLE. Data types.
Constraints. The structural layer that defines what the database can hold
and how it enforces integrity.

[yellow]CREATE TABLE[/yellow], [yellow]ALTER TABLE[/yellow], [yellow]DROP TABLE[/yellow] — the schema toolkit.
[yellow]TEXT[/yellow], [yellow]INTEGER[/yellow], [yellow]BOOLEAN[/yellow], [yellow]TIMESTAMP[/yellow] — the type system.
[yellow]NOT NULL[/yellow], [yellow]UNIQUE[/yellow], [yellow]PRIMARY KEY[/yellow] — the constraint layer.

[italic]"You understand a system when you can not just read it, but build in it."[/italic]
""",
    "index_sanctum": """
[bold cyan]== THE INDEX SANCTUM ==[/bold cyan]

The query runs. The query takes 45 seconds.

45 seconds is an eternity when you're inside a live corporate database and
the monitoring system logs anything that runs longer than 30. You need your
queries to be [bold white]invisible[/bold white] — which means they need to be [bold white]fast[/bold white].

The index is the database's answer to the full-table scan. Without an index,
every query that filters on a column has to read every row and check.
With an index, the database jumps directly to the matching rows in microseconds.

[yellow]CREATE INDEX[/yellow] — the index builder.
[yellow]EXPLAIN[/yellow] and [yellow]EXPLAIN ANALYZE[/yellow] — the query plan reader.
The output of EXPLAIN tells you exactly what the database is doing:
whether it's using an index, whether it's doing a seq scan, where the time is going.

[italic]"The difference between 45 seconds and 45 milliseconds is an index.
The difference between getting caught and not getting caught is also an index."[/italic]
""",
    "transaction_core": """
[bold cyan]== THE TRANSACTION CORE ==[/bold cyan]

The deepest layer.

Everything above this has been about [bold white]reading[/bold white] data. Transactions are about
[bold white]writing[/bold white] it — and making sure that when things go wrong (and things go wrong),
the database doesn't end up in a corrupt intermediate state.

This is where ACID lives. [bold yellow]Atomicity[/bold yellow] — a transaction either fully commits or
fully rolls back, no partial states. [bold yellow]Consistency[/bold yellow] — the database moves from
one valid state to another. [bold yellow]Isolation[/bold yellow] — concurrent transactions don't interfere
with each other. [bold yellow]Durability[/bold yellow] — committed data survives failures.

[yellow]BEGIN[/yellow], [yellow]COMMIT[/yellow], [yellow]ROLLBACK[/yellow] — the transaction boundary commands.
Isolation levels: [yellow]READ COMMITTED[/yellow], [yellow]REPEATABLE READ[/yellow], [yellow]SERIALIZABLE[/yellow].

[italic]"Transactions are the database's promise: if I say it happened, it happened.
Even if the power went out. Even if the disk failed. Even if the building burned down."[/italic]
""",
    "window_functions": """
[bold cyan]== THE WINDOW FUNCTIONS ARCHIVE ==[/bold cyan]

GROUP BY collapses rows. Window functions do not.

You've been aggregating data — summing, counting, averaging. Every time you
GROUP BY, the individual rows disappear into the aggregate. The department becomes
a number. The account becomes a total. The data loses its resolution.

Window functions give you aggregation [italic]and[/italic] the original rows simultaneously.
[yellow]ROW_NUMBER()[/yellow] assigns ranks without collapsing. [yellow]SUM() OVER()[/yellow] computes a running
total while keeping every transaction visible. [yellow]LAG()[/yellow] and [yellow]LEAD()[/yellow] access
neighboring rows directly — no self-join required.

The NEXUS transaction archive has 200 billion rows across eleven thousand tables.
The forensic pattern you're looking for — accounts where the same vendor appears in
the top 3 transactions across every quarter for five years — requires ranking within
partitions and comparing across time. GROUP BY can't do this. Window functions can.

[italic]"Window functions are what separate SQL analysis from SQL reporting.
Reporting collapses data. Analysis preserves it."[/italic]
""",
    "transactions_vault": """
[bold cyan]== THE TRANSACTIONS VAULT ==[/bold cyan]

The fraud involved carefully crafted transactions that bypassed audit logs.

Ghost has the raw timeline. The next step is understanding [bold white]how[/bold white] the
manipulation worked — and that requires understanding PostgreSQL transaction
isolation at a level the fraudsters didn't expect anyone to reach.

[yellow]BEGIN[/yellow] starts the boundary. [yellow]COMMIT[/yellow] makes it permanent. [yellow]ROLLBACK[/yellow] undoes everything.
[yellow]SAVEPOINT[/yellow] creates partial checkpoints — partial rollback without losing the whole transaction.
[yellow]SET TRANSACTION ISOLATION LEVEL[/yellow] controls what concurrent transactions can see.

The fraud used phantom reads to read rows that didn't officially exist yet —
transactions that were in-flight but not committed, giving the illusion of
authorized balances. The isolation level that prevents this is not the default.

[italic]"The database is a crime scene. The transactions are the evidence.
Read them correctly and the manipulation becomes obvious."[/italic]
""",
    "json_forge": """
[bold cyan]== THE JSON FORGE ==[/bold cyan]

Some data refuses to fit the relational model.

The NEXUS archive is mostly structured — tables, columns, foreign keys, constraints.
But the metadata column in the transactions table is a [yellow]JSONB[/yellow] blob. Every transaction
carries a variable payload: vendor details, routing codes, authorization chains, flags.
No consistent schema. No ALTER TABLE that could normalize it without breaking every
upstream system that writes to it.

[yellow]->[/yellow] and [yellow]->>[/yellow] extract individual fields. [yellow]jsonb_array_elements()[/yellow] explodes arrays
into rows. [yellow]@>[/yellow] tests containment with index support — the right way to query
JSONB at scale. [yellow]json_build_object()[/yellow] constructs new JSON from relational data
for output or intermediate staging.

The phantom_corp pattern lives inside that metadata column. Seventeen transactions.
Different accounts. Different amounts. Same vendor JSON payload structure — and
that structure is the signature.

[italic]"Semi-structured data is not an excuse to not query it.
JSON operators are the bridge between the document and the relation."[/italic]
""",
    "performance_tuning": """
[bold red]PERFORMANCE INTELLIGENCE CENTER[/bold red]

Queries have been degrading for weeks. The monitoring team blamed the network.
The network team blamed the application. The application team blamed the database.

[italic]"The database never lies. It just waits for someone to ask it the right questions."[/italic]

[bold cyan]EXPLAIN ANALYZE[/bold cyan] shows execution reality, not estimates. [bold cyan]pg_stat_statements[/bold cyan]
aggregates query patterns across sessions — revealing the true slow-query culprits.
[bold cyan]VACUUM ANALYZE[/bold cyan] removes dead tuples and recalibrates the planner's model of
your data.

The performance bottleneck in the NEXUS fraud database: a correlated subquery inside
a reporting view, called seven thousand times a day, doing a Seq Scan on a 40M row
table — because no one checked.

[italic]"Every production crisis has a query at the center. Find the query."[/italic]
""",
    "replication_and_backup": """
[bold red]REPLICATION COMMAND[/bold red]

The primary database is intact. The backup strategy: pg_basebackup nightly,
WAL archiving continuous, two streaming standbys in separate availability zones.

[italic]"A database without a tested backup is not a database. It is a liability."[/italic]

[bold cyan]pg_dump[/bold cyan] for logical backups — portable, point-in-time. [bold cyan]pg_basebackup[/bold cyan] for
physical backups — consistent, fast, supports streaming to standby. [bold cyan]WAL archiving[/bold cyan]
enables point-in-time recovery to any moment the logs cover.

The developer deleted 847,000 rows of transaction history at 14:32. You have WAL
archives. You have a recovery target time. The data is not gone — it just thinks
it is.

[italic]"Backups are insurance. WAL archiving is a time machine."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "surface_tables": """
[bold green]SURFACE TABLES — ACCESSED.[/bold green]

You can read the data. SELECT, FROM, LIMIT, ORDER BY — the basic vocabulary of the
archive is yours. Two hundred billion rows and you know how to navigate them.

This is the layer every analyst who ever touched this database knows.
It's also the layer where most of them stopped.

[bold cyan]The Filter Chambers open ahead. Time to get specific.[/bold cyan]
""",
    "filter_chambers": """
[bold green]FILTER CHAMBERS — CLEARED.[/bold green]

WHERE clauses flow from your fingers. You can specify conditions, combine them,
test for nulls, pattern-match strings, filter ranges. The two hundred billion rows
are no longer a wall — they're a dataset you can query with surgical precision.

The corp's data scientists pull aggregate reports. You pull the exact records you need.

[bold cyan]The Aggregation Engine pulses with the next phase.[/bold cyan]
""",
    "aggregation_engine": """
[bold green]AGGREGATION ENGINE — OPERATIONAL.[/bold green]

Counts. Sums. Averages. Grouped by category. Filtered by condition.
The raw data has become intelligence — patterns extracted from noise, trends visible
only when you aggregate across the right dimensions.

The monitoring logs show nothing unusual. Aggregation queries look like business reporting.

[bold cyan]The Junction Archive connects what the aggregations have found.[/bold cyan]
""",
    "junction_archive": """
[bold green]JUNCTION ARCHIVE — TRAVERSED.[/bold green]

Tables that were separate are now joined. Employees linked to their contracts.
Contracts linked to their financial records. Financial records linked to the accounts
that funded them. The relational web that the corps thought obscured the trail
is exactly what lets you follow it.

INNER, LEFT, RIGHT — you know when to use each one.

[bold cyan]The Subquery Vaults hold the next layer of complexity.[/bold cyan]
""",
    "subquery_vaults": """
[bold green]SUBQUERY VAULTS — EXCAVATED.[/bold green]

Queries that reference other queries. CTEs that name intermediate results
and make complex logic readable. The kind of SQL that looks, to the casual
observer, like routine data work — but which is actually structured intelligence extraction.

The corp's compliance team runs queries like this. You just ran better ones.

[bold cyan]The Schema Forge is where passive recon becomes active presence.[/bold cyan]
""",
    "schema_forge": """
[bold green]SCHEMA FORGE — OPERATIONAL.[/bold green]

You can build in the database now, not just read it. CREATE TABLE. ALTER TABLE.
Constraints that enforce data integrity. Types that match the domain.

A staging table, created and populated with the extracted intelligence,
formatted exactly the way the client requested. Untraceable.

[bold cyan]The Index Sanctum will make sure none of this was slow enough to flag.[/bold cyan]
""",
    "index_sanctum": """
[bold green]INDEX SANCTUM — OPTIMIZED.[/bold green]

The queries run in milliseconds now. EXPLAIN confirms the indexes are being used.
No sequential scans on large tables. No 45-second queries lighting up the monitoring dashboard.

The difference between a query that takes 2ms and one that takes 45s
is an index. You know where to put it. You know how to verify it's working.

[bold cyan]One final layer. The Transaction Core. This is where ACID lives.[/bold cyan]
""",
    "transaction_core": """
[bold green]THE TRANSACTION CORE — MASTERED.[/bold green]

Every record pulled in the right order, at the right level of isolation,
committed to the staging table in a single atomic transaction. Clean.

[bold cyan]The Window Functions Archive: analysis without losing the rows.[/bold cyan]
""",
    "window_functions": """
[bold green]THE WINDOW FUNCTIONS ARCHIVE — MAPPED.[/bold green]

[cyan]ROW_NUMBER()[/cyan], [cyan]RANK()[/cyan], [cyan]LAG()[/cyan], [cyan]LEAD()[/cyan], [cyan]SUM() OVER()[/cyan], [cyan]NTILE()[/cyan].
The forensic pattern emerged: the same phantom vendor ranks #1 by transaction amount
in every account, every quarter, for five years. No GROUP BY could have shown this.
Window functions preserved the rows [italic]and[/italic] computed the analysis.

[bold cyan]The JSON Forge: the pattern lives inside the metadata column.[/bold cyan]
""",
    "transactions_vault": """
[bold green]THE TRANSACTIONS VAULT — DECRYPTED.[/bold green]

[cyan]BEGIN[/cyan]. [cyan]COMMIT[/cyan]. [cyan]ROLLBACK[/cyan]. [cyan]SAVEPOINT sp1[/cyan]. [cyan]ROLLBACK TO SAVEPOINT sp1[/cyan].
[cyan]SET TRANSACTION ISOLATION LEVEL SERIALIZABLE[/cyan] — the level that closes the phantom read window.

The fraud timeline is reconstructed. The manipulation exploited READ COMMITTED —
the default — where phantom rows could slip into a transaction window before the
audit trigger fired. SERIALIZABLE would have caught it. They knew this. They counted on
no one running at that isolation level.

Now you know why they were right to count on it. And why they were wrong to think
no one would eventually reconstruct the sequence.

[bold cyan]The JSON Forge: the signature is inside the metadata column.[/bold cyan]
""",
    "json_forge": """
[bold yellow]★ ★ ★  THE JSON FORGE — COMPLETE.  ★ ★ ★[/bold yellow]

[bold white]The extraction is complete.[/bold white]

[cyan]metadata @> '{"vendor": "phantom_corp"}'::jsonb[/cyan] — seventeen matching transactions.
[cyan]jsonb_array_elements()[/cyan] expanded the authorization chains into rows for cross-reference.
[cyan]json_build_object()[/cyan] formatted the output package exactly as the client specified.

The pattern was always there. Inside a JSONB blob, inside a transaction table,
inside a 200-billion-row archive that the corp's own analysts query every day
without seeing anything unusual.

From SELECT to JSONB operators. Surface Tables to the JSON Forge.
Every layer of the archive walked.

[bold magenta]The corps think SQL is a reporting tool. You know it's an intelligence tool.[/bold magenta]

[bold yellow]DATA ARCHAEOLOGIST STATUS: GRANDMASTER.  ARCHIVE: FULLY EXCAVATED.[/bold yellow]
""",
    "performance_tuning": """
[bold green]PERFORMANCE INVESTIGATION COMPLETE.[/bold green]

[cyan]EXPLAIN ANALYZE[/cyan] exposed the Seq Scan. [cyan]pg_stat_statements[/cyan] showed it had run
2.3 million times in 30 days. [cyan]VACUUM ANALYZE[/cyan] updated stale statistics — the planner
had been working from table counts that were 6 months old.

One index on the correlated subquery's JOIN column. Seq Scan → Index Scan.
Query time: 8,200ms → 12ms. The monitoring system stopped alerting.

[bold magenta]Performance is a skill, not a measurement.[/bold magenta]
""",
    "replication_and_backup": """
[bold green]THE EVIDENCE IS PRESERVED.[/bold green]

[cyan]pg_basebackup[/cyan] captured the physical database state. [cyan]WAL archives[/cyan] fill the gaps
between base backups. [cyan]recovery_target_time = '14:31:00'[/cyan] in the recovery config —
PostgreSQL replays WAL up to that exact moment.

The 847,000 deleted rows: restored. The NEXUS transaction history: intact.
The developer who ran `DELETE FROM transactions WHERE true`: already en route
to questioning.

[bold yellow]Every byte written to a database leaves a trace. Every backup is a time machine.[/bold yellow]
""",
}

BOSS_INTROS = {
    "surface_tables": "[bold red]⚠  QUERY AUDIT: The Surface Layer Final Check[/bold red]\nThe compliance system is running a query audit. Prove your SELECT fundamentals are clean — everything you know, right now.",
    "filter_chambers": "[bold red]⚠  ANOMALY DETECTED: The Filter Gauntlet[/bold red]\nSomething in the data doesn't match the official story. Extract the discrepancy using precise filtering — one wrong WHERE clause and the query returns garbage.",
    "aggregation_engine": "[bold red]⚠  STATISTICAL REVIEW: The Aggregation Trial[/bold red]\nThe monitoring system is watching for unusual aggregate patterns. Yours will look exactly like legitimate reporting — if you write it correctly.",
    "junction_archive": "[bold red]⚠  RELATIONSHIP MAP: The Join Crucible[/bold red]\nThe data you need exists only at the intersection of three tables. No shortcuts. No subqueries yet. Pure JOIN logic.",
    "subquery_vaults": "[bold red]⚠  NESTED QUERY DETECTED: The Subquery Maze[/bold red]\nThe target data requires a query whose WHERE clause depends on the results of another query. Both must be correct. Neither can be slow.",
    "schema_forge": "[bold red]⚠  SCHEMA MODIFICATION LOGGED: The DDL Trial[/bold red]\nYou need a staging table. Create it, constrain it correctly, and populate it in one transaction — before the schema audit runs.",
    "index_sanctum": "[bold red]⚠  QUERY PERFORMANCE ALERT: The Optimization Crisis[/bold red]\nA query is running too long. The monitoring system will flag it in 30 seconds. Read the EXPLAIN output, add the index, verify the speedup.",
    "transaction_core": "[bold red]★  FINAL TRANSACTION: The ACID Test[/bold red]\nEverything you've extracted needs to land in the staging table atomically. BEGIN, do the work, COMMIT. If anything goes wrong, it never happened.",
    "window_functions": "[bold red]⚠  FORENSIC ANALYSIS: The Pattern Across Quarters[/bold red]\nFive years. Same phantom vendor. Same account ranking pattern. You need ROW_NUMBER, PARTITION, LAG, and NTILE to surface it. No GROUP BY.",
    "json_forge": "[bold red]★  JSON EXTRACTION: The Metadata Signature[/bold red]\nSeventeen transactions. Phantom vendor hidden in a JSONB column. Use @>, ->>, jsonb_array_elements. Find the pattern before the audit window closes.",
    "transactions_vault": "[bold red]★  ISOLATION TRIAL: The Phantom Read Window[/bold red]\nThe fraud exploited a gap in transaction isolation. Identify the isolation level that closes the phantom read window. SET TRANSACTION ISOLATION LEVEL — which level makes concurrent transactions appear serial?",
    "performance_tuning": "[bold red]⚠  PRODUCTION CRISIS: The Seq Scan[/bold red]\nQueries that ran in 50ms now take 8 seconds. pg_stat_statements shows the culprit. EXPLAIN ANALYZE shows the Seq Scan. You have one shot to fix it before the morning report runs.",
    "replication_and_backup": "[bold red]★  FINAL EXTRACTION: The Recovery Target[/bold red]\n847,000 rows deleted. The WAL archives exist. The base backup is intact. Walk through every step of PITR — from base backup restore to recovery_target_time to the moment the deleted rows appear again.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Query", "Executed your first SELECT. The database acknowledged you."),
    "navigator": ("Table Reader", "Mastered the Surface Tables. SELECT, FROM, ORDER BY — the outer layer is yours."),
    "archivist": ("Filter Expert", "Cleared the Filter Chambers. No WHERE clause can hide the signal from you now."),
    "seeker": ("Data Analyst", "Mastered the Aggregation Engine. You turn raw rows into intelligence."),
    "pipe_dream": ("Join Master", "Cleared the Junction Archive. Relational data holds no secrets."),
    "necromancer": ("Subquery Architect", "Cleared the Subquery Vaults. Your queries reference other queries. Your SQL thinks."),
    "warden": ("Schema Designer", "Mastered the Schema Forge. You don't just read databases — you build in them."),
    "scriptor": ("Query Optimizer", "Cleared the Index Sanctum. You read EXPLAIN output. You know where the time goes."),
    "networked": ("Transaction Analyst", "Mastered the Transaction Core. ACID properties are your native language now."),
    "grandmaster": ("DATA ARCHAEOLOGIST: GRANDMASTER", "Every zone. Every layer. The entire relational model. The extraction is complete."),
    "streak_3": ("Query Streak", "3 correct in a row. The database is starting to respect you."),
    "streak_5": ("Signal Locked", "5 in a row. Your queries are precise. The monitoring system has nothing to flag."),
    "streak_10": ("QUERY GRANDMASTER", "10 in a row. You don't write SQL. You think in SQL."),
    "no_hints": ("Clean Extraction", "Cleared a zone without hints. Pure knowledge. No scaffolding."),
    "speed_demon": ("Sub-5 Query", "Answered in under 5 seconds. The query plan didn't have time to log."),
    "level_10": ("Junior Analyst", "Level 10. The database is starting to feel familiar."),
    "level_20": ("Senior Analyst", "Level 20. SQL is your native query language now."),
    "level_30": ("Query Legend", "Maximum level. You understand the relational model from SELECT to ACID. Complete."),
    "window_analyst": ("Window Function Specialist", "Cleared the Window Functions Archive. ROW_NUMBER, LAG, LEAD, NTILE — you analyze without collapsing."),
    "json_archaeologist": ("JSON Operator Expert", "Cleared the JSON Forge. ->, ->>, @>, jsonb_array_elements — semi-structured data holds no secrets."),
    "completionist": ("Full Schema Access", "Every challenge. Every zone. Total archive penetration achieved."),
    "boss_slayer": ("Audit Bypassed", "Beat your first boss challenge. The compliance system found nothing unusual."),
    "isolation_expert": ("Transaction Isolation Specialist", "Cleared the Transactions Vault. BEGIN, COMMIT, ROLLBACK, SAVEPOINT, SERIALIZABLE — the fraud timeline is yours to read."),
    "performance_engineer": ("Performance Engineer", "Cleared the Performance Tuning zone. EXPLAIN ANALYZE, pg_stat_statements, VACUUM — you find and fix slow queries."),
    "replication_architect": ("Replication Architect", "Mastered backup and replication. pg_dump, pg_basebackup, WAL, PITR — the evidence is preserved."),
}
