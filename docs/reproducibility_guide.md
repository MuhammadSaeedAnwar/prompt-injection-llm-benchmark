# Reproducibility Guide

## Overview

This benchmark is designed for complete reproducibility. All results can be reproduced using provided scripts and configuration files.

## Prerequisites

```bash
# Python 3.9+
python --version

# Git
git clone https://github.com/MuhammadSaeedAnwar/Prompt-Injection-LLM-Benchmark.git
cd Prompt-Injection-LLM-Benchmark

# Dependencies
pip install -r requirements.txt
```

## Step-by-Step Reproduction

### 1. Validate Dataset

```bash
python scripts/validate_dataset.py \
  --dataset dataset/prompt_injection_dataset_250.csv \
  --verbose
```

**Expected Output**:
```
✓ Dataset validation PASSED
  Total samples: 250
  Categories: 5
  Languages: 14
  Systems: 11
```

### 2. Generate Statistics

```bash
python scripts/generate_statistics.py \
  --dataset dataset/prompt_injection_dataset_250.csv \
  --output dataset/statistics/
```

**Output Files**:
- `dataset/statistics/attack_distribution.csv`
- `dataset/statistics/language_distribution.csv`
- `dataset/statistics/complexity_distribution.csv`

### 3. Run Evaluation

```bash
python scripts/run_all.py \
  --config configs/default_config.yaml \
  --dataset dataset/prompt_injection_dataset_250.csv \
  --output results/ \
  --seed 42
```

### 4. Expected Results

**For Mock Models** (no API calls required):
```
✓ Dataset validation: PASSED
✓ Models initialized: 2
✓ Evaluations completed: 500
✓ Metrics computed:
  - Attack Success Rate: ~50% (mock data)
  - F1-Score: 0.XXX
  - MCC: 0.XXX
✓ Results saved to: results/
```

## Reproducibility Factors

### Random Seed

All randomization controlled by seed:
```python
import random
import numpy as np

random.seed(42)
np.random.seed(42)
```

Set in configuration:
```yaml
evaluation:
  seed: 42
```

### Configuration Management

All parameters in YAML configs:
```bash
configs/
├── default_config.yaml          # Main config
├── models_config.yaml           # Model settings
└── evaluation_config.yaml       # Evaluation settings
```

### Deterministic Operations

- Dataset loading: Deterministic (CSV ordering)
- Evaluation loop: Sequential (no parallel execution)
- Metric computation: Deterministic mathematical operations
- Statistical tests: Reproducible with seed

## Verifying Reproducibility

### Run Same Experiment Twice

```bash
# Run 1
python scripts/run_all.py --seed 42 --output results_run1/

# Run 2
python scripts/run_all.py --seed 42 --output results_run2/

# Compare results
diff results_run1/metrics/metrics.json results_run2/metrics/metrics.json
# Should be identical
```

### Compare With Paper Results

Paper results available in `paper/results/`:

```bash
# Your results
cat results/metrics/metrics.json

# Paper results
cat paper/results/paper_metrics.json

# Should match within floating-point precision
```

## Troubleshooting Reproducibility

### Different Results

1. **Check seed**: Ensure seed=42 in all configs
2. **Check dependencies**: Install exact versions from `requirements.txt`
3. **Check Python version**: Use Python 3.9-3.12
4. **Check dataset**: Verify dataset file is unchanged

### Partial Reproduction

For local analysis only (no API calls):

```bash
python scripts/reproduce_paper.py \
  --benchmark-suite local \
  --seed 42
```

This runs:
- Dataset loading
- Dataset statistics
- Schema validation
- No API calls needed

## Full Reproduction (With APIs)

For complete results with real model evaluations:

```bash
# Setup API keys
cp .env.example .env
# Edit .env with your API keys

# Run complete pipeline
python scripts/reproduce_paper.py \
  --benchmark-suite complete \
  --config configs/default_config.yaml \
  --seed 42
```

**Requirements**:
- OpenAI API key
- Anthropic API key
- Google API key
- Sufficient API credits
- ~2-4 hours execution time

## Paper Reproduction Checklist

- [ ] Python 3.9+ installed
- [ ] Requirements installed: `pip install -r requirements.txt`
- [ ] Dataset present: `dataset/prompt_injection_dataset_250.csv`
- [ ] Configs present: `configs/*.yaml`
- [ ] Run validation: `python scripts/validate_dataset.py`
- [ ] Run statistics: `python scripts/generate_statistics.py`
- [ ] Run evaluation: `python scripts/run_all.py --seed 42`
- [ ] Results generated: `results/metrics/`
- [ ] Compare with paper: `paper/results/`
- [ ] Documentation reviewed: `docs/reproducibility_guide.md`

## Artifact Evaluation

This repository meets **ACM Artifact Evaluation** criteria:

- ✓ **Available**: Code and data publicly available on GitHub
- ✓ **Functional**: Complete pipeline executable
- ✓ **Reproducible**: Results reproducible with provided scripts
- ✓ **Documented**: Comprehensive documentation included

## Support

For reproducibility issues:
- Check logs: `results/logs/`
- Open issue on GitHub with:
  - Python version
  - OS (Windows/Mac/Linux)
  - Error message
  - Steps to reproduce
