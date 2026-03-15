from pydantic import BaseModel, Field, field_validator

class ReviewRequest(BaseModel):
    review: str = Field(..., min_length=3, max_length=1000)

    @field_validator("review")
    @classmethod
    def review_not_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Review cannot be empty or contain only spaces.")
        return value

class PredictionResponse(BaseModel):
    sentiment: str