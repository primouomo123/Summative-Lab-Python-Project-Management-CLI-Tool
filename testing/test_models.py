import pytest
from models.user import User
from models.project import Project
from models.task import Task

class TestUser:
    def test_create_user_valid(self):
        user = User("Alice", "alice@example.com")
        assert user.name == "Alice"
        assert user.email == "alice@example.com"
        assert user.id is not None

    def test_create_user_invalid_name(self):
        with pytest.raises(ValueError):
            User("", "alice@example.com")

    def test_create_user_invalid_email(self):
        with pytest.raises(ValueError):
            User("Alice", "aliceatexample.com")

class TestProject:
    def test_create_project_valid(self):
        project = Project("Proj1", "Desc", "2025-12-31", "user1")
        assert project.title == "Proj1"
        assert project.description == "Desc"
        assert project.due_date == "2025-12-31"
        assert project.assigned_user_id == "user1"
        assert project.id is not None

    def test_create_project_invalid_date(self):
        with pytest.raises(ValueError):
            Project("Proj1", "Desc", "31-12-2025", "user1")

    def test_create_project_invalid_title(self):
        with pytest.raises(ValueError):
            Project(123, "Desc", "2025-12-31", "user1")

class TestTask:
    def test_create_task_valid(self):
        task = Task("Task1", "proj1")
        assert task.title == "Task1"
        assert task.status == "Pending"
        assert task.assigned_to == "proj1"
        assert task.id is not None

    def test_create_task_invalid_title(self):
        with pytest.raises(ValueError):
            Task(123, "proj1")

    def test_set_invalid_status(self):
        task = Task("Task1", "proj1")
        with pytest.raises(ValueError):
            task.status = "Unknown"

    def test_create_task_invalid_assigned_to(self):
        with pytest.raises(ValueError):
            Task("Task1", 123)
