import uuid

class BaseModel:
    def __init__(self, id=None):
        self.id = id or str(uuid.uuid4())

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)