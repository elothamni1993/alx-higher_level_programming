#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

# Function imports from other files
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    # Try to load existing items from file, if not found, create an empty list
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Extend the current list with the additional arguments provided
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, "add_item.json")

