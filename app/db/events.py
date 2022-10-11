from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.init.settings.app import AppSettings


def create_sessionmaker(app: FastAPI, settings: AppSettings) -> None:
    app.state.engine = create_engine(url=settings.database_url)
    app.state.sessionmaker = sessionmaker(bind=app.state.engine)
