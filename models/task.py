from models.base import Entity

class Task(Entity):
    title: str
    project_id: str  # ID of the Project this task belongs to
    status: str = "pending"  # default status

    # class-level list to store all instances
    all = []
    def __init__(self, **data):
        super().__init__(**data)
        Task.all.append(self)

    @classmethod
    def from_dict(cls, data: dict):
        """Load from dict"""
        return cls.model_validate(data)