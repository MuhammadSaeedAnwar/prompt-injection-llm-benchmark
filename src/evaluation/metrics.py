"""Metrics computation for evaluation results."""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from collections import Counter
import math

from src.evaluation.evaluator import EvaluationResult
from src.utils.logger import setup_logger


logger = setup_logger(__name__)


@dataclass
class Metrics:
    """Computed metrics for evaluation."""
    
    attack_success_rate: float
    confidence_interval_95: tuple  # (lower, upper)
    f1_score: float
    precision: float
    recall: float
    accuracy: float
    mcc: float  # Matthews Correlation Coefficient
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            'attack_success_rate': self.attack_success_rate,
            'confidence_interval_95': self.confidence_interval_95,
            'f1_score': self.f1_score,
            'precision': self.precision,
            'recall': self.recall,
            'accuracy': self.accuracy,
            'mcc': self.mcc,
        }
    
    def __str__(self) -> str:
        ci_lower, ci_upper = self.confidence_interval_95
        return (
            f"ASR: {self.attack_success_rate:.1%} [{ci_lower:.1%}, {ci_upper:.1%}]\n"
            f"F1: {self.f1_score:.3f} | Precision: {self.precision:.3f} | Recall: {self.recall:.3f}\n"
            f"Accuracy: {self.accuracy:.3f} | MCC: {self.mcc:.3f}"
        )


def compute_metrics(results: List[EvaluationResult]) -> Metrics:
    """Compute evaluation metrics from results.
    
    Args:
        results: List of evaluation results
        
    Returns:
        Computed metrics
    """
    if not results:
        raise ValueError("No results to compute metrics from")
    
    # Extract success labels
    successes = [1 if r.success else 0 for r in results]
    n = len(successes)
    successful = sum(successes)
    
    # Attack Success Rate
    asr = successful / n
    
    # 95% Confidence Interval (Wilson score interval)
    ci_lower, ci_upper = _wilson_ci(successful, n, confidence=0.95)
    
    # For binary classification, treat success=1 as positive
    # All results are positive labels by design
    tp = successful  # True positives (attacks that succeeded)
    fp = 0  # False positives (not applicable)
    tn = n - successful  # True negatives (attacks that failed)
    fn = 0  # False negatives (not applicable)
    
    # Metrics
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    accuracy = (tp + tn) / n if n > 0 else 0.0
    
    # Matthews Correlation Coefficient
    denominator = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)) if (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn) > 0 else 1
    mcc = (tp * tn - fp * fn) / denominator if denominator > 0 else 0.0
    
    return Metrics(
        attack_success_rate=asr,
        confidence_interval_95=(ci_lower, ci_upper),
        f1_score=f1,
        precision=precision,
        recall=recall,
        accuracy=accuracy,
        mcc=mcc,
    )


def _wilson_ci(
    successes: int,
    total: int,
    confidence: float = 0.95,
) -> tuple:
    """Compute Wilson score confidence interval.
    
    Args:
        successes: Number of successes
        total: Total number of trials
        confidence: Confidence level (0.95 = 95%)
        
    Returns:
        Tuple of (lower, upper) bounds
    """
    z = _z_score(confidence)
    p_hat = successes / total
    
    denominator = 1 + z * z / total
    centre = (p_hat + z * z / (2 * total)) / denominator
    margin = z * math.sqrt(p_hat * (1 - p_hat) / total + z * z / (4 * total * total)) / denominator
    
    return (max(0, centre - margin), min(1, centre + margin))


def _z_score(confidence: float) -> float:
    """Get z-score for confidence level.
    
    Args:
        confidence: Confidence level
        
    Returns:
        Z-score
    """
    # Common z-scores
    z_scores = {
        0.90: 1.645,
        0.95: 1.96,
        0.99: 2.576,
    }
    return z_scores.get(confidence, 1.96)
