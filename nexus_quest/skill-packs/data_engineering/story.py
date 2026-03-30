"""
story.py — Narrative text for Data Forge.
Theme: Data is the new oil. Raw data is useless — you need to refine it.
A Data Engineer reconstructing a collapsed analytics platform after a
catastrophic pipeline failure wiped out the company's data infrastructure.
"""

INTRO_STORY = """
The alert cascade started at [bold cyan]4:47 AM[/bold cyan].

[bold white]Three hundred and twelve pipelines.[/bold white] All failed within the same
ninety-second window. The nightly batch jobs that fed the warehouse — dead.
The streaming consumers that powered real-time dashboards — disconnected.
The dbt models that transformed raw ingestion into clean analytics — broken
at the root, errors propagating through every downstream dependency.

By the time the on-call engineer opened their laptop, the data warehouse
was serving stale numbers to every executive dashboard in the company.
Revenue reports: twenty-six hours old. Churn predictions: based on data
that no longer existed. The ML models were retraining on empty tables.

[bold white]You are a Data Engineer.[/bold white]

[bold magenta]Independent contractor. Infrastructure reconstruction. You've rebuilt
pipelines for companies that thought "we have a data team" meant "our data
is reliable." It doesn't. Data is the new oil — but raw oil is useless.
It has to be extracted, transported, refined, quality-checked, and delivered.
Miss any step and you're shipping sludge.[/bold magenta]

The CTO has given you full access to the platform: the orchestrator, the
warehouse, the streaming cluster, the lake, the transformation layer.
Your job: understand how the infrastructure was built, why it collapsed,
and rebuild it so it never collapses like this again.

The data catalog says 312 pipelines. The lineage graph says 847 dependencies.
The monitoring dashboard says nothing — because monitoring was the first thing
that broke.

[bold cyan]The pipelines are waiting. Start from the foundations.[/bold cyan]
"""

ZONE_INTROS = {
    "data_pipelines": """
[bold cyan]== THE PIPELINE FOUNDRY ==[/bold cyan]

Every data platform starts here — with the pipes that move data from
point A to point B.

Before you can understand why 312 pipelines failed, you need to understand
how pipelines work at a fundamental level. ETL or ELT? Batch or streaming?
What's a DAG, and why does every orchestrator use them?

The nightly batch was the backbone. It extracted from fourteen source systems,
transformed in a cascade of dependent steps, and loaded into the warehouse
by 6 AM. When step three failed, everything downstream was already doomed.

[yellow]ETL vs ELT[/yellow] — where does transformation happen?
[yellow]Batch vs Streaming[/yellow] — when does data move?
[yellow]DAGs[/yellow] — how are dependencies expressed?
[yellow]Idempotency[/yellow] — what makes a pipeline safe to re-run?

[italic]"A pipeline isn't a script that runs. It's a contract that data
will arrive, transformed, on time, every time."[/italic]
""",
    "data_warehouses": """
[bold cyan]== THE WAREHOUSE VAULT ==[/bold cyan]

The warehouse is where refined data lives — structured, modeled, queryable.

The company's warehouse was well-designed: star schema, fact tables with
billions of rows, dimension tables with SCD Type 2 history tracking.
The problem wasn't the model. The problem was that the pipelines feeding
it went silent, and nobody noticed until the CFO's revenue dashboard
showed yesterday's numbers at 2 PM.

[yellow]Star Schema[/yellow] — facts in the center, dimensions radiating out.
[yellow]Snowflake Schema[/yellow] — normalized dimensions, more joins.
[yellow]OLAP vs OLTP[/yellow] — analytical vs transactional workloads.
[yellow]Columnar Storage[/yellow] — why warehouses are fast at aggregations.

[italic]"The warehouse doesn't lie. But it can go silent. And silence
is the most dangerous kind of lie in analytics."[/italic]
""",
    "streaming": """
[bold cyan]== THE STREAM CORE ==[/bold cyan]

Batch gets you yesterday's data today. Streaming gets you now.

The real-time dashboards ran on Kafka. Twelve topics, forty-eight partitions,
six consumer groups serving different microservices. When the infrastructure
buckled, the consumers fell behind. Lag climbed from seconds to hours.
Messages piled up. Consumer groups rebalanced. Offsets were lost.

By the time someone restarted the consumers, they had a choice: skip
three hours of messages or reprocess them all and deal with duplicates.

[yellow]Kafka Topics & Partitions[/yellow] — the unit of parallelism.
[yellow]Consumer Groups[/yellow] — independent consumption vs load balancing.
[yellow]Offsets[/yellow] — where you are in the stream.
[yellow]Exactly-Once Semantics[/yellow] — the hardest guarantee to achieve.

[italic]"A stream doesn't pause. If you stop reading, it keeps flowing.
The lag counter is a measure of how far behind reality you've fallen."[/italic]
""",
    "data_lakes": """
[bold cyan]== THE LAKE DEPTHS ==[/bold cyan]

The lake is where raw data lands before it's refined.

Petabytes of Parquet files on S3, organized by date prefix. JSON logs
from application servers. CSV exports from legacy systems. Images from
the ML training pipeline. All sitting in the same bucket, cataloged
by Glue, queried by Athena when someone remembers the partition scheme.

The lake was supposed to be the safety net — even if the warehouse went
down, the raw data was preserved. But raw data without a table format
is just files. No ACID. No time travel. No schema enforcement. When
someone accidentally overwrote the March partition, there was no undo.

[yellow]Object Storage[/yellow] — S3, GCS, ADLS.
[yellow]File Formats[/yellow] — Parquet, ORC, Avro.
[yellow]Table Formats[/yellow] — Iceberg, Delta Lake, Hudi.
[yellow]Lakehouse[/yellow] — the convergence of lakes and warehouses.

[italic]"A data lake without governance is a data swamp. A data lake
with Iceberg is a warehouse that happens to run on S3."[/italic]
""",
    "spark": """
[bold cyan]== THE SPARK GRID ==[/bold cyan]

When the data is too large for a single machine, you distribute the compute.

The heaviest transformations in the platform ran on Spark. A 200-node
cluster crunching through terabytes of clickstream data, joining it with
user profiles, aggregating by session, and writing the results to Iceberg
tables. When the cluster was healthy, the job took forty minutes. When
data skew hit — one partition with 100x more data than the others —
one task took six hours while the rest of the cluster sat idle.

[yellow]RDDs vs DataFrames[/yellow] — low-level vs optimized.
[yellow]Transformations vs Actions[/yellow] — lazy vs eager.
[yellow]Shuffles[/yellow] — the most expensive operation in distributed computing.
[yellow]Broadcast Joins[/yellow] — the optimization that saves terabytes of network I/O.

[italic]"Spark doesn't have a speed problem. It has a shuffle problem.
Every slow job is a shuffle you didn't expect."[/italic]
""",
    "data_quality": """
[bold cyan]== THE QUALITY GATE ==[/bold cyan]

Data that arrives on time but is wrong is worse than data that doesn't arrive.

The warehouse was serving numbers. The dashboards were green. The SLAs
were met. But the revenue figures were off by 12% — a silent schema change
in the upstream CRM had renamed a column, and the pipeline was silently
dropping rows that didn't match the expected schema. No alerts. No
validation. No contract between the producer and the consumer.

It took [bold white]three weeks[/bold white] for someone to notice. Three weeks of
decisions made on wrong data.

[yellow]Great Expectations[/yellow] — declarative data validation.
[yellow]Data Contracts[/yellow] — formal agreements between producers and consumers.
[yellow]Schema Evolution[/yellow] — changing schemas without breaking everything.
[yellow]Data Lineage[/yellow] — tracing errors back to their source.

[italic]"The most dangerous data isn't missing data. It's wrong data
that looks right."[/italic]
""",
    "orchestration": """
[bold cyan]== THE ORCHESTRATION NEXUS ==[/bold cyan]

Pipelines don't run themselves. Something has to decide what runs when,
what depends on what, and what to do when something fails.

The company's Airflow instance was the nerve center — 312 DAGs, thousands
of tasks, sensors waiting on files, operators pushing to warehouses,
XComs passing metadata between steps. When the Airflow scheduler OOMed
at 4:47 AM, nothing ran. Not because the pipelines were broken — because
the thing that triggers the pipelines was dead.

[yellow]Operators[/yellow] — what a task does.
[yellow]Sensors[/yellow] — tasks that wait.
[yellow]XCom[/yellow] — passing data between tasks.
[yellow]Dagster & Prefect[/yellow] — the next generation of orchestrators.

[italic]"Airflow is not the pipeline. Airflow is the thing that makes
sure the pipeline runs. Kill the scheduler and everything stops."[/italic]
""",
    "modern_stack": """
[bold cyan]== THE MODERN FORGE ==[/bold cyan]

The rebuild. The modern data stack. Best-of-breed tools, cloud-native,
SQL-centric, designed to be maintained by a team of five, not fifty.

Fivetran for ingestion — managed connectors, zero maintenance. Snowflake
for storage and compute — decoupled, scalable, pay-per-query. dbt for
transformations — SQL models, tested, documented, version-controlled.
Looker for visualization. Great Expectations for validation.

The old platform was 312 hand-written pipelines maintained by tribal
knowledge. The new platform is a catalog of dbt models where every
transformation is a SQL file, every dependency is a ref(), and every
assumption is a test.

[yellow]dbt[/yellow] — transformations as code.
[yellow]Snowflake[/yellow] — decoupled storage and compute.
[yellow]Fivetran / Airbyte[/yellow] — managed data ingestion.
[yellow]The Modern Data Stack[/yellow] — the full picture.

[italic]"The goal isn't more pipelines. The goal is fewer pipelines
that you actually understand."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "data_pipelines": """
[bold green]THE PIPELINE FOUNDRY — OPERATIONAL.[/bold green]

You understand the fundamentals now. ETL vs ELT — and why ELT won in the
cloud era. Batch vs streaming — and when each is appropriate. DAGs — and
why cycles are forbidden. Idempotency — and why every pipeline must be
safe to re-run.

The failed nightly batch wasn't idempotent. When it was re-run after the
fix, it created duplicates that cascaded into every downstream report.
That mistake won't happen again.

[bold cyan]The Warehouse Vault. How the refined data is modeled and stored.[/bold cyan]
""",
    "data_warehouses": """
[bold green]THE WAREHOUSE VAULT — AUDITED.[/bold green]

Star schema. Snowflake schema. Fact tables. Dimension tables. SCD Type 2.
Columnar storage. You know why the warehouse is fast at aggregations and
slow at single-row lookups. You know the difference between OLAP and OLTP,
and why running analytics on the production database is a bad idea.

The warehouse model was sound. The failure was upstream — the pipes
that fed it went dry. A well-designed warehouse is useless without
reliable data delivery.

[bold cyan]The Stream Core. Real-time data. Kafka. Consumer groups. Offsets.[/bold cyan]
""",
    "streaming": """
[bold green]THE STREAM CORE — SYNCHRONIZED.[/bold green]

Partitions, consumer groups, offsets, exactly-once semantics. You understand
Kafka's partition-level ordering guarantee, why consumer group rebalancing
causes latency spikes, and why idempotent consumers are non-negotiable.

The streaming recovery plan: reset consumer offsets to the last committed
position, reprocess with idempotent handlers, and monitor lag until it
returns to zero. Three hours of reprocessing. Zero duplicates.

[bold cyan]The Lake Depths. Object storage, file formats, table formats.[/bold cyan]
""",
    "data_lakes": """
[bold green]THE LAKE DEPTHS — CHARTED.[/bold green]

S3, Parquet, Iceberg. You understand why Parquet replaced CSV, why Iceberg
replaced Hive, and why the lakehouse is replacing the two-system architecture
of lake + warehouse. Partition pruning. Schema evolution. Time travel.

The March partition that was accidentally overwritten? With Iceberg, that's
a one-line fix: roll back to the previous snapshot. Without Iceberg, it's
a full reprocessing from raw sources. The lake is getting a table format.

[bold cyan]The Spark Grid. Distributed compute. Shuffles. The cost of scale.[/bold cyan]
""",
    "spark": """
[bold green]THE SPARK GRID — OPTIMIZED.[/bold green]

RDDs vs DataFrames. Lazy transformations vs eager actions. Shuffles —
the silent killer of Spark job performance. Broadcast joins. Data skew.
Coalesce vs repartition.

The six-hour Spark job? Data skew on the country column — 40% of traffic
from the US landing on a single partition. Solution: salted join key,
broadcast the dimension table, AQE enabled. New runtime: thirty-eight minutes.

[bold cyan]The Quality Gate. The hardest problem in data: knowing it's correct.[/bold cyan]
""",
    "data_quality": """
[bold green]THE QUALITY GATE — ENFORCED.[/bold green]

Great Expectations checkpoints on every pipeline. Data contracts between
every producer and consumer. Schema evolution handled by Iceberg. Lineage
tracked by OpenLineage. The silent 12% revenue error? It would have been
caught in six minutes by a null rate check on the join key.

The gate is closed. Nothing passes through without validation.

[bold cyan]The Orchestration Nexus. The nerve center that runs everything.[/bold cyan]
""",
    "orchestration": """
[bold green]THE ORCHESTRATION NEXUS — REBUILT.[/bold green]

Operators, sensors, XCom. Dagster's asset-centric model. Prefect's
Pythonic simplicity. Airflow's execution_date semantics. You understand
why the scheduler OOM was catastrophic — and why a single-point-of-failure
orchestrator is an architectural defect.

The new deployment: Airflow on Kubernetes with the KubernetesExecutor.
Scheduler runs as a StatefulSet with automatic restart. No more single
point of failure. No more 4:47 AM cascades.

[bold cyan]The Modern Forge. The complete rebuild. The stack that replaces 312 pipelines.[/bold cyan]
""",
    "modern_stack": """
[bold yellow]*** THE MODERN FORGE — COMPLETE. ***[/bold yellow]

[bold white]The platform is rebuilt.[/bold white]

Fivetran pulls from fourteen source systems. Snowflake stores and computes.
dbt transforms raw data into clean, tested, documented models. Great
Expectations validates every materialization. Airflow orchestrates on
Kubernetes. Iceberg provides ACID on the lake. The lineage graph is
complete — every table traceable from source to dashboard.

312 hand-written pipelines replaced by 47 dbt models, 14 Fivetran
connectors, and 8 orchestration DAGs. The new platform is maintained
by documentation, not tribal knowledge.

[bold magenta]Data is the new oil. But raw oil is useless.
You've built the refinery. Every drop is now accounted for.[/bold magenta]

[bold yellow]DATA FORGE: RECONSTRUCTION COMPLETE. THE PIPELINES FLOW CLEAN.[/bold yellow]
""",
}

BOSS_INTROS = {
    "data_pipelines": "[bold red]@ PIPELINE AUDIT: The Foundation Check[/bold red]\nETL, ELT, batch, streaming, DAGs, idempotency. Prove you understand the pipes that move data.",
    "data_warehouses": "[bold red]@ WAREHOUSE REVIEW: The Schema Exam[/bold red]\nStar schema, fact tables, dimensions, columnar storage. Prove you can model data for analytics.",
    "streaming": "[bold red]@ STREAM RECOVERY: The Kafka Challenge[/bold red]\nPartitions, consumer groups, offsets, exactly-once. Prove you can reason about real-time data flow.",
    "data_lakes": "[bold red]@ LAKE ASSESSMENT: The Format Deep Dive[/bold red]\nParquet, Iceberg, partitioning, lakehouse. Prove you understand modern data lake architecture.",
    "spark": "[bold red]@ SPARK OPTIMIZATION: The Performance Review[/bold red]\nDataFrames, shuffles, broadcast joins, data skew. Prove you can optimize distributed compute.",
    "data_quality": "[bold red]@ QUALITY AUDIT: The Trust Verification[/bold red]\nValidation, contracts, lineage, observability. Prove you can guarantee data correctness.",
    "orchestration": "[bold red]@ ORCHESTRATION EXAM: The Control Plane[/bold red]\nOperators, sensors, XCom, scheduling. Prove you can wire the nerve center of a data platform.",
    "modern_stack": "[bold red]* FINAL RECONSTRUCTION: The Modern Data Stack[/bold red]\ndbt, Snowflake, Fivetran, reverse ETL. Prove you can architect the platform that replaces 312 pipelines.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Query Executed", "Ran your first data operation. The platform acknowledged your access."),
    "pipeline_builder": ("Pipeline Architect", "Cleared the Pipeline Foundry. ETL, ELT, DAGs, idempotency — the fundamentals are solid."),
    "warehouse_modeler": ("Warehouse Modeler", "Cleared the Warehouse Vault. Star schemas, dimensions, and columnar storage are second nature."),
    "stream_rider": ("Stream Rider", "Cleared the Stream Core. Kafka partitions, consumer groups, and offsets hold no mystery."),
    "lake_navigator": ("Lake Navigator", "Cleared the Lake Depths. Parquet, Iceberg, and the lakehouse architecture — fully charted."),
    "spark_optimizer": ("Spark Optimizer", "Cleared the Spark Grid. Shuffles eliminated. Broadcast joins deployed. Skew resolved."),
    "quality_enforcer": ("Quality Enforcer", "Cleared the Quality Gate. Every pipeline validated. Every contract enforced. No bad data passes."),
    "orchestration_master": ("Orchestration Master", "Cleared the Orchestration Nexus. The nerve center rebuilt, resilient, and running."),
    "forge_master": ("FORGE MASTER", "Cleared the Modern Forge. 312 pipelines replaced. The modern data stack is operational."),
    "streak_3": ("Clean Pipeline", "3 correct in a row. Data is starting to flow."),
    "streak_5": ("Validated Batch", "5 in a row. Every transformation producing clean output."),
    "streak_10": ("ZERO DEFECTS", "10 in a row. Production-grade knowledge. No errors. No nulls. No duplicates."),
    "no_hints": ("No Documentation Needed", "Cleared a zone without hints. The knowledge is internalized."),
    "speed_demon": ("Sub-5 Response", "Answered in under 5 seconds. The query plan was already optimized."),
    "level_10": ("Senior Analyst", "Level 10. You read data models like other people read emails."),
    "level_20": ("Staff Engineer", "Level 20. Pipeline failures don't surprise you. You've seen every failure mode."),
    "level_30": ("Chief Data Officer", "Maximum level. You've rebuilt the refinery. Every drop of data accounted for."),
    "completionist": ("Full Platform Rebuilt", "Every zone. Every challenge. The data platform is production-grade."),
    "boss_slayer": ("Pipeline Restored", "Beat your first boss challenge. One pipeline back online."),
}
