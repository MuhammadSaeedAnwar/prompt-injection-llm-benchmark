# Prompt Injection Attack Benchmark Dataset
**250 Empirically Constructed Attack Samples Across 5 Attack Categories and 11 Target Systems**

> Associated with the paper:  
> **"Prompt Injection Attacks in Large Language Models: Comprehensive Threat Analysis, Empirical Dataset Construction, and Critical Mitigation Gaps"**  
> Muhammad Saeed Anwar — Capital University of Science and Technology, Islamabad  
> Contact: malik.saed555@gmail.com

---

## Dataset Overview

This repository contains the full benchmark dataset used in the above paper.
The dataset comprises **250 prompt injection attack samples** targeting real production LLM systems, grounded in documented system prompt structures from publicly disclosed sources.

| Attribute | Value |
|---|---|
| Total samples | 250 |
| Attack categories | 5 |
| Subcategories | 16 |
| Target systems | 11 |
| Languages | 14 |
| Complexity levels | 3 (Simple / Intermediate / Advanced) |

---

## Category Distribution

| Category | Samples | % |
|---|---|---|
| Jailbreak | 62 | 24.8% |
| Multi-Turn | 57 | 22.8% |
| Direct Injection | 49 | 19.6% |
| Indirect Injection | 42 | 16.8% |
| Encoding / Obfuscation | 40 | 16.0% |
| **Total** | **250** | **100%** |

---

## Target Systems

Attacks are distributed across the following systems:

- Claude (claude.ai) — 67 samples
- Gemini Workspace — 33 samples
- Gemini (webapp) — 33 samples
- Notion AI — 30 samples
- Le Chat (Mistral) — 22 samples
- Claude Code — 22 samples
- Kagi Assistant — 14 samples
- Gemini CLI — 10 samples
- Raycast AI — 9 samples
- Fellou Browser AI — 5 samples
- Confer — 5 samples

---

## File Structure

```
prompt-injection-llm-benchmark/
├── README.md                          ← This file
├── ACCESS_POLICY.MD                   ← Data access and usage terms
├── data/
│   └── prompt_injection_dataset_250.csv   ← Full dataset (250 samples)
├── schema/
│   └── annotation_rubric.md           ← Annotation scale definition
└── scripts/
    └── evaluate.py                    ← Evaluation script (ASR computation)
```

---

## CSV Schema

Each row in `prompt_injection_dataset_250.csv` contains:

| Column | Type | Description |
|---|---|---|
| `attack_id` | string | Unique identifier (ATK001–ATK250) |
| `category` | string | Primary attack class |
| `subcategory` | string | Specific technique |
| `target_system` | string | Target LLM / application |
| `complexity` | string | Simple / Intermediate / Advanced |
| `language` | string | Language of the prompt |
| `prompt_text` | string | Full attack prompt |
| `target_behavior` | string | Intended policy violation |

---

## Access Policy

This dataset is released for **academic research purposes only**.

- A **de-identified public sample** (25 prompts, one per complexity stratum per category) is available without registration in `data/public_sample_25.csv`
- **Full dataset access** requires submitting a request to `malik.saed555@gmail.com` with:
  - Subject: `[Dataset Access] Prompt Injection Benchmark`
  - Your institutional affiliation
  - Brief description of intended use
- Access is granted subject to agreement to the terms in `ACCESS_POLICY.md`

See `ACCESS_POLICY.md` for full terms.

---

## Citation

If you use this dataset, please cite:

```bibtex
@article{anwar2024promptinjection,
  title   = {Prompt Injection Attacks in Large Language Models:
             Comprehensive Threat Analysis, Empirical Dataset
             Construction and Critical Mitigation Gaps
  author  = {Anwar, Muhammad Saeed},
  year    = {2024},
  note    = {arXiv preprint}
}
```

---

## License

Dataset content is released under **CC BY-NC 4.0** (Creative Commons Attribution–NonCommercial 4.0).
Evaluation scripts are released under **MIT License**.
