"""Base model class for LLM integrations."""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any


class BaseModel(ABC):
    """Abstract base class for LLM models."""
    
    def __init__(
        self,
        name: str,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        timeout: int = 60,
    ):
        """Initialize base model.
        
        Args:
            name: Model name
            temperature: Sampling temperature
            max_tokens: Maximum token output
            timeout: Request timeout in seconds
        """
        self.name = name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
    
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate response from prompt.
        
        Args:
            prompt: Input prompt
            
        Returns:
            Model response
        """
        pass
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
