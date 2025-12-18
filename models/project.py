from datetime import date, datetime
from models.base import Entity

class Project(Entity):
    title: str
    description: str
    due_date: date
    user_id: str  # ID of the User who owns this project

    # class-level list to store all instances
    all = []
    
    def __init__(self, **data):
        super().__init__(**data)
        Project.all.append(self)
    
    def all_tasks(self):
        """Return all tasks belonging to this project"""
        from models.task import Task
        return [task for task in Task.all if task.project_id == self.id]

    # Custom validation for due_date
    @property
    def due_date_str(self) -> str:
        """Return due date as a string"""
        return self.due_date.isoformat()

    @classmethod
    def from_dict(cls, data: dict):
        """Load from dict, converting due_date from string if necessary"""
        if "due_date" in data and isinstance(data["due_date"], str):
            data["due_date"] = datetime.strptime(data["due_date"], "%Y-%m-%d").date()
        return cls.model_validate(data)