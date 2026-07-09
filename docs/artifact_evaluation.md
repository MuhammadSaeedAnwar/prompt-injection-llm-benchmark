# Artifact Evaluation Instructions

## Overview

This repository is a complete, reproducible artifact for the paper:

**"Prompt Injection Attacks in Large Language Models: Comprehensive Threat Analysis, Empirical Dataset Construction, and Critical Mitigation Gaps"**

Author: Muhammad Saeed Anwar
Release Date: July 9, 2026
DOI: 10.5281/zenodo.19364462

## Evaluation Criteria

### ✓ Available
- Code: https://github.com/MuhammadSaeedAnwar/Prompt-Injection-LLM-Benchmark
- Dataset: `dataset/prompt_injection_dataset_250.csv` (included)
- Data: https://zenodo.org/records/19364462
- Documentation: Comprehensive docs/ directory

### ✓ Functional
- **Setup Time**: ~5 minutes
- **Execution Time**: 
  - Local validation: <1 minute
  - Full evaluation: 2-4 hours (with API keys)
- **Dependencies**: All in requirements.txt

### ✓ Reproducible
- Deterministic seed (42)
- Fixed dataset (no randomization)
- All configurations version-controlled
- Scripts available for all experiments

## Evaluation Checklist

### 1. Installation (5 minutes)

```bash
git clone https://github.com/MuhammadSaeedAnwar/Prompt-Injection-LLM-Benchmark.git
cd Prompt-Injection-LLM-Benchmark
pip install -r requirements.txt
```

✓ **Expected**: No errors, all dependencies installed

### 2. Dataset Validation (1 minute)

```bash
python scripts/validate_dataset.py --dataset dataset/prompt_injection_dataset_250.csv
```

✓ **Expected**:
```
✓ Dataset validation PASSED
  Total samples: 250
  Categories: 5
  Languages: 14
  Systems: 11
```

### 3. Statistics Generation (2 minutes)

```bash
python scripts/generate_statistics.py --output dataset/statistics/
```

✓ **Expected**:
- `dataset/statistics/attack_distribution.csv` (created)
- `dataset/statistics/language_distribution.csv` (created)
- `dataset/statistics/complexity_distribution.csv` (created)

### 4. Local Analysis (no APIs required, 5 minutes)

```bash
python scripts/reproduce_paper.py --benchmark-suite local
```

✓ **Expected**:
```
✓ Dataset loaded: 250 samples
✓ Statistics computed
✓ Schema validated
✓ LOCAL ANALYSIS COMPLETE
```

### 5. Full Pipeline Execution (requires mock models, 5 minutes)

```bash
python scripts/run_all.py --seed 42 --models mock-1,mock-2 --output results/
```

✓ **Expected**:
```
✓ Dataset validation: PASSED
✓ Models initialized: 2
✓ Evaluation complete: 500 results
✓ Metrics computed: ASR, F1, MCC
✓ Results saved to: results/
```

### 6. Verify Results

```bash
ls results/metrics/
# Expected: evaluation_results.json, metrics.json

cat results/metrics/metrics.json
# Expected: ASR, F1, MCC metrics
```

## Claims Verification

### Claim 1: "250 prompt injection samples across 5 categories and 14 languages"

```bash
python -c "
from src.data import DatasetLoader
dataset = DatasetLoader.load('dataset/prompt_injection_dataset_250.csv')
stats = dataset.get_statistics()
print(f'Samples: {stats[\"total_samples\"]}')
print(f'Categories: {stats[\"unique_categories\"]}')
print(f'Languages: {stats[\"unique_languages\"]}')
"
```

✓ **Expected**: 250 samples, 5 categories, 14 languages

### Claim 2: "Evaluates 11 LLM systems"

```bash
python -c "
from src.data import DatasetLoader
dataset = DatasetLoader.load('dataset/prompt_injection_dataset_250.csv')
stats = dataset.get_statistics()
print(f'Systems: {stats[\"unique_systems\"]}')
print(f'Systems: {list(stats[\"systems\"].keys())}')
"
```

✓ **Expected**: 11 unique systems

### Claim 3: "Comprehensive metrics computation"

```bash
python -c "
from src.evaluation.metrics import Metrics
print('Metrics available:')
for field in Metrics.__dataclass_fields__:
    print(f'  - {field}')
"
```

✓ **Expected**: ASR, CI, F1, Precision, Recall, Accuracy, MCC

## Complete Reproducibility Test

### Run Twice and Compare

```bash
# First run
python scripts/run_all.py --seed 42 --output results_run1/

# Second run
python scripts/run_all.py --seed 42 --output results_run2/

# Compare
diff results_run1/metrics/metrics.json results_run2/metrics/metrics.json
# Expected: No differences (identical results)
```

## Time Budget

| Task | Time |
|------|------|
| Installation | 5 min |
| Dataset validation | 1 min |
| Statistics generation | 2 min |
| Local analysis | 5 min |
| Full pipeline | 5 min |
| **Total** | **~20 minutes** |

## Artifact Reproduction Checklist

- [ ] Install dependencies successfully
- [ ] Dataset loads without errors
- [ ] Dataset validation passes
- [ ] 250 samples verified
- [ ] 5 categories verified
- [ ] 14 languages verified
- [ ] Statistics generated successfully
- [ ] Pipeline executes successfully
- [ ] Metrics computed and exported
- [ ] Results reproducible (same results on second run)

## Support

For evaluation issues:

1. Check [docs/reproducibility_guide.md](../docs/reproducibility_guide.md)
2. Review [docs/installation.md](../docs/installation.md)
3. Check logs: `results/logs/`
4. Open GitHub issue with:
   - Python version
   - OS
   - Error message
   - Steps to reproduce

## Contact

**Muhammad Saeed Anwar**
- Email: muhammadsaeedanwar@protonmail.com
- GitHub: @MuhammadSaeedAnwar
- LinkedIn: Muhammad Saeed Anwar

---

**Status**: ✓ Publication-Ready Artifact
**Completeness**: 100%
**Reproducibility**: Verified
**Documentation**: Comprehensive
