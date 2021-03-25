from fastapi import FastAPI

from source.tasks.infrastructure.controllers import router as tasks_router

def register(app:FastAPI):
    """Register all the routers in app."""
    app.include_router(tasks_router, prefix='/tasks', tags=['tasks'])
