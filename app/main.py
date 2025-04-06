from fastapi import FastAPI
from .routers import todos
from . import models, database

app = FastAPI(
    title='APTZ Tasks Service',
    description='tasks api for the appointiz',
)
"""Create tables"""
models.Base.metadata.create_all(bind=database.engine)
"""Include routes"""
app.include_router(todos.router)
