import uuid

class BaseModel:
    def __init__(self, id=None):
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id

    def to_dict(self):
        return self.__dict__.copy()