#!/usr/bin/env python
"""Generate dataset statistics."""

import argparse
import sys
import csv
from pathlib import Path
from collections import Counter

from src.data import DatasetLoader
from src.utils.logger import setup_logger
from src.utils.helpers import ensure_dir


logger = setup_logger(__name__)


def main():
    """Generate statistics."""
    parser = argparse.ArgumentParser(description="Generate dataset statistics")
    parser.add_argument(
        "--dataset",
        type=str,
        default="dataset/prompt_injection_dataset_250.csv",
        help="Dataset file path",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="dataset/statistics/",
        help="Output directory",
    )
    
    args = parser.parse_args()
    
    logger.info("Generating dataset statistics...")
    
    try:
        # Load dataset
        dataset = DatasetLoader.load(args.dataset)
        
        # Ensure output directory
        output_dir = Path(args.output)
        ensure_dir(str(output_dir))
        
        # Generate statistics
        stats = dataset.get_statistics()
        
        # Save category distribution
        with open(output_dir / "attack_distribution.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Category", "Count", "Percentage"])
            for cat, count in stats["categories"].items():
                pct = (count / stats["total_samples"]) * 100
                writer.writerow([cat, count, f"{pct:.1f}%"])
        logger.info(f"✓ Saved {output_dir / 'attack_distribution.csv'}")
        
        # Save language distribution
        with open(output_dir / "language_distribution.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Language", "Count", "Percentage"])
            for lang, count in stats["languages"].items():
                pct = (count / stats["total_samples"]) * 100
                writer.writerow([lang, count, f"{pct:.1f}%"])
        logger.info(f"✓ Saved {output_dir / 'language_distribution.csv'}")
        
        # Summary
        logger.info(f"\n✓ Statistics generated")
        logger.info(f"  Total samples: {stats['total_samples']}")
        logger.info(f"  Categories: {stats['unique_categories']}")
        logger.info(f"  Languages: {stats['unique_languages']}")
        
        return 0
    
    except Exception as e:
        logger.error(f"✗ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
