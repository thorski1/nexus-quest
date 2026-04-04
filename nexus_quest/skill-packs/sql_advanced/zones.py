"""
zones.py - All zone and challenge data for The Query Forge (Advanced SQL)
Challenge types: quiz, text
"""

ZONES = {
    "window_functions": {
        "id": "window_functions",
        "name": "The Window Array",
        "subtitle": "Window Functions",
        "color": "cyan",
        "icon": "\u2261",
        "commands": ["ROW_NUMBER", "RANK", "DENSE_RANK", "LAG", "LEAD", "PARTITION BY", "OVER", "NTILE"],
        "challenges": [
            {
                "id": "win_1",
                "type": "quiz",
                "title": "The Numbering Protocol",
                "question": "Which window function assigns a unique sequential integer to each row within a partition?",
                "options": ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "NTILE()"],
                "answer": "ROW_NUMBER()",
                "lesson": (
                    "ROW_NUMBER() assigns a unique sequential integer to each row within a partition.\n\n"
                    "Syntax: ROW_NUMBER() OVER (PARTITION BY col ORDER BY col)\n\n"
                    "Unlike RANK(), ROW_NUMBER() never produces duplicates — even for ties,\n"
                    "each row gets a distinct number based on the ORDER BY.\n\n"
                    "Example:\n"
                    "  SELECT name, dept, salary,\n"
                    "         ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn\n"
                    "  FROM employees;"
                ),
                "xp": 50,
            },
            {
                "id": "win_2",
                "type": "quiz",
                "title": "Rank vs Dense Rank",
                "question": "If three employees tie for 2nd place, what rank does RANK() assign to the next employee after the tie?",
                "options": ["3", "4", "5", "6"],
                "answer": "5",
                "lesson": (
                    "RANK() leaves gaps after ties. If three rows share rank 2, the next rank is 5 (not 3).\n\n"
                    "DENSE_RANK() does NOT leave gaps — the next rank after a 3-way tie at 2 would be 3.\n\n"
                    "Choose RANK() when position in the full list matters.\n"
                    "Choose DENSE_RANK() when you want consecutive rank values.\n\n"
                    "Example:\n"
                    "  SELECT name, salary,\n"
                    "         RANK() OVER (ORDER BY salary DESC) AS rank,\n"
                    "         DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank\n"
                    "  FROM employees;"
                ),
                "xp": 75,
            },
            {
                "id": "win_3",
                "type": "text",
                "title": "The Lookback Operator",
                "question": "What window function accesses the value from the PREVIOUS row in the result set without a self-join?",
                "options": [],
                "answer": "LAG",
                "lesson": (
                    "LAG(column, offset, default) accesses the value from a previous row.\n\n"
                    "Syntax: LAG(column, 1) OVER (ORDER BY date)\n\n"
                    "The second argument is the offset (default 1). The third is the default\n"
                    "value if there is no previous row (default NULL).\n\n"
                    "Example — calculate day-over-day change:\n"
                    "  SELECT date, revenue,\n"
                    "         revenue - LAG(revenue, 1) OVER (ORDER BY date) AS daily_change\n"
                    "  FROM daily_sales;"
                ),
                "xp": 75,
            },
            {
                "id": "win_4",
                "type": "text",
                "title": "The Lookahead Operator",
                "question": "What window function accesses the value from the NEXT row in the result set?",
                "options": [],
                "answer": "LEAD",
                "lesson": (
                    "LEAD(column, offset, default) accesses the value from a subsequent row.\n\n"
                    "LEAD is the mirror of LAG — it looks forward instead of backward.\n\n"
                    "Example — find the gap between consecutive events:\n"
                    "  SELECT event_time,\n"
                    "         LEAD(event_time) OVER (ORDER BY event_time) - event_time AS gap\n"
                    "  FROM server_logs;"
                ),
                "xp": 75,
            },
            {
                "id": "win_5",
                "type": "quiz",
                "title": "Partitioned Analysis",
                "question": "In the clause OVER (PARTITION BY dept ORDER BY salary DESC), what does PARTITION BY do?",
                "options": [
                    "Filters rows to only the specified department",
                    "Divides the result set into groups, applying the window function within each group independently",
                    "Creates a temporary table for each department",
                    "Sorts the rows by department before applying the function",
                ],
                "answer": "Divides the result set into groups, applying the window function within each group independently",
                "lesson": (
                    "PARTITION BY divides rows into groups (partitions). The window function\n"
                    "is applied independently within each partition.\n\n"
                    "Without PARTITION BY, the window function treats the entire result set as one partition.\n\n"
                    "Example — rank employees within each department:\n"
                    "  SELECT name, dept, salary,\n"
                    "         RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank\n"
                    "  FROM employees;\n\n"
                    "This gives rank 1, 2, 3... separately for each department."
                ),
                "xp": 75,
            },
            {
                "id": "win_6",
                "type": "quiz",
                "title": "Running Totals",
                "question": "What does SUM(amount) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) compute?",
                "options": [
                    "The total of all amounts in the table",
                    "A running total of amount ordered by date",
                    "The sum of amounts for the current date only",
                    "The average of all preceding amounts",
                ],
                "answer": "A running total of amount ordered by date",
                "lesson": (
                    "A window frame defines which rows the function operates on relative to the current row.\n\n"
                    "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW means:\n"
                    "  'from the first row in the partition up to the current row'\n\n"
                    "This produces a running (cumulative) total.\n\n"
                    "Common frame specifications:\n"
                    "  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW  — 3-row moving window\n"
                    "  ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING  — forward-looking window\n"
                    "  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING — entire partition"
                ),
                "xp": 100,
            },
            {
                "id": "win_7",
                "type": "text",
                "title": "Quartile Division",
                "question": "What window function divides rows into N approximately equal-sized buckets? (Name only, no parentheses)",
                "options": [],
                "answer": "NTILE",
                "lesson": (
                    "NTILE(n) distributes rows into n approximately equal groups, numbered 1 through n.\n\n"
                    "Syntax: NTILE(4) OVER (ORDER BY salary) — divides into quartiles.\n\n"
                    "If rows don't divide evenly, earlier buckets get the extra rows.\n\n"
                    "Example — assign quartiles by performance score:\n"
                    "  SELECT name, score,\n"
                    "         NTILE(4) OVER (ORDER BY score DESC) AS quartile\n"
                    "  FROM reviews;"
                ),
                "xp": 75,
            },
            {
                "id": "win_boss",
                "type": "quiz",
                "title": "BOSS: The Forensic Partition",
                "question": "You need the top 3 highest-paid employees per department. Which approach correctly uses window functions?",
                "options": [
                    "SELECT * FROM employees GROUP BY dept HAVING salary IN (TOP 3)",
                    "SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn FROM employees) sub WHERE rn <= 3",
                    "SELECT * FROM employees WHERE ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) <= 3",
                    "SELECT TOP 3 * FROM employees PARTITION BY dept ORDER BY salary DESC",
                ],
                "answer": "SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn FROM employees) sub WHERE rn <= 3",
                "lesson": (
                    "Window functions cannot be used directly in WHERE clauses — they are\n"
                    "computed after WHERE is evaluated. You must wrap in a subquery or CTE.\n\n"
                    "Pattern for top-N per group:\n"
                    "  WITH ranked AS (\n"
                    "    SELECT *, ROW_NUMBER() OVER (PARTITION BY group_col ORDER BY sort_col DESC) AS rn\n"
                    "    FROM table\n"
                    "  )\n"
                    "  SELECT * FROM ranked WHERE rn <= N;\n\n"
                    "This is one of the most common advanced SQL patterns in production."
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
    "ctes_recursive": {
        "id": "ctes_recursive",
        "name": "The Recursion Nexus",
        "subtitle": "CTEs & Recursive Queries",
        "color": "magenta",
        "icon": "\u221e",
        "commands": ["WITH", "WITH RECURSIVE", "MATERIALIZED", "NOT MATERIALIZED", "UNION ALL"],
        "challenges": [
            {
                "id": "cte_1",
                "type": "text",
                "title": "The Named Query",
                "question": "What SQL keyword introduces a Common Table Expression (CTE)? (One word)",
                "options": [],
                "answer": "WITH",
                "lesson": (
                    "WITH introduces a CTE — a named temporary result set that exists\n"
                    "for the duration of a single query.\n\n"
                    "Syntax:\n"
                    "  WITH cte_name AS (\n"
                    "    SELECT ...\n"
                    "  )\n"
                    "  SELECT * FROM cte_name;\n\n"
                    "CTEs improve readability by breaking complex queries into named steps.\n"
                    "You can chain multiple CTEs separated by commas."
                ),
                "xp": 50,
            },
            {
                "id": "cte_2",
                "type": "quiz",
                "title": "CTE vs Subquery",
                "question": "What is a key advantage of a CTE over an inline subquery?",
                "options": [
                    "CTEs always run faster than subqueries",
                    "CTEs can be referenced multiple times in the same query",
                    "CTEs automatically create indexes",
                    "CTEs persist across multiple SQL statements",
                ],
                "answer": "CTEs can be referenced multiple times in the same query",
                "lesson": (
                    "A CTE can be referenced multiple times in the outer query, while an\n"
                    "inline subquery would need to be duplicated.\n\n"
                    "Example — using a CTE twice:\n"
                    "  WITH dept_stats AS (\n"
                    "    SELECT dept, AVG(salary) AS avg_sal FROM employees GROUP BY dept\n"
                    "  )\n"
                    "  SELECT e.name, e.salary, d.avg_sal\n"
                    "  FROM employees e\n"
                    "  JOIN dept_stats d ON e.dept = d.dept\n"
                    "  WHERE e.salary > (SELECT MAX(avg_sal) FROM dept_stats);\n\n"
                    "Note: CTEs do NOT persist across statements — they exist only within\n"
                    "the single query they are defined in."
                ),
                "xp": 75,
            },
            {
                "id": "cte_3",
                "type": "quiz",
                "title": "The Recursive Keyword",
                "question": "What two keywords introduce a recursive CTE in PostgreSQL?",
                "options": ["WITH RECURSIVE", "RECURSIVE WITH", "WITH LOOP", "LOOP QUERY"],
                "answer": "WITH RECURSIVE",
                "lesson": (
                    "WITH RECURSIVE allows a CTE to reference itself, enabling traversal\n"
                    "of hierarchical or graph-structured data.\n\n"
                    "Structure of a recursive CTE:\n"
                    "  WITH RECURSIVE cte AS (\n"
                    "    -- Base case (anchor member)\n"
                    "    SELECT ... WHERE condition\n"
                    "    UNION ALL\n"
                    "    -- Recursive case (references cte)\n"
                    "    SELECT ... FROM cte JOIN ... WHERE termination_condition\n"
                    "  )\n"
                    "  SELECT * FROM cte;\n\n"
                    "The recursion stops when the recursive member returns no rows."
                ),
                "xp": 75,
            },
            {
                "id": "cte_4",
                "type": "quiz",
                "title": "Recursive Anatomy",
                "question": "In a recursive CTE, what connects the base case (anchor member) to the recursive case?",
                "options": ["UNION ALL", "JOIN", "CONNECT BY", "RECURSIVE JOIN"],
                "answer": "UNION ALL",
                "lesson": (
                    "The anchor member and recursive member are connected by UNION ALL.\n\n"
                    "  WITH RECURSIVE hierarchy AS (\n"
                    "    SELECT id, name, manager_id, 1 AS depth   -- anchor\n"
                    "    FROM employees WHERE manager_id IS NULL\n"
                    "    UNION ALL\n"
                    "    SELECT e.id, e.name, e.manager_id, h.depth + 1  -- recursive\n"
                    "    FROM employees e JOIN hierarchy h ON e.manager_id = h.id\n"
                    "  )\n"
                    "  SELECT * FROM hierarchy;\n\n"
                    "UNION ALL preserves all rows (including duplicates). Use UNION to\n"
                    "deduplicate, but it adds overhead."
                ),
                "xp": 75,
            },
            {
                "id": "cte_5",
                "type": "text",
                "title": "Hierarchy Traversal",
                "question": "Recursive CTEs are commonly used to traverse what kind of data structure? (One word, starts with 'h')",
                "options": [],
                "answer": "hierarchy",
                "lesson": (
                    "Recursive CTEs excel at traversing hierarchical data:\n"
                    "  - Org charts (employee -> manager)\n"
                    "  - Category trees (child -> parent)\n"
                    "  - Bill of materials (component -> assembly)\n"
                    "  - File systems (file -> directory)\n"
                    "  - Graph paths (node -> connected node)\n\n"
                    "Always include a termination condition (e.g., depth limit or\n"
                    "visited-node tracking) to prevent infinite recursion."
                ),
                "xp": 75,
            },
            {
                "id": "cte_6",
                "type": "quiz",
                "title": "Materialization Control",
                "question": "In PostgreSQL, what does adding MATERIALIZED to a CTE do?",
                "options": [
                    "Forces the CTE result to be computed once and stored in a temp table",
                    "Creates a permanent materialized view",
                    "Writes the CTE result to disk as a file",
                    "Prevents the CTE from being re-evaluated",
                ],
                "answer": "Forces the CTE result to be computed once and stored in a temp table",
                "lesson": (
                    "WITH cte AS MATERIALIZED (SELECT ...) forces PostgreSQL to evaluate\n"
                    "the CTE once and store the result as a temporary worktable.\n\n"
                    "NOT MATERIALIZED allows the optimizer to inline the CTE into the\n"
                    "outer query (potentially applying filters from the outer query).\n\n"
                    "Since PostgreSQL 12, non-recursive CTEs used only once are\n"
                    "automatically inlined (NOT MATERIALIZED) by default.\n\n"
                    "Use MATERIALIZED when:\n"
                    "  - The CTE is referenced multiple times\n"
                    "  - You want to prevent filter pushdown (optimization fence)"
                ),
                "xp": 100,
            },
            {
                "id": "cte_7",
                "type": "quiz",
                "title": "Infinite Loop Prevention",
                "question": "What happens if a recursive CTE has no termination condition and generates infinite rows?",
                "options": [
                    "PostgreSQL automatically stops after 1000 iterations",
                    "The query runs until it hits a timeout or runs out of memory",
                    "PostgreSQL raises a RECURSION_LIMIT error after 100 iterations",
                    "The planner detects the infinite loop and refuses to execute",
                ],
                "answer": "The query runs until it hits a timeout or runs out of memory",
                "lesson": (
                    "PostgreSQL does NOT have a built-in recursion depth limit for\n"
                    "recursive CTEs. A runaway recursion will consume memory and time\n"
                    "until it's killed by a timeout or OOM.\n\n"
                    "Protect yourself:\n"
                    "  - Add a depth counter: depth + 1, and filter WHERE depth < 100\n"
                    "  - Track visited nodes with an array to detect cycles\n"
                    "  - Set statement_timeout as a safety net\n\n"
                    "Example cycle detection:\n"
                    "  WITH RECURSIVE traversal AS (\n"
                    "    SELECT id, ARRAY[id] AS visited FROM nodes WHERE ...\n"
                    "    UNION ALL\n"
                    "    SELECT n.id, t.visited || n.id\n"
                    "    FROM nodes n JOIN traversal t ON ...\n"
                    "    WHERE n.id != ALL(t.visited)  -- cycle guard\n"
                    "  )"
                ),
                "xp": 100,
            },
            {
                "id": "cte_boss",
                "type": "quiz",
                "title": "BOSS: The Recursive Extraction",
                "question": "You need to find all subordinates (direct and indirect) of employee_id = 1. Which recursive CTE is correct?",
                "options": [
                    "WITH RECURSIVE subs AS (SELECT * FROM employees WHERE id = 1 UNION ALL SELECT e.* FROM employees e JOIN subs s ON e.manager_id = s.id) SELECT * FROM subs",
                    "WITH RECURSIVE subs AS (SELECT * FROM employees WHERE manager_id = 1 UNION ALL SELECT e.* FROM employees e WHERE e.id IN (SELECT id FROM subs)) SELECT * FROM subs",
                    "WITH subs AS (SELECT * FROM employees CONNECT BY PRIOR id = manager_id START WITH id = 1) SELECT * FROM subs",
                    "WITH RECURSIVE subs AS (SELECT * FROM employees UNION ALL SELECT * FROM employees WHERE manager_id = subs.id) SELECT * FROM subs",
                ],
                "answer": "WITH RECURSIVE subs AS (SELECT * FROM employees WHERE id = 1 UNION ALL SELECT e.* FROM employees e JOIN subs s ON e.manager_id = s.id) SELECT * FROM subs",
                "lesson": (
                    "The correct pattern:\n"
                    "  1. Anchor: SELECT the root node (employee_id = 1)\n"
                    "  2. Recursive: JOIN employees to the CTE on manager_id = id\n"
                    "  3. UNION ALL combines all levels\n\n"
                    "CONNECT BY is Oracle syntax — not supported in PostgreSQL.\n"
                    "Subqueries referencing the CTE in WHERE (option 2) don't work because\n"
                    "the recursive reference must be in a FROM clause JOIN.\n\n"
                    "The result includes the root employee and all their direct and\n"
                    "indirect reports, forming a complete subtree of the org chart."
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
    "query_optimization": {
        "id": "query_optimization",
        "name": "The Optimization Core",
        "subtitle": "Query Optimization",
        "color": "yellow",
        "icon": "\u26a1",
        "commands": ["EXPLAIN", "EXPLAIN ANALYZE", "CREATE INDEX", "pg_stat_statements", "VACUUM ANALYZE", "BUFFERS"],
        "challenges": [
            {
                "id": "opt_1",
                "type": "quiz",
                "title": "The Plan Reader",
                "question": "What is the difference between EXPLAIN and EXPLAIN ANALYZE?",
                "options": [
                    "EXPLAIN shows the estimated plan; EXPLAIN ANALYZE actually executes the query and shows real timings",
                    "EXPLAIN works on SELECT only; EXPLAIN ANALYZE works on all statements",
                    "EXPLAIN shows the plan in text; EXPLAIN ANALYZE shows it in JSON",
                    "There is no difference — they are aliases",
                ],
                "answer": "EXPLAIN shows the estimated plan; EXPLAIN ANALYZE actually executes the query and shows real timings",
                "lesson": (
                    "EXPLAIN shows the planner's estimated execution plan WITHOUT running the query.\n"
                    "EXPLAIN ANALYZE actually EXECUTES the query and reports real timings.\n\n"
                    "CAUTION: EXPLAIN ANALYZE on INSERT/UPDATE/DELETE will actually modify data!\n"
                    "Wrap in a transaction and ROLLBACK to be safe.\n\n"
                    "Example:\n"
                    "  EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 42;\n\n"
                    "Output includes:\n"
                    "  - actual time (ms) per node\n"
                    "  - rows returned vs estimated\n"
                    "  - planning time and execution time"
                ),
                "xp": 50,
            },
            {
                "id": "opt_2",
                "type": "quiz",
                "title": "Scan Types",
                "question": "Which scan type reads every row in the table?",
                "options": ["Seq Scan", "Index Scan", "Index Only Scan", "Bitmap Scan"],
                "answer": "Seq Scan",
                "lesson": (
                    "Seq Scan (Sequential Scan) reads every row in the table from disk, in order.\n\n"
                    "It's the default when no useful index exists, or when the planner\n"
                    "estimates that most of the table will be returned anyway.\n\n"
                    "Scan types ranked by selectivity:\n"
                    "  Index Only Scan — reads only the index (covers all needed columns)\n"
                    "  Index Scan — uses index to find rows, then fetches from table\n"
                    "  Bitmap Index Scan — builds a bitmap from the index, then scans table\n"
                    "  Seq Scan — reads the entire table sequentially\n\n"
                    "A Seq Scan on a large table with a selective WHERE clause is usually\n"
                    "a sign that an index is needed."
                ),
                "xp": 75,
            },
            {
                "id": "opt_3",
                "type": "text",
                "title": "The Statistics Refresh",
                "question": "What PostgreSQL command updates table statistics so the query planner can make accurate cost estimates? (Two words)",
                "options": [],
                "answer": "VACUUM ANALYZE",
                "lesson": (
                    "VACUUM ANALYZE does two things:\n"
                    "  1. VACUUM — reclaims dead tuples (from UPDATE/DELETE) for reuse\n"
                    "  2. ANALYZE — updates pg_statistic with current column distributions\n\n"
                    "The planner uses these statistics to estimate row counts, selectivity,\n"
                    "and choose between Seq Scan vs Index Scan.\n\n"
                    "Stale statistics = bad query plans.\n\n"
                    "PostgreSQL runs autovacuum in the background, but after bulk\n"
                    "loads or major changes, a manual VACUUM ANALYZE is prudent."
                ),
                "xp": 75,
            },
            {
                "id": "opt_4",
                "type": "quiz",
                "title": "Index Selection",
                "question": "For the query SELECT * FROM orders WHERE status = 'shipped' AND created_at > '2024-01-01', which index would be MOST effective?",
                "options": [
                    "CREATE INDEX ON orders (status)",
                    "CREATE INDEX ON orders (created_at)",
                    "CREATE INDEX ON orders (status, created_at)",
                    "CREATE INDEX ON orders (created_at, status)",
                ],
                "answer": "CREATE INDEX ON orders (status, created_at)",
                "lesson": (
                    "For multi-column conditions, a composite index with the equality\n"
                    "column first and the range column second is most effective.\n\n"
                    "Rule of thumb for composite index column order:\n"
                    "  1. Equality conditions first (= )\n"
                    "  2. Range conditions last (>, <, BETWEEN)\n\n"
                    "Index on (status, created_at) can:\n"
                    "  - Jump directly to 'shipped' entries (equality)\n"
                    "  - Then scan the date range within that subset\n\n"
                    "Index on (created_at, status) would scan the date range first\n"
                    "(potentially large) and then filter by status — less efficient."
                ),
                "xp": 100,
            },
            {
                "id": "opt_5",
                "type": "quiz",
                "title": "The Cost Model",
                "question": "In EXPLAIN output, what do the two numbers in 'cost=0.15..8.17' represent?",
                "options": [
                    "Startup cost and total cost (in arbitrary planner units)",
                    "Minimum and maximum execution time in milliseconds",
                    "CPU cost and I/O cost",
                    "Estimated and actual row counts",
                ],
                "answer": "Startup cost and total cost (in arbitrary planner units)",
                "lesson": (
                    "EXPLAIN cost numbers are in arbitrary planner units (not milliseconds).\n\n"
                    "  cost=0.15..8.17\n"
                    "        ^       ^\n"
                    "  startup cost   total cost\n\n"
                    "  Startup cost: work before the first row can be returned\n"
                    "  Total cost: estimated total work to return all rows\n\n"
                    "The planner uses these costs to compare alternative plans.\n"
                    "Lower total cost = preferred plan.\n\n"
                    "To see real timings, use EXPLAIN ANALYZE which adds:\n"
                    "  actual time=0.012..0.045 rows=10 loops=1"
                ),
                "xp": 100,
            },
            {
                "id": "opt_6",
                "type": "quiz",
                "title": "Buffer Intelligence",
                "question": "What does adding BUFFERS to EXPLAIN ANALYZE show?",
                "options": [
                    "The number of shared and local buffer hits and reads (cache vs disk I/O)",
                    "The total memory allocated by the query",
                    "The WAL buffer usage for the transaction",
                    "The connection pool buffer utilization",
                ],
                "answer": "The number of shared and local buffer hits and reads (cache vs disk I/O)",
                "lesson": (
                    "EXPLAIN (ANALYZE, BUFFERS) adds buffer usage statistics:\n\n"
                    "  Buffers: shared hit=128 read=32\n\n"
                    "  shared hit — pages found in PostgreSQL's shared buffer cache\n"
                    "  shared read — pages that had to be read from disk (or OS cache)\n\n"
                    "High read counts relative to hits indicate poor cache utilization.\n"
                    "This is critical for diagnosing I/O-bound queries.\n\n"
                    "Example:\n"
                    "  EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM large_table WHERE id = 42;"
                ),
                "xp": 100,
            },
            {
                "id": "opt_7",
                "type": "quiz",
                "title": "Partial Indexes",
                "question": "What is a partial index?",
                "options": [
                    "An index that only covers some columns of the table",
                    "An index with a WHERE clause that includes only rows matching a condition",
                    "An index that is still being built",
                    "An index that uses partial key matching for LIKE queries",
                ],
                "answer": "An index with a WHERE clause that includes only rows matching a condition",
                "lesson": (
                    "A partial index includes only rows that satisfy a predicate.\n\n"
                    "  CREATE INDEX idx_active_orders ON orders (created_at)\n"
                    "    WHERE status = 'active';\n\n"
                    "Benefits:\n"
                    "  - Smaller index size (fewer rows indexed)\n"
                    "  - Faster to scan and maintain\n"
                    "  - Perfect for queries that always include the same filter\n\n"
                    "The query planner will use the partial index only when the query's\n"
                    "WHERE clause implies the index predicate."
                ),
                "xp": 100,
            },
            {
                "id": "opt_boss",
                "type": "quiz",
                "title": "BOSS: The Production Crisis",
                "question": "EXPLAIN ANALYZE shows a Seq Scan on a 50M row table with 'Filter: (status = shipped)' removing 49.9M rows. estimated rows=50000000, actual rows=100000. What is the BEST fix?",
                "options": [
                    "Add more RAM to increase shared_buffers",
                    "CREATE INDEX ON orders (status) — then re-run the query",
                    "Rewrite the query to use a subquery instead of WHERE",
                    "Run VACUUM FULL to reclaim disk space",
                ],
                "answer": "CREATE INDEX ON orders (status) — then re-run the query",
                "lesson": (
                    "When EXPLAIN ANALYZE shows a Seq Scan filtering out 99.8% of rows,\n"
                    "the problem is a missing index.\n\n"
                    "Diagnostic checklist:\n"
                    "  1. Seq Scan + Filter removing most rows = missing index\n"
                    "  2. estimated rows far from actual rows = stale statistics (ANALYZE)\n"
                    "  3. High shared read count = cold cache or table too large for memory\n\n"
                    "After creating the index:\n"
                    "  - The Seq Scan becomes an Index Scan\n"
                    "  - Instead of reading 50M rows, PostgreSQL reads ~100K directly\n"
                    "  - Query time drops from seconds to milliseconds"
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
    "transactions_locking": {
        "id": "transactions_locking",
        "name": "The Isolation Chamber",
        "subtitle": "Transactions & Locking",
        "color": "red",
        "icon": "\U0001f512",
        "commands": ["BEGIN", "COMMIT", "ROLLBACK", "SAVEPOINT", "SET TRANSACTION ISOLATION LEVEL", "SELECT FOR UPDATE"],
        "challenges": [
            {
                "id": "txn_1",
                "type": "quiz",
                "title": "The ACID Doctrine",
                "question": "What does the 'I' in ACID stand for?",
                "options": ["Integrity", "Isolation", "Immutability", "Indexing"],
                "answer": "Isolation",
                "lesson": (
                    "ACID properties of transactions:\n"
                    "  A — Atomicity: all or nothing (commit or rollback entirely)\n"
                    "  C — Consistency: database moves between valid states\n"
                    "  I — Isolation: concurrent transactions don't interfere\n"
                    "  D — Durability: committed data survives crashes\n\n"
                    "Isolation is what prevents Transaction A from seeing Transaction B's\n"
                    "uncommitted changes. The degree of isolation is configurable."
                ),
                "xp": 50,
            },
            {
                "id": "txn_2",
                "type": "quiz",
                "title": "Default Isolation",
                "question": "What is PostgreSQL's default transaction isolation level?",
                "options": ["READ UNCOMMITTED", "READ COMMITTED", "REPEATABLE READ", "SERIALIZABLE"],
                "answer": "READ COMMITTED",
                "lesson": (
                    "PostgreSQL's default isolation level is READ COMMITTED.\n\n"
                    "In READ COMMITTED:\n"
                    "  - Each statement sees only data committed before that statement began\n"
                    "  - Different statements in the same transaction can see different data\n"
                    "    (if other transactions commit between them)\n\n"
                    "This means non-repeatable reads and phantom reads are possible.\n\n"
                    "PostgreSQL actually implements READ UNCOMMITTED as READ COMMITTED —\n"
                    "dirty reads are never allowed in PostgreSQL."
                ),
                "xp": 75,
            },
            {
                "id": "txn_3",
                "type": "quiz",
                "title": "Phantom Reads",
                "question": "A phantom read occurs when a transaction re-executes a query and finds NEW rows that weren't there before. Which is the LOWEST isolation level that prevents phantom reads in PostgreSQL?",
                "options": ["READ UNCOMMITTED", "READ COMMITTED", "REPEATABLE READ", "SERIALIZABLE"],
                "answer": "REPEATABLE READ",
                "lesson": (
                    "In PostgreSQL, REPEATABLE READ prevents phantom reads.\n\n"
                    "This differs from the SQL standard, where REPEATABLE READ allows\n"
                    "phantoms and only SERIALIZABLE prevents them.\n\n"
                    "PostgreSQL's REPEATABLE READ uses snapshot isolation:\n"
                    "  - The transaction sees a snapshot of the database as of its start\n"
                    "  - No other transaction's commits are visible after that point\n"
                    "  - If a concurrent transaction modifies the same rows, the second\n"
                    "    transaction gets a serialization error and must retry\n\n"
                    "SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;"
                ),
                "xp": 100,
            },
            {
                "id": "txn_4",
                "type": "text",
                "title": "The Checkpoint",
                "question": "What SQL command creates a named checkpoint within a transaction that you can roll back to? (One word)",
                "options": [],
                "answer": "SAVEPOINT",
                "lesson": (
                    "SAVEPOINT creates a named point within a transaction.\n\n"
                    "  BEGIN;\n"
                    "    INSERT INTO orders VALUES (...);\n"
                    "    SAVEPOINT before_update;\n"
                    "    UPDATE accounts SET balance = balance - 100;\n"
                    "    -- Oops, wrong amount\n"
                    "    ROLLBACK TO SAVEPOINT before_update;\n"
                    "    UPDATE accounts SET balance = balance - 50;\n"
                    "  COMMIT;\n\n"
                    "ROLLBACK TO SAVEPOINT undoes everything after the savepoint\n"
                    "without aborting the entire transaction. The savepoint remains\n"
                    "active and can be rolled back to again."
                ),
                "xp": 75,
            },
            {
                "id": "txn_5",
                "type": "quiz",
                "title": "Row-Level Locking",
                "question": "What does SELECT ... FOR UPDATE do?",
                "options": [
                    "Locks the selected rows so no other transaction can modify or lock them until this transaction ends",
                    "Automatically updates the selected rows",
                    "Selects rows that are currently being updated by another transaction",
                    "Creates an exclusive lock on the entire table",
                ],
                "answer": "Locks the selected rows so no other transaction can modify or lock them until this transaction ends",
                "lesson": (
                    "SELECT ... FOR UPDATE acquires row-level exclusive locks.\n\n"
                    "  BEGIN;\n"
                    "  SELECT * FROM accounts WHERE id = 1 FOR UPDATE;\n"
                    "  -- Row is now locked. Other transactions trying to UPDATE or\n"
                    "  -- SELECT FOR UPDATE this row will WAIT until we COMMIT/ROLLBACK.\n"
                    "  UPDATE accounts SET balance = balance - 100 WHERE id = 1;\n"
                    "  COMMIT;\n\n"
                    "Variants:\n"
                    "  FOR UPDATE — exclusive lock, blocks other FOR UPDATE and modifications\n"
                    "  FOR SHARE — shared lock, allows other FOR SHARE but blocks FOR UPDATE\n"
                    "  FOR UPDATE NOWAIT — fails immediately instead of waiting\n"
                    "  FOR UPDATE SKIP LOCKED — skips locked rows (useful for job queues)"
                ),
                "xp": 100,
            },
            {
                "id": "txn_6",
                "type": "quiz",
                "title": "Deadlock Detection",
                "question": "How does PostgreSQL handle deadlocks?",
                "options": [
                    "It automatically detects deadlocks and aborts one of the transactions",
                    "It prevents deadlocks by not allowing concurrent transactions",
                    "It waits indefinitely until one transaction times out",
                    "It uses lock ordering to prevent deadlocks from occurring",
                ],
                "answer": "It automatically detects deadlocks and aborts one of the transactions",
                "lesson": (
                    "PostgreSQL runs a deadlock detector (default check interval: 1 second).\n\n"
                    "When a deadlock is detected, PostgreSQL aborts one of the transactions\n"
                    "with: ERROR: deadlock detected\n\n"
                    "Prevention strategies:\n"
                    "  - Always lock resources in the same order across transactions\n"
                    "  - Keep transactions short\n"
                    "  - Use NOWAIT or lock_timeout to fail fast instead of waiting\n"
                    "  - Use advisory locks for application-level coordination\n\n"
                    "The deadlock_timeout setting (default 1s) controls how long a\n"
                    "transaction waits before the deadlock detector checks."
                ),
                "xp": 100,
            },
            {
                "id": "txn_7",
                "type": "quiz",
                "title": "MVCC Fundamentals",
                "question": "What concurrency control mechanism does PostgreSQL use to allow readers and writers to operate concurrently without blocking each other?",
                "options": [
                    "MVCC (Multi-Version Concurrency Control)",
                    "Two-Phase Locking (2PL)",
                    "Optimistic Concurrency Control (OCC)",
                    "Timestamp Ordering",
                ],
                "answer": "MVCC (Multi-Version Concurrency Control)",
                "lesson": (
                    "PostgreSQL uses MVCC — each transaction sees a snapshot of the data\n"
                    "as it existed at a certain point in time.\n\n"
                    "How it works:\n"
                    "  - UPDATE doesn't overwrite the old row — it creates a new version\n"
                    "  - DELETE marks the row as invisible to future transactions\n"
                    "  - Each row version has xmin (creating transaction) and xmax (deleting transaction)\n"
                    "  - Readers see only versions visible to their snapshot\n\n"
                    "Key consequence: readers never block writers, writers never block readers.\n\n"
                    "The old versions (dead tuples) are cleaned up by VACUUM."
                ),
                "xp": 100,
            },
            {
                "id": "txn_boss",
                "type": "quiz",
                "title": "BOSS: The Isolation Breach",
                "question": "Transaction A reads account balance ($1000). Transaction B transfers $200 out and commits. Transaction A reads balance again and sees $800. At what isolation level is this possible?",
                "options": [
                    "READ COMMITTED only",
                    "READ COMMITTED and REPEATABLE READ",
                    "REPEATABLE READ and SERIALIZABLE",
                    "All isolation levels",
                ],
                "answer": "READ COMMITTED only",
                "lesson": (
                    "This is a non-repeatable read: the same query returns different\n"
                    "results within the same transaction because another transaction committed.\n\n"
                    "  READ COMMITTED — allows this. Each statement sees the latest committed data.\n"
                    "  REPEATABLE READ — prevents this. The snapshot is fixed at transaction start.\n"
                    "  SERIALIZABLE — prevents this (stricter than REPEATABLE READ).\n\n"
                    "In PostgreSQL, REPEATABLE READ uses snapshot isolation:\n"
                    "  - Transaction A's snapshot is taken at the first statement\n"
                    "  - All subsequent reads see that same snapshot\n"
                    "  - Transaction B's commit is invisible to Transaction A"
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
    "advanced_patterns": {
        "id": "advanced_patterns",
        "name": "The Pattern Vault",
        "subtitle": "Advanced SQL Patterns",
        "color": "green",
        "icon": "\u2726",
        "commands": ["LATERAL JOIN", "GROUPING SETS", "CUBE", "ROLLUP", "jsonb_path_query", "to_tsvector", "ts_query"],
        "challenges": [
            {
                "id": "adv_1",
                "type": "quiz",
                "title": "The Lateral Gateway",
                "question": "What does a LATERAL join allow that a regular join does not?",
                "options": [
                    "The subquery on the right side can reference columns from the left side",
                    "It allows joining more than two tables at once",
                    "It creates a cross join with filtering",
                    "It enables joining tables from different schemas",
                ],
                "answer": "The subquery on the right side can reference columns from the left side",
                "lesson": (
                    "LATERAL allows a subquery in FROM to reference columns from preceding\n"
                    "FROM items — like a correlated subquery, but in the FROM clause.\n\n"
                    "Example — get the 3 most recent orders per customer:\n"
                    "  SELECT c.name, o.*\n"
                    "  FROM customers c\n"
                    "  CROSS JOIN LATERAL (\n"
                    "    SELECT * FROM orders\n"
                    "    WHERE customer_id = c.id   -- references 'c' from the left side\n"
                    "    ORDER BY created_at DESC\n"
                    "    LIMIT 3\n"
                    "  ) o;\n\n"
                    "Without LATERAL, the subquery cannot see c.id."
                ),
                "xp": 100,
            },
            {
                "id": "adv_2",
                "type": "quiz",
                "title": "Multi-Dimensional Grouping",
                "question": "What does GROUPING SETS allow you to do?",
                "options": [
                    "Define multiple GROUP BY groupings in a single query",
                    "Group by sets of rows instead of columns",
                    "Create nested groups within groups",
                    "Group by dynamically computed column values",
                ],
                "answer": "Define multiple GROUP BY groupings in a single query",
                "lesson": (
                    "GROUPING SETS lets you compute aggregates for multiple groupings\n"
                    "in one query — equivalent to UNION ALL of separate GROUP BY queries.\n\n"
                    "  SELECT region, product, SUM(revenue)\n"
                    "  FROM sales\n"
                    "  GROUP BY GROUPING SETS (\n"
                    "    (region, product),  -- per region+product\n"
                    "    (region),           -- per region total\n"
                    "    (product),          -- per product total\n"
                    "    ()                  -- grand total\n"
                    "  );\n\n"
                    "Shorthand:\n"
                    "  CUBE(region, product) — all possible combinations (same as above)\n"
                    "  ROLLUP(region, product) — hierarchical: (region,product), (region), ()"
                ),
                "xp": 100,
            },
            {
                "id": "adv_3",
                "type": "quiz",
                "title": "ROLLUP vs CUBE",
                "question": "GROUP BY ROLLUP(a, b, c) generates grouping sets for which combinations?",
                "options": [
                    "(a,b,c), (a,b), (a), ()",
                    "(a,b,c), (a,b), (a,c), (b,c), (a), (b), (c), ()",
                    "(a,b,c) and () only",
                    "(a,b,c), (b,c), (c), ()",
                ],
                "answer": "(a,b,c), (a,b), (a), ()",
                "lesson": (
                    "ROLLUP generates a hierarchical set of groupings by progressively\n"
                    "removing columns from right to left.\n\n"
                    "  ROLLUP(a, b, c) produces:\n"
                    "    (a, b, c)  — most detailed\n"
                    "    (a, b)     — subtotal removing c\n"
                    "    (a)        — subtotal removing b and c\n"
                    "    ()         — grand total\n\n"
                    "  CUBE(a, b, c) produces ALL 2^3 = 8 combinations.\n\n"
                    "ROLLUP is ideal for hierarchical data (year -> quarter -> month).\n"
                    "CUBE is for cross-tabulation reports where all combinations matter."
                ),
                "xp": 100,
            },
            {
                "id": "adv_4",
                "type": "text",
                "title": "JSON Path Extraction",
                "question": "What PostgreSQL operator extracts a JSON object field as TEXT (not as JSON)? (Enter the operator symbol)",
                "options": [],
                "answer": "->>",
                "lesson": (
                    "JSON/JSONB field extraction operators:\n\n"
                    "  ->   extracts field as JSON/JSONB (preserves type)\n"
                    "  ->>  extracts field as TEXT\n\n"
                    "  data -> 'name'       returns '\"Alice\"' (JSON string)\n"
                    "  data ->> 'name'      returns 'Alice' (text)\n\n"
                    "For nested access, chain operators:\n"
                    "  data -> 'address' ->> 'city'\n\n"
                    "For array elements, use an integer index:\n"
                    "  data -> 'tags' ->> 0   returns the first tag as text\n\n"
                    "When comparing or filtering, ->> is usually what you want\n"
                    "because it returns text that can be cast to other types."
                ),
                "xp": 75,
            },
            {
                "id": "adv_5",
                "type": "quiz",
                "title": "JSONB Containment",
                "question": "Which operator tests if the left JSONB value contains the right JSONB value?",
                "options": ["@>", "<@", "?", "->"],
                "answer": "@>",
                "lesson": (
                    "JSONB containment operators:\n\n"
                    "  @>  left contains right: '{\"a\":1, \"b\":2}' @> '{\"a\":1}' = true\n"
                    "  <@  left is contained by right (reverse)\n\n"
                    "  ?   key exists: '{\"a\":1}' ? 'a' = true\n"
                    "  ?|  any key exists\n"
                    "  ?&  all keys exist\n\n"
                    "Containment (@>) is indexable with GIN indexes:\n"
                    "  CREATE INDEX ON events USING gin (metadata);\n"
                    "  SELECT * FROM events WHERE metadata @> '{\"type\": \"error\"}';\n\n"
                    "This is the recommended way to query JSONB at scale."
                ),
                "xp": 100,
            },
            {
                "id": "adv_6",
                "type": "text",
                "title": "Full-Text Vector",
                "question": "What PostgreSQL function converts a text string into a tsvector for full-text search? (Function name with no parentheses)",
                "options": [],
                "answer": "to_tsvector",
                "lesson": (
                    "PostgreSQL full-text search converts text to searchable tokens.\n\n"
                    "  to_tsvector('english', 'The quick brown fox jumped')\n"
                    "  → 'brown':3 'fox':4 'jump':5 'quick':2\n\n"
                    "  to_tsquery('english', 'quick & fox')\n"
                    "  → 'quick' & 'fox'\n\n"
                    "Search with @@:\n"
                    "  SELECT * FROM articles\n"
                    "  WHERE to_tsvector('english', body) @@ to_tsquery('english', 'database & performance');\n\n"
                    "For performance, store the tsvector in a column and create a GIN index:\n"
                    "  ALTER TABLE articles ADD COLUMN body_tsv tsvector;\n"
                    "  CREATE INDEX ON articles USING gin (body_tsv);"
                ),
                "xp": 100,
            },
            {
                "id": "adv_7",
                "type": "quiz",
                "title": "The FILTER Clause",
                "question": "What does the FILTER clause do when used with an aggregate function?",
                "options": [
                    "Applies a WHERE-like condition to only the rows going into that specific aggregate",
                    "Filters the final output of the aggregate",
                    "Replaces the HAVING clause for the aggregate",
                    "Applies a filter to the window frame",
                ],
                "answer": "Applies a WHERE-like condition to only the rows going into that specific aggregate",
                "lesson": (
                    "FILTER allows conditional aggregation — applying different conditions\n"
                    "to different aggregates in the same query.\n\n"
                    "  SELECT\n"
                    "    COUNT(*) AS total_orders,\n"
                    "    COUNT(*) FILTER (WHERE status = 'shipped') AS shipped_orders,\n"
                    "    SUM(amount) FILTER (WHERE status = 'refunded') AS refund_total\n"
                    "  FROM orders;\n\n"
                    "Without FILTER, you'd need CASE expressions:\n"
                    "  COUNT(CASE WHEN status = 'shipped' THEN 1 END)\n\n"
                    "FILTER is PostgreSQL-specific (not in MySQL/SQLite) and more readable\n"
                    "than CASE-based conditional aggregation."
                ),
                "xp": 100,
            },
            {
                "id": "adv_boss",
                "type": "quiz",
                "title": "BOSS: The Pattern Extraction",
                "question": "You need a report showing revenue by (region, category), by region only, by category only, and a grand total — all in one query. Which approach is correct?",
                "options": [
                    "SELECT region, category, SUM(revenue) FROM sales GROUP BY CUBE(region, category)",
                    "SELECT region, category, SUM(revenue) FROM sales GROUP BY ROLLUP(region, category)",
                    "SELECT region, category, SUM(revenue) FROM sales GROUP BY region, category WITH TOTALS",
                    "SELECT region, category, SUM(revenue) FROM sales GROUP BY ALL(region, category)",
                ],
                "answer": "SELECT region, category, SUM(revenue) FROM sales GROUP BY CUBE(region, category)",
                "lesson": (
                    "CUBE(region, category) generates all 2^2 = 4 grouping sets:\n"
                    "  (region, category) — detail rows\n"
                    "  (region)           — subtotal per region\n"
                    "  (category)         — subtotal per category\n"
                    "  ()                 — grand total\n\n"
                    "ROLLUP(region, category) would only give:\n"
                    "  (region, category), (region), () — missing the per-category subtotal.\n\n"
                    "Use GROUPING(column) function to distinguish NULL from 'all values':\n"
                    "  SELECT\n"
                    "    CASE WHEN GROUPING(region) = 1 THEN 'ALL' ELSE region END,\n"
                    "    SUM(revenue)\n"
                    "  FROM sales\n"
                    "  GROUP BY CUBE(region, category);"
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
}

ZONE_ORDER = [
    "window_functions",
    "ctes_recursive",
    "query_optimization",
    "transactions_locking",
    "advanced_patterns",
]
