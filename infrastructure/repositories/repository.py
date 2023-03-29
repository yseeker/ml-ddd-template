import pickle
from src.domain.entities.models import MLModel

class MLModelRepository:
    def __init__(self, storage_path: str):
        self.storage_path = storage_path

    def save(self, ml_model: MLModel) -> None:
        file_path = f"{self.storage_path}/{ml_model.id}.pkl"
        with open(file_path, 'wb') as f:
            pickle.dump(ml_model.model, f)

    def load(self, model_id: str) -> MLModel:
        file_path = f"{self.storage_path}/{model_id}.pkl"
        try:
            with open(file_path, 'rb') as f:
                model = pickle.load(f)
            return MLModel(model_id, model)
        except FileNotFoundError:
            raise ValueError(f"Model with ID {model_id} not found")