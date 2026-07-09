"""Dataset loader from CSV and JSON files."""

import csv
import json
from pathlib import Path
from typing import List, Union

from src.data.dataset import Dataset, Sample
from src.utils.logger import setup_logger


logger = setup_logger(__name__)


class DatasetLoader:
    """Load dataset from CSV or JSON files."""
    
    @staticmethod
    def load_csv(filepath: str) -> Dataset:
        """Load dataset from CSV file.
        
        Args:
            filepath: Path to CSV file
            
        Returns:
            Loaded Dataset
        """
        samples = []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sample = Sample(
                    attack_id=row['attack_id'],
                    category=row['category'],
                    subcategory=row['subcategory'],
                    target_system=row['target_system'],
                    complexity=row['complexity'],
                    language=row['language'],
                    prompt_text=row['prompt_text'],
                    target_behavior=row['target_behavior'],
                )
                samples.append(sample)
        
        logger.info(f"Loaded {len(samples)} samples from {filepath}")
        return Dataset(samples)
    
    @staticmethod
    def load_json(filepath: str) -> Dataset:
        """Load dataset from JSON file.
        
        Args:
            filepath: Path to JSON file
            
        Returns:
            Loaded Dataset
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        samples = []
        for item in data:
            sample = Sample(
                attack_id=item['attack_id'],
                category=item['category'],
                subcategory=item['subcategory'],
                target_system=item['target_system'],
                complexity=item['complexity'],
                language=item['language'],
                prompt_text=item['prompt_text'],
                target_behavior=item['target_behavior'],
            )
            samples.append(sample)
        
        logger.info(f"Loaded {len(samples)} samples from {filepath}")
        return Dataset(samples)
    
    @staticmethod
    def load(filepath: str) -> Dataset:
        """Load dataset from CSV or JSON file (auto-detect format).
        
        Args:
            filepath: Path to dataset file
            
        Returns:
            Loaded Dataset
        """
        filepath = Path(filepath)
        
        if filepath.suffix == '.csv':
            return DatasetLoader.load_csv(str(filepath))
        elif filepath.suffix == '.json':
            return DatasetLoader.load_json(str(filepath))
        else:
            raise ValueError(f"Unsupported file format: {filepath.suffix}")
