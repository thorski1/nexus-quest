"""
story.py - Narrative text for The Query Forge (Advanced SQL)
CIPHER cyberpunk flavor — the Query Forge as a legendary optimization engine
buried in the NEXUS Corp mainframe.
"""

INTRO_STORY = """
They called it [bold cyan]The Query Forge[/bold cyan].

Buried seventeen layers below the NEXUS Corp production cluster, behind firewalls
that haven't been audited since the second merger, there's an execution engine that
predates the optimizer itself. The original architects built it during Year Zero —
a raw SQL processing core designed to handle queries that the standard planner
couldn't touch. Window functions that span petabyte partitions. Recursive traversals
across graph structures so deep that the standard CTE engine hits stack limits.
Optimization passes that rewrite query plans in real time based on live statistics.

For twenty years, nobody needed it. The standard planner was good enough.
The queries were simple enough. The data was small enough.

[bold yellow]None of those things are true anymore.[/bold yellow]

The NEXUS fraud investigation has hit a wall. The standard queries return results
in minutes when they need to return in milliseconds. The recursive structures in the
shell company hierarchy go forty levels deep. The transaction isolation analysis
requires understanding MVCC at a level the corp's own DBAs don't operate at.
The pattern matching requires LATERAL joins, GROUPING SETS, and full-text search
operators that most developers have never seen.

[bold white]You are a Query Architect.[/bold white]

[bold magenta]Elite-class. The kind of operator who reads EXPLAIN ANALYZE output
the way other people read prose. You don't just write SQL — you understand
what the planner does with it, why it chooses one path over another,
and how to make it choose the path you want.[/bold magenta]

The Query Forge is online. The advanced operators are available.

[bold cyan]Time to write queries that the standard planner never imagined.[/bold cyan]
"""

ZONE_INTROS = {
    "window_functions": """
[bold cyan]== THE WINDOW ARRAY ==[/bold cyan]

The standard aggregation engine collapses rows. That's the deal — you get a total,
you lose the detail. COUNT gives you a number. SUM gives you a total. The individual
rows that produced those numbers disappear into the aggregate.

The Window Array doesn't collapse anything.

[yellow]ROW_NUMBER()[/yellow], [yellow]RANK()[/yellow], [yellow]DENSE_RANK()[/yellow] — ranking functions that assign
positions without merging rows. [yellow]LAG()[/yellow] and [yellow]LEAD()[/yellow] — temporal access operators
that reach backward and forward through the result set. [yellow]SUM() OVER()[/yellow] — running
totals that accumulate while keeping every individual row visible.

The forensic pattern in the NEXUS fraud data requires ranking transactions within
partitions, computing running totals across time windows, and comparing each row
to its neighbors. GROUP BY can't do this. The Window Array can.

[italic]"Aggregation without destruction. Analysis without compression.
The window function sees every row and computes across all of them."[/italic]
""",
    "ctes_recursive": """
[bold cyan]== THE RECURSION NEXUS ==[/bold cyan]

The shell company hierarchy goes forty levels deep.

NEXUS Corp acquired seventeen subsidiaries. Each subsidiary had its own subsidiaries.
Each of those had holding companies. The ownership chain branches and merges and
branches again — a directed graph of corporate control that was designed specifically
to be difficult to traverse.

Standard joins can't follow a path of unknown depth. You need [bold white]recursion[/bold white].

[yellow]WITH RECURSIVE[/yellow] — the self-referencing CTE. An anchor query that starts at the root.
A recursive member that joins back to itself, expanding one level at a time.
[yellow]UNION ALL[/yellow] that accumulates every level into a single result set.

The recursion terminates when the recursive member returns no new rows.
Or it doesn't terminate — and your query runs until the server kills it.

[yellow]MATERIALIZED[/yellow] vs [yellow]NOT MATERIALIZED[/yellow] — control whether the CTE is evaluated
once and cached, or inlined into the outer query for the optimizer to rewrite.

[italic]"Hierarchies are recursive by nature. Your queries need to be recursive to match."[/italic]
""",
    "query_optimization": """
[bold cyan]== THE OPTIMIZATION CORE ==[/bold cyan]

The query runs in 8 seconds.

Eight seconds is a lifetime in a production database serving 12,000 concurrent
connections. Eight seconds means the connection pool backs up. The pool backing up
means application timeouts. Timeouts mean retries. Retries mean the 8-second query
is now running forty times simultaneously instead of once.

[yellow]EXPLAIN ANALYZE[/yellow] shows you what the planner actually did — not what it planned to do.
Real execution times. Real row counts. Real buffer hits and misses.

[yellow]CREATE INDEX[/yellow] — the most impactful single optimization in all of SQL.
Composite indexes for multi-column WHERE clauses. Partial indexes for selective queries.
Covering indexes that eliminate table lookups entirely.

[yellow]pg_stat_statements[/yellow] — the aggregated query log that shows you which queries
consume the most total time across all executions.

[italic]"The database is not slow. Your query is slow. EXPLAIN will show you why."[/italic]
""",
    "transactions_locking": """
[bold cyan]== THE ISOLATION CHAMBER ==[/bold cyan]

Two transactions. Same row. Same moment.

This is where concurrency stops being theoretical and starts being a production
incident. Transaction A reads a balance. Transaction B updates it. Transaction A
reads it again. What does it see? The answer depends on the [bold white]isolation level[/bold white] —
and most developers have never changed it from the default.

[yellow]READ COMMITTED[/yellow] — the default. Each statement sees the latest committed data.
[yellow]REPEATABLE READ[/yellow] — snapshot isolation. The transaction sees one consistent snapshot.
[yellow]SERIALIZABLE[/yellow] — full serializability. Transactions behave as if they ran one at a time.

[yellow]SELECT FOR UPDATE[/yellow] — row-level locking. Claim rows before modifying them.
[yellow]SAVEPOINT[/yellow] — partial rollback without losing the whole transaction.
[yellow]MVCC[/yellow] — PostgreSQL's multi-version concurrency control, where every UPDATE creates
a new row version and readers never block writers.

The NEXUS fraud exploited a gap in isolation. Understanding that gap requires
understanding MVCC at the implementation level.

[italic]"Concurrency is not a feature. It's a weapon — and isolation is the safety."[/italic]
""",
    "advanced_patterns": """
[bold cyan]== THE PATTERN VAULT ==[/bold cyan]

The final layer. The operators that separate a SQL user from a SQL architect.

[yellow]LATERAL JOIN[/yellow] — a correlated subquery in the FROM clause. The right side can
reference the left side. Top-N per group. Dependent row generation. The kind of
query that used to require application-level loops now runs in a single statement.

[yellow]GROUPING SETS[/yellow], [yellow]CUBE[/yellow], [yellow]ROLLUP[/yellow] — multi-dimensional aggregation.
A single query that produces detail rows, subtotals, cross-tabulations, and grand
totals simultaneously. The reporting layer that used to require four separate queries
and a UNION ALL now requires one GROUP BY clause.

[yellow]JSONB operators[/yellow] — [yellow]@>[/yellow] containment, [yellow]->>[/yellow] extraction, [yellow]jsonb_array_elements()[/yellow]
expansion. Semi-structured data queried with the full power of the relational engine.

[yellow]Full-text search[/yellow] — [yellow]to_tsvector()[/yellow], [yellow]to_tsquery()[/yellow], [yellow]@@[/yellow] match operator.
Linguistic search with stemming, ranking, and GIN index support, built into PostgreSQL.

[italic]"The Pattern Vault holds the constructs that most SQL practitioners never learn.
Every one of them solves a problem that 'cannot be done in SQL'."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "window_functions": """
[bold green]THE WINDOW ARRAY — MASTERED.[/bold green]

ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, NTILE, SUM OVER, window frames.
You rank without collapsing. You aggregate without destroying. You reach
backward and forward through time within a single result set.

The forensic ranking pattern is visible: the same phantom vendor appearing
in the top 3 by amount across every partition, every quarter, for five years.

[bold cyan]The Recursion Nexus opens. The hierarchy goes forty levels deep.[/bold cyan]
""",
    "ctes_recursive": """
[bold green]THE RECURSION NEXUS — TRAVERSED.[/bold green]

WITH. WITH RECURSIVE. MATERIALIZED. Anchor members. Recursive members.
Cycle detection. Depth limits. The forty-level shell company hierarchy
flattened into a single result set in under 200 milliseconds.

The ownership chain is visible. Every subsidiary. Every holding company.
Every layer of indirection the architects designed to obscure the trail.

[bold cyan]The Optimization Core is next. Time to make these queries fast.[/bold cyan]
""",
    "query_optimization": """
[bold green]THE OPTIMIZATION CORE — CALIBRATED.[/bold green]

EXPLAIN ANALYZE. Buffer statistics. Seq Scan vs Index Scan. Composite indexes.
Partial indexes. The query that took 8 seconds now takes 12 milliseconds.
The monitoring system has nothing to flag. The connection pool is clear.

You read query plans the way other operators read logs — the execution path,
the cost estimates, the row count discrepancies that signal stale statistics.

[bold cyan]The Isolation Chamber awaits. Concurrency and locking are the next frontier.[/bold cyan]
""",
    "transactions_locking": """
[bold green]THE ISOLATION CHAMBER — SEALED.[/bold green]

ACID. MVCC. Snapshot isolation. Row-level locking. Deadlock detection.
SAVEPOINT for partial rollback. SERIALIZABLE for full isolation.

The fraud exploited READ COMMITTED — the default — where non-repeatable reads
allowed phantom balances to appear authorized. REPEATABLE READ would have
prevented it. Now you know why, and how.

[bold cyan]The Pattern Vault. The final layer. The advanced constructs that most never learn.[/bold cyan]
""",
    "advanced_patterns": """
[bold yellow]THE PATTERN VAULT — UNLOCKED.[/bold yellow]

[bold white]The Query Forge is complete.[/bold white]

LATERAL joins that correlate across FROM items. GROUPING SETS that produce
multi-dimensional reports in a single pass. JSONB operators that bridge the
relational and document worlds. Full-text search with linguistic stemming
and GIN-indexed performance.

From window functions to recursive CTEs. From query optimization to transaction
isolation. From LATERAL joins to full-text search. Every advanced SQL pattern
in the PostgreSQL arsenal — understood, practiced, and deployed.

[bold magenta]The standard planner writes queries. You write query plans.
The database does not surprise you. You surprise the database.[/bold magenta]

[bold yellow]QUERY ARCHITECT STATUS: FORGEMASTER.  THE QUERY FORGE: FULLY OPERATIONAL.[/bold yellow]
""",
}

BOSS_INTROS = {
    "window_functions": "[bold red]FORENSIC ANALYSIS: The Partition Ranking[/bold red]\nFive years of transaction data. The phantom vendor's pattern is hidden in the partition rankings. You need ROW_NUMBER, PARTITION BY, and subquery wrapping to surface the top-N per group. No GROUP BY.",
    "ctes_recursive": "[bold red]HIERARCHY EXTRACTION: The Recursive Descent[/bold red]\nThe shell company hierarchy goes forty levels deep. One recursive CTE. One anchor. One JOIN back to the CTE. Traverse the entire ownership chain or miss the connection.",
    "query_optimization": "[bold red]PRODUCTION CRISIS: The Missing Index[/bold red]\nEXPLAIN ANALYZE shows a Seq Scan on 50 million rows. 99.8% of rows are filtered out. The monitoring system is alerting. One index fixes everything — if you choose the right columns.",
    "transactions_locking": "[bold red]ISOLATION BREACH: The Non-Repeatable Read[/bold red]\nTwo concurrent transactions. Same account. Different balances. The fraud exploited the default isolation level. Identify the level, explain the vulnerability, prove you understand MVCC.",
    "advanced_patterns": "[bold red]FINAL EXTRACTION: The Multi-Dimensional Report[/bold red]\nThe client needs revenue broken down by region, by category, by both, and a grand total — in one query. CUBE, ROLLUP, or GROUPING SETS. One shot. Get it right.",
}
