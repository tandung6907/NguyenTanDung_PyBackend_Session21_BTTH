from fastapi import FastAPI
from database import *
from routers import auth_router

Base.metadata.create_all(bind= engine)

app = FastAPI()
app.include_router(auth_router)