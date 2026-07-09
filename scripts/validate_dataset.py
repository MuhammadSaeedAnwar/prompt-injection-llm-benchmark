#!/usr/bin/env python
"""Validate dataset integrity and schema."""

import argparse
import sys
from pathlib import Path

from src.data import DatasetLoader, DatasetValidator
from src.utils.logger import setup_logger


logger = setup_logger(__name__)


def main():
    """Validate dataset."""
    parser = argparse.ArgumentParser(description="Validate prompt injection dataset")
    parser.add_argument(
        "--dataset",
        type=str,
        default="dataset/prompt_injection_dataset_250.csv",
        help="Dataset file path",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output",
    )
    
    args = parser.parse_args()
    
    logger.info("Validating dataset...")
    
    try:
        # Load dataset
        dataset = DatasetLoader.load(args.dataset)
        logger.info(f"✓ Loaded {len(dataset)} samples")
        
        # Validate
        validator = DatasetValidator()
        is_valid, errors = validator.validate(dataset)
        
        if is_valid:
            logger.info("✓ Dataset validation PASSED")
            stats = dataset.get_statistics()
            logger.info(f"\nStatistics:")
            logger.info(f"  Total samples: {stats['total_samples']}")
            logger.info(f"  Categories: {stats['unique_categories']}")
            logger.info(f"  Languages: {stats['unique_languages']}")
            logger.info(f"  Systems: {stats['unique_systems']}")
            return 0
        else:
            logger.error(f"✗ Dataset validation FAILED with {len(errors)} error(s)")
            for error in errors:
                logger.error(f"  - {error}")
            return 1
    
    except Exception as e:
        logger.error(f"✗ Validation error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
