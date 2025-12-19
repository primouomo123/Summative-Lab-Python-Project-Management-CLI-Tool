from datetime import datetime
from models.base import BaseModel
from models.user import User

class Project(BaseModel):
    all = []

    def __init__(self, title, description, due_date, assigned_user_id, id=None):
        super().__init__(id)
        self.title = title
        self.description = description
        self.due_date = due_date  # will trigger setter validation
        self.assigned_user_id = assigned_user_id
        Project.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        self._title = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("Description must be a string")
        self._description = value
    
    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, value):
        try:
            # Parse the date to make sure it's valid
            parsed_date = datetime.strptime(value, "%Y-%m-%d")
            self._due_date = value
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format")
    
    @property
    def assigned_user_id(self):
        return self._assigned_user_id
    
    @assigned_user_id.setter
    def assigned_user_id(self, value):
        if value not in User.get_user_ids():
            raise ValueError("Invalid user ID")
        self._assigned_user_id = value
    
    def get_all_projects_ids():
        return [p.id for p in Project.all]
