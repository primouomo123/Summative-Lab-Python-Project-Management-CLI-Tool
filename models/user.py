from models.base import BaseModel

class User(BaseModel):
    all = []

    def __init__(self, name, email, id=None):
        super().__init__(id)  # auto-generate id if None
        self.name = name
        self.email = email
        User.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Email must be a valid email address")
        self._email = value
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }