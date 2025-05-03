# merge_dicts.py
# Author: Akash Chandran
# Description: Merges two dictionaries, combining values for common keys.

from utils import load_json, validate_dict

def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries, combining values for keys that appear in both dictionaries.
    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.
    Returns:
        dict: A dictionary that combines values from both input dictionaries.
    """
    try:
        if not validate_dict(dict1) or not validate_dict(dict2):
            return {}
        
        # Combine dictionaries
        merged_dict = dict1.copy()  # Copy first dictionary to avoid modifying the original
        for key, value in dict2.items():
            if key in merged_dict:
                # Combine values (can be adjusted based on how values should be merged)
                merged_dict[key] += value
            else:
                merged_dict[key] = value
        
        return merged_dict
    except Exception as e:
        print(f"An unexpected error occurred while merging dictionaries: {e}")
        return {}

if __name__ == "__main__":
    # Example usage of loading JSON files and merging them
    dict1 = load_json('data1.json')
    dict2 = load_json('data2.json')
    
    # Merge the dictionaries
    merged_result = merge_dicts(dict1, dict2)
    
    if merged_result:
        print("Merged Dictionary:")
        print(merged_result)
    else:
        print("Error: Could not merge dictionaries.")
