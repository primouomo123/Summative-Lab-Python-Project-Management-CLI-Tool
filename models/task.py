from models.base import BaseModel

class Task(BaseModel):
    all = []
    ALLOWED_STATUSES = ["Pending", "Completed"]

    def __init__(self, title, assigned_to, id=None):
        super().__init__(id)
        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to
        Task.all.append(self)
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        self._title = value
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        if value not in Task.ALLOWED_STATUSES:
            raise ValueError("Invalid status value")
        self._status = value
    
    @property
    def assigned_to(self):
        return self._assigned_to
    @assigned_to.setter
    def assigned_to(self, value):
        if not isinstance(value, str):
            raise ValueError("Assigned to must be a string")
        self._assigned_to = value
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }