from fastapi import APIRouter
from models import Book, BookResponse
from typing import List

router_book = APIRouter()


@router_book.post("/books/", response_model=Book, tags=["books"])
async def create_book(book: Book):
    return {"title": book.title, "author": book.author, "year": book.year}


@router_book.get("/books/{book_id}", response_model=BookResponse, tags=["books"])
async def read_book(book_id: int) -> BookResponse:
    # Simulating a book retrieval from a database
    return BookResponse(title="Sample Book", author="Sample Author")


@router_book.get("/Allbooks", response_model=List[BookResponse], tags=["books"])
async def read_all_book() -> List[BookResponse]:
    # Simulating a list of book retrieval from a database
    return [
        {"title": "Sample Book", "author": "Sample Author"},
        {"title": "Another Book", "author": "Another Author"},
    ]
