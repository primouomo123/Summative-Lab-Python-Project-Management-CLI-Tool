# Project Management CLI Tool

A command-line tool for managing users, projects, and tasks. Data is stored in `data/data.json`.

## Requirements
- Python 3.12+
- Install dependencies with Pipenv or pip:
  - `pipenv install`  
  or
  - `pip install -r requirements.txt`

## Usage
Run the CLI tool from the project root:

```
python main.py <command> [options]
```

### User Commands
- **Add a user:**
  ```
  python main.py add_user --name "Alice" --email "alice@example.com"
  ```
- **List users:**
  ```
  python main.py list_users
  ```
- **List projects by user:**
  ```
  python main.py projects_by_user --user-id <USER_ID>
  ```

### Project Commands
- **Add a project:**
  ```
  python main.py add_project --title "Project X" --description "Desc" --due-date "YYYY-MM-DD" --assigned-user-id <USER_ID>
  ```
- **List projects:**
  ```
  python main.py list_projects
  ```

### Task Commands
- **Add a task:**
  ```
  python main.py add_task --title "Task 1" --assigned-to <PROJECT_ID>
  ```
- **List tasks:**
  ```
  python main.py list_tasks
  ```
- **List tasks by project:**
  ```
  python main.py tasks_by_project --project-id <PROJECT_ID>
  ```
- **Complete a task:**
  ```
  python main.py complete_task --task-id <TASK_ID>
  ```
- **List pending tasks:**
  ```
  python main.py list_pending_tasks
  ```
- **List completed tasks:**
  ```
  python main.py list_completed_tasks
  ```

## Data Persistence
All data is stored in `data/data.json`. The file is created automatically if it does not exist.

## Testing
To run tests (if available):
```
pytest
```

## Notes
- User, project, and task IDs are auto-generated.
- Make sure to use valid IDs when referencing users or projects.
