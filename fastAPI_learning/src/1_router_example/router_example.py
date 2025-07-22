from fastapi import APIRouter

router = APIRouter()


@router.get("/items/")  # decorator for defining a route
async def read_item(item_id: int = None):
    if item_id is None:
        return {"items": "all_items are here"}
    return {"item_id": item_id, "description": "This is an item.", "tags": ["items"]}


"""
decorator tells FastAPI
that this function will respond to GET requests at the /books/{book_id} path. {book_id} in
the path is a path parameter, which you can use to pass values dynamically. FastAPI automatically
extracts the book_id parameter and passes it to your function.
Notice the use of type hints (book_id: int). FastAPI uses these hints to perform data
validation. If a request is made with a non-integer book_id parameter, FastAPI automatically
sends a helpful error response.

"""
