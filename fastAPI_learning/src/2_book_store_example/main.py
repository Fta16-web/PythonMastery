from fastapi import FastAPI, HTTPException
from scalar_fastapi import get_scalar_api_reference
from router_book import router_book
from starlette.responses import JSONResponse

app = FastAPI()

app.include_router(router_book)


# custom exception handler for HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "Oops! Something went wrong"},
    )


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
