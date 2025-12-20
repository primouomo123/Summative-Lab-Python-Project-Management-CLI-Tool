import pytest
import os
import json
from utils.storage import load_from_json, save_to_json

def test_load_and_save_json(tmp_path):
    test_file = tmp_path / "test.json"
    # Should create file with default structure if not exists
    data = load_from_json(str(test_file))
    assert data == {"users": [], "projects": [], "tasks": []}
    # Save new data
    data["users"].append({"id": "1", "name": "Test", "email": "test@example.com"})
    save_to_json(str(test_file), data)
    # Load again and check
    loaded = load_from_json(str(test_file))
    assert loaded["users"][0]["name"] == "Test"
    assert os.path.exists(test_file)
