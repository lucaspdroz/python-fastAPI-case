# app/routes/tiny_url.py
from fastapi import APIRouter, Request, Query
from fastapi.responses import JSONResponse
import pyshorteners

router = APIRouter()


# curl -X POST http://localhost:8000/tiny_url -H "Content-Type: application/json" -d '{"input_url": "https://www.google.com"}'


@router.post("/tiny_url")
async def question(request: Request):
    shortener = pyshorteners.Shortener()
    request_data = await request.json()

    if request_data and "input_url" in request_data:
        input_url = request_data["input_url"]
        tiny_url = shortener.tinyurl.short(input_url)
        return JSONResponse(
            content={"old_url": input_url, "tiny_url": tiny_url, "status": 200}
        )

    return JSONResponse(content={"error": "Invalid input"}, status_code=400)


# curl -X GET "http://localhost:8000/tiny_url_parameter?url=https://www.google.com"


@router.get("/tiny_url_parameter")
async def generate_tiny_url(url: str = Query(..., description="The URL to shorten")):
    shortener = pyshorteners.Shortener()

    try:
        tiny_url = shortener.tinyurl.short(url)
        return JSONResponse(
            content={"old_url": url, "tiny_url": tiny_url, "status": 200}
        )
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
