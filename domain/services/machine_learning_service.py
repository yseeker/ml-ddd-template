from src.infrastructure.adapters.ml_api_adapter import MLApiAdapter
from src.infrastructure.repositories.ml_model_repository import MLModelRepository
from src.domain.aggregates.ml_model import MLModel
from src.domain.value_objects.model_type import ModelType

class MachineLearningService:
    def __init__(self, ml_api_adapter: MLApiAdapter, ml_model_repository: MLModelRepository):
        self.ml_api_adapter = ml_api_adapter
        self.ml_model_repository = ml_model_repository

    def train_model(self, model_type: str, X, y, test_size: float = 0.2) -> MLModel:
        model_type = ModelType(model_type)
        trained_model = self.ml_api_adapter.train_model(model_type, X, y, test_size)
        ml_model = MLModel(None, model_type, trained_model)
        saved_ml_model = self.ml_model_repository.save(ml_model)
        return saved_ml_model

    def predict(self, model_id: int, X):
        ml_model = self.ml_model_repository.get(model_id)
        y_pred = self.ml_api_adapter.predict(ml_model.trained_model, X)
        return y_pred