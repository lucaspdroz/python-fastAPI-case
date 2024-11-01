# app/main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI

# Load environment variables from .env file
load_dotenv()

# Access environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

# Import and include routers
from app.routes import hello, tiny_url, webhook

app.include_router(hello.router)
app.include_router(webhook.router)
app.include_router(tiny_url.router)

# To run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
