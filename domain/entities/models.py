from typing import Any

class MLModel:
    def __init__(self, id: str, model: Any):
        self.id = id
        self.model = model