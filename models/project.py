from models.base import BaseModel
from models.user import User
from models.task import Task

class Project(BaseModel):
    all_by_id = {}

    def __init__(self, title, description, due_date, user_id, id=None):
        super().__init__(id)
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_id = user_id  # store User ID for JSON
        Project.all_by_id[self.id] = self

    @property
    def user(self):
        return User.all_by_id.get(self.user_id)

    @property
    def tasks(self):
        """Return all tasks belonging to this project"""
        return [t for t in Task.all_by_id.values() if t.project_id == self.id]

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_id": self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            user_id=data["user_id"],
            id=data["id"]
        )