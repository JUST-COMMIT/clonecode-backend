import pymysql

from fastapi import FastAPI
from sqlalchemy.pool import QueuePool

from app.core.settings.app import AppSettings


def connect_to_db(app: FastAPI, settings: AppSettings) -> None:
    app.state.pool = QueuePool(
        lambda: pymysql.connect(
            host=settings.database_url,
            user=settings.database_user,
            password=settings.database_password,
            database=settings.database_schema,
        )
    )

def close_db_connection(app: FastAPI) -> None:
    app.state.pool.close()
