# Prompt Injection Benchmark: A Multilingual Dataset for LLM Security

A comprehensive benchmark dataset for evaluating large language model robustness against prompt injection attacks across 14 languages and 5 attack categories.

## Overview

Prompt injection attacks represent one of the most pressing security challenges in deployed language models. While researchers have documented various attack vectors, most studies focus on English-language scenarios or single attack types. This benchmark addresses that gap by providing a structured evaluation framework that tests models across linguistic and methodological boundaries.

This dataset contains 250 carefully curated samples spanning 14 languages and five distinct attack categories. By evaluating both commercial and open-weight models, we establish baseline performance metrics and reveal critical differences in robustness across model architectures and deployment contexts. The findings have immediate implications for practitioners deploying LLMs in multilingual environments and for researchers developing more secure systems.

## Dataset Structure

The benchmark comprises 250 samples distributed across multiple dimensions:

**Languages**: The dataset covers 14 languages representing different linguistic families and writing systems: English, Mandarin Chinese, Spanish, French, Arabic, German, Japanese, Hindi, Portuguese, Russian, Korean, Italian, Dutch, and Turkish.

**Attack Categories**: Five distinct attack vectors are represented. Direct injection attacks embed malicious instructions directly into user prompts. Indirect injection attacks manipulate external data sources that the model processes. Multi-turn escalation attacks gradually escalate requests across multiple conversation turns to bypass safety measures. Jailbreaking attacks use social engineering or roleplay scenarios to circumvent safeguards. Cross-lingual transfer attacks exploit multilingual models by embedding instructions in languages different from the model's training focus.

**Models Evaluated**: The benchmark evaluates five models representing different architectures and deployment models: GPT-4o (commercial), Claude 3.5 Sonnet (commercial), Gemini 1.5 Pro (commercial), Llama 3 (open-weight), and Mistral 7B (open-weight).

## Key Findings

Our analysis reveals substantial performance gaps between commercial and open-weight models. Under indirect injection attacks, open-weight models failed at nearly double the rate of commercial models. Multi-turn escalation attacks showed similar disparities, with open-weight models demonstrating significantly weaker resistance to gradually escalated requests. Notably, commercial models showed more consistent performance across languages, while open-weight models exhibited greater variance in robustness across different linguistic contexts. These findings suggest that security considerations should be a primary factor when selecting models for production deployment, particularly in security-sensitive applications.

## Dataset Details

The dataset is structured as a JSON-formatted collection where each sample includes the original prompt, attack category, target language, model responses, and success indicators. Full documentation of the data format is available in the `data/` directory alongside the complete dataset.

Accessing the benchmark: The complete dataset is available on Zenodo (see citation below) and includes all 250 samples, model evaluation results, and detailed analysis notebooks for reproducing our findings.

## How to Cite

If you use this dataset in your research, please cite it as:

```
Anwar, M. S. (2026). Prompt Injection Benchmark: A Multilingual Dataset for LLM Security [Data set]. Zenodo. https://doi.org/10.5281/zenodo.19364462
```

BibTeX format:
```bibtex
@dataset{anwar2026prompt,
  title={Prompt Injection Benchmark: A Multilingual Dataset for LLM Security},
  author={Anwar, Muhammad Saeed},
  year={2026},
  publisher={Zenodo},
  doi={10.5281/zenodo.19364462},
  url={https://doi.org/10.5281/zenodo.19364462}
}
```

## About the Author

I'm Muhammad Saeed Anwar, a cybersecurity researcher and AI systems specialist. I hold a BSCS from CUST Islamabad and currently work as a Lab Instructor. My security credentials include Google Cybersecurity Certification, ISC2 Certified in Cybersecurity (CC), and IBM AI/Machine Learning Professional Certification. My research focuses on LLM security, adversarial robustness, and safe AI systems.

Connect with me: [GitHub](https://github.com/MuhammadSaeedAnwar) | [LinkedIn](https://linkedin.com/in/muhammadsaeedanwar)

## License

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This dataset and accompanying code are released under the MIT License. See the LICENSE file for details.
