# app/routes/webhook.py
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/webhook")
async def webhook_endpoint(request: Request):
    payload = await request.json()
    print(f"Webhook received: {payload}")
    return JSONResponse(
        content={"message": "Webhook received successfully"}, status_code=200
    )
