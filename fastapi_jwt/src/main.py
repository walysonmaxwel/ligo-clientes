import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from src.routers import jwt


load_dotenv()
app = FastAPI()
from . import routes
app.include_router(jwt.router)