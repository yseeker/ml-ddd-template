from src.domain.value_objects.model_type import ModelType

class MLModel:
    def __init__(self, model_id: int, model_type: ModelType, trained_model):
        self.model_id = model_id
        self.model_type = model_type
        self.trained_model = trained_model