# utils.py
# Author: Akash Chandran
# Description: Helper functions for dictionary merging.

import json

def load_json(file_path):
    """
    Loads a JSON file and returns the data as a dictionary.
    Args:
        file_path (str): Path to the JSON file.
    Returns:
        dict: Parsed JSON data as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while loading '{file_path}': {e}")
        return {}

def validate_dict(data):
    """
    Validates if the data is a dictionary.
    Args:
        data: The data to validate.
    Returns:
        bool: True if data is a dictionary, False otherwise.
    """
    if isinstance(data, dict):
        return True
    print("Error: The provided data is not a dictionary.")
    return False
