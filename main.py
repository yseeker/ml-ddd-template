from fastapi import FastAPI
from src.interfaces.api.routers.ml_router import MLRouter

app = FastAPI()

app.include_router(MLRouter, prefix="/ml", tags=["ml"])