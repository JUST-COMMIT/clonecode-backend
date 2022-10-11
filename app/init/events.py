from typing import Callable
from fastapi import FastAPI

from app.init.settings.app import AppSettings
from app.db.events import create_sessionmaker


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    def start_app() -> None:
        create_sessionmaker(app, settings)
    return start_app
