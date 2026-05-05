"""
Root-level utils module with common utility functions.
"""
import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if repo_root not in sys.path:
  sys.path.insert(0, repo_root)


def format_string(text: str, uppercase: bool = False) -> str:
    """
    Format a string with optional uppercase transformation.

    Args:
        text: Input string to format
        uppercase: If True, convert to uppercase

    Returns:
        Formatted string
    """
    formatted = text.strip()
    return formatted.upper() if uppercase else formatted


def calculate_sum(numbers: list) -> float:
    """
    Calculate the sum of a list of numbers.

    Args:
        numbers: List of numbers to sum

    Returns:
        Sum of all numbers
    """
    return sum(numbers)


def validate_config(config: dict) -> bool:
    """
    Validate a configuration dictionary.

    Args:
        config: Configuration dictionary to validate

    Returns:
        True if valid, False otherwise
    """
    required_keys = ['name', 'version']
    return all(key in config for key in required_keys)
