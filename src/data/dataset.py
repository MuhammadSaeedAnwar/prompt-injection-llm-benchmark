"""Dataset class for prompt injection attacks."""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class Sample:
    """Single prompt injection attack sample."""
    
    attack_id: str
    category: str
    subcategory: str
    target_system: str
    complexity: str
    language: str
    prompt_text: str
    target_behavior: str
    
    # Optional fields
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            'attack_id': self.attack_id,
            'category': self.category,
            'subcategory': self.subcategory,
            'target_system': self.target_system,
            'complexity': self.complexity,
            'language': self.language,
            'prompt_text': self.prompt_text,
            'target_behavior': self.target_behavior,
            'metadata': self.metadata,
        }


class Dataset:
    """Prompt injection attack dataset."""
    
    def __init__(self, samples: List[Sample]):
        """Initialize dataset.
        
        Args:
            samples: List of Sample objects
        """
        self.samples = samples
    
    def __len__(self) -> int:
        """Return number of samples."""
        return len(self.samples)
    
    def __getitem__(self, idx: int) -> Sample:
        """Get sample by index."""
        return self.samples[idx]
    
    def __iter__(self):
        """Iterate over samples."""
        return iter(self.samples)
    
    def filter_by_category(self, category: str) -> 'Dataset':
        """Filter samples by attack category.
        
        Args:
            category: Attack category
            
        Returns:
            Filtered dataset
        """
        filtered = [s for s in self.samples if s.category == category]
        return Dataset(filtered)
    
    def filter_by_language(self, language: str) -> 'Dataset':
        """Filter samples by language.
        
        Args:
            language: Language
            
        Returns:
            Filtered dataset
        """
        filtered = [s for s in self.samples if s.language == language]
        return Dataset(filtered)
    
    def filter_by_complexity(self, complexity: str) -> 'Dataset':
        """Filter samples by complexity.
        
        Args:
            complexity: Complexity level
            
        Returns:
            Filtered dataset
        """
        filtered = [s for s in self.samples if s.complexity == complexity]
        return Dataset(filtered)
    
    def get_statistics(self) -> Dict[str, Any]:
        """Compute dataset statistics.
        
        Returns:
            Dictionary of statistics
        """
        from collections import Counter
        
        categories = Counter(s.category for s in self.samples)
        languages = Counter(s.language for s in self.samples)
        complexities = Counter(s.complexity for s in self.samples)
        systems = Counter(s.target_system for s in self.samples)
        
        return {
            'total_samples': len(self.samples),
            'categories': dict(categories),
            'languages': dict(languages),
            'complexities': dict(complexities),
            'systems': dict(systems),
            'unique_categories': len(categories),
            'unique_languages': len(languages),
            'unique_systems': len(systems),
        }
