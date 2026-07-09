"""Prompt Injection LLM Benchmark - Core Package."""

__version__ = "1.0.0"
__author__ = "Muhammad Saeed Anwar"
__email__ = "muhammadsaeedanwar@protonmail.com"
__description__ = "Comprehensive multilingual prompt injection attack benchmark for evaluating LLM robustness"

from src.data import DatasetLoader
from src.models import ModelRegistry
from src.evaluation import Evaluator

__all__ = [
    "DatasetLoader",
    "ModelRegistry",
    "Evaluator",
    "__version__",
]
