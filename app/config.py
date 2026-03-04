# FastAPI Configuration Settings

from fastapi import FastAPI
from pydantic import BaseSettings

class Settings(BaseSettings):
    title: str = "Stock Analyzer"
    version: str = "1.0.0"
    description: str = "A FastAPI application for analyzing stock data"
    debug: bool = False
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
app = FastAPI(title=settings.title, version=settings.version, description=settings.description)

# Add more configurations or endpoints as needed