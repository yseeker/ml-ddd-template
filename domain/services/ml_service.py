import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.domain.entities.models import MLModel
from src.infrastructure.adapters.ml_api_adapter import MLApiAdapter
from src.infrastructure.storage.repository import MLModelRepository

class MachineLearningService:
    def __init__(self, ml_api_adapter: MLApiAdapter, ml_model_repository: MLModelRepository):
        self.ml_api_adapter = ml_api_adapter
        self.ml_model_repository = ml_model_repository

    def train_model(self, model_type: str, X: np.ndarray, y: np.ndarray, test_size: float = 0.2):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

        # Train the model
        model = self.ml_api_adapter.train_model(model_type, X_train, y_train)

        # Calculate the accuracy
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Save the trained model
        ml_model = MLModel(model_type=model_type, model=model, accuracy=accuracy)
        self.ml_model_repository.save(ml_model)

        return ml_model

    def predict(self, model_id: int, X: np.ndarray):
        ml_model = self.ml_model_repository.get(model_id)

        if ml_model is None:
            raise ValueError(f"No model found with the id: {model_id}")

        y_pred = ml_model.model.predict(X)

        return y_pred