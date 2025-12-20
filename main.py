import argparse
from rich_argparse import RichHelpFormatter
from rich.console import Console
import utils.util_functions as util
console = Console()


def main():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool",
        formatter_class=RichHelpFormatter
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # ---------- USER COMMANDS ----------
    add_user_parser = subparsers.add_parser(
        "add_user",
        help="Add a new user"
    )
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=util.add_user)

    list_users_parser = subparsers.add_parser(
        "list_users",
        help="List all users"
    )
    list_users_parser.set_defaults(func=util.list_users)

    projects_by_user_parser = subparsers.add_parser(
        "projects_by_user",
        help="List projects by user ID"
    )
    projects_by_user_parser.add_argument("--user-id", required=True)
    projects_by_user_parser.set_defaults(func=util.projects_by_user)

    # ---------- PROJECT COMMANDS ----------
    add_project_parser = subparsers.add_parser(
        "add_project",
        help="Add a new project"
    )
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument("--due-date", required=True)
    add_project_parser.add_argument("--assigned-user-id", required=True)
    add_project_parser.set_defaults(func=util.add_project)

    list_projects_parser = subparsers.add_parser(
        "list_projects",
        help="List all projects"
    )
    list_projects_parser.set_defaults(func=util.list_projects)

    # ---------- TASK COMMANDS ----------
    add_task_parser = subparsers.add_parser(
        "add_task",
        help="Add a new task"
    )
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--assigned-to", required=True)
    add_task_parser.set_defaults(func=util.add_task)

    list_tasks_parser = subparsers.add_parser(
        "list_tasks",
        help="List all tasks"
    )
    list_tasks_parser.set_defaults(func=util.list_tasks)

    tasks_by_project_parser = subparsers.add_parser(
        "tasks_by_project",
        help="List tasks by project ID"
    )
    tasks_by_project_parser.add_argument("--project-id", required=True)
    tasks_by_project_parser.set_defaults(func=util.tasks_by_project)

    complete_task_parser = subparsers.add_parser(
        "complete_task",
        help="Mark a task as completed"
    )
    complete_task_parser.add_argument(
        "--task-id",
        required=True,
        help="Task ID to mark as completed"
    )
    complete_task_parser.set_defaults(func=util.complete_task)

    # ---------- ADDITIONAL TASK COMMANDS ----------
    list_pending_tasks_parser = subparsers.add_parser(
        "list_pending_tasks",
        help="List all pending tasks"
    )
    list_pending_tasks_parser.set_defaults(func=util.list_pending_tasks)

    list_completed_tasks_parser = subparsers.add_parser(
        "list_completed_tasks",
        help="List all completed tasks"
    )
    list_completed_tasks_parser.set_defaults(func=util.list_completed_tasks)

    # ---------- DISPATCH ----------
    args = parser.parse_args()
    args.func(args, console=console)


if __name__ == "__main__":
    main()