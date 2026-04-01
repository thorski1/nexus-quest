"""
story.py — Narrative text for ML Forge.
Theme: Train the machines. Deploy the models. Monitor everything.
A Machine Learning Engineer building an AI platform for a megacorp
whose previous ML infrastructure collapsed under technical debt.
"""

INTRO_STORY = """
The alert came from the [bold cyan]production inference cluster[/bold cyan] at 2:47 AM.

[bold white]Model accuracy had dropped to coin-flip levels.[/bold white] The recommendation engine
that drives 40% of the platform's revenue was serving predictions based on
feature distributions that hadn't existed in six months. Data drift. Concept drift.
Nobody was monitoring either.

The previous ML team built models in notebooks, deployed them by copying pickle
files to a shared drive, and tracked experiments in a spreadsheet that hadn't
been updated since Q2. No feature store. No model registry. No evaluation pipeline.
No monitoring. Forty-seven models in production. Zero observability.

[bold white]You are an ML Engineer.[/bold white]

[bold magenta]Hired to rebuild the platform from the ground up. Not just the models —
the entire lifecycle. Training pipelines. Feature stores. Model serving.
Experiment tracking. Drift detection. Responsible AI practices.
The whole stack. The whole discipline.[/bold magenta]

The CTO's brief was three sentences:

"Train the machines. Deploy the models. Monitor everything."

[bold cyan]The learning core is waiting. Start with the fundamentals.[/bold cyan]
"""

ZONE_INTROS = {
    "ml_fundamentals": """
[bold cyan]== THE LEARNING CORE ==[/bold cyan]

Before you build the platform, you need to audit what the previous team understood.

Supervised. Unsupervised. Reinforcement. The three paradigms.
Train/validation/test splits. Overfitting. The bias-variance tradeoff.
These aren't academic concepts — they're the foundation every other
decision rests on. The previous team skipped this. You won't.

[yellow]supervised learning[/yellow] — labeled data, learn input→output mapping.
[yellow]unsupervised learning[/yellow] — unlabeled data, discover structure.
[yellow]reinforcement learning[/yellow] — agent, environment, reward signal.
[yellow]bias-variance tradeoff[/yellow] — the tension that defines model selection.

[italic]"Every model failure traces back to a fundamental misunderstanding.
Fix the foundation before you build the tower."[/italic]
""",
    "model_training": """
[bold cyan]== THE GRADIENT DESCENT ==[/bold cyan]

The previous team's training logs — what little exists — show learning rates
of 0.1 on deep networks, no early stopping, batch sizes chosen at random,
and loss functions mismatched to their task types.

The models weren't trained. They were tortured.

[yellow]loss function[/yellow] — measures how wrong the model is.
[yellow]gradient descent[/yellow] — iterative optimization to minimize loss.
[yellow]learning rate[/yellow] — step size per weight update.
[yellow]early stopping[/yellow] — halt training before overfitting begins.

[italic]"A model that doesn't converge isn't learning. A model that converges
to the wrong minimum isn't useful. The training loop is where discipline
separates from guesswork."[/italic]
""",
    "feature_engineering": """
[bold cyan]== THE FEATURE FOUNDRY ==[/bold cyan]

The feature pipeline is a disaster. One-hot encoding on a column with 50,000
unique values. Label encoding on nominal categories fed into a linear model.
No normalization. Missing values filled with zeros — including the 'income'
column where zero means something very different from 'unknown.'

Features are the language your model speaks. Bad features produce fluent nonsense.

[yellow]one-hot encoding[/yellow] — binary column per category.
[yellow]label encoding[/yellow] — integer per category (ordinal only).
[yellow]normalization[/yellow] — scale features to comparable ranges.
[yellow]imputation[/yellow] — handle missing data without lying.

[italic]"The model is only as good as the features you give it.
Garbage in, garbage out — but with gradient descent."[/italic]
""",
    "ml_ops": """
[bold cyan]== THE EXPERIMENT VAULT ==[/bold cyan]

Forty-seven models in production. No experiment tracking. No model registry.
No record of which hyperparameters produced which results. The "best model"
was whatever the last person to copy a file to the shared drive happened to train.

MLOps is not overhead. It's the difference between science and guessing.

[yellow]experiment tracking[/yellow] — log every run, every param, every metric.
[yellow]model registry[/yellow] — version models, manage lifecycle stages.
[yellow]MLflow / W&B[/yellow] — tools that make this possible.
[yellow]A/B testing[/yellow] — compare models on live traffic.

[italic]"If you can't reproduce it, you didn't build it. You got lucky."[/italic]
""",
    "model_serving": """
[bold cyan]== THE INFERENCE GRID ==[/bold cyan]

The recommendation model takes 3 seconds per prediction. The fraud model
runs once a day as a batch job — but fraud happens in real time. Two models
are running on GPU instances at 8% utilization, burning $14,000/month.

Serving is where ML meets engineering. Latency. Throughput. Cost.
The model that's too slow to serve is a model that doesn't exist.

[yellow]REST API[/yellow] — model-as-a-service for real-time inference.
[yellow]batch inference[/yellow] — score many records on a schedule.
[yellow]GPU vs CPU[/yellow] — the cost/speed tradeoff.
[yellow]quantization[/yellow] — shrink models for faster, cheaper inference.

[italic]"A model in a notebook is a hypothesis. A model behind an API
with sub-100ms latency is a product."[/italic]
""",
    "llm_ops": """
[bold cyan]== THE LANGUAGE NEXUS ==[/bold cyan]

The CTO wants an internal AI assistant. The previous team hardcoded prompts
in 12 different services, fine-tuned a model on unvetted data, and the
monthly API bill hit $47,000 because every request stuffed 15 documents
into the context window.

LLM ops is ML ops on hard mode. Prompts are code. Tokens are money.
Evaluation is an unsolved problem. Ship it anyway.

[yellow]RAG[/yellow] — retrieve context, ground the model in facts.
[yellow]fine-tuning[/yellow] — adapt the model's behavior, not just its knowledge.
[yellow]prompt management[/yellow] — version, test, deploy prompts like code.
[yellow]token costs[/yellow] — every token costs money. Optimize ruthlessly.

[italic]"The LLM doesn't know what it doesn't know.
RAG gives it facts. Fine-tuning gives it discipline.
Monitoring tells you when both fail."[/italic]
""",
    "data_pipelines_ml": """
[bold cyan]== THE PIPELINE FORGE ==[/bold cyan]

The training pipeline is a Jupyter notebook that someone runs manually
on Thursdays. If they're out sick, the model doesn't retrain. The feature
engineering step uses a different code path than serving. The model trained
on feature v3 is being served features from v1.

Training-serving skew. No feature store. No drift detection.
No automated retraining. The pipeline is a person. That's not a pipeline.

[yellow]feature store[/yellow] — same features for training and serving.
[yellow]training pipeline[/yellow] — automated, reproducible, orchestrated.
[yellow]data drift[/yellow] — input distributions shift over time.
[yellow]model monitoring[/yellow] — catch degradation before users do.

[italic]"A model without a pipeline is a one-time experiment.
A pipeline without monitoring is a ticking clock."[/italic]
""",
    "responsible_ai": """
[bold cyan]== THE ETHICS CORE ==[/bold cyan]

The hiring model has a 25-point approval gap between demographic groups.
The loan model can't explain its decisions. No model cards exist.
The legal team found out about the models from a customer complaint,
not from engineering.

Responsible AI is not optional. It's not a checkbox. It's the difference
between deploying technology and deploying liability.

[yellow]SHAP / LIME[/yellow] — explain individual predictions.
[yellow]model cards[/yellow] — document what the model does and doesn't do.
[yellow]bias detection[/yellow] — measure fairness across groups.
[yellow]AI governance[/yellow] — organizational oversight and accountability.

[italic]"If you can't explain why the model made a decision,
you can't defend it. And you will have to defend it."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "ml_fundamentals": """
[bold green]THE LEARNING CORE — CALIBRATED.[/bold green]

Supervised. Unsupervised. Reinforcement. You know when to use each one.
You understand the train/validation/test split and why the test set is sacred.
Overfitting isn't a mystery — it's a measurable gap between training and
validation performance. The bias-variance tradeoff isn't abstract — it's
the decision framework for model complexity.

The foundation is solid.

[bold cyan]The Gradient Descent is next. Learn to train models properly.[/bold cyan]
""",
    "model_training": """
[bold green]THE GRADIENT DESCENT — CONVERGED.[/bold green]

Loss functions matched to task types. Gradient descent understood from
batch to stochastic to mini-batch. Learning rates that converge instead
of diverge. Early stopping that prevents the overfitting the previous
team never caught.

The training loop is no longer a black box.

[bold cyan]The Feature Foundry. Fix the input pipeline.[/bold cyan]
""",
    "feature_engineering": """
[bold green]THE FEATURE FOUNDRY — FORGED.[/bold green]

One-hot encoding for nominal categories. Label encoding only for ordinals
and tree models. Normalization for distance-based algorithms. Imputation
strategies that respect the missingness mechanism. And the cardinal rule:
split first, then fit the scaler on training data only.

The features are clean. The pipeline is honest.

[bold cyan]The Experiment Vault. Bring order to the chaos.[/bold cyan]
""",
    "ml_ops": """
[bold green]THE EXPERIMENT VAULT — ORGANIZED.[/bold green]

Every experiment tracked. Every model versioned. MLflow logging params,
metrics, and artifacts for every run. The model registry managing lifecycle
stages: Staging, Production, Archived. A/B testing comparing models on
live traffic instead of guessing.

The spreadsheet is dead. Long live the experiment tracker.

[bold cyan]The Inference Grid. Serve models like a real platform.[/bold cyan]
""",
    "model_serving": """
[bold green]THE INFERENCE GRID — ONLINE.[/bold green]

Real-time inference for fraud detection. Batch inference for recommendations.
GPU instances right-sized to actual utilization. Model latency broken down
and optimized end-to-end — not just the forward pass, but preprocessing,
feature retrieval, and serialization.

The models are no longer trapped in notebooks. They're running in production.

[bold cyan]The Language Nexus. LLMs are a different beast.[/bold cyan]
""",
    "llm_ops": """
[bold green]THE LANGUAGE NEXUS — CONNECTED.[/bold green]

RAG architecture grounding the LLM in company documents. Fine-tuning for
consistent output format. Prompt templates versioned and tested. Token costs
cut by 60% through better retrieval and context management. Evaluation
metrics that catch hallucination before users do.

The AI assistant is no longer a $47,000/month autocomplete.

[bold cyan]The Pipeline Forge. Automate the entire lifecycle.[/bold cyan]
""",
    "data_pipelines_ml": """
[bold green]THE PIPELINE FORGE — AUTOMATED.[/bold green]

Feature store serving consistent features to training and inference.
Orchestrated pipelines that retrain weekly without human intervention.
Data drift detection catching distribution shifts before they tank accuracy.
Model monitoring dashboards that show exactly what's degrading and why.

The Thursday notebook is retired. The pipeline runs itself.

[bold cyan]The Ethics Core. Build AI that can withstand scrutiny.[/bold cyan]
""",
    "responsible_ai": """
[bold yellow]★ ★ ★  THE ETHICS CORE — ESTABLISHED.  ★ ★ ★[/bold yellow]

[bold white]The platform rebuild is complete.[/bold white]

SHAP explanations for every high-stakes prediction. Model cards documenting
intended use, limitations, and demographic performance. Bias detection
catching disparate impact before deployment. AI governance ensuring no model
reaches production without review.

Forty-seven models. Fully tracked. Fully versioned. Fully monitored.
Fully explainable. Fully governed.

[bold magenta]The previous team built models. You built a platform.
The models will change. The platform will hold.[/bold magenta]

[bold yellow]ML ENGINEER STATUS: AI DIRECTOR.  PLATFORM: OPERATIONAL.[/bold yellow]
""",
}

BOSS_INTROS = {
    "ml_fundamentals": "[bold red]⚠  PARADIGM AUDIT: The Foundation Check[/bold red]\nSupervised, unsupervised, reinforcement — prove you know when each applies and why overfitting is the enemy.",
    "model_training": "[bold red]⚠  TRAINING LOOP AUDIT: The Convergence Test[/bold red]\nLoss functions, learning rates, early stopping — prove the training loop is under control.",
    "feature_engineering": "[bold red]⚠  FEATURE PIPELINE AUDIT: The Data Integrity Check[/bold red]\nEncoding, normalization, imputation, leakage — prove the features are clean and honest.",
    "ml_ops": "[bold red]⚠  EXPERIMENT AUDIT: The Reproducibility Check[/bold red]\nTracking, versioning, registry, A/B testing — prove every experiment is reproducible.",
    "model_serving": "[bold red]⚠  INFERENCE AUDIT: The Latency Challenge[/bold red]\nReal-time vs batch, GPU vs CPU, latency breakdown — prove the serving layer is production-ready.",
    "llm_ops": "[bold red]⚠  LLM AUDIT: The Token Economics Review[/bold red]\nRAG, fine-tuning, prompt management, costs — prove the LLM stack is efficient and governed.",
    "data_pipelines_ml": "[bold red]⚠  PIPELINE AUDIT: The Drift Detection Test[/bold red]\nFeature stores, training pipelines, data drift, monitoring — prove the lifecycle is automated.",
    "responsible_ai": "[bold red]★  ETHICS AUDIT: The Accountability Review[/bold red]\nSHAP, LIME, model cards, bias detection, governance — prove the AI platform can withstand scrutiny.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Model Inspected", "Answered your first ML challenge. The platform acknowledged your access."),
    "fundamentals_master": ("Foundation Calibrated", "Cleared The Learning Core. Supervised, unsupervised, reinforcement — you know the paradigms."),
    "training_master": ("Training Converged", "Cleared The Gradient Descent. Loss functions, learning rates, early stopping — the training loop is solid."),
    "feature_master": ("Features Forged", "Cleared The Feature Foundry. Encoding, normalization, imputation — the input pipeline is clean."),
    "mlops_master": ("Experiments Organized", "Cleared The Experiment Vault. Every run tracked. Every model versioned. Reproducibility achieved."),
    "serving_master": ("Inference Online", "Cleared The Inference Grid. Models are served, not stranded in notebooks."),
    "llm_master": ("Language Nexus Connected", "Cleared The Language Nexus. RAG, fine-tuning, prompt management — LLM ops under control."),
    "pipeline_master": ("Pipelines Automated", "Cleared The Pipeline Forge. Feature stores, drift detection, automated retraining — the lifecycle runs itself."),
    "ethics_master": ("AI DIRECTOR: ETHICS ESTABLISHED", "Cleared The Ethics Core. Explainability, fairness, governance — the platform withstands scrutiny."),
    "streak_3": ("Clean Batch", "3 correct in a row. Your ML knowledge is converging."),
    "streak_5": ("Gradient Flow", "5 in a row. Smooth descent toward mastery."),
    "streak_10": ("GLOBAL MINIMUM", "10 in a row. You've found the optimal weights. No more updates needed."),
    "no_hints": ("No Hints Needed", "Cleared a zone without hints. The documentation is already in your weights."),
    "speed_demon": ("Sub-5 Inference", "Answered in under 5 seconds. Lower latency than your production models."),
    "level_10": ("Data Scientist", "Level 10. You read confusion matrices like other people read dashboards."),
    "level_20": ("ML Engineer", "Level 20. You build platforms, not just models."),
    "level_30": ("AI Director", "Maximum level. From fundamentals to governance — the full ML lifecycle is yours."),
    "completionist": ("Full Platform Built", "Every zone. Every challenge. The ML platform is complete."),
    "boss_slayer": ("Model Validated", "Beat your first boss challenge. The model passed the audit."),
}
