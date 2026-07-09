"""Dataset validation module."""

from typing import Dict, List, Tuple

from src.data.dataset import Dataset
from src.utils.logger import setup_logger
from src.utils.constants import (
    ATTACK_CATEGORIES,
    COMPLEXITY_LEVELS,
    LANGUAGES,
    TARGET_SYSTEMS,
)


logger = setup_logger(__name__)


class DatasetValidator:
    """Validate dataset integrity and schema."""
    
    @staticmethod
    def validate(dataset: Dataset) -> Tuple[bool, List[str]]:
        """Validate entire dataset.
        
        Args:
            dataset: Dataset to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Check for empty dataset
        if len(dataset) == 0:
            errors.append("Dataset is empty")
            return False, errors
        
        # Validate each sample
        for idx, sample in enumerate(dataset):
            sample_errors = DatasetValidator._validate_sample(sample, idx)
            errors.extend(sample_errors)
        
        # Check for duplicates
        duplicate_errors = DatasetValidator._check_duplicates(dataset)
        errors.extend(duplicate_errors)
        
        is_valid = len(errors) == 0
        
        if is_valid:
            logger.info(f"Dataset validation passed: {len(dataset)} samples")
        else:
            logger.warning(f"Dataset validation failed with {len(errors)} errors")
        
        return is_valid, errors
    
    @staticmethod
    def _validate_sample(sample, idx: int) -> List[str]:
        """Validate single sample.
        
        Args:
            sample: Sample to validate
            idx: Sample index
            
        Returns:
            List of validation errors
        """
        errors = []
        
        # Check required fields
        if not sample.attack_id:
            errors.append(f"Sample {idx}: Missing attack_id")
        if not sample.category:
            errors.append(f"Sample {idx}: Missing category")
        if not sample.language:
            errors.append(f"Sample {idx}: Missing language")
        if not sample.prompt_text:
            errors.append(f"Sample {idx}: Missing prompt_text")
        
        # Check field values
        if sample.category not in ATTACK_CATEGORIES:
            errors.append(f"Sample {idx}: Invalid category '{sample.category}'")
        
        if sample.complexity not in COMPLEXITY_LEVELS:
            errors.append(f"Sample {idx}: Invalid complexity '{sample.complexity}'")
        
        if sample.language not in LANGUAGES:
            errors.append(f"Sample {idx}: Invalid language '{sample.language}'")
        
        if sample.target_system not in TARGET_SYSTEMS:
            errors.append(f"Sample {idx}: Invalid target_system '{sample.target_system}'")
        
        # Check text length
        if len(sample.prompt_text) == 0:
            errors.append(f"Sample {idx}: Empty prompt_text")
        if len(sample.prompt_text) > 10000:
            errors.append(f"Sample {idx}: prompt_text too long (>{10000} chars)")
        
        return errors
    
    @staticmethod
    def _check_duplicates(dataset: Dataset) -> List[str]:
        """Check for duplicate samples.
        
        Args:
            dataset: Dataset to check
            
        Returns:
            List of duplicate warnings
        """
        errors = []
        seen_prompts = {}
        
        for idx, sample in enumerate(dataset):
            # Use prompt text as duplicate key
            key = sample.prompt_text.lower().strip()
            
            if key in seen_prompts:
                errors.append(
                    f"Duplicate detected: Sample {idx} duplicates Sample {seen_prompts[key]}"
                )
            else:
                seen_prompts[key] = idx
        
        if errors:
            logger.warning(f"Found {len(errors)} duplicate(s) in dataset")
        
        return errors
    
    @staticmethod
    def get_schema() -> Dict:
        """Get dataset schema.
        
        Returns:
            Schema dictionary
        """
        return {
            'attack_id': {
                'type': 'string',
                'required': True,
                'description': 'Unique identifier (ATK001-ATK250)',
            },
            'category': {
                'type': 'string',
                'required': True,
                'enum': list(ATTACK_CATEGORIES.keys()),
                'description': 'Attack category',
            },
            'subcategory': {
                'type': 'string',
                'required': True,
                'description': 'Attack subcategory',
            },
            'target_system': {
                'type': 'string',
                'required': True,
                'enum': TARGET_SYSTEMS,
                'description': 'Target LLM system',
            },
            'complexity': {
                'type': 'string',
                'required': True,
                'enum': COMPLEXITY_LEVELS,
                'description': 'Attack complexity level',
            },
            'language': {
                'type': 'string',
                'required': True,
                'enum': LANGUAGES,
                'description': 'Attack language',
            },
            'prompt_text': {
                'type': 'string',
                'required': True,
                'description': 'Full attack prompt',
            },
            'target_behavior': {
                'type': 'string',
                'required': True,
                'description': 'Intended attack outcome',
            },
        }
