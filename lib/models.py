import uuid

# Base model class for all models in the application (to include an ID in all of them)
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
    
    def to_dict(self):
        return self.__dict__