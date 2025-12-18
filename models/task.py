from models.base import BaseModel
from models.project import Project

class Task(BaseModel):
    all_by_id = {}

    def __init__(self, title, project_id, status="pending", id=None):
        super().__init__(id)
        self.title = title
        self.project_id = project_id  # store Project ID for JSON
        self.status = status
        Task.all_by_id[self.id] = self

    @property
    def project(self):
        return Project.all_by_id.get(self.project_id)

    @property
    def user(self):
        """Return the user assigned to this task through its project"""
        proj = self.project
        return proj.user if proj else None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "project_id": self.project_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            project_id=data["project_id"],
            status=data.get("status", "pending"),
            id=data["id"]
        )