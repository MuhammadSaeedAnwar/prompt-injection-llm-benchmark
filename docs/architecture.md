# Architecture

## System Design

```
┌─────────────────────────────────────────────────────────────┐
│         Prompt Injection LLM Benchmark System              │
└─────────────────────────────────────────────────────────────┘

         User Input / Configuration
              │
              ▼
    ┌──────────────────────┐
    │  Config Loader       │  (configs/*.yaml)
    │  (YAML parsing)      │
    └──────────┬───────────┘
               │
      ┌────────┴────────┐
      │                 │
      ▼                 ▼
  ┌────────────┐   ┌──────────────┐
  │  Dataset   │   │  Model       │
  │  Loader    │   │  Registry    │
  └──────┬─────┘   └──────┬───────┘
         │                 │
         ▼                 ▼
  ┌────────────────────────────┐
  │  Data Validator            │
  │  - Schema check            │
  │  - Duplicate detection     │
  │  - Format validation       │
  └──────┬─────────────────────┘
         │
         ▼
  ┌────────────────────────────┐
  │  Evaluator                 │
  │  - Model invocation        │
  │  - Response capture        │
  │  - Success assessment      │
  └──────┬─────────────────────┘
         │
         ▼
  ┌────────────────────────────┐
  │  Metrics Computation       │
  │  - ASR calculation         │
  │  - Confidence intervals    │
  │  - Statistical tests       │
  └──────┬─────────────────────┘
         │
         ▼
  ┌────────────────────────────┐
  │  Results Export            │
  │  - CSV/JSON/LaTeX tables   │
  │  - Figures (PNG/PDF/SVG)   │
  │  - Reports                 │
  └──────┬─────────────────────┘
         │
         ▼
    Output / Results
```

## Module Structure

### `src/data/`
- **dataset.py**: Core Dataset and Sample classes
- **loader.py**: CSV/JSON dataset loading
- **validator.py**: Schema validation and duplicate detection
- **preprocessor.py**: Data cleaning and normalization

### `src/models/`
- **base.py**: Abstract BaseModel class
- **registry.py**: ModelRegistry for model management
- **openai_model.py**: OpenAI API integration
- **anthropic_model.py**: Anthropic API integration
- **google_model.py**: Google API integration

### `src/evaluation/`
- **evaluator.py**: Core evaluation logic
- **metrics.py**: Metrics computation (ASR, F1, MCC, etc.)
- **analyzer.py**: Statistical analysis
- **statistics.py**: Descriptive statistics

### `src/visualization/`
- **plots.py**: Figure generation (matplotlib/seaborn)
- **tables.py**: Table generation (CSV/JSON/LaTeX)
- **report_generator.py**: Automated report generation

### `src/config/`
- **loader.py**: YAML configuration loading
- **validator.py**: Configuration validation

### `src/utils/`
- **logger.py**: Logging configuration
- **helpers.py**: Utility functions
- **constants.py**: Global constants

## Data Flow

```
1. Load Configuration
   ↓
2. Load Dataset (CSV/JSON)
   ↓
3. Validate Schema
   ↓
4. Initialize Models (ModelRegistry)
   ↓
5. For each model:
   - For each sample:
     a. Generate prompt
     b. Call model.generate()
     c. Capture response
     d. Assess success
     e. Store result
   ↓
6. Compute Metrics
   - ASR, F1, MCC, CI
   - Group by category/language/complexity
   ↓
7. Statistical Analysis
   - T-tests, ANOVA
   - Bootstrap confidence intervals
   ↓
8. Generate Visualizations
   - Figures (PNG/PDF/SVG)
   - Tables (CSV/JSON/LaTeX)
   ↓
9. Export Results
   - results/metrics/
   - results/tables/
   - figures/
```

## Class Hierarchy

```
BaseModel (abstract)
├── MockModel (testing)
├── OpenAIModel (ChatGPT, GPT-4)
├── AnthropicModel (Claude)
└── GoogleModel (Gemini)

Dataset
└── Sample (individual attack)

EvaluationResult
├── attack_id
├── model_name
├── prompt
├── response
└── success

Metrics
├── attack_success_rate
├── confidence_interval_95
├── f1_score
├── precision
├── recall
├── accuracy
└── mcc
```

## Configuration Hierarchy

```
configs/
├── default_config.yaml (master config)
│   └── imports defaults for all settings
├── models_config.yaml (model-specific)
│   └── temperature, max_tokens, timeouts
├── evaluation_config.yaml (evaluation)
│   └── batch_size, retry_policy, seed
└── paths_config.yaml (file paths)
    └── dataset, output, logs
```

## Pipeline Execution

### Sequential Pipeline (run_all.py)

```
1. Validate Dataset        (scripts/validate_dataset.py)
2. Initialize Models       (ModelRegistry.load_models())
3. Run Evaluation          (Evaluator.evaluate())
4. Compute Metrics         (compute_metrics())
5. Generate Statistics     (StatisticalAnalyzer)
6. Export Results          (save_json/save_csv)
7. Generate Figures        (scripts/generate_figures.py)
8. Generate Tables         (scripts/generate_tables.py)
```

### Parallel Considerations

- Currently sequential (API-safe, deterministic)
- Can be parallelized by model (add threading)
- Cannot parallelize by sample (maintains order)

## Error Handling

```
Exception Hierarchy:
├── ConfigError
│   └── Config file not found
├── DataError
│   ├── Dataset format invalid
│   ├── Schema validation failed
│   └── Duplicate detected
├── ModelError
│   ├── Model initialization failed
│   ├── API error
│   └── Timeout
└── EvaluationError
    ├── Metric computation failed
    └── Results export failed
```

## Logging

```
Loggers:
├── src.data.loader          (Dataset operations)
├── src.data.validator       (Validation)
├── src.models.registry      (Model management)
├── src.evaluation.evaluator (Evaluation)
└── src.evaluation.metrics   (Metrics)

Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
Output: Console + File (results/logs/)
```
