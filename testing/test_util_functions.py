import pytest
import types
import json
import os
from utils import util_functions as util
from utils.storage import save_to_json, load_from_json

def setup_data(tmp_path):
    data_file = tmp_path / "data.json"
    data = {
        "users": [
            {"id": "u1", "name": "Alice", "email": "alice@example.com"},
            {"id": "u2", "name": "Bob", "email": "bob@example.com"}
        ],
        "projects": [
            {"id": "p1", "title": "Proj1", "description": "Desc", "due_date": "2025-12-31", "assigned_user_id": "u1"}
        ],
        "tasks": [
            {"id": "t1", "title": "Task1", "status": "Pending", "assigned_to": "p1"}
        ]
    }
    save_to_json(str(data_file), data)
    return data_file

def test_all_users(tmp_path, monkeypatch):
    data_file = setup_data(tmp_path)
    monkeypatch.setattr(util, "load_from_json", lambda path: load_from_json(str(data_file)))
    users = util.all_users()
    assert len(users) == 2
    assert users[0]["name"] == "Alice"

def test_all_projects(tmp_path, monkeypatch):
    data_file = setup_data(tmp_path)
    monkeypatch.setattr(util, "load_from_json", lambda path: load_from_json(str(data_file)))
    projects = util.all_projects()
    assert len(projects) == 1
    assert projects[0]["title"] == "Proj1"

def test_all_tasks(tmp_path, monkeypatch):
    data_file = setup_data(tmp_path)
    monkeypatch.setattr(util, "load_from_json", lambda path: load_from_json(str(data_file)))
    tasks = util.all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task1"
