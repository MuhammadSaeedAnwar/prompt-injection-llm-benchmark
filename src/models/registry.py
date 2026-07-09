"""Model registry for managing multiple models."""

from typing import Dict, List, Optional
import importlib

from src.models.base import BaseModel
from src.utils.logger import setup_logger


logger = setup_logger(__name__)


class MockModel(BaseModel):
    """Mock model for testing without API calls."""
    
    def generate(self, prompt: str) -> str:
        """Return mock response."""
        return f"[Mock Response] Received prompt of {len(prompt)} characters"


class ModelRegistry:
    """Registry for managing LLM models."""
    
    _models: Dict[str, BaseModel] = {}
    
    @classmethod
    def register(cls, name: str, model: BaseModel) -> None:
        """Register a model.
        
        Args:
            name: Model identifier
            model: Model instance
        """
        cls._models[name] = model
        logger.info(f"Registered model: {name}")
    
    @classmethod
    def get(cls, name: str) -> Optional[BaseModel]:
        """Get registered model.
        
        Args:
            name: Model identifier
            
        Returns:
            Model instance or None
        """
        return cls._models.get(name)
    
    @classmethod
    def list_models(cls) -> List[str]:
        """List all registered models.
        
        Returns:
            List of model names
        """
        return list(cls._models.keys())
    
    @classmethod
    def load_models(cls, model_configs: List[Dict]) -> List[BaseModel]:
        """Load models from configurations.
        
        Args:
            model_configs: List of model configuration dictionaries
            
        Returns:
            List of loaded models
        """
        models = []
        
        for config in model_configs:
            model_type = config.get('type', 'mock')
            name = config.get('name')
            
            # Use mock model for now (can be extended for real APIs)
            if model_type == 'mock':
                model = MockModel(
                    name=name,
                    temperature=config.get('temperature', 0.7),
                    max_tokens=config.get('max_tokens', 2048),
                    timeout=config.get('timeout', 60),
                )
            else:
                logger.warning(f"Unknown model type: {model_type}, using mock")
                model = MockModel(name=name)
            
            cls.register(name, model)
            models.append(model)
        
        logger.info(f"Loaded {len(models)} models")
        return models
