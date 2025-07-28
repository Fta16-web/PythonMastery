from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1450, le=2025)


class BookResponse(BaseModel):
    title: str
    author: str
