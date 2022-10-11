from fastapi import FastAPI
from typing import Callable

from app.core.settings.app import AppSettings
from app.db.events import connect_to_db, close_db_connection


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    def start_app() -> None:
        connect_to_db(app, settings)
    return start_app

def create_stop_app_handler(
    app: FastAPI,
) -> Callable:
    def stop_app() -> None:
        close_db_connection(app)
    return stop_app
