"""Configuration loader for YAML configs."""

import os
from pathlib import Path
from typing import Any, Dict, Optional

import yaml
from dotenv import load_dotenv


class ConfigLoader:
    """Load and manage YAML configuration files."""
    
    def __init__(self, config_dir: str = "configs"):
        """Initialize config loader.
        
        Args:
            config_dir: Directory containing config files
        """
        self.config_dir = Path(config_dir)
        load_dotenv()  # Load environment variables
        self.configs: Dict[str, Dict[str, Any]] = {}
    
    def load(self, filename: str) -> Dict[str, Any]:
        """Load YAML config file.
        
        Args:
            filename: Config file name (with or without .yaml)
            
        Returns:
            Configuration dictionary
        """
        if not filename.endswith('.yaml'):
            filename += '.yaml'
        
        filepath = self.config_dir / filename
        
        if not filepath.exists():
            raise FileNotFoundError(f"Config file not found: {filepath}")
        
        with open(filepath, 'r') as f:
            config = yaml.safe_load(f)
        
        # Substitute environment variables
        config = self._substitute_env_vars(config)
        self.configs[filename] = config
        
        return config
    
    def load_all(self) -> Dict[str, Dict[str, Any]]:
        """Load all YAML config files from config directory.
        
        Returns:
            Dictionary of all configurations
        """
        configs = {}
        for filepath in self.config_dir.glob('*.yaml'):
            key = filepath.stem
            with open(filepath, 'r') as f:
                config = yaml.safe_load(f)
                config = self._substitute_env_vars(config)
                configs[key] = config
        return configs
    
    @staticmethod
    def _substitute_env_vars(obj: Any) -> Any:
        """Recursively substitute environment variables in config.
        
        Args:
            obj: Configuration object (dict, list, str, etc.)
            
        Returns:
            Configuration with substituted values
        """
        if isinstance(obj, dict):
            return {k: ConfigLoader._substitute_env_vars(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [ConfigLoader._substitute_env_vars(item) for item in obj]
        elif isinstance(obj, str):
            # Replace ${VAR_NAME} with environment variable
            if obj.startswith('${') and obj.endswith('}'):
                var_name = obj[2:-1]
                return os.getenv(var_name, obj)
            return obj
        else:
            return obj
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get config value using dot notation.
        
        Args:
            key: Config key (e.g., 'models.gpt4o.temperature')
            default: Default value if key not found
            
        Returns:
            Config value or default
        """
        keys = key.split('.')
        value = self.configs
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        
        return value
    
    def save(self, filename: str, config: Dict[str, Any]) -> None:
        """Save configuration to YAML file.
        
        Args:
            filename: Output filename
            config: Configuration dictionary
        """
        if not filename.endswith('.yaml'):
            filename += '.yaml'
        
        filepath = self.config_dir / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)
