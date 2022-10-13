from fastapi import FastAPI

from app.routes.projects.api import router as projects_router
from app.routes.users.api import router as users_router


def get_application() -> FastAPI:
    application = FastAPI()

    # App Routes
    application.include_router(users_router)
    application.include_router(projects_router)

    return application


app = get_application()
