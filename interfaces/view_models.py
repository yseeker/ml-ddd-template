from pydantic import BaseModel
import numpy as np

class TrainModelInput(BaseModel):
    model_type: str
    X: list[list[float]]
    y: list[float]
    test_size: float = 0.2

class PredictModelInput(BaseModel):
    model_id: int
    X: list[list[float]]

class MLModelResponse(BaseModel):
    id: int
    model_type: str
    accuracy: float = None
    y_pred: list[int] = None