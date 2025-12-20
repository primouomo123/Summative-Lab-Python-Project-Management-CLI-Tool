# Project Management CLI Tool

A command-line tool for managing users, projects, and tasks. This tool allows you to add, list, and query users, projects, and tasks, as well as mark tasks as completed and filter by status.

## Features
- Add and list users
- Add and list projects
- Add and list tasks
- List projects by user
- List tasks by project
- Mark tasks as completed
- List pending and completed tasks

## Requirements
- Python 3.12+
- Install dependencies with pip or pipenv (see below)

## Installation

1. **Clone the repository** (if not already):
   ```sh
   git clone <repo-url>
   cd Summative-Lab-Python-Project-Management-CLI-Tool
   ```

2. **Install dependencies**:
   - With pip:
     ```sh
     pip install -r requirements.txt
     ```
   - Or with pipenv:
     ```sh
     pipenv install
     pipenv shell
     ```

## Usage

Run the CLI tool with:
```sh
python main.py <command> [options]
```

### User Commands
- Add a user:
  ```sh
  python main.py add_user --name "Alice" --email "alice@example.com"
  ```
- List all users:
  ```sh
  python main.py list_users
  ```
- List projects by user:
  ```sh
  python main.py projects_by_user --user-id <USER_ID>
  ```

### Project Commands
- Add a project:
  ```sh
  python main.py add_project --title "Project X" --description "Desc" --due-date 2025-12-31 --assigned-user-id <USER_ID>
  ```
- List all projects:
  ```sh
  python main.py list_projects
  ```

### Task Commands
- Add a task:
  ```sh
  python main.py add_task --title "Task 1" --assigned-to <PROJECT_ID>
  ```
- List all tasks:
  ```sh
  python main.py list_tasks
  ```
- List tasks by project:
  ```sh
  python main.py tasks_by_project --project-id <PROJECT_ID>
  ```
- Mark a task as completed:
  ```sh
  python main.py complete_task --task-id <TASK_ID>
  ```
- List pending tasks:
  ```sh
  python main.py list_pending_tasks
  ```
- List completed tasks:
  ```sh
  python main.py list_completed_tasks
  ```

## Data Storage
- All data is stored in `data/data.json`.

## Testing
Run all tests with:
```sh
pytest
```

## License
MIT
