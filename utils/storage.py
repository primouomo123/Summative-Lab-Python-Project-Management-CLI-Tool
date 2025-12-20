import json
import os

def load_from_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        # Default structure
        default_data = {"users": [], "projects": [], "tasks": []}
        # Create the file and save default data
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            json.dump(default_data, file, indent=4)
        return default_data

def save_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)