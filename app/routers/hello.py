# app/routes/hello.py
from fastapi import APIRouter,Query
from fastapi.responses import JSONResponse
from app.custom_annotatons.annotation import greet

router = APIRouter()

# http://localhost:8000/hello?name=

@router.get("/hello")
async def hello_world(name: str = Query(default=None, description="Name to greet")):
    # Check if the name is provided
    if not name:  # This checks for both None and empty string
        return JSONResponse(content={"error": "Query parameter 'name' is required."}, status_code=400)

    # Use the custom greeting function
    try:
        return JSONResponse(content={"message": name})
    except TypeError as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
