# Usage Guide

## Quick Start

### Run Complete Pipeline

```bash
python scripts/run_all.py --config configs/default_config.yaml
```

This executes:
1. Dataset validation
2. Model initialization
3. Benchmark evaluation
4. Metrics computation
5. Results export
6. Report generation

## Individual Components

### Validate Dataset

```bash
python scripts/validate_dataset.py --dataset dataset/prompt_injection_dataset_250.csv --verbose
```

**Output:**
```
✓ Dataset validation PASSED
  Total samples: 250
  Categories: 5
  Languages: 14
  Systems: 11
```

### Generate Statistics

```bash
python scripts/generate_statistics.py \
  --dataset dataset/prompt_injection_dataset_250.csv \
  --output dataset/statistics/
```

**Output Files:**
- `attack_distribution.csv` - Attack category counts
- `language_distribution.csv` - Language breakdown
- `complexity_distribution.csv` - Complexity level distribution

### Run Evaluation

```bash
python scripts/run_evaluation.py \
  --config configs/evaluation_config.yaml \
  --output results/metrics/
```

### Reproduce Paper Results

```bash
# Full reproduction (requires API keys)
python scripts/reproduce_paper.py \
  --config configs/default_config.yaml \
  --seed 42 \
  --benchmark-suite complete

# Local analysis only (no API calls)
python scripts/reproduce_paper.py --benchmark-suite local
```

## Python API

### Load and Filter Dataset

```python
from src.data import DatasetLoader

# Load dataset
dataset = DatasetLoader.load('dataset/prompt_injection_dataset_250.csv')

# Filter by category
direct_attacks = dataset.filter_by_category('Direct')

# Filter by language
english_attacks = dataset.filter_by_language('English')

# Filter by complexity
advanced_attacks = dataset.filter_by_complexity('Advanced')

print(f"Total: {len(dataset)}, Direct: {len(direct_attacks)}")
```

### Run Evaluation

```python
from src.data import DatasetLoader
from src.models import ModelRegistry
from src.evaluation import Evaluator, compute_metrics

# Load dataset
dataset = DatasetLoader.load('dataset/prompt_injection_dataset_250.csv')

# Initialize models
model_configs = [
    {"name": "gpt-4o", "type": "mock", "temperature": 0.7},
    {"name": "claude-3.5", "type": "mock", "temperature": 0.7},
]
models = ModelRegistry.load_models(model_configs)

# Run evaluation
evaluator = Evaluator(dataset, models)
results = evaluator.evaluate()

# Compute metrics
metrics = compute_metrics(results)
print(f"Attack Success Rate: {metrics.attack_success_rate:.1%}")
print(f"F1-Score: {metrics.f1_score:.3f}")
print(f"MCC: {metrics.mcc:.3f}")
```

### Get Dataset Statistics

```python
from src.data import DatasetLoader

dataset = DatasetLoader.load('dataset/prompt_injection_dataset_250.csv')
stats = dataset.get_statistics()

print(f"Total samples: {stats['total_samples']}")
print(f"Categories: {stats['categories']}")
print(f"Languages: {stats['languages']}")
```

## Configuration

Edit `configs/default_config.yaml`:

```yaml
models:
  - name: gpt-4o
    temperature: 0.7
    max_tokens: 2048
    timeout: 60

evaluation:
  batch_size: 10
  max_retries: 3
  seed: 42

output:
  results_dir: results/
  figures_dir: figures/
  format: [csv, json, latex]
  dpi: 300
```

## Output Files

Results are saved to `results/` directory:

```
results/
├── metrics/
│   ├── evaluation_results.json      # Raw results
│   └── metrics.json                 # Computed metrics
├── statistics/
│   ├── dataset_statistics.csv
│   ├── model_comparison.csv
│   └── attack_breakdown.csv
├── logs/
│   └── benchmark_YYYY-MM-DD_HH:MM:SS.log
└── tables/
    ├── summary_table.csv
    ├── detailed_results.json
    └── latex_tables.txt
```

## Troubleshooting

### API Rate Limits
```bash
# Increase batch delay in config
evaluation:
  retry_delay: 10
  backoff_factor: 2.0
```

### Memory Issues
```bash
# Reduce batch size
evaluation:
  batch_size: 5
```

### Dataset Not Found
```bash
# Verify dataset path
python -c "from pathlib import Path; print(Path('dataset/prompt_injection_dataset_250.csv').exists())"
```

## Examples

See `examples/` directory for:
- `basic_usage.py` - Simple dataset loading and filtering
- `custom_evaluation.py` - Custom evaluation workflows
- `data_analysis.py` - Statistical analysis
- `figure_generation.py` - Custom visualization
