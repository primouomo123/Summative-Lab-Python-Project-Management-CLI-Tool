from models.base import Entity
from pydantic import EmailStr

class User(Entity):
    name: str
    email: EmailStr

    all = []

    def __init__(self, **data):
        super().__init__(**data)
        User.all.append(self)
    
    def all_projects(self):
        """Return all projects belonging to this user"""
        from models.project import Project
        return [project for project in Project.all if project.user_id == self.id]

    @classmethod
    def from_dict(cls, data: dict):
        return cls.model_validate(data)