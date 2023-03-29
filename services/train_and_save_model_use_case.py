from src.domain.services.machine_learning_service import MachineLearningService
from src.infrastructure.adapters.ml_api_adapter import MLApiAdapter
from src.infrastructure.repositories.ml_model_repository import MLModelRepository

class TrainAndSaveModelUseCase:
    def __init__(self):
        self.ml_service = MachineLearningService(MLApiAdapter(), MLModelRepository())

    def execute(self, model_type: str, X, y, test_size: float = 0.2):
        ml_model = self.ml_service.train_model(model_type, X, y, test_size)
        return ml_model