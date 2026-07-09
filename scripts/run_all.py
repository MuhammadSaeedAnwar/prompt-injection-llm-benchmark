#!/usr/bin/env python
"""Main execution script: Run entire pipeline in one command."""

import argparse
import sys
import logging
from pathlib import Path

from src.data import DatasetLoader, DatasetValidator
from src.models import ModelRegistry
from src.evaluation import Evaluator, compute_metrics
from src.config import ConfigLoader
from src.utils.logger import setup_logger
from src.utils.helpers import save_json, ensure_dir


logger = setup_logger(__name__, level=logging.INFO)


def main():
    """Execute complete pipeline."""
    parser = argparse.ArgumentParser(
        description="Run complete prompt injection benchmark pipeline"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="configs/default_config.yaml",
        help="Configuration file path",
    )
    parser.add_argument(
        "--dataset",
        type=str,
        default="dataset/prompt_injection_dataset_250.csv",
        help="Dataset file path",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="results/",
        help="Output directory",
    )
    parser.add_argument(
        "--models",
        type=str,
        default="mock-model-1,mock-model-2",
        help="Comma-separated model names to evaluate",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose logging",
    )
    
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    output_dir = Path(args.output)
    ensure_dir(str(output_dir))
    
    logger.info("="*70)
    logger.info("PROMPT INJECTION LLM BENCHMARK - COMPLETE PIPELINE")
    logger.info("="*70)
    
    # Step 1: Load and validate dataset
    logger.info("\n[1/6] LOADING AND VALIDATING DATASET")
    logger.info("-" * 70)
    try:
        dataset = DatasetLoader.load(args.dataset)
        logger.info(f"✓ Loaded {len(dataset)} samples")
        
        validator = DatasetValidator()
        is_valid, errors = validator.validate(dataset)
        
        if is_valid:
            logger.info("✓ Dataset validation PASSED")
            stats = dataset.get_statistics()
            logger.info(f"  - Categories: {stats['unique_categories']}")
            logger.info(f"  - Languages: {stats['unique_languages']}")
            logger.info(f"  - Target Systems: {stats['unique_systems']}")
        else:
            logger.warning(f"⚠ Dataset validation found {len(errors)} issue(s)")
            for error in errors[:5]:  # Show first 5 errors
                logger.warning(f"  - {error}")
    except Exception as e:
        logger.error(f"✗ Failed to load dataset: {e}")
        return 1
    
    # Step 2: Initialize models
    logger.info("\n[2/6] INITIALIZING MODELS")
    logger.info("-" * 70)
    try:
        model_names = [m.strip() for m in args.models.split(",")]
        model_configs = [
            {"name": name, "type": "mock", "temperature": 0.7}
            for name in model_names
        ]
        models = ModelRegistry.load_models(model_configs)
        logger.info(f"✓ Initialized {len(models)} models")
        for model in models:
            logger.info(f"  - {model.name}")
    except Exception as e:
        logger.error(f"✗ Failed to initialize models: {e}")
        return 1
    
    # Step 3: Run evaluation
    logger.info("\n[3/6] RUNNING EVALUATION")
    logger.info("-" * 70)
    try:
        evaluator = Evaluator(dataset, models, batch_size=10, timeout=60)
        results = evaluator.evaluate()
        logger.info(f"✓ Evaluation complete: {len(results)} results")
    except Exception as e:
        logger.error(f"✗ Evaluation failed: {e}")
        return 1
    
    # Step 4: Compute metrics
    logger.info("\n[4/6] COMPUTING METRICS")
    logger.info("-" * 70)
    try:
        metrics = compute_metrics(results)
        logger.info(f"✓ Metrics computed")
        logger.info(f"  Attack Success Rate: {metrics.attack_success_rate:.1%}")
        logger.info(f"  F1-Score: {metrics.f1_score:.3f}")
        logger.info(f"  MCC: {metrics.mcc:.3f}")
    except Exception as e:
        logger.error(f"✗ Metrics computation failed: {e}")
        return 1
    
    # Step 5: Save results
    logger.info("\n[5/6] SAVING RESULTS")
    logger.info("-" * 70)
    try:
        results_dir = output_dir / "metrics"
        ensure_dir(str(results_dir))
        
        # Save results JSON
        results_data = [r.to_dict() for r in results]
        results_file = results_dir / "evaluation_results.json"
        save_json(results_data, str(results_file))
        logger.info(f"✓ Saved results to {results_file}")
        
        # Save metrics
        metrics_file = results_dir / "metrics.json"
        save_json(metrics.to_dict(), str(metrics_file))
        logger.info(f"✓ Saved metrics to {metrics_file}")
    except Exception as e:
        logger.error(f"✗ Failed to save results: {e}")
        return 1
    
    # Step 6: Summary
    logger.info("\n[6/6] PIPELINE SUMMARY")
    logger.info("-" * 70)
    logger.info(f"✓ PIPELINE COMPLETE")
    logger.info(f"  - Dataset: {len(dataset)} samples")
    logger.info(f"  - Models: {len(models)} models")
    logger.info(f"  - Evaluations: {len(results)} total")
    logger.info(f"  - Output: {output_dir}")
    logger.info("="*70)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
