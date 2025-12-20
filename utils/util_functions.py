from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_from_json, save_to_json

# Function to get all users
def all_users():
    return load_from_json("data/data.json")["users"]

#function to get all projects
def all_projects():
    return load_from_json("data/data.json")["projects"]

# Function to get all tasks
def all_tasks():
    return load_from_json("data/data.json")["tasks"]

# Add user function
def add_user(args):
    """Function to add a new user"""
    user = next((u for u in all_users() if u["name"] == args.name), None)

    if user:
        print(f"User with name {args.name} already exists. The user id is {user['id']}")
    else:
        new_user = User(args.name, args.email)
        data = load_from_json("data/data.json")
        data["users"].append(new_user.to_dict())
        save_to_json("data/data.json", data)
        print(f"✅ User {args.name} added with ID {new_user.id}")

# List users function
def list_users(args):
    """Function to list all users"""
    users = all_users()
    if not users:
        print("No users found.")
        return

    print("List of Users:\n")
    for user in users:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}\n")

# Projects by user function
def projects_by_user(user_id):
    user = next((u for u in all_users() if u["id"] == user_id), None)
    """Function to get projects by user ID"""
    if not all_projects():
        print("No projects found.")
        return
    projects_found = [p for p in all_projects() if p["assigned_user_id"] == user_id]
    if not projects_found:
        print(f"No projects found for {user['name']} with user ID {user_id}.")
        return
    print (f"Projects for {user['name']} with user ID {user_id}:\n")
    for project in projects_found:
        print(f"ID: {project['id']}, Title: {project['title']}, Due Date: {project['due_date']}\n")

# Add project function
def add_project(args):
    """Function to add a new project"""
    user_ids = [u["id"] for u in all_users()]
    if args.assigned_user_id not in user_ids:
        print(f"Error: User ID {args.assigned_user_id} does not exist.")
        return

    new_project = Project(args.title, args.description, args.due_date, args.assigned_user_id)
    data = load_from_json("data/data.json")
    data["projects"].append(new_project.to_dict())
    save_to_json("data/data.json", data)
    print(f"✅ Project {args.title} added with ID {new_project.id}")

# List projects function
def list_projects(args):
    """Function to list all projects"""
    projects = all_projects()
    if not projects:
        print("No projects found.")
        return

    print("List of Projects:\n")
    for project in projects:
        print(f"ID: {project['id']}, Title: {project['title']}, Due Date: {project['due_date']}, Assigned User ID: {project['assigned_user_id']}\n")

# Tasks by project function
def tasks_by_project(project_id):
    """Function to get tasks by project ID"""
    project = next((p for p in all_projects() if p["id"] == project_id), None)
    if not all_tasks():
        print("No tasks found.")
        return
    tasks_found = [t for t in all_tasks() if t["assigned_to"] == project_id]
    if not tasks_found:
        print(f"No tasks found for Project {project['title']} with ID {project_id}.")
        return
    print (f"Tasks for Project {project['title']} with ID {project_id}:\n")
    for task in tasks_found:
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}\n")

# Add task function
def add_task(args):
    """Function to add a new task"""
    project_ids = [p["id"] for p in all_projects()]
    if args.assigned_to not in project_ids:
        print(f"Error: Project ID {args.assigned_to} does not exist.")
        return
    new_task = Task(args.title, args.assigned_to)
    data = load_from_json("data/data.json")
    data["tasks"].append(new_task.to_dict())
    save_to_json("data/data.json", data)
    print(f"✅ Task {args.title} added with ID {new_task.id}")

# List tasks function
def list_tasks(args):
    """Function to list all tasks"""
    tasks = all_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("List of Tasks:\n")
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Assigned To Project ID: {task['assigned_to']}\n")

# Complete task function
def complete_task(task_id):
    """Function to mark a task as completed"""
    data = load_from_json("data/data.json")
    task = next((t for t in data["tasks"] if t["id"] == task_id), None)

    if not task:
        print(f"Error: Task ID {task_id} does not exist.")
        return

    if task["status"] == "Completed":
        print(f"Task ID {task_id} is already completed.")
        return

    task["status"] = "Completed"
    save_to_json("data/data.json", data)
    print(f"✅ Task ID {task_id} marked as completed.")

def list_pending_tasks(args):
    """Function to list all pending tasks"""
    tasks = all_tasks()
    pending_tasks = [t for t in tasks if t["status"] == "Pending"]
    if not pending_tasks:
        print("No pending tasks found.")
        return

    print("List of Pending Tasks:\n")
    for task in pending_tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Assigned To Project ID: {task['assigned_to']}\n")

def list_completed_tasks(args):
    """Function to list all completed tasks"""
    tasks = all_tasks()
    completed_tasks = [t for t in tasks if t["status"] == "Completed"]
    if not completed_tasks:
        print("No completed tasks found.")
        return

    print("List of Completed Tasks:\n")
    for task in completed_tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Assigned To Project ID: {task['assigned_to']}\n")