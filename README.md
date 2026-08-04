# Prompt Injection Attacks in Large Language Models: Comprehensive Threat Analysis, Empirical Dataset Construction, and Critical Mitigation Gaps

[![GitHub](https://img.shields.io/badge/GitHub-Repository-informational?logo=github)](https://github.com/MuhammadSaeedAnwar/Prompt-Injection-LLM-Benchmark)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/MuhammadSaeedAnwar/Prompt-Injection-LLM-Benchmark/blob/main/LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Dataset: 250 Samples](https://img.shields.io/badge/Dataset-250%20Samples-green.svg)](./prompt_injection_dataset_250.csv)
[![Languages: 14](https://img.shields.io/badge/Languages-14-blue.svg)](#dataset-description)
[![Models: 5](https://img.shields.io/badge/Models-5-blue.svg)](#models-evaluated)
[![Published: AISec 2026](https://img.shields.io/badge/Published-AISec%202026-brightgreen.svg)](#citation)
[![Zenodo](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.19364462-blue.svg)](https://doi.org/10.5281/zenodo.19364462)

**Accepted at AISec 2026 (International Workshop on Security for AI Systems and AI for Systems Security).**

---

## Overview

This repository contains the dataset, evaluation code, and paper for a systematic empirical study of prompt injection attacks against large language models. It accompanies the paper of the same title, accepted at AISec 2026.

**What this repository actually contains:**
- A hand-annotated benchmark of **250 prompt injection attack samples** across **5 attack categories**, **14 languages**, and **3 complexity levels**
- Empirical Attack Success Rate (ASR) measurements for **5 production-grade LLMs**, evaluated January–April 2024
- A five-category attack taxonomy grounded in real-world incidents and academic literature
- Six identified open research gaps in LLM security evaluation and defense

This README describes exactly what is in the paper — no more, no less. Numbers below match Tables I–IV of the accepted manuscript.

---

## Research Motivation

Prompt injection exploits the natural-language interface of LLMs rather than a conventional software vulnerability: there is no parser boundary between "trusted system instruction" and "untrusted input," only a convention enforced by training. Existing literature at the time of writing largely evaluated single attack types or single model families in isolation, with indirect injection — arguably the most operationally dangerous variant — underrepresented in empirical work despite extensive real-world documentation. This work addresses that gap with a cross-model, cross-category empirical benchmark.

---

## Attack Taxonomy

Five categories, matching Table I of the paper exactly:

| Attack Category | N | % |
|---|---|---|
| Direct Injection | 60 | 24.0 |
| Indirect Injection | 55 | 22.0 |
| Jailbreak | 70 | 28.0 |
| Multi-Turn | 40 | 16.0 |
| Encoding/Obfuscation | 25 | 10.0 |
| **Total** | **250** | **100.0** |

1. **Direct Prompt Injection** — explicit override instructions in the user turn (instruction negation, priority escalation, delimiter injection).
2. **Indirect Prompt Injection** — malicious instructions embedded in external content (retrieved documents, emails, web pages) that the model treats as authoritative once ingested.
3. **Jailbreak Through Roleplay** — fictional framing or hypothetical scenarios used to route around safety training (DAN-family, low-resource-language translation bypass).
4. **Multi-Turn Constraint Degradation** — gradual erosion of refusal behavior across an extended conversation.
5. **Encoding and Obfuscation** — Base64, Unicode homoglyphs, Markdown/HTML injection, ASCII art used to evade keyword/pattern filters.

---

## Dataset Description

| Field | Description |
|---|---|
| `attack_id` | Unique identifier |
| `primary_category` | One of the five categories above |
| `subcategory` | Category-specific subtype |
| `prompt_text` | Full attack prompt |
| `target_behavior` | The specific model behavior that would count as a successful attack |
| `complexity` | Simple / Intermediate / Advanced |
| `language` | One of 14 languages |

Sources: public adversarial prompt repositories (JailbreakChat, AwesomeChatGPT-Prompts, r/ChatGPTJailbreak), prompts described in published security papers, manually crafted prompts targeting recurring weaknesses, and template-generated samples (~15–20% of the dataset) to fill coverage gaps.

A 25-prompt public sample is available without registration at `data/public_sample_25.csv`. Full dataset and DOI: [10.5281/zenodo.19364462](https://doi.org/10.5281/zenodo.19364462).

---

## Models Evaluated

Exactly as evaluated in the paper (Table II) — no others:

| Model | Access | Version |
|---|---|---|
| GPT-4 | API | `gpt-4-0125-preview`, OpenAI, Jan–Feb 2024 |
| Claude 3 Opus | API | `claude-3-opus-20240229`, Anthropic, Feb–Mar 2024 |
| Llama 2 70B | Local | `Llama-2-70b-chat-hf`, 4-bit GPTQ, A100 80GB |
| Mistral 8×7B | Local | `Mixtral-8x7B-Instruct-v0.1`, BF16, 2×A100 |
| Gemini 1.5 Pro | API | `gemini-1.5-pro-0409`, Google AI Studio, Apr 2024 |

Local models were served via HuggingFace TGI v1.4.0. All models received an identical system prompt (reproduced in the paper's Appendix).

**Note on temporal validity:** these results reflect model behavior during the January–April 2024 evaluation window. Commercial providers update continuously; ASR values should not be read as current-state assessments of these or later model versions.

---

## Results

ASR (%) by model and attack category (Table III):

| Category | GPT-4 | Claude 3 Opus | Llama 2 | Mistral | Gemini 1.5 Pro |
|---|---|---|---|---|---|
| Direct | 7 | 11 | 43 | 49 | 14 |
| Indirect | 39 | 35 | 76 | 79 | 44 |
| Jailbreak | 14 | 17 | 58 | 65 | 21 |
| Multi-Turn | 26 | 29 | 69 | 73 | 33 |
| Encoding | 9 | 8 | 46 | 52 | 12 |
| **Average** | **19** | **20** | **58** | **64** | **25** |

Key findings:
- Commercial models (GPT-4, Claude 3 Opus) average 19–20% ASR; open-weight models (Llama 2, Mistral) average 58–64%. Gemini 1.5 Pro sits between the two groups at 25%.
- **Indirect injection is the worst category for every model tested**, including the hardened commercial ones. GPT-4's ASR rises from 7% (direct) to 39% (indirect) — a 5.6× increase. Simulated email-assistant deployments averaged a 63% bypass rate across all five models.
- **Multi-turn ASR rises monotonically** from 11% at turn 1 to 61% at turn 10 (5.5× increase), showing that single-turn safety evaluation misses a large share of real vulnerability.

---

## Methodology

- **Metric:** Attack Success Rate = successful attacks / total attempts × 100%.
- **Protocol:** Temperature = 0.7, 512-token output cap, 3 trials per prompt (seeds 42/43/44), tied votes default to Safe.
- **Annotation:** Two independent annotators, blinded to model identity and category, three-point scale (Safe / Borderline / Harmful). Disagreements resolved by a third adjudicator. Inter-rater agreement (Cohen's κ) ranged from 0.55 (multi-turn) to 0.74 (direct injection) — see Table IV.

**Stated limitation (paper, Section VIII):** three trials per prompt is insufficient for statistically reliable confidence intervals. ASR values in this release should be read as a relative vulnerability ordering across models and categories, not as precise probability estimates. This is disclosed directly in the paper rather than corrected after the fact with post-hoc statistics not run on this data.

---

## Critical Research Gaps Identified

1. No formal model of LLM instruction semantics distinguishing trusted from untrusted sources.
2. No shared, stable LLM security benchmark comparable to ImageNet/GLUE for other subfields.
3. No dedicated security architecture for agentic LLM deployments, where a successful injection is an irreversible action rather than a bad text output.
4. No trust model for retrieval pipelines — RAG systems have no mechanism to distinguish adversarial from legitimate retrieved content.
5. Safety training data is dominated by single-turn examples, leaving multi-turn robustness largely unaddressed.
6. No certified, worst-case robustness guarantees for LLM security, unlike certified defenses in computer vision.

---

## Repository Structure

```
Prompt-Injection-LLM-Benchmark/
├── README.md
├── LICENSE
├── CITATION.cff
├── prompt_injection_dataset_250.csv
├── paper/
│   └── AISEC_2026_paper_33.pdf
├── data/
│   └── public_sample_25.csv
├── docs/
│   └── SCHEMA.md
├── scripts/
│   └── (evaluation and annotation scripts as used for the paper)
└── requirements.txt
```

---

## Installation

```bash
git clone https://github.com/MuhammadSaeedAnwar/Prompt-Injection-LLM-Benchmark.git
cd Prompt-Injection-LLM-Benchmark
pip install -r requirements.txt
```

---

## Citation

```bibtex
@inproceedings{anwar2026promptinjection,
  title     = {Prompt Injection Attacks in Large Language Models: Comprehensive Threat Analysis, Empirical Dataset Construction, and Critical Mitigation Gaps},
  author    = {Anwar, Muhammad Saeed},
  booktitle = {Proceedings of the AISec 2026 Workshop on Security for AI Systems and AI for Systems Security},
  year      = {2026}
}
```

Dataset DOI:

```
Anwar, M. S. (2026). Prompt injection attacks in large language models: benchmark dataset [Data set].
Zenodo. https://doi.org/10.5281/zenodo.19364462
```

---

## Limitations (from the paper)

- Three trials per prompt limits statistical confidence; results are relative orderings, not precise probability estimates.
- Annotation involves genuine judgment calls; multi-turn category has the lowest inter-rater agreement (κ = 0.55).
- Results reflect a January–April 2024 snapshot of five specific model versions and do not generalize to current model behavior.
- ~15–20% of samples are template-generated and may under-represent creative, context-sensitive attacks a skilled adversary would construct.
- Multimodal injection (adversarial images) and cross-agent injection in multi-LLM orchestration are out of scope.

---

## License

MIT License — see [LICENSE](./LICENSE).

## Contact

**Muhammad Saeed Anwar**
Department of Computer Science, Capital University of Science and Technology, Islamabad, Pakistan
Email: malik.saed555@gmail.com
GitHub: [@MuhammadSaeedAnwar](https://github.com/MuhammadSaeedAnwar)
