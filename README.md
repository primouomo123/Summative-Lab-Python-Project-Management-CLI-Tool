# Project Management CLI Tool

This CLI tool helps you manage users, projects, and tasks, storing all data in a JSON file.

## Setup

1. **Install Python 3**  
  Make sure Python 3 is installed on your system.

2. **Create and activate a virtual environment (recommended)**
  Using pipenv:
  ```bash
  pipenv install
  pipenv shell
  ```

3. **Install dependencies**  
  If you have dependencies, install them with:
  ```bash
  pip install -r requirements.txt
  ```

4. **Run the CLI**  
  From the project root directory:
  ```bash
  python main.py <command> [options]
  ```

## Commands & Usage

### User Commands
- **Add a user**
  ```bash
  python main.py add_user --name "Alice" --email "alice@example.com"
  ```
- **List all users**
  ```bash
  python main.py list_users
  ```
- **List projects by user**
  ```bash
  python main.py projects_by_user --user-id <USER_ID>
  ```

### Project Commands
- **Add a project**
  ```bash
  python main.py add_project --title "Project X" --description "Desc" --due-date "2025-12-31" --assigned-user-id <USER_ID>
  ```
- **List all projects**
  ```bash
  python main.py list_projects
  ```

### Task Commands
- **Add a task**
  ```bash
  python main.py add_task --title "Task 1" --assigned-to <PROJECT_ID>
  ```
- **List all tasks**
  ```bash
  python main.py list_tasks
  ```
- **List tasks by project**
  ```bash
  python main.py tasks_by_project --project-id <PROJECT_ID>
  ```
- **Mark a task as completed**
  ```bash
  python main.py complete_task --task-id <TASK_ID>
  ```
- **List pending tasks**
  ```bash
  python main.py list_pending_tasks
  ```
- **List completed tasks**
  ```bash
  python main.py list_completed_tasks
  ```

## Notes
- All data is stored in `data/data.json`.
- User, project, and task IDs are auto-generated.
- Make sure to use valid IDs when assigning users or projects.
- Task status can be `Pending` or `Completed`.

---
