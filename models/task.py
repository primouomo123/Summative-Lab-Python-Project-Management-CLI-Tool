from models.base import BaseModel

class Task(BaseModel):
    def __init__(self, title, status, assigned_to):
        all =[]
        status = ["Pending", "In Progress", "Completed"]

        super().__init__()
        self.title = title
        self.status = status
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
        if value not in Task.status:
            raise ValueError("Invalid status value")
        self._status = value
    

    def update_status(self, new_status):
        if new_status not in Task.status:
            raise ValueError("Invalid status value")
        self.status = new_status