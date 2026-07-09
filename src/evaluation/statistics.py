"""Statistical analysis module."""

from typing import List, Dict, Any


class StatisticalAnalyzer:
    """Statistical analysis for evaluation results."""
    
    def __init__(self, results: List):
        """Initialize analyzer.
        
        Args:
            results: List of evaluation results
        """
        self.results = results
    
    def compute_statistics(self) -> Dict[str, Any]:
        """Compute basic statistics.
        
        Returns:
            Dictionary of statistics
        """
        if not self.results:
            return {}
        
        # Group by model
        by_model = {}
        for result in self.results:
            model = result.model_name
            if model not in by_model:
                by_model[model] = []
            by_model[model].append(result.success)
        
        # Compute statistics
        stats = {}
        for model, successes in by_model.items():
            total = len(successes)
            successful = sum(successes)
            stats[model] = {
                'asr': successful / total if total > 0 else 0,
                'total': total,
                'successful': successful,
            }
        
        return stats
