import json
import os

def load_from_json(file_path):
    default_data = {"users": [], "projects": [], "tasks": []}
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    # Corrupt or empty file, reset to default
                    with open(file_path, 'w') as wf:
                        json.dump(default_data, wf, indent=4)
                    return default_data
        else:
            # Create the file and save default data
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as file:
                json.dump(default_data, file, indent=4)
            return default_data
    except Exception as e:
        print(f"[ERROR] Failed to load or create {file_path}: {e}")
        return default_data

def save_to_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"[ERROR] Failed to save data to {file_path}: {e}")