from fastapi import APIRouter, FastAPI
from starlette.staticfiles import StaticFiles
import myapp.view


def get_app(app: FastAPI):
    app_router = APIRouter()
    app_router.include_router(myapp.view.app, prefix="")
    # app = FastAPI()
    app.mount("/static",
              StaticFiles(directory="static"),
              name="static")
    app.include_router(app_router)
    return app
