import pytest
import subprocess
import sys
import os
import json

def run_cli(args, data_file):
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()
    # Patch data file path in util_functions
    code = f"import utils.util_functions as util; util.load_from_json = lambda path: __import__('utils.storage').storage.load_from_json('{data_file}'); util.save_to_json = lambda path, data: __import__('utils.storage').storage.save_to_json('{data_file}', data); import main; main.main()"
    result = subprocess.run([sys.executable, "-c", code] + args, capture_output=True, text=True, env=env)
    return result

def test_add_and_list_user(tmp_path):
    data_file = tmp_path / "data.json"
    # Add user
    result = run_cli(["add_user", "--name", "TestUser", "--email", "test@ex.com"], str(data_file))
    assert "User TestUser added" in result.stdout
    # List users
    result = run_cli(["list_users"], str(data_file))
    assert "TestUser" in result.stdout

def test_add_and_list_project(tmp_path):
    data_file = tmp_path / "data.json"
    # Add user first
    run_cli(["add_user", "--name", "TestUser", "--email", "test@ex.com"], str(data_file))
    # Get the actual user ID from the data file
    with open(data_file) as f:
        data = json.load(f)
        user_id = data["users"][0]["id"]
    # Add project with real user ID
    result = run_cli([
        "add_project", "--title", "Proj1", "--description", "Desc", "--due-date", "2025-12-31", "--assigned-user-id", user_id
    ], str(data_file))
    assert "Project Proj1 added" in result.stdout
    # List projects
    result = run_cli(["list_projects"], str(data_file))
    assert "Proj1" in result.stdout

def test_add_and_list_task(tmp_path):
    data_file = tmp_path / "data.json"
    # Add user and project first
    run_cli(["add_user", "--name", "TestUser", "--email", "test@ex.com"], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        user_id = data["users"][0]["id"]
    run_cli([
        "add_project", "--title", "Proj1", "--description", "Desc", "--due-date", "2025-12-31", "--assigned-user-id", user_id
    ], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        project_id = data["projects"][0]["id"]
    # Add task with real project ID
    result = run_cli([
        "add_task", "--title", "Task1", "--assigned-to", project_id
    ], str(data_file))
    assert "Task Task1 added" in result.stdout
    # List tasks
    result = run_cli(["list_tasks"], str(data_file))
    assert "Task1" in result.stdout


def test_projects_by_user(tmp_path):
    data_file = tmp_path / "data.json"
    # Add user and project
    run_cli(["add_user", "--name", "TestUser", "--email", "test@ex.com"], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        user_id = data["users"][0]["id"]
    run_cli([
        "add_project", "--title", "Proj1", "--description", "Desc", "--due-date", "2025-12-31", "--assigned-user-id", user_id
    ], str(data_file))
    # Test projects_by_user
    result = run_cli(["projects_by_user", "--user-id", user_id], str(data_file))
    assert "Projects for TestUser" in result.stdout
    assert "Proj1" in result.stdout


def test_tasks_by_project(tmp_path):
    data_file = tmp_path / "data.json"
    # Add user, project, and task
    run_cli(["add_user", "--name", "TestUser", "--email", "test@ex.com"], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        user_id = data["users"][0]["id"]
    run_cli([
        "add_project", "--title", "Proj1", "--description", "Desc", "--due-date", "2025-12-31", "--assigned-user-id", user_id
    ], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        project_id = data["projects"][0]["id"]
    run_cli([
        "add_task", "--title", "Task1", "--assigned-to", project_id
    ], str(data_file))
    # Test tasks_by_project
    result = run_cli(["tasks_by_project", "--project-id", project_id], str(data_file))
    assert "Tasks for Project Proj1" in result.stdout
    assert "Task1" in result.stdout

def test_complete_task(tmp_path):
    data_file = tmp_path / "data.json"
    # Add user, project, and task
    run_cli(["add_user", "--name", "TestUser", "--email", "test@ex.com"], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        user_id = data["users"][0]["id"]
    run_cli([
        "add_project", "--title", "Proj1", "--description", "Desc", "--due-date", "2025-12-31", "--assigned-user-id", user_id
    ], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        project_id = data["projects"][0]["id"]
    run_cli([
        "add_task", "--title", "Task1", "--assigned-to", project_id
    ], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        task_id = data["tasks"][0]["id"]
    # Complete the task
    result = run_cli(["complete_task", "--task-id", task_id], str(data_file))
    assert "marked as completed" in result.stdout
    # Check status is now Completed
    with open(data_file) as f:
        data = json.load(f)
        assert data["tasks"][0]["status"] == "Completed"

def test_list_pending_tasks(tmp_path):
    data_file = tmp_path / "data.json"
    # Add user, project, and two tasks
    run_cli(["add_user", "--name", "TestUser", "--email", "test@ex.com"], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        user_id = data["users"][0]["id"]
    run_cli([
        "add_project", "--title", "Proj1", "--description", "Desc", "--due-date", "2025-12-31", "--assigned-user-id", user_id
    ], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        project_id = data["projects"][0]["id"]
    run_cli([
        "add_task", "--title", "Task1", "--assigned-to", project_id
    ], str(data_file))
    run_cli([
        "add_task", "--title", "Task2", "--assigned-to", project_id
    ], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        task2_id = [t for t in data["tasks"] if t["title"] == "Task2"][0]["id"]
    # Complete Task2
    run_cli(["complete_task", "--task-id", task2_id], str(data_file))
    # List pending tasks
    result = run_cli(["list_pending_tasks"], str(data_file))
    assert "Task1" in result.stdout
    assert "Task2" not in result.stdout

def test_list_completed_tasks(tmp_path):
    data_file = tmp_path / "data.json"
    # Add user, project, and two tasks
    run_cli(["add_user", "--name", "TestUser", "--email", "test@ex.com"], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        user_id = data["users"][0]["id"]
    run_cli([
        "add_project", "--title", "Proj1", "--description", "Desc", "--due-date", "2025-12-31", "--assigned-user-id", user_id
    ], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        project_id = data["projects"][0]["id"]
    run_cli([
        "add_task", "--title", "Task1", "--assigned-to", project_id
    ], str(data_file))
    run_cli([
        "add_task", "--title", "Task2", "--assigned-to", project_id
    ], str(data_file))
    with open(data_file) as f:
        data = json.load(f)
        task2_id = [t for t in data["tasks"] if t["title"] == "Task2"][0]["id"]
    # Complete Task2
    run_cli(["complete_task", "--task-id", task2_id], str(data_file))
    # List completed tasks
    result = run_cli(["list_completed_tasks"], str(data_file))
    assert "Task2" in result.stdout
    assert "Task1" not in result.stdout
