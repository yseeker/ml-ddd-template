from src.domain.services.machine_learning_service import MachineLearningService
from src.infrastructure.adapters.ml_api_adapter import MLApiAdapter
from src.infrastructure.repositories.ml_model_repository import MLModelRepository

class PredictWithModelUseCase:
    def __init__(self):
        self.ml_service = MachineLearningService(MLApiAdapter(), MLModelRepository())

    def execute(self, model_id: int, X):
        y_pred = self.ml_service.predict(model_id, X)
        return y_pred