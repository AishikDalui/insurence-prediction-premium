from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        example="High"
    )

    confidence: float = Field(
        ...,
        example=0.36,
        description="Probability of the predicted category"
    )

    probabilities: Dict[str, float] = Field(
        ...,
        example={
            "High": 0.36,
            "Medium": 0.15,
            "Low": 0.49
        }
    )

    model_version: str = Field(
        ...,
        example="1.0.0"
    )
