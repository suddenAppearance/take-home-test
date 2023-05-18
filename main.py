from fastapi import FastAPI

from api.api_v1.api import router as api_v1
from settings import Settings

settings = Settings()

app = FastAPI(
    title=settings.SERVICE_NAME
)

app.include_router(api_v1, prefix="/api/v1")
