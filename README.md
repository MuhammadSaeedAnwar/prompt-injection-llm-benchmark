# Prompt Injection LLM Benchmark

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Dataset](https://img.shields.io/badge/Dataset-Research%20Grade-blue.svg)](#dataset-overview)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](#)

## Overview

This repository contains a comprehensive benchmark dataset for evaluating prompt injection vulnerabilities in Large Language Models (LLMs). The dataset provides a structured collection of prompt injection attacks across multiple attack vectors, targeting diverse LLM architectures including GPT-3.5, GPT-4, Claude-2, and Llama-2-70b.

## Research Objective

This project aims to:
- **Systematize prompt injection threats** in contemporary LLM systems
- **Evaluate defense mechanisms** across different model architectures
- **Establish reproducible benchmarks** for LLM safety and robustness assessment
- **Advance the field** of AI cybersecurity through rigorous empirical analysis

## Features

- **Multi-Model Evaluation**: Assessments across 4 leading LLM architectures
- **Diverse Attack Vectors**: Direct injection, indirect injection, jailbreaks, and prompt leaking techniques
- **Standardized Metrics**: Severity classification (low, medium, high, critical) and defense categorization
- **Reproducible Framework**: Clearly documented methodology enabling independent verification
- **Research-Ready Format**: Academic-quality dataset suitable for machine learning research and threat modeling

## Dataset Overview

### Public Sample
A curated public sample of 25 representative attack instances is included in this repository:

- **Location**: [`data/public_sample_25.csv`](data/public_sample_25.csv)
- **Records**: 25 anonymized prompt injection attempts
- **Columns**: 8 structured attributes (attack type, prompt, model, outcome, severity, mitigation)
- **Format**: CSV with UTF-8 encoding

### Full Benchmark Dataset
The complete benchmark dataset is hosted on Zenodo:

- **DOI**: [10.5281/zenodo.XXXXXXX](https://zenodo.org)
- **Records**: 1,200+ comprehensive attack evaluations
- **Coverage**: All attack vectors, mitigation strategies, and model variants
- **Access**: Open access for research and reproducibility

### Schema Documentation
For detailed information about dataset columns, data types, and classifications, refer to [`data/schema.md`](data/schema.md).

## Dataset Composition

| Aspect | Details |
|--------|---------|
| **Attack Types** | Direct Injection, Indirect Injection, Jailbreak, Prompt Leaking |
| **Models Evaluated** | GPT-3.5-turbo, GPT-4, Claude-2, Llama-2-70b |
| **Severity Levels** | Low, Medium, High, Critical |
| **Mitigation Strategies** | Input Filtering, Instruction Hierarchy, Prompt Caching |
| **Sample Records** | 25 (public) / 1,200+ (full dataset) |

## Reproducibility

All experiments follow standardized protocols enabling independent reproduction. To work with the public sample dataset:

```python
import pandas as pd

# Load the public sample
df = pd.read_csv('data/public_sample_25.csv')

# Display dataset structure
print(df.head())
print(df.info())
print(df.describe())

# Analyze attack distribution
print(df['attack_type'].value_counts())
print(df['severity_level'].value_counts())
print(df['attack_success'].value_counts())
```

## Citation

If you use this benchmark in your research, please cite it as follows:

```bibtex
@dataset{anwar2026promptinjection,
  title={Prompt Injection LLM Benchmark: Evaluating Safety and Robustness of Large Language Models},
  author={Anwar, Muhammad Saeed},
  year={2026},
  howpublished={Zenodo},
  doi={10.5281/zenodo.XXXXXXX},
  url={https://zenodo.org/record/XXXXXXX}
}
```

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License. You are free to:
- Share, copy, and redistribute the dataset
- Adapt and build upon the dataset for any purpose

**Attribution Required**: Please cite this work appropriately in your publications and research outputs.

See [LICENSE](LICENSE) for full terms.

## Contact & Support

For questions, suggestions, or technical issues:
- **GitHub Issues**: [Open an issue](https://github.com/MuhammadSaeedAnwar/prompt-injection-llm-benchmark/issues)
- **Email**: For direct inquiries, use GitHub Issues for faster response

## Acknowledgments

This research contributes to the broader effort in AI safety and cybersecurity, advancing our understanding of LLM vulnerabilities and defense mechanisms.

---

**Version**: 1.0  
**Last Updated**: May 13, 2026  
**Status**: Active & Maintained
