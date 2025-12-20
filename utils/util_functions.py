from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_from_json, save_to_json
from datetime import datetime
from rich.console import Console
from rich.table import Table

# Function to get all users
def all_users():
    return load_from_json("data/data.json")["users"]

#function to get all projects
def all_projects():
    return load_from_json("data/data.json")["projects"]

# Function to get all tasks
def all_tasks():
    return load_from_json("data/data.json")["tasks"]


# ---------- USERS FUNCTIONS FOR THE COMMANDS ----------
# Add user function
def add_user(args, console: Console):
    """Function to add a new user"""
    # Validate name is a string
    if not isinstance(args.name, str):
        console.print(f"[red]Error: Name must be a string.[/red]")
        return
    # Validate email is a string
    if not isinstance(args.email, str):
        console.print(f"[red]Error: Email must be a string.[/red]")
        return
    # Validate email format
    import re
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, args.email):
        console.print(f"[red]Error: Email '{args.email}' is not a valid email address.[/red]")
        return

    user = next((u for u in all_users() if u["name"] == args.name), None)
    if user:
        console.print(f"[yellow]User with name {args.name} already exists. The user id is {user['id']}[/yellow]")
    else:
        new_user = User(args.name, args.email)
        data = load_from_json("data/data.json")
        data["users"].append(new_user.to_dict())
        save_to_json("data/data.json", data)
        console.print(f"[green]✅ User {args.name} added with ID {new_user.id}[/green]")

# List users function
def list_users(args, console: Console):
    """Function to list all users"""
    users = all_users()
    if not users:
        console.print("[yellow]No users found.[/yellow]")
        return
    table = Table(title="List of Users")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Email")
    for user in users:
        table.add_row(user['id'], user['name'], user['email'])
    console.print(table)

# Projects by user function
def projects_by_user(args, console: Console):
    """Function to get projects by user ID"""
    user = next((u for u in all_users() if u["id"] == args.user_id), None)
    if not user:
        console.print(f"[red]Error: User ID {args.user_id} does not exist.[/red]")
        return
    if not all_projects():
        console.print("[yellow]No projects found.[/yellow]")
        return
    projects_found = [p for p in all_projects() if p["assigned_user_id"] == args.user_id]
    if not projects_found:
        console.print(f"[yellow]No projects found for {user['name']} with user ID {args.user_id}.[/yellow]")
        return
    table = Table(title=f"Projects for {user['name']} (ID: {args.user_id})")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Due Date")
    for project in projects_found:
        table.add_row(project['id'], project['title'], project['due_date'])
    console.print(table)


# ---------- PROJECTS FUNCTIONS FOR THE COMMANDS ----------
# Add project function
def add_project(args, console: Console):
    """Function to add a new project"""
    # Validate title
    if not isinstance(args.title, str) or not args.title.strip():
        console.print(f"[red]Error: Title must be a non-empty string.[/red]")
        return
    # Validate description
    if not isinstance(args.description, str):
        console.print(f"[red]Error: Description must be a string.[/red]")
        return
    # Validate due-date using datetime
    if not isinstance(args.due_date, str):
        console.print(f"[red]Error: Due date must be a string in YYYY-MM-DD format.[/red]")
        return
    try:
        datetime.strptime(args.due_date, "%Y-%m-%d")
    except ValueError:
        console.print(f"[red]Error: Due date must be a valid date in YYYY-MM-DD format.[/red]")
        return
    # Validate assigned_user_id
    if not isinstance(args.assigned_user_id, str):
        console.print(f"[red]Error: Assigned user ID must be a string.[/red]")
        return
    user_ids = [u["id"] for u in all_users()]
    if args.assigned_user_id not in user_ids:
        console.print(f"[red]Error: User ID {args.assigned_user_id} does not exist.[/red]")
        return
    project = next((p for p in all_projects() if p["title"] == args.title and p["assigned_user_id"] == args.assigned_user_id), None)
    if project:
        console.print(f"[yellow]Project with title {args.title} already exists for the user. The project id is {project['id']}[/yellow]")
        return
    new_project = Project(args.title, args.description, args.due_date, args.assigned_user_id)
    data = load_from_json("data/data.json")
    data["projects"].append(new_project.to_dict())
    save_to_json("data/data.json", data)
    console.print(f"[green]✅ Project {args.title} added with ID {new_project.id}[/green]")

# List projects function
def list_projects(args, console: Console):
    """Function to list all projects"""
    projects = all_projects()
    if not projects:
        console.print("[yellow]No projects found.[/yellow]")
        return
    table = Table(title="List of Projects")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Due Date")
    table.add_column("Assigned User ID")
    for project in projects:
        table.add_row(project['id'], project['title'], project['due_date'], project['assigned_user_id'])
    console.print(table)

# Tasks by project function
def tasks_by_project(args, console: Console):
    """Function to get tasks by project ID"""
    project = next((p for p in all_projects() if p["id"] == args.project_id), None)
    if not all_tasks():
        console.print("[yellow]No tasks found.[/yellow]")
        return
    tasks_found = [t for t in all_tasks() if t["assigned_to"] == args.project_id]
    if not tasks_found:
        console.print(f"[yellow]No tasks found for Project {project['title']} with ID {args.project_id}.[/yellow]")
        return
    table = Table(title=f"Tasks for Project {project['title']} (ID: {args.project_id})")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")
    for task in tasks_found:
        table.add_row(task['id'], task['title'], task['status'])
    console.print(table)

# ---------- TASKS FUNCTIONS FOR THE COMMANDS ----------
# Add task function
def add_task(args, console: Console):
    """Function to add a new task"""
    # Validate title
    if not isinstance(args.title, str) or not args.title.strip():
        console.print(f"[red]Error: Title must be a non-empty string.[/red]")
        return
    # Validate assigned_to
    if not isinstance(args.assigned_to, str):
        console.print(f"[red]Error: Assigned to (project ID) must be a string.[/red]")
        return
    project_ids = [p["id"] for p in all_projects()]
    if args.assigned_to not in project_ids:
        console.print(f"[red]Error: Project ID {args.assigned_to} does not exist.[/red]")
        return
    task = next((t for t in all_tasks() if t["title"] == args.title and t["assigned_to"] == args.assigned_to), None)
    if task:
        console.print(f"[yellow]Task with title {args.title} already exists for the project. The task id is {task['id']}[/yellow]")
        return
    new_task = Task(args.title, args.assigned_to)
    data = load_from_json("data/data.json")
    data["tasks"].append(new_task.to_dict())
    save_to_json("data/data.json", data)
    console.print(f"[green]✅ Task {args.title} added with ID {new_task.id}[/green]")

# List tasks function
def list_tasks(args, console: Console):
    """Function to list all tasks"""
    tasks = all_tasks()
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return
    table = Table(title="List of Tasks")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")
    table.add_column("Assigned To Project ID")
    for task in tasks:
        table.add_row(task['id'], task['title'], task['status'], task['assigned_to'])
    console.print(table)

# Complete task function
def complete_task(args, console: Console):
    """Function to mark a task as completed"""
    data = load_from_json("data/data.json")
    task = next((t for t in data["tasks"] if t["id"] == args.task_id), None)

    if not task:
        console.print(f"[red]Error: Task ID {args.task_id} does not exist.[/red]")
        return
    if task["status"] == "Completed":
        console.print(f"[yellow]Task ID {args.task_id} is already completed.[/yellow]")
        return
    task["status"] = "Completed"
    save_to_json("data/data.json", data)
    console.print(f"[green]✅ Task ID {args.task_id} marked as completed.[/green]")

def list_pending_tasks(args, console: Console):
    """Function to list all pending tasks"""
    tasks = all_tasks()
    pending_tasks = [t for t in tasks if t["status"] == "Pending"]
    if not pending_tasks:
        console.print("[yellow]No pending tasks found.[/yellow]")
        return
    table = Table(title="List of Pending Tasks")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Assigned To Project ID")
    for task in pending_tasks:
        table.add_row(task['id'], task['title'], task['assigned_to'])
    console.print(table)

def list_completed_tasks(args, console: Console):
    """Function to list all completed tasks"""
    tasks = all_tasks()
    completed_tasks = [t for t in tasks if t["status"] == "Completed"]
    if not completed_tasks:
        console.print("[yellow]No completed tasks found.[/yellow]")
        return
    table = Table(title="List of Completed Tasks")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Assigned To Project ID")
    for task in completed_tasks:
        table.add_row(task['id'], task['title'], task['assigned_to'])
    console.print(table)