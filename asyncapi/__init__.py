from fastapi import APIRouter, FastAPI
import asyncapi.view


def get_asyncapp(app: FastAPI):
    app_router = APIRouter()
    app_router.include_router(asyncapi.view.app, prefix="/api")
    app.include_router(app_router)
    return app
