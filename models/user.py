from models.base import BaseModel
from models.project import Project

class User(BaseModel):
    all_by_id = {}

    def __init__(self, name, email, id=None):
        super().__init__(id)
        self.name = name
        self.email = email
        User.all_by_id[self.id] = self

    @property
    def projects(self):
        """Return all projects assigned to this user"""
        return [p for p in Project.all_by_id.values() if p.user_id == self.id]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"], email=data["email"], id=data["id"])