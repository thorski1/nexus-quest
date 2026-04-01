"""
zones.py — ML Engineering zones and challenges for ML Forge.

8 zones, ~45 challenges. All challenges use "type": "quiz" with
multiple-choice options (a/b/c/d) and two hints each.
"""

ZONE_ORDER = [
    "ml_fundamentals",
    "model_training",
    "feature_engineering",
    "ml_ops",
    "model_serving",
    "llm_ops",
    "data_pipelines_ml",
    "responsible_ai",
]

ZONES = {
    # ── ZONE 1: ML FUNDAMENTALS ─────────────────────────────────────────
    "ml_fundamentals": {
        "id": "ml_fundamentals",
        "name": "The Learning Core",
        "subtitle": "Supervised, Unsupervised, Reinforcement & Model Evaluation",
        "color": "cyan",
        "icon": "🧠",
        "commands": ["supervised", "unsupervised", "reinforcement", "train/val/test", "overfitting", "bias-variance"],
        "challenges": [
            {
                "id": "mlf_1",
                "type": "quiz",
                "title": "Supervised vs Unsupervised",
                "question": (
                    "You have a dataset of emails, each labeled 'spam' or 'not spam.'\n"
                    "You train a model to predict the label for new emails.\n\n"
                    "What type of learning is this?"
                ),
                "lesson": (
                    "Supervised learning trains on labeled data — each input has a known output.\n\n"
                    "The model learns a mapping from features to labels.\n"
                    "Examples: spam detection, image classification, house price prediction.\n\n"
                    "Unsupervised learning works with unlabeled data — the model finds patterns\n"
                    "on its own (clustering, dimensionality reduction).\n\n"
                    "Semi-supervised uses a small labeled set plus a large unlabeled set."
                ),
                "options": [
                    "Supervised learning — labeled inputs and outputs",
                    "Unsupervised learning — no labels, find patterns",
                    "Reinforcement learning — agent maximizes reward",
                    "Semi-supervised learning — mix of labeled and unlabeled",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "Each email already has a label. The model learns from those labels.",
                    "Labeled data + prediction = supervised learning.",
                ],
            },
            {
                "id": "mlf_2",
                "type": "quiz",
                "title": "Clustering Use Case",
                "question": (
                    "A marketing team wants to segment customers into groups based on\n"
                    "purchase behavior. No predefined categories exist.\n\n"
                    "Which learning paradigm fits?"
                ),
                "lesson": (
                    "Unsupervised learning discovers structure in unlabeled data.\n\n"
                    "Clustering algorithms:\n"
                    "  - K-Means: partition data into K clusters by minimizing within-cluster variance\n"
                    "  - DBSCAN: density-based, finds arbitrarily shaped clusters\n"
                    "  - Hierarchical: builds a tree of nested clusters\n\n"
                    "Other unsupervised tasks:\n"
                    "  - Dimensionality reduction (PCA, t-SNE, UMAP)\n"
                    "  - Anomaly detection (Isolation Forest)"
                ),
                "options": [
                    "Supervised classification — predict predefined categories",
                    "Unsupervised clustering — discover natural groupings",
                    "Reinforcement learning — agent explores and learns",
                    "Supervised regression — predict continuous values",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "There are no predefined categories — the model must find them.",
                    "Grouping without labels = clustering = unsupervised.",
                ],
            },
            {
                "id": "mlf_3",
                "type": "quiz",
                "title": "Reinforcement Learning",
                "question": (
                    "A robot learns to navigate a warehouse by receiving +1 reward for\n"
                    "reaching the target shelf and -0.1 penalty for each step taken.\n\n"
                    "What type of learning is this?"
                ),
                "lesson": (
                    "Reinforcement learning (RL): an agent interacts with an environment,\n"
                    "takes actions, and receives rewards or penalties.\n\n"
                    "Key concepts:\n"
                    "  - Agent: the learner/decision-maker\n"
                    "  - Environment: what the agent interacts with\n"
                    "  - State: current situation\n"
                    "  - Action: what the agent can do\n"
                    "  - Reward: feedback signal (+/-)\n"
                    "  - Policy: the strategy the agent learns\n\n"
                    "Examples: game AI (AlphaGo), robotics, recommendation engines."
                ),
                "options": [
                    "Supervised learning — the path is labeled",
                    "Unsupervised learning — no feedback signal",
                    "Reinforcement learning — agent maximizes cumulative reward",
                    "Transfer learning — pre-trained on another warehouse",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "The robot gets rewards and penalties for its actions.",
                    "Agent + environment + reward signal = reinforcement learning.",
                ],
            },
            {
                "id": "mlf_4",
                "type": "quiz",
                "title": "Train / Validation / Test Split",
                "question": (
                    "You split your dataset into three parts: 70% for training, 15% for\n"
                    "hyperparameter tuning, and 15% held out until final evaluation.\n\n"
                    "What is the 15% used for hyperparameter tuning called?"
                ),
                "lesson": (
                    "The three-way split:\n\n"
                    "  Training set (60-80%): model learns parameters (weights)\n"
                    "  Validation set (10-20%): tune hyperparameters, select model architecture\n"
                    "  Test set (10-20%): final unbiased evaluation — touched ONCE\n\n"
                    "Why validation ≠ test:\n"
                    "  If you use the test set to choose hyperparameters, you're indirectly\n"
                    "  fitting to the test set. The test set must remain unseen until the\n"
                    "  very end to give an honest performance estimate."
                ),
                "options": [
                    "Test set — final evaluation only",
                    "Validation set — hyperparameter tuning and model selection",
                    "Training set — model learns from it",
                    "Holdout set — synonym for training set",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "This split is used for tuning, not final evaluation.",
                    "Hyperparameter tuning happens on the validation set.",
                ],
            },
            {
                "id": "mlf_5",
                "type": "quiz",
                "title": "Overfitting",
                "question": (
                    "Your model gets 99% accuracy on training data but only 62% on\n"
                    "the test set.\n\n"
                    "What is this called?"
                ),
                "lesson": (
                    "Overfitting: the model memorizes training data instead of learning\n"
                    "generalizable patterns.\n\n"
                    "Symptoms:\n"
                    "  - High training accuracy, low test/validation accuracy\n"
                    "  - Large gap between training and validation loss\n\n"
                    "Remedies:\n"
                    "  - More training data\n"
                    "  - Regularization (L1/L2, dropout)\n"
                    "  - Early stopping\n"
                    "  - Simpler model architecture\n"
                    "  - Data augmentation\n"
                    "  - Cross-validation"
                ),
                "options": [
                    "Underfitting — model is too simple",
                    "Overfitting — model memorized training data",
                    "Bias-variance tradeoff — balanced error",
                    "Data leakage — test data leaked into training",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Training accuracy is great, but test accuracy is poor.",
                    "The model learned the training set too well — it memorized it.",
                ],
            },
            {
                "id": "mlf_6",
                "type": "quiz",
                "title": "Bias-Variance Tradeoff",
                "question": (
                    "A linear regression model consistently predicts too low on a highly\n"
                    "nonlinear dataset, regardless of how much data you add.\n\n"
                    "What kind of error dominates?"
                ),
                "lesson": (
                    "Bias-variance tradeoff:\n\n"
                    "  High bias: model is too simple, underfits.\n"
                    "    - Consistently wrong in the same direction\n"
                    "    - Adding more data doesn't help\n"
                    "    - Fix: use a more complex model\n\n"
                    "  High variance: model is too complex, overfits.\n"
                    "    - Predictions change wildly with different training sets\n"
                    "    - Training accuracy >> test accuracy\n"
                    "    - Fix: regularize, get more data, simplify\n\n"
                    "The goal: minimize total error = bias² + variance + irreducible noise."
                ),
                "options": [
                    "High variance — model changes with different data",
                    "High bias — model is too simple to capture the pattern",
                    "Irreducible error — noise in the data",
                    "High variance and high bias simultaneously",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The model is consistently wrong, not randomly wrong.",
                    "A linear model on nonlinear data = systematic underprediction = high bias.",
                ],
            },
        ],
    },

    # ── ZONE 2: MODEL TRAINING ──────────────────────────────────────────
    "model_training": {
        "id": "model_training",
        "name": "The Gradient Descent",
        "subtitle": "Loss Functions, Optimizers, Learning Rate & Training Loops",
        "color": "green",
        "icon": "📉",
        "commands": ["loss", "gradient descent", "learning rate", "epochs", "batch size", "early stopping"],
        "challenges": [
            {
                "id": "mt_1",
                "type": "quiz",
                "title": "Loss Functions",
                "question": (
                    "You are training a binary classifier to detect fraudulent transactions.\n"
                    "The output layer uses a sigmoid activation.\n\n"
                    "Which loss function is most appropriate?"
                ),
                "lesson": (
                    "Common loss functions:\n\n"
                    "  Binary Cross-Entropy (Log Loss):\n"
                    "    - For binary classification (0 or 1)\n"
                    "    - Pairs with sigmoid output\n"
                    "    - Penalizes confident wrong predictions heavily\n\n"
                    "  Categorical Cross-Entropy:\n"
                    "    - For multi-class classification\n"
                    "    - Pairs with softmax output\n\n"
                    "  Mean Squared Error (MSE):\n"
                    "    - For regression tasks\n"
                    "    - Penalizes large errors quadratically"
                ),
                "options": [
                    "Mean Squared Error — regression loss",
                    "Binary Cross-Entropy — binary classification loss",
                    "Categorical Cross-Entropy — multi-class loss",
                    "Hinge Loss — SVM margin loss",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Binary classifier + sigmoid output = binary problem.",
                    "Binary classification uses binary cross-entropy.",
                ],
            },
            {
                "id": "mt_2",
                "type": "quiz",
                "title": "Gradient Descent",
                "question": (
                    "During training, the model computes the loss, then updates weights\n"
                    "by moving in the direction that reduces the loss.\n\n"
                    "What is this optimization process called?"
                ),
                "lesson": (
                    "Gradient descent: iteratively update model parameters to minimize loss.\n\n"
                    "Steps per iteration:\n"
                    "  1. Forward pass: compute predictions\n"
                    "  2. Compute loss: compare predictions to true labels\n"
                    "  3. Backward pass: compute gradients via backpropagation\n"
                    "  4. Update weights: w = w - learning_rate * gradient\n\n"
                    "Variants:\n"
                    "  - Batch GD: uses entire dataset per update (slow, stable)\n"
                    "  - Stochastic GD (SGD): uses one sample per update (noisy, fast)\n"
                    "  - Mini-batch GD: uses a small batch (best of both worlds)"
                ),
                "options": [
                    "Backpropagation — computing gradients only",
                    "Gradient descent — iterative weight updates to minimize loss",
                    "Forward propagation — computing predictions",
                    "Regularization — preventing overfitting",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The model follows the slope (gradient) downhill toward lower loss.",
                    "Moving weights in the direction of steepest descent = gradient descent.",
                ],
            },
            {
                "id": "mt_3",
                "type": "quiz",
                "title": "Learning Rate Too High",
                "question": (
                    "During training, the loss oscillates wildly and never converges.\n"
                    "The model's predictions get worse over time.\n\n"
                    "What is the most likely cause?"
                ),
                "lesson": (
                    "Learning rate controls how big each weight update step is.\n\n"
                    "  Too high:\n"
                    "    - Loss oscillates or diverges\n"
                    "    - Overshoots the minimum, bounces around\n"
                    "    - Training becomes unstable\n\n"
                    "  Too low:\n"
                    "    - Training is very slow\n"
                    "    - May get stuck in local minima\n"
                    "    - Loss decreases but takes forever\n\n"
                    "  Just right:\n"
                    "    - Loss decreases steadily\n"
                    "    - Common starting values: 0.001, 0.01\n"
                    "    - Learning rate schedulers reduce it over time"
                ),
                "options": [
                    "Learning rate is too high — overshooting the minimum",
                    "Learning rate is too low — stuck in local minimum",
                    "Too few epochs — not enough training time",
                    "Batch size is too large — poor generalization",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "The loss is oscillating, not plateauing.",
                    "Oscillation and divergence = steps are too large = learning rate too high.",
                ],
            },
            {
                "id": "mt_4",
                "type": "quiz",
                "title": "Epochs and Iterations",
                "question": (
                    "You have 10,000 training samples and a batch size of 100.\n"
                    "One epoch means the model has seen every sample once.\n\n"
                    "How many iterations (weight updates) occur per epoch?"
                ),
                "lesson": (
                    "Epoch: one complete pass through the entire training dataset.\n\n"
                    "  Iterations per epoch = total_samples / batch_size\n"
                    "  10,000 / 100 = 100 iterations per epoch\n\n"
                    "Each iteration:\n"
                    "  1. Take one batch (100 samples)\n"
                    "  2. Forward pass\n"
                    "  3. Compute loss\n"
                    "  4. Backward pass (gradients)\n"
                    "  5. Update weights\n\n"
                    "More epochs = more passes through the data.\n"
                    "Too many epochs → overfitting. Too few → underfitting."
                ),
                "options": [
                    "10 iterations per epoch",
                    "100 iterations per epoch",
                    "1,000 iterations per epoch",
                    "10,000 iterations per epoch",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Divide total samples by batch size.",
                    "10,000 samples / 100 per batch = 100 iterations.",
                ],
            },
            {
                "id": "mt_5",
                "type": "quiz",
                "title": "Batch Size Tradeoffs",
                "question": (
                    "A colleague switches from batch size 32 to batch size 1024.\n"
                    "Training is faster per epoch, but the model generalizes worse.\n\n"
                    "Why does a very large batch size hurt generalization?"
                ),
                "lesson": (
                    "Batch size tradeoffs:\n\n"
                    "  Small batches (16-64):\n"
                    "    - Noisy gradient estimates → acts as regularization\n"
                    "    - Better generalization (empirically)\n"
                    "    - More iterations per epoch → slower wall-clock time\n"
                    "    - Lower GPU memory usage\n\n"
                    "  Large batches (512-4096+):\n"
                    "    - Smoother, more accurate gradients\n"
                    "    - Fewer iterations → faster per epoch\n"
                    "    - Tends to converge to sharp minima → worse generalization\n"
                    "    - Higher GPU memory usage\n\n"
                    "The noise in small-batch gradients helps escape sharp minima\n"
                    "and find flatter minima that generalize better."
                ),
                "options": [
                    "Large batches overfit to the training data",
                    "Large batches converge to sharp minima that generalize poorly",
                    "Large batches cause the learning rate to be too small",
                    "Large batches shuffle the data incorrectly",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It's about what kind of minimum the optimizer finds.",
                    "Smooth gradients from large batches → sharp minima → poor generalization.",
                ],
            },
            {
                "id": "mt_6",
                "type": "quiz",
                "title": "Early Stopping",
                "question": (
                    "Your training loss keeps decreasing, but validation loss stopped\n"
                    "improving 5 epochs ago and is now increasing.\n\n"
                    "What technique should you apply?"
                ),
                "lesson": (
                    "Early stopping: halt training when validation performance stops improving.\n\n"
                    "How it works:\n"
                    "  - Monitor validation loss (or metric) each epoch\n"
                    "  - Keep track of the best validation score\n"
                    "  - If no improvement for N epochs (patience), stop training\n"
                    "  - Restore the model weights from the best epoch\n\n"
                    "Why it works:\n"
                    "  - Training loss always decreases (model keeps fitting training data)\n"
                    "  - Validation loss decreases, then increases (overfitting begins)\n"
                    "  - The gap = overfitting region\n"
                    "  - Early stopping prevents entering that region\n\n"
                    "Patience: how many epochs to wait for improvement before stopping.\n"
                    "Typical values: 3-10 epochs."
                ),
                "options": [
                    "Increase the learning rate to escape the plateau",
                    "Add more training data to reduce validation loss",
                    "Early stopping — halt training when validation loss stops improving",
                    "Remove the validation set and train on all data",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Validation loss is going up while training loss goes down.",
                    "Stop before overfitting gets worse — that's early stopping.",
                ],
            },
        ],
    },

    # ── ZONE 3: FEATURE ENGINEERING ──────────────────────────────────────
    "feature_engineering": {
        "id": "feature_engineering",
        "name": "The Feature Foundry",
        "subtitle": "Selection, Encoding, Normalization & Missing Data",
        "color": "yellow",
        "icon": "⚙️",
        "commands": ["feature selection", "one-hot", "label encoding", "normalization", "imputation"],
        "challenges": [
            {
                "id": "fe_1",
                "type": "quiz",
                "title": "One-Hot Encoding",
                "question": (
                    "Your dataset has a 'color' column with values: red, blue, green.\n"
                    "You need to convert it to numerical features for a linear model.\n\n"
                    "Which encoding creates a separate binary column for each category?"
                ),
                "lesson": (
                    "One-hot encoding: creates one binary column per category.\n\n"
                    "  color → color_red  color_blue  color_green\n"
                    "  red   →    1           0           0\n"
                    "  blue  →    0           1           0\n"
                    "  green →    0           0           1\n\n"
                    "Pros: No ordinal relationship implied between categories.\n"
                    "Cons: High cardinality features (1000+ categories) create many columns.\n\n"
                    "Use one-hot for: low-cardinality nominal categories.\n"
                    "Alternatives for high cardinality: target encoding, embeddings."
                ),
                "options": [
                    "Label encoding — assign integer to each category",
                    "One-hot encoding — binary column per category",
                    "Ordinal encoding — assign ordered integers",
                    "Binary encoding — encode integers in binary",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Each category gets its own column with 0 or 1.",
                    "One column per category, one hot (1) per row = one-hot encoding.",
                ],
            },
            {
                "id": "fe_2",
                "type": "quiz",
                "title": "Label Encoding Danger",
                "question": (
                    "You label-encode a 'city' column: NYC=0, London=1, Tokyo=2.\n"
                    "A linear model now treats Tokyo as 'greater than' London.\n\n"
                    "What is this problem called?"
                ),
                "lesson": (
                    "Label encoding assigns an integer to each category.\n\n"
                    "  NYC → 0, London → 1, Tokyo → 2\n\n"
                    "Problem: linear models interpret this as an ordinal relationship.\n"
                    "  The model thinks Tokyo (2) > London (1) > NYC (0)\n"
                    "  There is no such ordering for cities.\n\n"
                    "When label encoding is safe:\n"
                    "  - Tree-based models (Random Forest, XGBoost) — they split on thresholds\n"
                    "  - Truly ordinal features (low/medium/high, education level)\n\n"
                    "When to avoid it:\n"
                    "  - Linear models, SVMs, neural networks with nominal categories"
                ),
                "options": [
                    "Imposing a false ordinal relationship on nominal data",
                    "Data leakage from the test set",
                    "Multicollinearity between features",
                    "Curse of dimensionality from too many features",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "Cities have no natural order, but integers imply one.",
                    "Label encoding on nominal data creates a false ordinal relationship.",
                ],
            },
            {
                "id": "fe_3",
                "type": "quiz",
                "title": "Feature Normalization",
                "question": (
                    "Your dataset has 'age' (18-90) and 'income' (20,000-500,000).\n"
                    "A KNN model is dominated by the income feature.\n\n"
                    "What should you do?"
                ),
                "lesson": (
                    "Feature normalization/scaling ensures all features contribute equally.\n\n"
                    "  Min-Max Scaling (normalization):\n"
                    "    x_scaled = (x - min) / (max - min) → range [0, 1]\n"
                    "    Good for: bounded features, neural networks\n\n"
                    "  Standard Scaling (standardization):\n"
                    "    x_scaled = (x - mean) / std → mean=0, std=1\n"
                    "    Good for: features with outliers, linear models\n\n"
                    "  Distance-based models (KNN, SVM, K-Means) are especially sensitive\n"
                    "  to feature scales. Tree-based models are NOT affected."
                ),
                "options": [
                    "Remove the income feature entirely",
                    "Normalize/scale features so they have comparable ranges",
                    "Use label encoding on both features",
                    "Increase the K value in KNN",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Income has a much larger range, dominating the distance calculation.",
                    "Scale features to comparable ranges — normalization or standardization.",
                ],
            },
            {
                "id": "fe_4",
                "type": "quiz",
                "title": "Handling Missing Data",
                "question": (
                    "30% of rows in the 'income' column are missing. The data is\n"
                    "Missing At Random (MAR) — missingness depends on other observed variables.\n\n"
                    "Which approach is generally most appropriate?"
                ),
                "lesson": (
                    "Missing data strategies:\n\n"
                    "  Drop rows:\n"
                    "    - Simple but loses data. OK if <5% is missing.\n\n"
                    "  Imputation (fill in values):\n"
                    "    - Mean/median: simple, works for MCAR\n"
                    "    - Model-based (KNN, regression): uses other features to predict\n"
                    "    - Multiple imputation: generates several filled datasets\n\n"
                    "  Missing types:\n"
                    "    - MCAR: missingness is random (rare in practice)\n"
                    "    - MAR: depends on other observed variables\n"
                    "    - MNAR: depends on the missing value itself\n\n"
                    "  For MAR with 30% missing: model-based imputation is preferred.\n"
                    "  Dropping 30% of rows wastes too much data."
                ),
                "options": [
                    "Drop all rows with missing values",
                    "Fill with zeros",
                    "Model-based imputation using other features",
                    "Drop the income column entirely",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "30% is too much to drop. The missingness depends on other variables.",
                    "Use other features to predict the missing values — model-based imputation.",
                ],
            },
            {
                "id": "fe_5",
                "type": "quiz",
                "title": "Feature Selection",
                "question": (
                    "Your model has 500 features. Many are redundant or irrelevant.\n"
                    "Training is slow and the model overfits.\n\n"
                    "Which technique removes irrelevant features based on model performance?"
                ),
                "lesson": (
                    "Feature selection methods:\n\n"
                    "  Filter methods:\n"
                    "    - Correlation analysis, mutual information, chi-squared\n"
                    "    - Fast, model-agnostic, but ignores feature interactions\n\n"
                    "  Wrapper methods (e.g., Recursive Feature Elimination):\n"
                    "    - Train model, rank features by importance, remove weakest\n"
                    "    - Repeat until desired number of features\n"
                    "    - Considers feature interactions, but computationally expensive\n\n"
                    "  Embedded methods:\n"
                    "    - L1 (Lasso) regularization drives coefficients to zero\n"
                    "    - Tree-based feature importance (Random Forest, XGBoost)\n"
                    "    - Feature selection happens during model training"
                ),
                "options": [
                    "PCA — dimensionality reduction, not selection",
                    "Recursive Feature Elimination — remove weakest features iteratively",
                    "One-hot encoding — convert categories to binary",
                    "Standardization — scale features to zero mean",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The question says 'based on model performance' — that's a wrapper method.",
                    "Train, rank, remove weakest, repeat = Recursive Feature Elimination.",
                ],
            },
            {
                "id": "fe_6",
                "type": "quiz",
                "title": "Data Leakage",
                "question": (
                    "You normalize your entire dataset before splitting into train/test.\n"
                    "The test set's mean and standard deviation influenced the scaling.\n\n"
                    "What problem did this create?"
                ),
                "lesson": (
                    "Data leakage: information from outside the training set leaks into\n"
                    "the model, giving unrealistically good results.\n\n"
                    "Common causes:\n"
                    "  - Scaling/normalizing before splitting (test stats leak into train)\n"
                    "  - Using future data to predict past events\n"
                    "  - Target leakage: a feature that encodes the label\n\n"
                    "Correct approach:\n"
                    "  1. Split data first\n"
                    "  2. Fit scaler on training set only\n"
                    "  3. Transform both train and test with the training scaler\n\n"
                    "Use sklearn Pipelines to prevent leakage automatically."
                ),
                "options": [
                    "Overfitting — model memorized training data",
                    "Underfitting — model is too simple",
                    "Data leakage — test set information leaked into preprocessing",
                    "Class imbalance — unequal distribution of labels",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "The test set statistics were used during preprocessing.",
                    "Information from the test set leaked into the training pipeline = data leakage.",
                ],
            },
        ],
    },

    # ── ZONE 4: ML OPS ──────────────────────────────────────────────────
    "ml_ops": {
        "id": "ml_ops",
        "name": "The Experiment Vault",
        "subtitle": "Model Registry, Experiment Tracking, Versioning & A/B Testing",
        "color": "magenta",
        "icon": "🔬",
        "commands": ["mlflow", "wandb", "model registry", "experiment tracking", "a/b testing"],
        "challenges": [
            {
                "id": "mlo_1",
                "type": "quiz",
                "title": "Experiment Tracking",
                "question": (
                    "Your team trains dozens of models with different hyperparameters.\n"
                    "Nobody can remember which run produced the best results.\n\n"
                    "What practice solves this?"
                ),
                "lesson": (
                    "Experiment tracking: systematically log every training run.\n\n"
                    "What to track:\n"
                    "  - Hyperparameters (learning rate, batch size, architecture)\n"
                    "  - Metrics (loss, accuracy, F1, AUC) over time\n"
                    "  - Artifacts (model weights, plots, confusion matrices)\n"
                    "  - Code version (git commit hash)\n"
                    "  - Data version (dataset hash or version tag)\n\n"
                    "Tools:\n"
                    "  - MLflow Tracking: open-source, self-hosted or managed\n"
                    "  - Weights & Biases (W&B): cloud-first, great visualization\n"
                    "  - Neptune, Comet, ClearML"
                ),
                "options": [
                    "Experiment tracking — log all runs, params, and metrics",
                    "Model serving — deploy models to production",
                    "Feature engineering — create better input features",
                    "Data versioning — track dataset changes only",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "You need to log hyperparameters and metrics for every run.",
                    "Systematically recording every experiment = experiment tracking.",
                ],
            },
            {
                "id": "mlo_2",
                "type": "quiz",
                "title": "Model Registry",
                "question": (
                    "After experiment tracking identifies the best model, it needs to be\n"
                    "promoted through stages: Staging → Production → Archived.\n\n"
                    "What system manages these model lifecycle stages?"
                ),
                "lesson": (
                    "Model registry: a centralized store for versioned, production-ready models.\n\n"
                    "Key features:\n"
                    "  - Version control for models (v1, v2, v3...)\n"
                    "  - Stage transitions: None → Staging → Production → Archived\n"
                    "  - Metadata: who trained it, when, on what data, what metrics\n"
                    "  - Lineage: link model to experiment run, dataset, code commit\n\n"
                    "Tools:\n"
                    "  - MLflow Model Registry\n"
                    "  - Vertex AI Model Registry (GCP)\n"
                    "  - SageMaker Model Registry (AWS)\n"
                    "  - Azure ML Model Registry"
                ),
                "options": [
                    "Experiment tracker — logs training runs",
                    "Model registry — manages model versions and lifecycle stages",
                    "Feature store — serves features for inference",
                    "Container registry — stores Docker images",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The model moves through lifecycle stages: Staging → Production.",
                    "Versioned models with stage transitions = model registry.",
                ],
            },
            {
                "id": "mlo_3",
                "type": "quiz",
                "title": "MLflow Components",
                "question": (
                    "Your team uses MLflow. A data scientist calls mlflow.log_param(),\n"
                    "mlflow.log_metric(), and mlflow.log_artifact() during training.\n\n"
                    "Which MLflow component handles this?"
                ),
                "lesson": (
                    "MLflow has four main components:\n\n"
                    "  1. MLflow Tracking:\n"
                    "     - Log parameters, metrics, artifacts per run\n"
                    "     - API: mlflow.log_param(), mlflow.log_metric(), mlflow.log_artifact()\n"
                    "     - UI for comparing runs\n\n"
                    "  2. MLflow Projects:\n"
                    "     - Package code in a reproducible format (MLproject file)\n\n"
                    "  3. MLflow Models:\n"
                    "     - Standard format for packaging models\n"
                    "     - Deploy to REST API, Spark, Docker, etc.\n\n"
                    "  4. Model Registry:\n"
                    "     - Versioning and stage management for models"
                ),
                "options": [
                    "MLflow Tracking — log params, metrics, artifacts",
                    "MLflow Projects — package reproducible code",
                    "MLflow Models — standard model packaging format",
                    "MLflow Registry — version and stage models",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "log_param, log_metric, log_artifact — all logging functions.",
                    "Logging training runs = MLflow Tracking.",
                ],
            },
            {
                "id": "mlo_4",
                "type": "quiz",
                "title": "Model Versioning",
                "question": (
                    "Your production model was trained on data from January. New data\n"
                    "arrives monthly. You retrain and want to compare v1, v2, v3.\n\n"
                    "Which practice ensures you can reproduce any previous model exactly?"
                ),
                "lesson": (
                    "Reproducibility requires versioning everything:\n\n"
                    "  1. Code versioning: git commit hash pinned to each run\n"
                    "  2. Data versioning: track which dataset version was used\n"
                    "     Tools: DVC, Delta Lake, lakeFS\n"
                    "  3. Model versioning: store model artifacts with metadata\n"
                    "  4. Environment versioning: pip freeze, conda env, Docker image\n"
                    "  5. Random seed: set seeds for numpy, torch, python\n\n"
                    "Without all five, you cannot reproduce a training run.\n"
                    "Model versioning alone is not enough — you need the full lineage."
                ),
                "options": [
                    "Version the model weights only",
                    "Version code, data, model, environment, and random seeds together",
                    "Keep a spreadsheet of hyperparameters",
                    "Save the final model and discard training artifacts",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Reproducing a model requires more than just the weights.",
                    "Full reproducibility = code + data + model + environment + seeds.",
                ],
            },
            {
                "id": "mlo_5",
                "type": "quiz",
                "title": "A/B Testing Models",
                "question": (
                    "You've trained a new recommendation model. Before replacing the\n"
                    "current model, you want to compare them on live traffic.\n\n"
                    "What deployment strategy sends a fraction of users to each model?"
                ),
                "lesson": (
                    "A/B testing models in production:\n\n"
                    "  Setup:\n"
                    "    - Model A (control): current production model\n"
                    "    - Model B (challenger): new candidate model\n"
                    "    - Split traffic: e.g., 90% to A, 10% to B\n\n"
                    "  Measure:\n"
                    "    - Business metrics (CTR, revenue, engagement)\n"
                    "    - Statistical significance (p-value < 0.05)\n"
                    "    - Practical significance (is the lift worth the complexity?)\n\n"
                    "  Related strategies:\n"
                    "    - Shadow mode: new model runs but doesn't serve results\n"
                    "    - Canary deployment: gradual traffic ramp-up\n"
                    "    - Multi-armed bandit: dynamically allocate more traffic to winner"
                ),
                "options": [
                    "Blue-green deployment — instant full switch",
                    "A/B testing — split traffic between models and measure",
                    "Shadow deployment — new model runs silently",
                    "Rolling deployment — gradual instance replacement",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Users are split between two models to compare live performance.",
                    "Splitting traffic + measuring outcomes = A/B testing.",
                ],
            },
        ],
    },

    # ── ZONE 5: MODEL SERVING ────────────────────────────────────────────
    "model_serving": {
        "id": "model_serving",
        "name": "The Inference Grid",
        "subtitle": "REST APIs, Batch Inference, Latency & GPU/CPU Tradeoffs",
        "color": "blue",
        "icon": "🚀",
        "commands": ["rest api", "batch inference", "real-time", "latency", "gpu", "cpu"],
        "challenges": [
            {
                "id": "ms_1",
                "type": "quiz",
                "title": "Real-Time vs Batch Inference",
                "question": (
                    "A fraud detection system must score each transaction in under 50ms\n"
                    "as it happens.\n\n"
                    "Which inference pattern is required?"
                ),
                "lesson": (
                    "Real-time (online) inference:\n"
                    "  - Single prediction per request\n"
                    "  - Low latency requirement (ms to seconds)\n"
                    "  - Served via REST API or gRPC endpoint\n"
                    "  - Use cases: fraud detection, search ranking, chatbots\n\n"
                    "Batch inference:\n"
                    "  - Score many records at once (hourly, daily)\n"
                    "  - Higher latency acceptable (minutes to hours)\n"
                    "  - Results stored in a database or data warehouse\n"
                    "  - Use cases: email campaigns, recommendation pre-computation,\n"
                    "    credit scoring overnight"
                ),
                "options": [
                    "Batch inference — score all transactions nightly",
                    "Real-time inference — score each transaction as it arrives",
                    "Streaming inference — process micro-batches every minute",
                    "Offline inference — generate scores in a Jupyter notebook",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Under 50ms per transaction, as it happens.",
                    "Immediate, per-request scoring = real-time inference.",
                ],
            },
            {
                "id": "ms_2",
                "type": "quiz",
                "title": "Model Serving via REST API",
                "question": (
                    "You wrap a trained model in a Flask/FastAPI server. Clients send\n"
                    "JSON with features, the server returns predictions.\n\n"
                    "What is this deployment pattern called?"
                ),
                "lesson": (
                    "Model-as-a-Service via REST API:\n\n"
                    "  Architecture:\n"
                    "    Client → HTTP POST /predict {features} → Server → {prediction}\n\n"
                    "  Implementation:\n"
                    "    - Flask, FastAPI, or dedicated serving frameworks\n"
                    "    - TensorFlow Serving, TorchServe, Triton Inference Server\n"
                    "    - BentoML, MLflow serve, Seldon Core\n\n"
                    "  Concerns:\n"
                    "    - Latency: model load time, preprocessing, inference\n"
                    "    - Throughput: requests per second\n"
                    "    - Scaling: horizontal (more replicas) vs vertical (bigger machine)\n"
                    "    - Versioning: /v1/predict vs /v2/predict"
                ),
                "options": [
                    "Model-as-a-Service — REST API serving predictions",
                    "Embedded model — model compiled into the client application",
                    "Batch pipeline — model runs on a schedule",
                    "Edge deployment — model runs on device hardware",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "HTTP request in, JSON prediction out.",
                    "Wrapping a model behind a REST API = Model-as-a-Service.",
                ],
            },
            {
                "id": "ms_3",
                "type": "quiz",
                "title": "GPU vs CPU Inference",
                "question": (
                    "Your image classification model takes 200ms on CPU but 15ms on GPU.\n"
                    "However, GPU instances cost 8x more.\n\n"
                    "When does GPU inference make economic sense?"
                ),
                "lesson": (
                    "GPU vs CPU inference tradeoffs:\n\n"
                    "  GPU:\n"
                    "    - Massively parallel (thousands of cores)\n"
                    "    - Best for: large neural networks, batch inference, vision, NLP\n"
                    "    - Higher throughput per dollar at high utilization\n"
                    "    - Expensive when idle (GPU instances cost 3-10x more)\n\n"
                    "  CPU:\n"
                    "    - Lower latency for simple models (tree-based, small NNs)\n"
                    "    - Better cost efficiency at low/variable traffic\n"
                    "    - Easier to scale horizontally\n"
                    "    - Best for: tabular models, lightweight inference\n\n"
                    "  Rule of thumb: GPU pays off when throughput demand is high\n"
                    "  enough to keep the GPU utilized (>60-70%)."
                ),
                "options": [
                    "Always — GPUs are always faster",
                    "When throughput demand is high enough to keep GPUs utilized",
                    "Never — the cost difference is too large",
                    "Only for training, never for inference",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "GPUs cost more but are much faster. It depends on utilization.",
                    "High utilization = GPU cost per inference drops below CPU.",
                ],
            },
            {
                "id": "ms_4",
                "type": "quiz",
                "title": "Model Latency Breakdown",
                "question": (
                    "Your model endpoint has p99 latency of 500ms. The model inference\n"
                    "itself takes only 50ms.\n\n"
                    "Where is the remaining latency most likely coming from?"
                ),
                "lesson": (
                    "End-to-end inference latency breakdown:\n\n"
                    "  1. Network latency: request/response transit time\n"
                    "  2. Preprocessing: feature extraction, tokenization, normalization\n"
                    "  3. Feature retrieval: fetching features from a feature store\n"
                    "  4. Model inference: the actual forward pass\n"
                    "  5. Postprocessing: formatting, thresholding, business logic\n"
                    "  6. Serialization: JSON encode/decode\n\n"
                    "Often, preprocessing and feature retrieval dominate latency,\n"
                    "not the model itself. Optimize the entire pipeline, not just the model.\n\n"
                    "Tools: profiling, distributed tracing, caching hot features."
                ),
                "options": [
                    "The model is secretly larger than reported",
                    "Preprocessing, feature retrieval, and network overhead",
                    "GPU cold start from power-saving mode",
                    "Database writes for logging predictions",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Model inference is 50ms out of 500ms total.",
                    "The other 450ms = preprocessing, feature fetch, network, serialization.",
                ],
            },
            {
                "id": "ms_5",
                "type": "quiz",
                "title": "Model Optimization Techniques",
                "question": (
                    "You need to deploy a large neural network on edge devices with\n"
                    "limited memory and compute.\n\n"
                    "Which technique reduces model size while preserving most accuracy?"
                ),
                "lesson": (
                    "Model optimization for deployment:\n\n"
                    "  Quantization:\n"
                    "    - Reduce precision: FP32 → FP16 → INT8\n"
                    "    - 2-4x smaller model, faster inference\n"
                    "    - Small accuracy loss (often <1%)\n\n"
                    "  Pruning:\n"
                    "    - Remove weights close to zero\n"
                    "    - Structured (remove entire neurons) vs unstructured (individual weights)\n\n"
                    "  Knowledge Distillation:\n"
                    "    - Train a smaller 'student' model to mimic a larger 'teacher'\n"
                    "    - Student is much smaller but retains most performance\n\n"
                    "  ONNX Runtime:\n"
                    "    - Framework-agnostic inference optimization\n"
                    "    - Graph optimization, operator fusion"
                ),
                "options": [
                    "Quantization — reduce numerical precision to shrink model",
                    "Data augmentation — generate more training data",
                    "Gradient accumulation — simulate larger batch sizes",
                    "Learning rate scheduling — adjust training speed",
                ],
                "answer": "a",
                "xp": 35,
                "hints": [
                    "You need to reduce model size for edge deployment.",
                    "Lowering precision (FP32 → INT8) = quantization = smaller, faster model.",
                ],
            },
        ],
    },

    # ── ZONE 6: LLM OPS ─────────────────────────────────────────────────
    "llm_ops": {
        "id": "llm_ops",
        "name": "The Language Nexus",
        "subtitle": "Fine-Tuning, RAG, Prompt Management & Token Economics",
        "color": "red",
        "icon": "🤖",
        "commands": ["fine-tuning", "rag", "prompt management", "tokens", "evaluation"],
        "challenges": [
            {
                "id": "llm_1",
                "type": "quiz",
                "title": "RAG Architecture",
                "question": (
                    "Your LLM needs to answer questions about internal company documents\n"
                    "that were not in its training data.\n\n"
                    "Which architecture retrieves relevant documents and includes them\n"
                    "in the prompt?"
                ),
                "lesson": (
                    "Retrieval-Augmented Generation (RAG):\n\n"
                    "  Flow:\n"
                    "    1. User asks a question\n"
                    "    2. Retrieve relevant documents from a vector store\n"
                    "    3. Stuff retrieved context into the prompt\n"
                    "    4. LLM generates answer grounded in retrieved context\n\n"
                    "  Components:\n"
                    "    - Embedding model: convert text to vectors\n"
                    "    - Vector store: Pinecone, Weaviate, Chroma, pgvector\n"
                    "    - Retriever: similarity search (cosine, dot product)\n"
                    "    - Generator: LLM that produces the final answer\n\n"
                    "  RAG vs Fine-tuning:\n"
                    "    - RAG: better for factual, up-to-date knowledge\n"
                    "    - Fine-tuning: better for style, format, domain behavior"
                ),
                "options": [
                    "Fine-tuning — retrain the LLM on company documents",
                    "RAG — retrieve relevant docs and include them in the prompt",
                    "Prompt engineering — write better system prompts",
                    "RLHF — train with human feedback on company data",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The model doesn't have this knowledge — it needs to retrieve it.",
                    "Retrieve documents, put them in the prompt, generate = RAG.",
                ],
            },
            {
                "id": "llm_2",
                "type": "quiz",
                "title": "Fine-Tuning vs Prompting",
                "question": (
                    "You want your LLM to always respond in a specific JSON schema\n"
                    "with a particular tone. Prompt engineering alone is unreliable.\n\n"
                    "What approach should you consider next?"
                ),
                "lesson": (
                    "Fine-tuning: further train a pre-trained LLM on your specific data.\n\n"
                    "  When to fine-tune:\n"
                    "    - Consistent output format/style needed\n"
                    "    - Domain-specific behavior (legal, medical, code)\n"
                    "    - Prompt engineering is insufficient or too expensive (long prompts)\n\n"
                    "  Types:\n"
                    "    - Full fine-tuning: update all weights (expensive)\n"
                    "    - LoRA/QLoRA: update small adapter layers (efficient)\n"
                    "    - Instruction tuning: train on instruction-response pairs\n\n"
                    "  Costs:\n"
                    "    - Compute for training (GPU hours)\n"
                    "    - Data preparation (curated examples)\n"
                    "    - Ongoing maintenance (retrain when base model updates)"
                ),
                "options": [
                    "Increase temperature to add randomness",
                    "Fine-tune the model on examples of the desired format/tone",
                    "Use a larger context window",
                    "Add more retrieval documents via RAG",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "You need consistent style and format that prompting can't achieve.",
                    "Training on examples of desired output = fine-tuning.",
                ],
            },
            {
                "id": "llm_3",
                "type": "quiz",
                "title": "Token Cost Management",
                "question": (
                    "Your RAG system stuffs 10 retrieved documents into every prompt.\n"
                    "Monthly API costs have tripled.\n\n"
                    "What is the most effective way to reduce token costs?"
                ),
                "lesson": (
                    "Token cost optimization strategies:\n\n"
                    "  1. Reduce input tokens:\n"
                    "     - Retrieve fewer, more relevant documents\n"
                    "     - Summarize retrieved chunks before stuffing\n"
                    "     - Use smaller chunk sizes with better retrieval\n\n"
                    "  2. Reduce output tokens:\n"
                    "     - Set max_tokens limit\n"
                    "     - Constrain output format\n\n"
                    "  3. Use cheaper models:\n"
                    "     - Route simple queries to smaller/cheaper models\n"
                    "     - Use model cascading: try cheap model first, escalate if needed\n\n"
                    "  4. Caching:\n"
                    "     - Cache common query responses\n"
                    "     - Semantic caching (similar queries → cached answer)\n\n"
                    "  Input tokens typically cost less than output tokens per token,\n"
                    "  but volume of input is usually much higher."
                ),
                "options": [
                    "Switch to a more expensive, faster model",
                    "Retrieve fewer, more relevant documents and summarize context",
                    "Increase the temperature parameter",
                    "Add more documents for better accuracy",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "10 documents means huge prompts. Fewer but better docs = fewer tokens.",
                    "Better retrieval + fewer documents + summarization = lower token costs.",
                ],
            },
            {
                "id": "llm_4",
                "type": "quiz",
                "title": "Prompt Management",
                "question": (
                    "Your team has 50 prompt templates across 12 services. Nobody knows\n"
                    "which version of a prompt is running in production.\n\n"
                    "What practice addresses this?"
                ),
                "lesson": (
                    "Prompt management: version, test, and deploy prompts systematically.\n\n"
                    "  Key practices:\n"
                    "    - Version control prompts (git, or dedicated prompt registry)\n"
                    "    - A/B test prompt variations\n"
                    "    - Track which prompt version is in production\n"
                    "    - Evaluate prompts against test cases before deploying\n\n"
                    "  Tools:\n"
                    "    - LangSmith, PromptLayer, Humanloop\n"
                    "    - Or: store prompts in config files with version tags\n\n"
                    "  Anti-patterns:\n"
                    "    - Hardcoded prompts scattered across codebase\n"
                    "    - No evaluation before deployment\n"
                    "    - No rollback capability"
                ),
                "options": [
                    "Prompt management — version, test, and track prompt templates",
                    "Fine-tuning — eliminate the need for prompts entirely",
                    "Caching — store all prompt responses",
                    "Model distillation — bake prompts into a smaller model",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "50 templates, no versioning, no tracking — it's a management problem.",
                    "Version control + testing + tracking prompts = prompt management.",
                ],
            },
            {
                "id": "llm_5",
                "type": "quiz",
                "title": "LLM Evaluation Metrics",
                "question": (
                    "You need to evaluate whether your RAG system's answers are factually\n"
                    "grounded in the retrieved documents.\n\n"
                    "Which evaluation approach checks for faithfulness to source context?"
                ),
                "lesson": (
                    "LLM evaluation metrics:\n\n"
                    "  RAG-specific:\n"
                    "    - Faithfulness: is the answer supported by retrieved context?\n"
                    "    - Answer relevance: does the answer address the question?\n"
                    "    - Context relevance: are retrieved docs relevant to the question?\n\n"
                    "  General:\n"
                    "    - BLEU/ROUGE: n-gram overlap with reference (machine translation)\n"
                    "    - Perplexity: how surprised the model is (lower = better)\n"
                    "    - Human evaluation: gold standard but expensive\n\n"
                    "  Frameworks:\n"
                    "    - RAGAS: faithfulness, relevance, context metrics\n"
                    "    - DeepEval, TruLens: automated LLM evaluation\n"
                    "    - LLM-as-judge: use a strong LLM to evaluate a weaker one"
                ),
                "options": [
                    "BLEU score — n-gram overlap with reference text",
                    "Perplexity — model confidence in its predictions",
                    "Faithfulness evaluation — answer grounded in retrieved context",
                    "Accuracy — percentage of correct predictions",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "The question is about grounding answers in source documents.",
                    "Checking if output is supported by retrieved context = faithfulness.",
                ],
            },
            {
                "id": "llm_6",
                "type": "quiz",
                "title": "Embedding Models",
                "question": (
                    "In a RAG pipeline, documents and queries must be converted to\n"
                    "numerical vectors for similarity search.\n\n"
                    "What model performs this conversion?"
                ),
                "lesson": (
                    "Embedding models convert text to dense numerical vectors.\n\n"
                    "  How it works:\n"
                    "    - Input: text string (sentence, paragraph, document)\n"
                    "    - Output: fixed-size vector (e.g., 768 or 1536 dimensions)\n"
                    "    - Similar texts → similar vectors (close in vector space)\n\n"
                    "  Popular models:\n"
                    "    - OpenAI text-embedding-3-small/large\n"
                    "    - Sentence-Transformers (open source)\n"
                    "    - Cohere embed, Voyage AI\n\n"
                    "  Vector similarity:\n"
                    "    - Cosine similarity: angle between vectors\n"
                    "    - Dot product: magnitude-aware similarity\n"
                    "    - Euclidean distance: straight-line distance"
                ),
                "options": [
                    "A classification model — assigns category labels",
                    "An embedding model — converts text to dense vectors",
                    "A generative model — produces new text",
                    "A regression model — predicts continuous values",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Text in, numerical vector out — for similarity search.",
                    "Converting text to vectors = embedding model.",
                ],
            },
        ],
    },

    # ── ZONE 7: DATA PIPELINES FOR ML ───────────────────────────────────
    "data_pipelines_ml": {
        "id": "data_pipelines_ml",
        "name": "The Pipeline Forge",
        "subtitle": "Feature Stores, Training Pipelines, Data Drift & Monitoring",
        "color": "white",
        "icon": "🔗",
        "commands": ["feature store", "training pipeline", "data drift", "model monitoring"],
        "challenges": [
            {
                "id": "dp_1",
                "type": "quiz",
                "title": "Feature Stores",
                "question": (
                    "Multiple teams need the same 'customer_lifetime_value' feature.\n"
                    "Each team computes it differently, causing inconsistency.\n\n"
                    "What infrastructure solves this?"
                ),
                "lesson": (
                    "Feature store: centralized system for storing, sharing, and serving features.\n\n"
                    "  Key capabilities:\n"
                    "    - Single source of truth for feature definitions\n"
                    "    - Serve features for both training (batch) and inference (online)\n"
                    "    - Feature versioning and lineage\n"
                    "    - Point-in-time correctness (avoid future data leakage)\n\n"
                    "  Online store: low-latency serving for real-time inference (Redis, DynamoDB)\n"
                    "  Offline store: batch access for training (S3, BigQuery, data warehouse)\n\n"
                    "  Tools: Feast (open source), Tecton, Hopsworks, Vertex AI Feature Store"
                ),
                "options": [
                    "Data warehouse — store raw and transformed data",
                    "Feature store — centralized feature storage and serving",
                    "Model registry — version and manage trained models",
                    "ETL pipeline — extract, transform, load data",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Multiple teams need the same feature computed the same way.",
                    "Centralized, shared feature computation and serving = feature store.",
                ],
            },
            {
                "id": "dp_2",
                "type": "quiz",
                "title": "Training Pipelines",
                "question": (
                    "Your model must be retrained weekly with new data. The process includes:\n"
                    "data validation, feature engineering, training, evaluation, and registration.\n\n"
                    "What should orchestrate these steps?"
                ),
                "lesson": (
                    "ML training pipelines: automated, reproducible workflows.\n\n"
                    "  Typical steps:\n"
                    "    1. Data ingestion and validation\n"
                    "    2. Feature engineering / preprocessing\n"
                    "    3. Model training\n"
                    "    4. Model evaluation (compare to baseline)\n"
                    "    5. Model registration (if better than current)\n"
                    "    6. Deployment trigger\n\n"
                    "  Orchestration tools:\n"
                    "    - Kubeflow Pipelines (Kubernetes-native)\n"
                    "    - Vertex AI Pipelines (GCP managed)\n"
                    "    - SageMaker Pipelines (AWS managed)\n"
                    "    - Airflow / Prefect / Dagster (general-purpose)\n"
                    "    - ZenML, Metaflow (ML-specific)"
                ),
                "options": [
                    "A Jupyter notebook run manually each week",
                    "An orchestrated ML pipeline with automated steps",
                    "A cron job that runs a single Python script",
                    "A CI/CD pipeline designed for code deployment",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Multiple steps that must run in order, weekly, reliably.",
                    "Automated, multi-step workflow = orchestrated ML pipeline.",
                ],
            },
            {
                "id": "dp_3",
                "type": "quiz",
                "title": "Data Drift Detection",
                "question": (
                    "Your model was trained on data from Q1. By Q3, the input feature\n"
                    "distributions have shifted significantly. Model performance degrades.\n\n"
                    "What is this phenomenon called?"
                ),
                "lesson": (
                    "Data drift: input data distribution changes over time.\n\n"
                    "  Types of drift:\n"
                    "    - Data drift (covariate shift): input feature distributions change\n"
                    "      Example: customer demographics shift seasonally\n\n"
                    "    - Concept drift: relationship between inputs and outputs changes\n"
                    "      Example: what counts as 'spam' evolves over time\n\n"
                    "    - Label drift: target variable distribution changes\n"
                    "      Example: fraud rate increases during holidays\n\n"
                    "  Detection methods:\n"
                    "    - Statistical tests (KS test, PSI, chi-squared)\n"
                    "    - Monitor feature distributions over time\n"
                    "    - Track model performance metrics continuously\n\n"
                    "  Response: retrain, adjust decision thresholds, or trigger alerts."
                ),
                "options": [
                    "Overfitting — model memorized training data",
                    "Data drift — input feature distributions shifted",
                    "Model decay — weights degrade over time",
                    "Feature leakage — test data leaked into training",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The input data changed between training and serving.",
                    "Input distribution shift over time = data drift.",
                ],
            },
            {
                "id": "dp_4",
                "type": "quiz",
                "title": "Model Performance Monitoring",
                "question": (
                    "Your production model's accuracy is gradually declining over weeks.\n"
                    "You need to detect this automatically and trigger retraining.\n\n"
                    "What should you monitor?"
                ),
                "lesson": (
                    "Model monitoring in production:\n\n"
                    "  What to monitor:\n"
                    "    - Prediction metrics: accuracy, F1, AUC (when ground truth is available)\n"
                    "    - Proxy metrics: prediction distribution, confidence scores\n"
                    "    - Data quality: missing values, schema violations, outliers\n"
                    "    - Feature drift: distribution changes vs training data\n"
                    "    - Operational metrics: latency, throughput, error rates\n\n"
                    "  Challenge: ground truth delay\n"
                    "    - Fraud labels arrive weeks later\n"
                    "    - Use proxy metrics until ground truth is available\n\n"
                    "  Tools: Evidently AI, Whylabs, Arize, Fiddler, NannyML"
                ),
                "options": [
                    "Only server CPU and memory usage",
                    "Prediction metrics, data quality, feature drift, and operational metrics",
                    "Only the number of API requests per second",
                    "Only the model's training loss from the last run",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Accuracy is declining — you need to catch this across multiple dimensions.",
                    "Comprehensive monitoring = predictions + data quality + drift + operations.",
                ],
            },
            {
                "id": "dp_5",
                "type": "quiz",
                "title": "Concept Drift",
                "question": (
                    "A spam classifier trained in 2023 performs poorly in 2025 because\n"
                    "spammers now use AI-generated text that looks legitimate.\n\n"
                    "What type of drift is this?"
                ),
                "lesson": (
                    "Concept drift: the relationship between inputs and the target changes.\n\n"
                    "  Data drift vs Concept drift:\n"
                    "    - Data drift: P(X) changes, but P(Y|X) stays the same\n"
                    "      → same patterns, different input distribution\n"
                    "    - Concept drift: P(Y|X) changes\n"
                    "      → the meaning of 'spam' itself has evolved\n\n"
                    "  Examples of concept drift:\n"
                    "    - Spam evolves to bypass filters\n"
                    "    - Customer preferences change (recommendation models)\n"
                    "    - Economic conditions change (credit scoring models)\n\n"
                    "  Concept drift is harder to detect than data drift because\n"
                    "  the inputs may look similar but the correct labels change."
                ),
                "options": [
                    "Data drift — input distributions changed",
                    "Concept drift — the input-output relationship changed",
                    "Label drift — the target distribution shifted",
                    "Model drift — the weights degraded",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "What counts as spam has changed, not just the email distribution.",
                    "The definition of the target concept evolved = concept drift.",
                ],
            },
        ],
    },

    # ── ZONE 8: RESPONSIBLE AI ───────────────────────────────────────────
    "responsible_ai": {
        "id": "responsible_ai",
        "name": "The Ethics Core",
        "subtitle": "Fairness, Explainability, Model Cards & AI Governance",
        "color": "bright_white",
        "icon": "⚖️",
        "commands": ["fairness", "shap", "lime", "model cards", "bias detection", "governance"],
        "challenges": [
            {
                "id": "ra_1",
                "type": "quiz",
                "title": "SHAP Explainability",
                "question": (
                    "A loan approval model rejects an applicant. The applicant asks:\n"
                    "'Why was I rejected?'\n\n"
                    "Which technique shows how each feature contributed to the decision?"
                ),
                "lesson": (
                    "SHAP (SHapley Additive exPlanations):\n\n"
                    "  Based on game theory (Shapley values).\n"
                    "  For each prediction, assigns each feature a contribution score.\n\n"
                    "  Example output:\n"
                    "    income: -0.3 (pushed toward rejection)\n"
                    "    credit_score: +0.5 (pushed toward approval)\n"
                    "    debt_ratio: -0.4 (pushed toward rejection)\n\n"
                    "  Properties:\n"
                    "    - Local explanations (per prediction)\n"
                    "    - Global explanations (aggregate feature importance)\n"
                    "    - Model-agnostic (works with any model)\n"
                    "    - Mathematically grounded (Shapley values are fair)\n\n"
                    "  Tools: shap library (Python), integrated in many ML platforms"
                ),
                "options": [
                    "SHAP — Shapley values showing each feature's contribution",
                    "PCA — reduce dimensionality to visualize data",
                    "Cross-validation — evaluate model on different data splits",
                    "Gradient descent — show how weights were optimized",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "You need per-feature contribution to a single prediction.",
                    "Shapley values decompose a prediction into feature contributions = SHAP.",
                ],
            },
            {
                "id": "ra_2",
                "type": "quiz",
                "title": "LIME Explanations",
                "question": (
                    "You need to explain a single prediction from a complex deep learning\n"
                    "model by approximating its behavior locally with a simple model.\n\n"
                    "Which technique does this?"
                ),
                "lesson": (
                    "LIME (Local Interpretable Model-agnostic Explanations):\n\n"
                    "  How it works:\n"
                    "    1. Perturb the input (create similar variants)\n"
                    "    2. Get predictions from the complex model on perturbed inputs\n"
                    "    3. Fit a simple, interpretable model (e.g., linear) locally\n"
                    "    4. The simple model explains the complex model's behavior nearby\n\n"
                    "  LIME vs SHAP:\n"
                    "    - LIME: faster, approximate, local only\n"
                    "    - SHAP: theoretically grounded, exact, local + global\n"
                    "    - Both are model-agnostic\n\n"
                    "  Use LIME when:\n"
                    "    - Speed matters more than theoretical guarantees\n"
                    "    - You need quick local explanations for individual predictions"
                ),
                "options": [
                    "SHAP — exact Shapley value decomposition",
                    "LIME — local surrogate model approximation",
                    "Feature importance — global ranking from tree models",
                    "Attention maps — visualize transformer attention weights",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Approximate complex model behavior locally with a simple model.",
                    "Local surrogate model = LIME.",
                ],
            },
            {
                "id": "ra_3",
                "type": "quiz",
                "title": "Model Cards",
                "question": (
                    "Before deploying a model, your organization requires documentation\n"
                    "of its intended use, limitations, training data, and performance\n"
                    "across demographic groups.\n\n"
                    "What is this documentation called?"
                ),
                "lesson": (
                    "Model cards: standardized documentation for ML models.\n\n"
                    "  Contents (originally proposed by Mitchell et al., 2019):\n"
                    "    - Model details: architecture, version, owner\n"
                    "    - Intended use: what the model is designed for\n"
                    "    - Out-of-scope use: what it should NOT be used for\n"
                    "    - Training data: what data was used, any known biases\n"
                    "    - Evaluation: metrics across different subgroups\n"
                    "    - Ethical considerations: potential harms, limitations\n"
                    "    - Caveats and recommendations\n\n"
                    "  Purpose: transparency, accountability, informed deployment decisions.\n"
                    "  Required by some regulations (EU AI Act, NIST AI RMF)."
                ),
                "options": [
                    "A README file in the git repository",
                    "A model card — standardized model documentation",
                    "An API specification (OpenAPI/Swagger)",
                    "A data dictionary for the training dataset",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Standardized documentation of use, limitations, and demographic performance.",
                    "This is a model card — proposed by Google researchers in 2019.",
                ],
            },
            {
                "id": "ra_4",
                "type": "quiz",
                "title": "Bias Detection",
                "question": (
                    "Your hiring model approves 80% of male applicants but only 55% of\n"
                    "female applicants with equivalent qualifications.\n\n"
                    "What type of fairness metric measures this disparity?"
                ),
                "lesson": (
                    "Fairness metrics for ML:\n\n"
                    "  Demographic Parity (Statistical Parity):\n"
                    "    - P(positive | group A) = P(positive | group B)\n"
                    "    - Equal approval rates across groups\n\n"
                    "  Equalized Odds:\n"
                    "    - Equal true positive rates AND false positive rates across groups\n\n"
                    "  Disparate Impact:\n"
                    "    - Ratio of approval rates: min_group / max_group\n"
                    "    - 55/80 = 0.69 (below the 0.8 threshold = disparate impact)\n"
                    "    - The '80% rule' (or 4/5ths rule) from US employment law\n\n"
                    "  Predictive Parity:\n"
                    "    - Equal precision across groups\n\n"
                    "  Tools: Fairlearn, AI Fairness 360, What-If Tool"
                ),
                "options": [
                    "Accuracy — overall percentage of correct predictions",
                    "Disparate impact — ratio of approval rates across groups",
                    "AUC-ROC — model's ability to discriminate classes",
                    "Perplexity — model's surprise at the data",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Different approval rates for different demographic groups.",
                    "Ratio of approval rates across groups = disparate impact.",
                ],
            },
            {
                "id": "ra_5",
                "type": "quiz",
                "title": "AI Governance",
                "question": (
                    "Your company is deploying ML models across multiple business units.\n"
                    "There's no central oversight for model risk, compliance, or auditing.\n\n"
                    "What organizational practice addresses this?"
                ),
                "lesson": (
                    "AI governance: organizational framework for responsible AI deployment.\n\n"
                    "  Components:\n"
                    "    - AI ethics board or review committee\n"
                    "    - Model risk management (inventory, classification, auditing)\n"
                    "    - Compliance with regulations (EU AI Act, NIST AI RMF, SOC 2)\n"
                    "    - Incident response procedures for AI failures\n"
                    "    - Regular model audits and bias assessments\n\n"
                    "  Maturity levels:\n"
                    "    1. Ad hoc: no formal governance\n"
                    "    2. Defined: policies exist but inconsistently applied\n"
                    "    3. Managed: centralized oversight and enforcement\n"
                    "    4. Optimized: continuous improvement, automated compliance\n\n"
                    "  Key: governance is not just technical — it's organizational."
                ),
                "options": [
                    "More experiment tracking tools",
                    "AI governance — centralized oversight, risk management, and auditing",
                    "Better model architecture to prevent bias",
                    "Automated testing in CI/CD pipelines",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "No central oversight for risk, compliance, or auditing.",
                    "Organizational framework for responsible AI = AI governance.",
                ],
            },
            {
                "id": "ra_6",
                "type": "quiz",
                "title": "Fairness-Accuracy Tradeoff",
                "question": (
                    "After applying fairness constraints, your model's overall accuracy\n"
                    "drops from 92% to 89%, but approval rates are now equal across\n"
                    "demographic groups.\n\n"
                    "What does this illustrate?"
                ),
                "lesson": (
                    "The fairness-accuracy tradeoff:\n\n"
                    "  Enforcing fairness constraints often reduces overall accuracy.\n"
                    "  This happens because the model can no longer exploit patterns\n"
                    "  correlated with protected attributes.\n\n"
                    "  Key insight: a 'fair' model is not necessarily less useful.\n"
                    "    - The accuracy drop may be small (often 1-3%)\n"
                    "    - The unfair model's 'accuracy' came partly from discrimination\n"
                    "    - Regulatory and reputational costs of bias can far exceed\n"
                    "      the cost of slightly lower accuracy\n\n"
                    "  Approaches to mitigate:\n"
                    "    - Pre-processing: rebalance or re-weight training data\n"
                    "    - In-processing: add fairness constraints to the loss function\n"
                    "    - Post-processing: adjust decision thresholds per group"
                ),
                "options": [
                    "Overfitting — the model memorized the constraints",
                    "Data leakage — fairness constraints leaked test data",
                    "The fairness-accuracy tradeoff — fairness may reduce overall accuracy",
                    "Model degradation — the model needs retraining",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "Accuracy dropped slightly when fairness was enforced.",
                    "Enforcing fairness at some cost to accuracy = fairness-accuracy tradeoff.",
                ],
            },
        ],
    },
}
