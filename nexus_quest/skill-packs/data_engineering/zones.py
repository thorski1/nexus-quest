"""
zones.py — Data Engineering zones and challenges for Data Forge.

8 zones, ~45 challenges. All challenges use "type": "quiz" with
multiple-choice options (a/b/c/d) and two hints each.
"""

ZONE_ORDER = [
    "data_pipelines",
    "data_warehouses",
    "streaming",
    "data_lakes",
    "spark",
    "data_quality",
    "orchestration",
    "modern_stack",
]

ZONES = {
    # ── ZONE 1: DATA PIPELINES ─────────────────────────────────────────
    "data_pipelines": {
        "id": "data_pipelines",
        "name": "The Pipeline Foundry",
        "subtitle": "ETL vs ELT, Batch vs Streaming, DAGs & Airflow",
        "color": "cyan",
        "icon": "🔧",
        "commands": ["etl", "elt", "batch", "streaming", "dag", "airflow"],
        "challenges": [
            {
                "id": "pipe_1",
                "type": "quiz",
                "title": "ETL vs ELT",
                "question": (
                    "Your company loads raw clickstream data into a cloud data warehouse,\n"
                    "then transforms it using SQL views and dbt models.\n\n"
                    "Which pattern is this?"
                ),
                "lesson": (
                    "ELT (Extract, Load, Transform) loads raw data into the target system first,\n"
                    "then transforms it in place using the warehouse's compute power.\n\n"
                    "ETL (Extract, Transform, Load) transforms data before loading it.\n"
                    "Historically popular when storage was expensive and warehouse compute was limited.\n\n"
                    "ELT is the modern default because:\n"
                    "  - Cloud warehouses have massive compute (Snowflake, BigQuery)\n"
                    "  - Raw data is preserved for re-transformation\n"
                    "  - Transformations are versioned in SQL/dbt, not buried in ETL scripts"
                ),
                "options": [
                    "ETL — transform before loading",
                    "ELT — load first, transform in the warehouse",
                    "Reverse ETL — push warehouse data to SaaS tools",
                    "CDC — capture changes from the source database",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The data lands raw in the warehouse, then gets transformed there.",
                    "Load first, transform second = ELT.",
                ],
            },
            {
                "id": "pipe_2",
                "type": "quiz",
                "title": "Batch vs Streaming",
                "question": (
                    "A nightly cron job extracts the day's sales records from Postgres,\n"
                    "transforms them, and loads them into the warehouse at 2 AM.\n\n"
                    "What type of pipeline is this?"
                ),
                "lesson": (
                    "Batch processing handles data in discrete chunks on a schedule.\n\n"
                    "Characteristics:\n"
                    "  - Runs on a schedule (hourly, daily, weekly)\n"
                    "  - Processes a bounded dataset (yesterday's data, last hour's logs)\n"
                    "  - Higher latency (data is stale until the next batch runs)\n"
                    "  - Simpler to build, debug, and reason about\n\n"
                    "Streaming processes data continuously as it arrives.\n"
                    "  - Sub-second to seconds of latency\n"
                    "  - Unbounded dataset (the stream never ends)\n"
                    "  - More complex: backpressure, ordering, exactly-once semantics"
                ),
                "options": [
                    "Streaming pipeline",
                    "Batch pipeline",
                    "Micro-batch pipeline",
                    "Lambda architecture",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It runs once a day on a schedule, processing a fixed set of records.",
                    "Scheduled, bounded data = batch.",
                ],
            },
            {
                "id": "pipe_3",
                "type": "quiz",
                "title": "DAG Fundamentals",
                "question": (
                    "In Airflow, tasks are organized into a DAG.\n"
                    "Task B depends on Task A. Task C depends on Task A.\n"
                    "Task D depends on both B and C.\n\n"
                    "What does DAG stand for?"
                ),
                "lesson": (
                    "DAG = Directed Acyclic Graph.\n\n"
                    "  Directed — edges have direction (A -> B means A must run before B)\n"
                    "  Acyclic  — no cycles (you can't have A -> B -> C -> A)\n"
                    "  Graph    — a set of nodes (tasks) connected by edges (dependencies)\n\n"
                    "DAGs are the fundamental abstraction in orchestration tools because\n"
                    "they guarantee a valid execution order exists. If there were cycles,\n"
                    "no task could start — each would be waiting on another in an infinite loop."
                ),
                "options": [
                    "Directed Acyclic Graph",
                    "Data Analysis Group",
                    "Distributed Application Gateway",
                    "Dynamic Allocation Grid",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "It's a graph theory term — nodes and edges with no cycles.",
                    "Directed Acyclic G___.",
                ],
            },
            {
                "id": "pipe_4",
                "type": "quiz",
                "title": "Idempotent Pipelines",
                "question": (
                    "Your daily pipeline fails halfway through. You re-run it.\n"
                    "It produces the same output as if it had succeeded the first time.\n\n"
                    "What property does this pipeline have?"
                ),
                "lesson": (
                    "Idempotency — running the same operation multiple times produces the same result.\n\n"
                    "Critical for data pipelines because failures are inevitable:\n"
                    "  - Network timeouts, OOM kills, source system outages\n"
                    "  - Re-running a non-idempotent pipeline creates duplicates or corruption\n\n"
                    "Common idempotency patterns:\n"
                    "  - UPSERT instead of INSERT (merge on primary key)\n"
                    "  - DELETE + INSERT for the partition being processed\n"
                    "  - Write to a staging table, then atomic swap\n"
                    "  - Use deterministic file names in object storage"
                ),
                "options": [
                    "Atomicity",
                    "Idempotency",
                    "Eventual consistency",
                    "Fault tolerance",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Re-running produces identical results — no duplicates, no side effects.",
                    "The mathematical term: f(f(x)) = f(x).",
                ],
            },
            {
                "id": "pipe_5",
                "type": "quiz",
                "title": "Backfilling",
                "question": (
                    "You discover a bug in your transformation logic that has been\n"
                    "producing incorrect aggregations for the last 30 days.\n"
                    "You fix the code and re-run the pipeline for each of those 30 days.\n\n"
                    "What is this operation called?"
                ),
                "lesson": (
                    "Backfilling = re-running a pipeline for historical time periods.\n\n"
                    "Common triggers:\n"
                    "  - Bug fix that requires reprocessing past data\n"
                    "  - New column or metric added that needs historical values\n"
                    "  - Source data was corrected retroactively\n\n"
                    "Backfilling requires:\n"
                    "  - Idempotent pipelines (safe to re-run without duplicates)\n"
                    "  - Parameterized execution dates (process any date, not just today)\n"
                    "  - Partitioned output (rewrite only affected partitions)\n\n"
                    "Airflow supports backfilling natively with 'airflow dags backfill'."
                ),
                "options": [
                    "Data replay",
                    "Backfilling",
                    "Rehydration",
                    "Schema migration",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "You're filling in corrected data for past dates.",
                    "Back + filling = processing historical periods again.",
                ],
            },
            {
                "id": "pipe_6",
                "type": "quiz",
                "title": "Airflow Core Concept",
                "question": (
                    "In Apache Airflow, what is the role of the Scheduler?\n"
                ),
                "lesson": (
                    "The Airflow Scheduler is the core process that:\n\n"
                    "  1. Parses DAG files to discover tasks and dependencies\n"
                    "  2. Determines which tasks are ready to run (dependencies met + schedule due)\n"
                    "  3. Submits ready tasks to the Executor for execution\n\n"
                    "Airflow architecture:\n"
                    "  Scheduler  — decides WHAT runs and WHEN\n"
                    "  Executor   — decides WHERE tasks run (local, Celery, Kubernetes)\n"
                    "  Worker     — the process that actually executes the task code\n"
                    "  Webserver  — the UI for monitoring DAGs and task states\n"
                    "  Metadata DB — stores DAG state, task history, connections, variables"
                ),
                "options": [
                    "Executes task code on worker nodes",
                    "Serves the web UI for monitoring DAGs",
                    "Parses DAGs, determines ready tasks, and submits them for execution",
                    "Stores task state and run history in the metadata database",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The Scheduler doesn't execute tasks itself — it decides what's ready.",
                    "Parse, evaluate dependencies, submit to executor.",
                ],
            },
        ],
    },

    # ── ZONE 2: DATA WAREHOUSES ─────────────────────────────────────────
    "data_warehouses": {
        "id": "data_warehouses",
        "name": "The Warehouse Vault",
        "subtitle": "Star Schema, Snowflake Schema, Facts, Dimensions & OLAP",
        "color": "yellow",
        "icon": "🏛",
        "commands": ["star-schema", "snowflake-schema", "fact-table", "dimension", "olap", "oltp"],
        "challenges": [
            {
                "id": "wh_1",
                "type": "quiz",
                "title": "OLTP vs OLAP",
                "question": (
                    "Your production Postgres database handles thousands of INSERT and UPDATE\n"
                    "transactions per second from your web application.\n\n"
                    "Is this an OLTP or OLAP system?"
                ),
                "lesson": (
                    "OLTP (Online Transaction Processing):\n"
                    "  - Optimized for many small read/write transactions\n"
                    "  - Normalized schema (3NF) to minimize write overhead\n"
                    "  - Row-oriented storage (entire rows stored together)\n"
                    "  - Examples: Postgres, MySQL, SQL Server for production apps\n\n"
                    "OLAP (Online Analytical Processing):\n"
                    "  - Optimized for complex analytical queries over large datasets\n"
                    "  - Denormalized schema (star/snowflake) for fast aggregations\n"
                    "  - Columnar storage (columns stored together for compression + scan speed)\n"
                    "  - Examples: Snowflake, BigQuery, Redshift, ClickHouse"
                ),
                "options": [
                    "OLAP — optimized for analytical queries",
                    "OLTP — optimized for transactional read/write operations",
                    "HTAP — hybrid transactional and analytical",
                    "DSS — decision support system",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "High-frequency inserts and updates from a web app = transactional workload.",
                    "OLTP = Online Transaction Processing.",
                ],
            },
            {
                "id": "wh_2",
                "type": "quiz",
                "title": "Star Schema",
                "question": (
                    "You design a warehouse model with a central 'sales_fact' table\n"
                    "connected directly to 'dim_product', 'dim_store', 'dim_date',\n"
                    "and 'dim_customer'. No dimension references another dimension.\n\n"
                    "What schema design is this?"
                ),
                "lesson": (
                    "Star Schema — the most common data warehouse modeling pattern.\n\n"
                    "Structure:\n"
                    "  - Central fact table (measurements: revenue, quantity, clicks)\n"
                    "  - Dimension tables radiate outward (who, what, when, where)\n"
                    "  - Dimensions connect directly to the fact table — not to each other\n\n"
                    "Advantages:\n"
                    "  - Simple to understand and query (few JOINs)\n"
                    "  - Optimized for aggregation queries\n"
                    "  - Works well with BI tools (Looker, Tableau, Power BI)\n\n"
                    "Named 'star' because the diagram looks like a star — fact in the center,\n"
                    "dimensions radiating out."
                ),
                "options": [
                    "Star schema",
                    "Snowflake schema",
                    "Third normal form (3NF)",
                    "Data vault",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "Fact in the center, dimensions around it, no dimension-to-dimension joins.",
                    "It looks like a star when you draw it.",
                ],
            },
            {
                "id": "wh_3",
                "type": "quiz",
                "title": "Snowflake Schema",
                "question": (
                    "Your 'dim_product' dimension is normalized: it references\n"
                    "'dim_category', which references 'dim_department'.\n"
                    "Dimensions reference other dimensions.\n\n"
                    "What schema design is this?"
                ),
                "lesson": (
                    "Snowflake Schema — a normalized variation of the star schema.\n\n"
                    "  - Dimension tables are broken into sub-dimensions\n"
                    "  - dim_product -> dim_category -> dim_department\n"
                    "  - Reduces data redundancy in dimensions\n"
                    "  - Requires more JOINs for queries\n\n"
                    "Trade-offs vs Star Schema:\n"
                    "  + Less storage (normalized dimensions)\n"
                    "  + Easier to maintain dimension hierarchies\n"
                    "  - More complex queries (more JOINs)\n"
                    "  - Slower query performance in some warehouses\n\n"
                    "Named 'snowflake' because the branching dimensions look like\n"
                    "snowflake arms radiating outward."
                ),
                "options": [
                    "Star schema",
                    "Snowflake schema",
                    "Galaxy schema",
                    "Normalized OLTP schema",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Dimensions reference other dimensions — that's normalization within the schema.",
                    "Branching dimensions = snowflake.",
                ],
            },
            {
                "id": "wh_4",
                "type": "quiz",
                "title": "Fact vs Dimension",
                "question": (
                    "A table contains columns: order_id, product_key, customer_key,\n"
                    "store_key, order_date_key, quantity, revenue, discount_amount.\n\n"
                    "Is this a fact table or a dimension table?"
                ),
                "lesson": (
                    "Fact Table — stores quantitative measurements (metrics/events).\n\n"
                    "Characteristics:\n"
                    "  - Contains foreign keys to dimension tables\n"
                    "  - Contains numeric measures (revenue, quantity, duration)\n"
                    "  - Very large (millions to billions of rows)\n"
                    "  - Append-mostly (new events/transactions added continuously)\n\n"
                    "Dimension Table — stores descriptive context (who, what, where, when).\n"
                    "  - Contains attributes for filtering and grouping\n"
                    "  - Relatively small (thousands to millions of rows)\n"
                    "  - Changes slowly (product names, customer addresses)\n\n"
                    "The fact table is the 'what happened.' The dimensions are the 'context.'"
                ),
                "options": [
                    "Dimension table",
                    "Fact table",
                    "Bridge table",
                    "Staging table",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It has foreign keys to dimensions AND numeric measures like revenue and quantity.",
                    "Measurements + dimension keys = fact table.",
                ],
            },
            {
                "id": "wh_5",
                "type": "quiz",
                "title": "Columnar Storage",
                "question": (
                    "Snowflake and BigQuery store data in columnar format rather than\n"
                    "row-oriented format. Why is columnar storage faster for analytical\n"
                    "queries like 'SELECT SUM(revenue) FROM sales WHERE year = 2025'?"
                ),
                "lesson": (
                    "Columnar storage stores each column's values contiguously on disk.\n\n"
                    "For analytical queries that read a few columns from many rows:\n"
                    "  - Row storage: must read entire rows (all columns) to get the few you need\n"
                    "  - Columnar: reads only the columns referenced in the query\n\n"
                    "Additional benefits:\n"
                    "  - Compression: same-type values compress extremely well (10-100x)\n"
                    "  - Vectorized execution: process batches of values from one column at once\n"
                    "  - Predicate pushdown: skip entire column chunks that don't match filters\n\n"
                    "Trade-off: row-oriented is better for OLTP (inserting/updating full rows)."
                ),
                "options": [
                    "It reads only the columns needed, skipping irrelevant data",
                    "It stores data in memory instead of disk",
                    "It uses B-tree indexes on every column automatically",
                    "It replicates data across multiple nodes for parallel reads",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "The query only needs 'revenue' and 'year' — columnar avoids reading other columns.",
                    "Column pruning: read only what you need.",
                ],
            },
            {
                "id": "wh_6",
                "type": "quiz",
                "title": "Slowly Changing Dimensions",
                "question": (
                    "A customer changes their address. In your dimension table, you\n"
                    "keep both the old and new address rows, each with an effective\n"
                    "date range and a current_flag.\n\n"
                    "What type of Slowly Changing Dimension (SCD) is this?"
                ),
                "lesson": (
                    "SCD Type 2 — preserves full history by adding a new row for each change.\n\n"
                    "SCD Types:\n"
                    "  Type 0: No changes tracked. Dimension is static.\n"
                    "  Type 1: Overwrite. Old value lost. No history.\n"
                    "  Type 2: New row with effective dates and current flag. Full history.\n"
                    "  Type 3: Add column for previous value. Limited history (one change).\n\n"
                    "Type 2 is the most common in warehouses because:\n"
                    "  - Historical accuracy: reports for Q1 use Q1's dimension values\n"
                    "  - Audit trail: every change is recorded\n"
                    "  - Cost: storage is cheap; losing history is expensive"
                ),
                "options": [
                    "SCD Type 1 — overwrite the old value",
                    "SCD Type 2 — add new row with effective dates",
                    "SCD Type 3 — add a column for the previous value",
                    "SCD Type 0 — never update the dimension",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Both old and new rows exist, with date ranges — that's historical tracking.",
                    "New row per change + effective dates = Type 2.",
                ],
            },
        ],
    },

    # ── ZONE 3: STREAMING ───────────────────────────────────────────────
    "streaming": {
        "id": "streaming",
        "name": "The Stream Core",
        "subtitle": "Kafka Deep Dive — Partitions, Consumer Groups & Exactly-Once",
        "color": "green",
        "icon": "🌊",
        "commands": ["kafka", "topic", "partition", "consumer-group", "offset", "exactly-once"],
        "challenges": [
            {
                "id": "strm_1",
                "type": "quiz",
                "title": "Kafka Topics & Partitions",
                "question": (
                    "A Kafka topic has 12 partitions. You have a consumer group\n"
                    "with 6 consumers.\n\n"
                    "How many partitions does each consumer read from?"
                ),
                "lesson": (
                    "Kafka distributes partitions evenly across consumers in a group.\n\n"
                    "12 partitions / 6 consumers = 2 partitions per consumer.\n\n"
                    "Key rules:\n"
                    "  - Each partition is read by exactly ONE consumer in a group\n"
                    "  - A consumer can read from multiple partitions\n"
                    "  - If consumers > partitions, some consumers sit idle\n"
                    "  - If consumers < partitions, some consumers handle multiple partitions\n\n"
                    "This is why partition count = maximum parallelism for a consumer group."
                ),
                "options": [
                    "1 partition each",
                    "2 partitions each",
                    "6 partitions each",
                    "12 partitions each (all consumers read all)",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Kafka divides partitions evenly among consumers in a group.",
                    "12 partitions / 6 consumers = ?",
                ],
            },
            {
                "id": "strm_2",
                "type": "quiz",
                "title": "Consumer Groups",
                "question": (
                    "Two different microservices each need to independently consume\n"
                    "every message from the same Kafka topic.\n\n"
                    "How should you configure this?"
                ),
                "lesson": (
                    "Each service gets its own consumer group.\n\n"
                    "Consumer groups provide independent consumption:\n"
                    "  - Each group maintains its own offsets\n"
                    "  - Each group reads every message in the topic independently\n"
                    "  - Within a group, partitions are distributed (load balancing)\n"
                    "  - Across groups, all messages are delivered to each group (fan-out)\n\n"
                    "This is Kafka's publish-subscribe model:\n"
                    "  Same group   = competing consumers (queue semantics)\n"
                    "  Different groups = independent subscribers (pub-sub semantics)"
                ),
                "options": [
                    "Put both services in the same consumer group",
                    "Give each service its own consumer group",
                    "Create two separate topics with the same data",
                    "Use Kafka Streams to duplicate the messages",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Each service needs ALL messages independently — not competing for them.",
                    "Different consumer groups = independent consumption of the full stream.",
                ],
            },
            {
                "id": "strm_3",
                "type": "quiz",
                "title": "Message Ordering",
                "question": (
                    "You need strict ordering for events from the same user_id, but\n"
                    "don't care about ordering across different users.\n\n"
                    "How do you achieve this in Kafka?"
                ),
                "lesson": (
                    "Use user_id as the partition key.\n\n"
                    "Kafka guarantees ordering within a partition, not across partitions.\n\n"
                    "When you produce a message with a key:\n"
                    "  partition = hash(key) % num_partitions\n\n"
                    "  - All messages with the same key go to the same partition\n"
                    "  - Within that partition, order is preserved (FIFO)\n"
                    "  - Different keys may land on different partitions (no cross-partition ordering)\n\n"
                    "This is the fundamental trade-off: ordering vs parallelism.\n"
                    "  - 1 partition = total order, zero parallelism\n"
                    "  - N partitions = per-key order, N-way parallelism"
                ),
                "options": [
                    "Use a single partition for the entire topic",
                    "Use user_id as the partition key",
                    "Enable global ordering on the Kafka cluster",
                    "Sort messages on the consumer side after reading",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Same key = same partition. Same partition = guaranteed order.",
                    "Partition key determines which partition a message lands on.",
                ],
            },
            {
                "id": "strm_4",
                "type": "quiz",
                "title": "Exactly-Once Semantics",
                "question": (
                    "Your payment processing consumer must never process a\n"
                    "transaction twice and never lose one.\n\n"
                    "What delivery guarantee do you need?"
                ),
                "lesson": (
                    "Exactly-once semantics (EOS) — each message is processed exactly one time.\n\n"
                    "Delivery guarantees:\n"
                    "  At-most-once:  fire and forget. May lose messages. No duplicates.\n"
                    "  At-least-once: retry on failure. No message loss. May have duplicates.\n"
                    "  Exactly-once:  no loss, no duplicates. Hardest to achieve.\n\n"
                    "Kafka achieves EOS through:\n"
                    "  - Idempotent producers (enable.idempotence=true)\n"
                    "  - Transactional API (atomic writes across multiple partitions)\n"
                    "  - Consumer offset commits in the same transaction as output\n\n"
                    "In practice, 'exactly-once' often means 'effectively once' —\n"
                    "at-least-once delivery + idempotent processing."
                ),
                "options": [
                    "At-most-once delivery",
                    "At-least-once delivery",
                    "Exactly-once semantics",
                    "Best-effort delivery",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "No loss AND no duplicates — the strongest guarantee.",
                    "Exactly once: every message processed one time, no more, no less.",
                ],
            },
            {
                "id": "strm_5",
                "type": "quiz",
                "title": "Kafka Offsets",
                "question": (
                    "A consumer crashes after processing a batch of messages but before\n"
                    "committing offsets. When it restarts, what happens?"
                ),
                "lesson": (
                    "The consumer re-reads from the last committed offset — reprocessing messages.\n\n"
                    "Kafka offsets:\n"
                    "  - Each partition maintains a monotonically increasing offset (0, 1, 2, ...)\n"
                    "  - Consumer groups store their committed offset per partition\n"
                    "  - On restart, a consumer reads from its last committed offset\n\n"
                    "Commit strategies:\n"
                    "  Auto-commit:  commits periodically (default 5s). Risk: uncommitted messages\n"
                    "                get reprocessed on crash.\n"
                    "  Manual commit: commit after processing. Gives control but adds complexity.\n"
                    "  Sync vs Async: commitSync() blocks, commitAsync() doesn't.\n\n"
                    "This is why idempotent consumers matter — reprocessing will happen."
                ),
                "options": [
                    "It skips ahead to the latest message",
                    "It re-reads from the last committed offset, reprocessing some messages",
                    "Kafka replays only the uncommitted messages automatically",
                    "The consumer group rebalances and assigns those partitions to another consumer",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Offsets weren't committed, so Kafka doesn't know they were processed.",
                    "Last committed offset = where the consumer resumes.",
                ],
            },
            {
                "id": "strm_6",
                "type": "quiz",
                "title": "Stream Processing Frameworks",
                "question": (
                    "You need to process a Kafka stream with complex windowed\n"
                    "aggregations, event-time processing, and exactly-once guarantees.\n\n"
                    "Which framework was purpose-built for this?"
                ),
                "lesson": (
                    "Apache Flink — a distributed stream processing framework.\n\n"
                    "Flink's strengths:\n"
                    "  - True streaming (event-by-event, not micro-batch)\n"
                    "  - Event-time processing with watermarks\n"
                    "  - Exactly-once state consistency via checkpointing\n"
                    "  - Complex windowing (tumbling, sliding, session windows)\n\n"
                    "Alternatives:\n"
                    "  Spark Structured Streaming: micro-batch (seconds latency), strong SQL support\n"
                    "  Kafka Streams: library (not a cluster), good for simpler transformations\n"
                    "  Apache Beam: abstraction layer, runs on Flink/Spark/Dataflow\n\n"
                    "Flink is the go-to when you need low-latency, stateful stream processing."
                ),
                "options": [
                    "Apache Spark Structured Streaming",
                    "Apache Flink",
                    "Apache Beam",
                    "Kafka Connect",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "True streaming (not micro-batch), event-time, exactly-once state.",
                    "The framework with checkpointing and watermarks as first-class concepts.",
                ],
            },
        ],
    },

    # ── ZONE 4: DATA LAKES ──────────────────────────────────────────────
    "data_lakes": {
        "id": "data_lakes",
        "name": "The Lake Depths",
        "subtitle": "Object Storage, File Formats, Table Formats & the Lakehouse",
        "color": "blue",
        "icon": "🌊",
        "commands": ["s3", "parquet", "orc", "iceberg", "delta-lake", "lakehouse"],
        "challenges": [
            {
                "id": "lake_1",
                "type": "quiz",
                "title": "What Is a Data Lake?",
                "question": (
                    "Your company stores raw JSON logs, CSV exports, Parquet files,\n"
                    "and images all in the same S3 bucket organized by date prefix.\n\n"
                    "What is this storage pattern called?"
                ),
                "lesson": (
                    "A Data Lake — centralized repository for storing data at any scale\n"
                    "in its raw, native format.\n\n"
                    "Characteristics:\n"
                    "  - Schema-on-read (no schema enforced at write time)\n"
                    "  - Stores structured, semi-structured, and unstructured data\n"
                    "  - Built on cheap object storage (S3, GCS, ADLS)\n"
                    "  - Decouples storage from compute\n\n"
                    "Risk: without governance, a data lake becomes a 'data swamp' —\n"
                    "files nobody understands, no catalog, no lineage, no quality checks."
                ),
                "options": [
                    "Data warehouse",
                    "Data lake",
                    "Data mesh",
                    "Data catalog",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Raw files in multiple formats on object storage = lake, not warehouse.",
                    "Schema-on-read, not schema-on-write.",
                ],
            },
            {
                "id": "lake_2",
                "type": "quiz",
                "title": "Parquet File Format",
                "question": (
                    "You convert your CSV data files to Apache Parquet before storing\n"
                    "them in the data lake. File sizes drop from 10 GB to 1.2 GB,\n"
                    "and analytical queries run 20x faster.\n\n"
                    "Why is Parquet so much more efficient?"
                ),
                "lesson": (
                    "Apache Parquet — a columnar, compressed, binary file format.\n\n"
                    "Why it's faster and smaller than CSV:\n"
                    "  - Columnar: stores column values together (great for SELECT col1, col2)\n"
                    "  - Compression: same-type values compress well (Snappy, Zstd, Gzip)\n"
                    "  - Predicate pushdown: skip row groups that don't match filters\n"
                    "  - Schema embedded: self-describing (no external schema file needed)\n"
                    "  - Binary: no parsing overhead (CSV requires text parsing)\n\n"
                    "Parquet is the de facto standard for data lakes and analytical workloads.\n"
                    "ORC is the alternative (originally from Hive), with similar properties."
                ),
                "options": [
                    "Parquet uses row-oriented storage which is faster for full table scans",
                    "Parquet is columnar, compressed, and supports predicate pushdown",
                    "Parquet stores data as JSON internally for easier parsing",
                    "Parquet replicates data across multiple files for parallel reads",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Columnar + compression = smaller files. Column pruning = faster queries.",
                    "Parquet stores columns together, compresses them, and skips irrelevant data.",
                ],
            },
            {
                "id": "lake_3",
                "type": "quiz",
                "title": "Apache Iceberg",
                "question": (
                    "Your data lake on S3 needs ACID transactions, time travel queries,\n"
                    "schema evolution, and partition evolution without rewriting data.\n\n"
                    "Which open table format provides this?"
                ),
                "lesson": (
                    "Apache Iceberg — an open table format for huge analytic datasets.\n\n"
                    "Iceberg adds warehouse-like features to data lake files:\n"
                    "  - ACID transactions (snapshot isolation, no partial reads)\n"
                    "  - Time travel (query any historical snapshot)\n"
                    "  - Schema evolution (add/rename/drop columns safely)\n"
                    "  - Partition evolution (change partitioning without rewriting data)\n"
                    "  - Hidden partitioning (users don't need to know partition columns)\n\n"
                    "Alternatives:\n"
                    "  Delta Lake — Databricks-originated, strong Spark integration\n"
                    "  Apache Hudi — optimized for upserts and incremental processing\n\n"
                    "All three solve the same core problem: making data lakes reliable."
                ),
                "options": [
                    "Apache Iceberg",
                    "Apache Avro",
                    "Apache Arrow",
                    "Apache Parquet",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "Parquet is a file format. You need a table format that sits on top.",
                    "ACID + time travel + schema evolution on S3 = Iceberg.",
                ],
            },
            {
                "id": "lake_4",
                "type": "quiz",
                "title": "Lake vs Warehouse vs Lakehouse",
                "question": (
                    "A 'lakehouse' architecture aims to combine the best of both worlds.\n\n"
                    "What two things does a lakehouse combine?"
                ),
                "lesson": (
                    "Lakehouse = Data Lake flexibility + Data Warehouse reliability.\n\n"
                    "Data Lake strengths:\n"
                    "  - Cheap object storage, any file format, schema-on-read\n"
                    "  - Great for data science, ML, raw data exploration\n\n"
                    "Data Warehouse strengths:\n"
                    "  - ACID transactions, strong schema, fast SQL queries\n"
                    "  - Great for BI, reporting, dashboards\n\n"
                    "Lakehouse combines them:\n"
                    "  - Data stored on object storage (lake-cheap)\n"
                    "  - Table format (Iceberg/Delta) adds ACID, schema, time travel\n"
                    "  - Query engine (Spark/Trino/Presto) provides fast SQL\n"
                    "  - One copy of data serves both analytics and ML\n\n"
                    "Examples: Databricks Lakehouse, Snowflake (with external tables), Dremio"
                ),
                "options": [
                    "Data lake storage with data warehouse reliability and performance",
                    "Streaming systems with batch processing engines",
                    "On-premise storage with cloud computing",
                    "SQL databases with NoSQL flexibility",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "Lake + warehouse = lakehouse. It's in the name.",
                    "Cheap storage from lakes, ACID and SQL from warehouses.",
                ],
            },
            {
                "id": "lake_5",
                "type": "quiz",
                "title": "Partitioning in Data Lakes",
                "question": (
                    "Your S3 data lake stores events partitioned as:\n"
                    "s3://bucket/events/year=2025/month=03/day=29/\n\n"
                    "A query filters WHERE year=2025 AND month=03.\n"
                    "What performance optimization does this partitioning enable?"
                ),
                "lesson": (
                    "Partition pruning — the query engine reads only matching partitions.\n\n"
                    "Without partitioning: the engine must scan ALL files to find March 2025 data.\n"
                    "With partitioning: the engine reads only the files under year=2025/month=03/.\n\n"
                    "Hive-style partitioning (key=value/ directories) is the standard.\n\n"
                    "Partitioning best practices:\n"
                    "  - Choose columns frequently used in WHERE clauses\n"
                    "  - Avoid too many partitions (millions of tiny files = slow listing)\n"
                    "  - Avoid too few partitions (huge files = no pruning benefit)\n"
                    "  - Target 100 MB - 1 GB per file for Parquet"
                ),
                "options": [
                    "Data compression — files are smaller in partitioned layouts",
                    "Partition pruning — only matching partitions are read",
                    "Indexing — partition keys are indexed like database B-trees",
                    "Caching — partitioned data stays in memory longer",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The query engine skips directories that don't match the filter.",
                    "Pruning = eliminating partitions from the scan.",
                ],
            },
        ],
    },

    # ── ZONE 5: SPARK ───────────────────────────────────────────────────
    "spark": {
        "id": "spark",
        "name": "The Spark Grid",
        "subtitle": "RDDs, DataFrames, Transformations, Actions & Partitioning",
        "color": "red",
        "icon": "⚡",
        "commands": ["rdd", "dataframe", "transformation", "action", "partition", "broadcast-join"],
        "challenges": [
            {
                "id": "spk_1",
                "type": "quiz",
                "title": "RDD vs DataFrame",
                "question": (
                    "You're writing a Spark job. You could use the low-level RDD API\n"
                    "or the higher-level DataFrame API.\n\n"
                    "Why do most Spark applications use DataFrames today?"
                ),
                "lesson": (
                    "DataFrames provide optimization that RDDs cannot.\n\n"
                    "RDD (Resilient Distributed Dataset):\n"
                    "  - Low-level API, manual optimization\n"
                    "  - No schema — just rows of objects\n"
                    "  - No Catalyst optimizer, no Tungsten execution engine\n"
                    "  - Still useful for unstructured data or custom partitioning\n\n"
                    "DataFrame:\n"
                    "  - Schema-aware (named columns with types)\n"
                    "  - Catalyst optimizer generates efficient physical plans\n"
                    "  - Tungsten engine: off-heap memory, code generation\n"
                    "  - Same performance in Python, Scala, Java, R (optimizer does the work)\n\n"
                    "Rule of thumb: use DataFrames unless you have a specific reason not to."
                ),
                "options": [
                    "DataFrames are faster because they bypass the JVM",
                    "DataFrames have schema awareness and use the Catalyst optimizer",
                    "DataFrames store data in memory while RDDs use disk",
                    "DataFrames support Python while RDDs only support Scala",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The key advantage is the query optimizer, not raw speed.",
                    "Catalyst optimizer + schema = better execution plans.",
                ],
            },
            {
                "id": "spk_2",
                "type": "quiz",
                "title": "Transformations vs Actions",
                "question": (
                    "You write: df.filter(col('age') > 30).select('name', 'age')\n"
                    "No output appears. Nothing happens until you add .show() at the end.\n\n"
                    "Why?"
                ),
                "lesson": (
                    "Spark uses lazy evaluation. Transformations are recorded but not executed.\n\n"
                    "Transformations (lazy — build a plan):\n"
                    "  filter(), select(), groupBy(), join(), withColumn(), map(), flatMap()\n"
                    "  These return a new DataFrame/RDD but execute nothing.\n\n"
                    "Actions (eager — trigger execution):\n"
                    "  show(), count(), collect(), write(), take(), first(), foreach()\n"
                    "  These force Spark to execute the full transformation chain.\n\n"
                    "Why lazy evaluation?\n"
                    "  - Catalyst can optimize the entire chain before executing\n"
                    "  - Unnecessary computations are eliminated (predicate pushdown)\n"
                    "  - Pipelining: multiple transformations fused into a single pass"
                ),
                "options": [
                    "Spark has a bug that requires explicit execution triggers",
                    "filter() and select() are transformations — they're lazy until an action triggers execution",
                    "Spark batches operations every 5 seconds automatically",
                    "Python DataFrames are always lazy regardless of the framework",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Spark doesn't execute anything until you ask for a result.",
                    "Lazy transformations + eager actions = deferred execution.",
                ],
            },
            {
                "id": "spk_3",
                "type": "quiz",
                "title": "Shuffle Operations",
                "question": (
                    "Your Spark job runs a groupBy().agg() operation and suddenly\n"
                    "performance tanks. Executors are writing gigabytes to disk and\n"
                    "exchanging data across the network.\n\n"
                    "What is happening?"
                ),
                "lesson": (
                    "A shuffle — Spark redistributes data across partitions.\n\n"
                    "Shuffles happen when data needs to be regrouped:\n"
                    "  - groupBy(), reduceByKey(), join(), repartition(), distinct()\n\n"
                    "During a shuffle:\n"
                    "  1. Map side: each executor writes its output to local disk, sorted by key\n"
                    "  2. Reduce side: executors fetch their partitions from every other executor\n"
                    "  3. Network transfer: O(N*M) data movement (N executors, M partitions)\n\n"
                    "Shuffles are expensive because they involve:\n"
                    "  - Disk I/O (spill to disk if data exceeds memory)\n"
                    "  - Network I/O (cross-node data transfer)\n"
                    "  - Serialization/deserialization\n\n"
                    "Optimization: minimize shuffles. Use broadcast joins for small tables."
                ),
                "options": [
                    "A memory leak in the executor JVMs",
                    "A shuffle — data is being redistributed across partitions over the network",
                    "Spark is checkpointing data to HDFS for fault tolerance",
                    "The driver is collecting all results before distributing them",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "groupBy requires all rows with the same key on the same partition.",
                    "Data redistribution across the network = shuffle.",
                ],
            },
            {
                "id": "spk_4",
                "type": "quiz",
                "title": "Broadcast Joins",
                "question": (
                    "You're joining a 500 GB fact table with a 50 MB dimension table.\n"
                    "The default sort-merge join is slow due to shuffling the large table.\n\n"
                    "What optimization should you use?"
                ),
                "lesson": (
                    "Broadcast join — send the small table to every executor.\n\n"
                    "Default join (sort-merge): both tables are shuffled by join key.\n"
                    "  - 500 GB + 50 MB both shuffled across the cluster. Expensive.\n\n"
                    "Broadcast join: the small table is broadcast to every executor.\n"
                    "  - 50 MB copied to each executor (cheap, fits in memory)\n"
                    "  - Large table stays in place — no shuffle needed\n"
                    "  - Each executor joins its local partition with the broadcast table\n\n"
                    "Usage:\n"
                    "  from pyspark.sql.functions import broadcast\n"
                    "  df_large.join(broadcast(df_small), 'key')\n\n"
                    "Spark auto-broadcasts tables under spark.sql.autoBroadcastJoinThreshold\n"
                    "(default 10 MB). Set it higher if your small table is larger."
                ),
                "options": [
                    "Broadcast join — send the small table to all executors",
                    "Hash join — hash both tables and merge locally",
                    "Nested loop join — iterate over both tables",
                    "Partition join — pre-partition both tables by join key",
                ],
                "answer": "a",
                "xp": 35,
                "hints": [
                    "The small table fits in memory — send it to every executor.",
                    "broadcast(df_small) avoids shuffling the large table.",
                ],
            },
            {
                "id": "spk_5",
                "type": "quiz",
                "title": "Data Skew",
                "question": (
                    "One Spark task takes 45 minutes while all others finish in 2 minutes.\n"
                    "The slow task's partition has 100x more data because most records share\n"
                    "the same join key (e.g., country='US').\n\n"
                    "What is this problem called?"
                ),
                "lesson": (
                    "Data skew — uneven data distribution across partitions.\n\n"
                    "Symptoms:\n"
                    "  - One task takes dramatically longer than others\n"
                    "  - One executor uses all its memory while others are idle\n"
                    "  - OOM errors on specific tasks\n\n"
                    "Solutions:\n"
                    "  - Salting: add a random suffix to the skewed key, join, then aggregate\n"
                    "  - Broadcast join: if the other table is small enough\n"
                    "  - Adaptive Query Execution (AQE): Spark 3.x handles skew automatically\n"
                    "  - Pre-filter: remove or split the hot key into its own processing path\n"
                    "  - Repartition: explicitly redistribute data more evenly"
                ),
                "options": [
                    "Data corruption",
                    "Data skew",
                    "Partition fragmentation",
                    "Executor starvation",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "One key has far more data than others — the partition is lopsided.",
                    "Uneven data distribution = skew.",
                ],
            },
            {
                "id": "spk_6",
                "type": "quiz",
                "title": "Spark Partitioning",
                "question": (
                    "Your Spark job reads a 100 GB Parquet dataset from S3.\n"
                    "Spark creates 800 tasks. You notice many tasks process < 1 MB.\n\n"
                    "What should you do?"
                ),
                "lesson": (
                    "Coalesce to reduce the number of partitions (fewer, larger tasks).\n\n"
                    "Too many partitions:\n"
                    "  - Scheduling overhead (each task has fixed overhead)\n"
                    "  - Tiny tasks that finish in milliseconds\n"
                    "  - Too many output files\n\n"
                    "Too few partitions:\n"
                    "  - Large tasks that OOM or run slowly\n"
                    "  - Underutilized cluster (not enough parallelism)\n\n"
                    "Rules of thumb:\n"
                    "  - Target 128 MB - 256 MB per partition\n"
                    "  - coalesce(N): reduces partitions WITHOUT a shuffle (narrows)\n"
                    "  - repartition(N): increases or decreases WITH a shuffle (full redistribution)\n"
                    "  - Use coalesce to shrink, repartition to grow or rebalance"
                ),
                "options": [
                    "Repartition to increase the number of partitions",
                    "Coalesce to reduce partitions and create fewer, larger tasks",
                    "Cache the dataset in memory to speed up small tasks",
                    "Increase executor memory to handle more partitions",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Many tiny tasks = too many partitions. You need fewer, larger ones.",
                    "coalesce() reduces partitions without a shuffle.",
                ],
            },
        ],
    },

    # ── ZONE 6: DATA QUALITY ────────────────────────────────────────────
    "data_quality": {
        "id": "data_quality",
        "name": "The Quality Gate",
        "subtitle": "Great Expectations, Data Contracts, Schema Evolution & Lineage",
        "color": "magenta",
        "icon": "🔍",
        "commands": ["great-expectations", "data-contract", "schema-evolution", "lineage"],
        "challenges": [
            {
                "id": "dq_1",
                "type": "quiz",
                "title": "Great Expectations",
                "question": (
                    "You want to validate that a column 'email' is never null,\n"
                    "always contains '@', and has fewer than 0.1% duplicates.\n\n"
                    "Which tool lets you define these as declarative expectations?"
                ),
                "lesson": (
                    "Great Expectations (GX) — an open-source data validation framework.\n\n"
                    "Core concepts:\n"
                    "  Expectation:  a declarative assertion about data\n"
                    "                (expect_column_values_to_not_be_null)\n"
                    "  Suite:        a collection of expectations for a dataset\n"
                    "  Checkpoint:   runs a suite against data and produces a validation result\n"
                    "  Data Docs:    auto-generated HTML reports of validation results\n\n"
                    "Example:\n"
                    "  validator.expect_column_values_to_not_be_null('email')\n"
                    "  validator.expect_column_values_to_match_regex('email', r'.*@.*')\n\n"
                    "GX integrates with Airflow, Spark, Pandas, and SQL databases."
                ),
                "options": [
                    "dbt tests",
                    "Great Expectations",
                    "Apache Griffin",
                    "Soda Core",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Declarative expectations, suites, checkpoints, and data docs.",
                    "The framework name literally contains the word 'Expectations'.",
                ],
            },
            {
                "id": "dq_2",
                "type": "quiz",
                "title": "Data Contracts",
                "question": (
                    "The upstream team changes a column name from 'user_id' to 'uid'\n"
                    "without telling you. Your pipeline breaks.\n\n"
                    "What practice would have prevented this?"
                ),
                "lesson": (
                    "Data Contracts — formal agreements between data producers and consumers.\n\n"
                    "A data contract specifies:\n"
                    "  - Schema: exact column names, types, and nullability\n"
                    "  - Semantics: what each field means (business definitions)\n"
                    "  - SLAs: freshness, completeness, availability guarantees\n"
                    "  - Ownership: who is responsible for the data\n"
                    "  - Change protocol: how schema changes are communicated\n\n"
                    "Without contracts, producers change schemas freely and consumers break.\n"
                    "With contracts, changes require agreement — like an API versioning contract.\n\n"
                    "Data contracts shift quality left — the producer owns correctness,\n"
                    "not the consumer."
                ),
                "options": [
                    "Data lineage tracking",
                    "Data contracts between producer and consumer",
                    "Schema-on-read validation",
                    "Automated data profiling",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "A formal agreement about schema, semantics, and change protocol.",
                    "Like an API contract, but for data.",
                ],
            },
            {
                "id": "dq_3",
                "type": "quiz",
                "title": "Schema Evolution",
                "question": (
                    "Your Parquet-based data lake needs to add a new column to an\n"
                    "existing table without rewriting historical data files.\n\n"
                    "What capability makes this possible?"
                ),
                "lesson": (
                    "Schema evolution — modifying a table's schema without rewriting existing data.\n\n"
                    "Common schema changes:\n"
                    "  - Add column: new column, old files return NULL for it (backward compatible)\n"
                    "  - Rename column: map old name to new name in metadata\n"
                    "  - Widen type: INT -> LONG, FLOAT -> DOUBLE\n"
                    "  - Drop column: remove from schema, old files still have the data\n\n"
                    "Table formats that support schema evolution:\n"
                    "  - Apache Iceberg: full support (add, rename, drop, reorder)\n"
                    "  - Delta Lake: add columns, change nullability\n"
                    "  - Apache Hudi: add columns\n\n"
                    "Without schema evolution, adding a column means rewriting every file —\n"
                    "petabytes of data just to add one field."
                ),
                "options": [
                    "Schema-on-read",
                    "Schema evolution",
                    "Schema migration",
                    "Schema registry",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Modifying the schema of an existing table without rewriting data.",
                    "Evolution: the schema changes, the data stays.",
                ],
            },
            {
                "id": "dq_4",
                "type": "quiz",
                "title": "Data Lineage",
                "question": (
                    "A dashboard shows incorrect revenue numbers. You need to trace\n"
                    "the data back through every transformation to find where the error\n"
                    "was introduced.\n\n"
                    "What do you need?"
                ),
                "lesson": (
                    "Data Lineage — tracking data from source through every transformation to output.\n\n"
                    "Lineage answers:\n"
                    "  - Where did this data come from? (upstream sources)\n"
                    "  - What transformations were applied? (SQL, Spark jobs, dbt models)\n"
                    "  - What downstream assets does this affect? (dashboards, ML models)\n"
                    "  - When did the data last update? (freshness)\n\n"
                    "Lineage tools:\n"
                    "  - OpenLineage: open standard for lineage metadata\n"
                    "  - DataHub (LinkedIn): lineage + discovery + governance\n"
                    "  - Amundsen (Lyft): data discovery with lineage\n"
                    "  - Marquez: reference implementation of OpenLineage\n\n"
                    "Without lineage, debugging data issues is archaeology. With it, it's a graph traversal."
                ),
                "options": [
                    "Data profiling",
                    "Data lineage",
                    "Data cataloging",
                    "Data versioning",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Tracing data from source through transformations to the output.",
                    "The path data takes through your system = lineage.",
                ],
            },
            {
                "id": "dq_5",
                "type": "quiz",
                "title": "Data Observability",
                "question": (
                    "You want automated monitoring that alerts you when:\n"
                    "- A table's row count drops 50% from its normal range\n"
                    "- A column's null rate spikes from 1% to 30%\n"
                    "- Data freshness exceeds the SLA\n\n"
                    "What practice is this?"
                ),
                "lesson": (
                    "Data Observability — automated monitoring of data health.\n\n"
                    "The five pillars of data observability:\n"
                    "  1. Freshness:  Is the data up to date?\n"
                    "  2. Volume:     Did the expected number of rows arrive?\n"
                    "  3. Schema:     Did the schema change unexpectedly?\n"
                    "  4. Distribution: Are column value distributions normal?\n"
                    "  5. Lineage:    What upstream/downstream is affected?\n\n"
                    "Tools:\n"
                    "  - Monte Carlo: ML-powered anomaly detection on data\n"
                    "  - Bigeye: automated data quality monitoring\n"
                    "  - Elementary: dbt-native data observability\n"
                    "  - Soda Core: open-source data checks\n\n"
                    "Data observability is to data pipelines what APM is to applications."
                ),
                "options": [
                    "Data governance",
                    "Data observability",
                    "Data validation",
                    "Data reconciliation",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Automated monitoring with anomaly detection on data health metrics.",
                    "Observability: freshness, volume, schema, distribution, lineage.",
                ],
            },
        ],
    },

    # ── ZONE 7: ORCHESTRATION ───────────────────────────────────────────
    "orchestration": {
        "id": "orchestration",
        "name": "The Orchestration Nexus",
        "subtitle": "Airflow Operators, Sensors, XCom, Dagster & Prefect",
        "color": "white",
        "icon": "🎛",
        "commands": ["operator", "sensor", "xcom", "dagster", "prefect", "schedule"],
        "challenges": [
            {
                "id": "orch_1",
                "type": "quiz",
                "title": "Airflow Operators",
                "question": (
                    "In Airflow, you need a task that executes a Python function.\n\n"
                    "Which operator should you use?"
                ),
                "lesson": (
                    "PythonOperator — executes a Python callable as an Airflow task.\n\n"
                    "Common Airflow operators:\n"
                    "  PythonOperator:      run a Python function\n"
                    "  BashOperator:        run a bash command\n"
                    "  PostgresOperator:    execute SQL against Postgres\n"
                    "  S3ToRedshiftOperator: load from S3 to Redshift (provider package)\n"
                    "  KubernetesPodOperator: run a container on Kubernetes\n\n"
                    "Operators define WHAT a task does.\n"
                    "Dependencies (>>, set_downstream) define the execution ORDER.\n\n"
                    "Modern Airflow also supports the @task decorator (TaskFlow API)\n"
                    "which is syntactic sugar over PythonOperator."
                ),
                "options": [
                    "BashOperator",
                    "PythonOperator",
                    "PythonSensor",
                    "SimpleHttpOperator",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "You're running a Python function — which operator matches?",
                    "PythonOperator: the most basic operator for Python callables.",
                ],
            },
            {
                "id": "orch_2",
                "type": "quiz",
                "title": "Airflow Sensors",
                "question": (
                    "Your pipeline must wait until a file appears in S3 before\n"
                    "proceeding. The file is uploaded by an external system on\n"
                    "an unpredictable schedule.\n\n"
                    "What Airflow component handles this?"
                ),
                "lesson": (
                    "A Sensor — an operator that waits for a condition to be true.\n\n"
                    "Sensors poll at a configurable interval (poke_interval) until:\n"
                    "  - The condition is met (sensor succeeds)\n"
                    "  - The timeout is reached (sensor fails)\n\n"
                    "Common sensors:\n"
                    "  S3KeySensor:          wait for a file in S3\n"
                    "  ExternalTaskSensor:   wait for another DAG's task to complete\n"
                    "  HttpSensor:           wait for an HTTP endpoint to return success\n"
                    "  SqlSensor:            wait for a SQL query to return rows\n\n"
                    "Sensor modes:\n"
                    "  poke (default): occupies a worker slot while waiting\n"
                    "  reschedule:     releases the slot between pokes (better for long waits)"
                ),
                "options": [
                    "A Sensor — polls until a condition is met",
                    "A Trigger — fires immediately when the event occurs",
                    "A Hook — connects to the external system",
                    "An Operator — executes the wait as a Python function",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "It waits by polling at intervals until the file exists.",
                    "Sensors sense — they wait for external conditions.",
                ],
            },
            {
                "id": "orch_3",
                "type": "quiz",
                "title": "Airflow XCom",
                "question": (
                    "Task A computes a value (e.g., a row count) that Task B needs.\n"
                    "In Airflow, what mechanism passes data between tasks?\n"
                ),
                "lesson": (
                    "XCom (cross-communication) — Airflow's mechanism for passing small data\n"
                    "between tasks.\n\n"
                    "How it works:\n"
                    "  - Task A pushes: xcom_push(key='row_count', value=42)\n"
                    "  - Task B pulls: xcom_pull(task_ids='task_a', key='row_count')\n"
                    "  - XComs are stored in Airflow's metadata database\n\n"
                    "Important limitations:\n"
                    "  - XCom is for SMALL data (a file path, a row count, a status)\n"
                    "  - NOT for large datasets (use S3/GCS as intermediate storage)\n"
                    "  - XCom values are serialized to the metadata DB (size limits apply)\n\n"
                    "TaskFlow API (@task decorator) passes XComs implicitly via return values."
                ),
                "options": [
                    "Environment variables",
                    "XCom (cross-communication)",
                    "Shared filesystem",
                    "Airflow Variables",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Airflow's built-in mechanism for inter-task data passing.",
                    "XCom = cross-communication. Push and pull between tasks.",
                ],
            },
            {
                "id": "orch_4",
                "type": "quiz",
                "title": "Dagster vs Airflow",
                "question": (
                    "In Dagster, pipelines are defined around 'software-defined assets'\n"
                    "— each asset declares its dependencies and the code that produces it.\n\n"
                    "How does this differ from Airflow's core abstraction?"
                ),
                "lesson": (
                    "Airflow is task-centric. Dagster is asset-centric.\n\n"
                    "Airflow:\n"
                    "  - Core unit: Task (a unit of execution)\n"
                    "  - DAGs define execution order: Task A >> Task B >> Task C\n"
                    "  - Focus: WHEN and HOW tasks run\n"
                    "  - Doesn't natively know what data a task produces\n\n"
                    "Dagster:\n"
                    "  - Core unit: Software-Defined Asset (a dataset + its computation)\n"
                    "  - Assets declare dependencies: asset_b depends on asset_a\n"
                    "  - Focus: WHAT data exists and HOW it's derived\n"
                    "  - Built-in data lineage, type checking, and materialization tracking\n\n"
                    "Dagster's asset-centric model makes it easier to reason about data\n"
                    "freshness, lineage, and whether derived datasets are up to date."
                ),
                "options": [
                    "Airflow uses Python; Dagster uses YAML for pipeline definitions",
                    "Airflow is task-centric; Dagster is asset-centric",
                    "Airflow runs on Kubernetes; Dagster runs on Docker only",
                    "Airflow is open source; Dagster is proprietary",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Airflow defines tasks and their order. Dagster defines assets and their dependencies.",
                    "Task-centric vs asset-centric is the fundamental distinction.",
                ],
            },
            {
                "id": "orch_5",
                "type": "quiz",
                "title": "Prefect Flow Concepts",
                "question": (
                    "In Prefect, you decorate a Python function with @flow and its\n"
                    "sub-functions with @task. There's no DAG file, no scheduler config,\n"
                    "no operator class.\n\n"
                    "What is Prefect's design philosophy?"
                ),
                "lesson": (
                    "Prefect: 'just Python' — orchestration as native Python code.\n\n"
                    "Prefect's approach:\n"
                    "  - @flow decorator: turns a function into an orchestrated workflow\n"
                    "  - @task decorator: turns a function into a retryable, observable unit\n"
                    "  - No DAG definition: the execution graph is inferred from code\n"
                    "  - Dynamic workflows: conditionals, loops, and branching are natural\n\n"
                    "vs Airflow:\n"
                    "  - Airflow requires DAG objects, operator classes, and explicit dependencies\n"
                    "  - Prefect lets you write normal Python that happens to be orchestrated\n\n"
                    "Prefect 2+ uses a hybrid model:\n"
                    "  - Prefect Cloud: scheduling, monitoring, and API\n"
                    "  - Your infrastructure: execution happens where you choose"
                ),
                "options": [
                    "YAML-first configuration with minimal code",
                    "Native Python with @flow and @task decorators — no DAG boilerplate",
                    "SQL-based pipeline definitions for data teams",
                    "Visual drag-and-drop pipeline builder",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Decorate Python functions. No DAG objects, no operator classes.",
                    "Prefect's motto: orchestration should be Pythonic.",
                ],
            },
            {
                "id": "orch_6",
                "type": "quiz",
                "title": "Scheduling Patterns",
                "question": (
                    "Your pipeline must run at 2 AM UTC every day, but only process\n"
                    "data for the previous day (not the current day).\n\n"
                    "In Airflow, what concept handles this?"
                ),
                "lesson": (
                    "Airflow's execution_date and data_interval.\n\n"
                    "A common source of confusion:\n"
                    "  - A DAG scheduled daily at 2 AM runs at 2 AM on March 30th\n"
                    "  - But it processes data for March 29th (the previous interval)\n"
                    "  - execution_date = start of the data interval (March 29th 00:00)\n"
                    "  - logical_date (Airflow 2.2+) = same as execution_date\n\n"
                    "Airflow 2.x introduced data_interval_start and data_interval_end\n"
                    "to make this clearer:\n"
                    "  data_interval_start = March 29th 00:00 UTC\n"
                    "  data_interval_end   = March 30th 00:00 UTC\n"
                    "  The run triggers at data_interval_end (2 AM March 30th)\n\n"
                    "This is 'interval-based scheduling' — each run processes a defined window."
                ),
                "options": [
                    "The catchup parameter",
                    "The execution_date / data_interval concept",
                    "The start_date parameter in the DAG definition",
                    "The trigger_rule on each task",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The run at 2 AM on March 30 processes data for March 29.",
                    "execution_date = the data interval being processed, not when the run triggers.",
                ],
            },
        ],
    },

    # ── ZONE 8: MODERN DATA STACK ───────────────────────────────────────
    "modern_stack": {
        "id": "modern_stack",
        "name": "The Modern Forge",
        "subtitle": "dbt, Snowflake, Fivetran, Airbyte — The Modern Data Stack",
        "color": "bright_white",
        "icon": "🏗",
        "commands": ["dbt", "snowflake", "fivetran", "airbyte", "elt"],
        "challenges": [
            {
                "id": "mds_1",
                "type": "quiz",
                "title": "What is dbt?",
                "question": (
                    "Your analytics team writes SQL SELECT statements that\n"
                    "transform raw data into clean models. They want version control,\n"
                    "testing, documentation, and dependency management — all in SQL.\n\n"
                    "What tool does this?"
                ),
                "lesson": (
                    "dbt (data build tool) — the T in ELT.\n\n"
                    "dbt lets you:\n"
                    "  - Write transformations as SQL SELECT statements (models)\n"
                    "  - Define dependencies between models (ref() function)\n"
                    "  - Test data (not_null, unique, accepted_values, relationships)\n"
                    "  - Generate documentation automatically\n"
                    "  - Version control everything in Git\n\n"
                    "dbt compiles your models into SQL and runs them in your warehouse.\n"
                    "It doesn't extract or load data — it only transforms.\n\n"
                    "dbt Core: open source CLI\n"
                    "dbt Cloud: hosted IDE, scheduler, and CI/CD"
                ),
                "options": [
                    "Apache Airflow",
                    "dbt (data build tool)",
                    "Apache Spark",
                    "Fivetran",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "SQL-based transformations with testing, docs, and version control.",
                    "The 'T' in ELT — it only handles transformations.",
                ],
            },
            {
                "id": "mds_2",
                "type": "quiz",
                "title": "dbt ref() Function",
                "question": (
                    "In a dbt model, you write:\n"
                    "  SELECT * FROM {{ ref('stg_orders') }}\n\n"
                    "What does ref() do?"
                ),
                "lesson": (
                    "ref() creates a dependency between dbt models and resolves table names.\n\n"
                    "When you write {{ ref('stg_orders') }}:\n"
                    "  1. dbt registers that this model depends on stg_orders\n"
                    "  2. dbt ensures stg_orders runs BEFORE this model\n"
                    "  3. dbt resolves the actual table name (schema.table) at compile time\n\n"
                    "Why ref() matters:\n"
                    "  - Automatic dependency graph (no manual ordering)\n"
                    "  - Environment-aware (dev schema vs prod schema)\n"
                    "  - Refactoring: rename a model, ref() updates everywhere\n\n"
                    "Never hardcode table names in dbt. Always use ref() for models\n"
                    "and source() for raw tables."
                ),
                "options": [
                    "References an external database connection",
                    "Creates a dependency and resolves the model's table name",
                    "Refreshes the table's data from the source system",
                    "Adds a referential integrity constraint to the table",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "ref() tells dbt about model dependencies and resolves names.",
                    "Dependency management + name resolution in one function.",
                ],
            },
            {
                "id": "mds_3",
                "type": "quiz",
                "title": "Snowflake Architecture",
                "question": (
                    "Snowflake separates storage, compute, and cloud services into\n"
                    "independent layers. You can scale compute up/down without touching\n"
                    "storage.\n\n"
                    "What is this architecture called?"
                ),
                "lesson": (
                    "Multi-cluster shared data architecture (decoupled storage and compute).\n\n"
                    "Snowflake's three layers:\n"
                    "  1. Storage: data stored in a proprietary columnar format on cloud object storage\n"
                    "  2. Compute: virtual warehouses (clusters) that process queries independently\n"
                    "  3. Cloud Services: authentication, metadata, query optimization, transactions\n\n"
                    "Key benefits:\n"
                    "  - Scale compute independently of storage\n"
                    "  - Multiple warehouses query the same data simultaneously\n"
                    "  - Pay for compute only when queries are running (auto-suspend)\n"
                    "  - No contention between workloads (each warehouse is isolated)\n\n"
                    "This is fundamentally different from traditional MPP databases\n"
                    "where storage and compute are tightly coupled on the same nodes."
                ),
                "options": [
                    "Shared-nothing MPP architecture",
                    "Decoupled storage and compute architecture",
                    "Federated query architecture",
                    "Lambda architecture",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Storage and compute scale independently — they're separated.",
                    "Decoupled: change one layer without affecting the other.",
                ],
            },
            {
                "id": "mds_4",
                "type": "quiz",
                "title": "Fivetran vs Airbyte",
                "question": (
                    "You need to replicate data from Salesforce, Stripe, and Postgres\n"
                    "into your Snowflake warehouse. You want managed connectors with\n"
                    "no code.\n\n"
                    "Both Fivetran and Airbyte do this. What's the key difference?"
                ),
                "lesson": (
                    "Fivetran is fully managed SaaS. Airbyte is open-source-first.\n\n"
                    "Fivetran:\n"
                    "  - Fully managed, zero infrastructure to run\n"
                    "  - 300+ pre-built connectors, heavily tested\n"
                    "  - Pricing based on monthly active rows (MAR) — can be expensive\n"
                    "  - Best for: teams that want zero maintenance\n\n"
                    "Airbyte:\n"
                    "  - Open-source core (self-hosted) + Cloud offering\n"
                    "  - 350+ connectors (community-contributed, quality varies)\n"
                    "  - Free to self-host, pay for Airbyte Cloud\n"
                    "  - Best for: teams that want control and cost savings\n\n"
                    "Both handle the E and L in ELT. dbt handles the T."
                ),
                "options": [
                    "Fivetran handles transformations; Airbyte only extracts",
                    "Fivetran is fully managed SaaS; Airbyte is open-source-first",
                    "Fivetran supports SQL sources; Airbyte supports APIs only",
                    "Fivetran is batch only; Airbyte supports real-time streaming",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "One is fully managed SaaS, the other started as open source.",
                    "Fivetran = managed service. Airbyte = open source you can self-host.",
                ],
            },
            {
                "id": "mds_5",
                "type": "quiz",
                "title": "The Modern Data Stack",
                "question": (
                    "A company uses Fivetran to extract data, Snowflake to store it,\n"
                    "dbt to transform it, and Looker to visualize it.\n\n"
                    "What is this combination commonly called?"
                ),
                "lesson": (
                    "The Modern Data Stack (MDS) — a set of cloud-native, best-of-breed tools\n"
                    "that work together for analytics.\n\n"
                    "Typical MDS components:\n"
                    "  Ingestion:       Fivetran, Airbyte, Stitch\n"
                    "  Storage:         Snowflake, BigQuery, Redshift, Databricks\n"
                    "  Transformation:  dbt\n"
                    "  Orchestration:   Airflow, Dagster, Prefect\n"
                    "  BI/Visualization: Looker, Tableau, Metabase, Mode\n"
                    "  Data Quality:    Great Expectations, Monte Carlo, Elementary\n"
                    "  Reverse ETL:     Census, Hightouch\n\n"
                    "Philosophy:\n"
                    "  - ELT over ETL (leverage warehouse compute)\n"
                    "  - Best-of-breed over monolithic (swap any component)\n"
                    "  - Cloud-native (managed, scalable, pay-per-use)\n"
                    "  - SQL-centric (analytics engineers write SQL, not Python)"
                ),
                "options": [
                    "The data mesh",
                    "The modern data stack",
                    "The data lakehouse",
                    "The analytics platform",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "A set of cloud-native, best-of-breed tools for analytics.",
                    "Modern + Data + Stack = the industry term.",
                ],
            },
            {
                "id": "mds_6",
                "type": "quiz",
                "title": "Reverse ETL",
                "question": (
                    "Your marketing team needs customer segments computed in your\n"
                    "warehouse to be pushed back into Salesforce and Braze for\n"
                    "targeted campaigns.\n\n"
                    "What is this pattern called?"
                ),
                "lesson": (
                    "Reverse ETL — pushing transformed data from the warehouse to operational tools.\n\n"
                    "Traditional ETL: operational systems -> warehouse (for analysis)\n"
                    "Reverse ETL:     warehouse -> operational systems (for action)\n\n"
                    "Use cases:\n"
                    "  - Sync customer segments to CRM (Salesforce)\n"
                    "  - Push lead scores to marketing tools (Braze, HubSpot)\n"
                    "  - Send product recommendations to personalization engines\n"
                    "  - Update support tickets with customer health scores\n\n"
                    "Tools:\n"
                    "  - Census: 'operational analytics' platform\n"
                    "  - Hightouch: warehouse-native reverse ETL\n"
                    "  - Polytomic: sync warehouse to SaaS apps\n\n"
                    "The warehouse becomes the single source of truth for both\n"
                    "analytics AND operations."
                ),
                "options": [
                    "Data replication",
                    "Change data capture",
                    "Reverse ETL",
                    "Data federation",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Data flows from the warehouse back to operational systems.",
                    "The reverse of ETL: warehouse -> SaaS tools.",
                ],
            },
        ],
    },
}
