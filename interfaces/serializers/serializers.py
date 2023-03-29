from pydantic import BaseModel
from src.domain.entities.models import MLModel


class MLModelResponse(BaseModel):
    id: str

    @classmethod
    def from_domain_model(cls, domain_model: MLModel):
        return cls(id=domain_model.id)