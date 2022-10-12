from typing import Callable, Type
from fastapi import Depends, Request
from sqlalchemy.orm import Session, sessionmaker

from app.db.repositories.base import BaseRepository


def _get_sessionmaker(request: Request) -> sessionmaker:
    return request.app.state.sessionmaker

def _get_session(
    factory: sessionmaker = Depends(_get_sessionmaker),
) -> Session:
    with factory() as session:
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

def get_repository(
    repo_type: Type[BaseRepository],
) -> Callable[[Session], BaseRepository]:
    def _get_repo(
        session: Session = Depends(_get_session),
    ) -> BaseRepository:
        return repo_type(session)

    return _get_repo
