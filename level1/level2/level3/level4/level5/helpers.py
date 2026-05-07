"""
Helpers class with utility functions deep in the folder structure.
"""
from datetime import datetime
from typing import List, Dict, Any

# import sys
# import os

# repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../'))
# if repo_root not in sys.path:
#   sys.path.insert(0, repo_root)

class Helpers:
    """
    A helper class containing various utility functions for data processing.
    """

    def __init__(self, debug: bool = False):
        """
        Initialize the Helpers class.

        Args:
            debug: Enable debug mode for verbose logging
        """
        self.debug = debug
        self.created_at = datetime.now()

    def transform_data(self, data: List[Dict[str, Any]], key: str) -> List[Any]:
        """
        Extract specific key values from a list of dictionaries.

        Args:
            data: List of dictionaries to process
            key: Key to extract from each dictionary

        Returns:
            List of values for the specified key
        """
        if self.debug:
            print(f"Transforming data for key: {key}")

        return [item.get(key) for item in data if key in item]

    def filter_by_condition(self, data: List[int], threshold: int) -> List[int]:
        """
        Filter a list of numbers based on a threshold.

        Args:
            data: List of integers to filter
            threshold: Minimum value to include

        Returns:
            Filtered list of integers
        """
        if self.debug:
            print(f"Filtering data with threshold: {threshold}")

        return [x for x in data if x >= threshold]

    def merge_dictionaries(self, dict1: Dict, dict2: Dict) -> Dict:
        """
        Merge two dictionaries with dict2 values taking precedence.

        Args:
            dict1: First dictionary
            dict2: Second dictionary

        Returns:
            Merged dictionary
        """
        if self.debug:
            print("Merging dictionaries")

        merged = dict1.copy()
        merged.update(dict2)
        return merged

    def calculate_statistics(self, numbers: List[float]) -> Dict[str, float]:
        """
        Calculate basic statistics for a list of numbers.

        Args:
            numbers: List of numbers

        Returns:
            Dictionary with mean, min, max, and count
        """
        if not numbers:
            return {'mean': 0, 'min': 0, 'max': 0, 'count': 0}

        return {
            'mean': sum(numbers) / len(numbers),
            'min': min(numbers),
            'max': max(numbers),
            'count': len(numbers)
        }

    def format_timestamp(self, timestamp: datetime = None) -> str:
        """
        Format a timestamp to a readable string.

        Args:
            timestamp: Datetime object (uses current time if None)

        Returns:
            Formatted timestamp string
        """
        ts = timestamp or datetime.now()
        return ts.strftime("%Y-%m-%d %H:%M:%S")
