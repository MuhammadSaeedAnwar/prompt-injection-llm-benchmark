"""Helper functions for benchmark."""

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


def ensure_dir(path: str) -> Path:
    """Ensure directory exists, create if necessary.
    
    Args:
        path: Directory path
        
    Returns:
        Path object
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def save_json(data: Any, filepath: str, indent: int = 2) -> None:
    """Save data to JSON file.
    
    Args:
        data: Data to save
        filepath: Output file path
        indent: JSON indentation level
    """
    ensure_dir(Path(filepath).parent)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def load_json(filepath: str) -> Any:
    """Load data from JSON file.
    
    Args:
        filepath: Input file path
        
    Returns:
        Loaded data
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def compute_file_hash(filepath: str, algorithm: str = 'sha256') -> str:
    """Compute hash of file.
    
    Args:
        filepath: File path
        algorithm: Hash algorithm ('sha256', 'md5', etc.)
        
    Returns:
        Hex hash string
    """
    hasher = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def compute_string_hash(text: str, algorithm: str = 'sha256') -> str:
    """Compute hash of string.
    
    Args:
        text: Input text
        algorithm: Hash algorithm
        
    Returns:
        Hex hash string
    """
    hasher = hashlib.new(algorithm)
    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()


def find_duplicates(items: List[Any], key_func=None) -> List[List[int]]:
    """Find duplicate items by index.
    
    Args:
        items: List of items
        key_func: Optional function to extract comparison key
        
    Returns:
        List of duplicate index groups
    """
    seen = {}
    duplicates = []
    
    for idx, item in enumerate(items):
        key = key_func(item) if key_func else item
        if key in seen:
            # Find or create group
            found = False
            for group in duplicates:
                if seen[key] in group:
                    group.append(idx)
                    found = True
                    break
            if not found:
                duplicates.append([seen[key], idx])
        else:
            seen[key] = idx
    
    return duplicates


def merge_dicts(*dicts: Dict) -> Dict:
    """Recursively merge multiple dictionaries.
    
    Args:
        *dicts: Variable number of dictionaries
        
    Returns:
        Merged dictionary
    """
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value)
            else:
                result[key] = value
    return result
