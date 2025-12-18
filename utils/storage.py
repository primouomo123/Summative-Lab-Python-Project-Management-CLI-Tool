from models.user import User
from models.project import Project
from models.task import Task

import json

def save_to_json(file_path):
    data = {
        "users": [u.to_dict() for u in User.all_by_id.values()],
        "projects": [p.to_dict() for p in Project.all_by_id.values()],
        "tasks": [t.to_dict() for t in Task.all_by_id.values()]
    }
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def load_from_json(file_path):
    with open(file_path) as f:
        data = json.load(f)

    # Clear current data
    User.all_by_id.clear()
    Project.all_by_id.clear()
    Task.all_by_id.clear()

    # Load users
    for u in data.get("users", []):
        User.from_dict(u)
    # Load projects
    for p in data.get("projects", []):
        Project.from_dict(p)
    # Load tasks
    for t in data.get("tasks", []):
        Task.from_dict(t)