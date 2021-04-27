from fastapi import Depends, FastAPI

from app.config import Settings, get_settings

app = FastAPI()


@app.get("/")
async def base():
    return "hello world the app has been updated"


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
        "update": "The app has been updated"
    }
