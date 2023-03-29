from pydantic import BaseModel
from src.domain.aggregates.ml_model import MLModel
from src.domain.value_objects.model_type import ModelType

class TrainModelInput(BaseModel):
    model_type: ModelType
    X: list
    y: list
    test_size: float = 0.2

class PredictModelInput(BaseModel):
    model_id: int
    X: list

class MLModelResponse(BaseModel):
    model_id: int
    model_type: ModelType
    y_pred: list = None

    @classmethod
    def from_domain_model(cls, ml_model: MLModel):
        return cls(
            model_id=ml_model.model_id,
            model_type=ml_model.model_type,
            y_pred=None
        )