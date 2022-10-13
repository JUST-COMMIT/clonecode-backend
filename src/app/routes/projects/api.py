from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.app.dependencies.rdb_session import db
from src.app.models.tbl_projects import TblProjects
from src.app.routes.projects.domain_model import ProjectCreateRequest, ProjectListResponse

router = APIRouter()


@router.post("/projects", status_code=201)
def create_project(project: ProjectCreateRequest, session: Session = Depends(db.get_session)):
    project = TblProjects(
        name=project.name
    )
    session.add(project)
    session.commit()

    return {}


@router.get('/projects', response_model=ProjectListResponse)
def get_projects(session: Session = Depends(db.get_session)) -> ProjectListResponse:
    projects = session.scalars(select(TblProjects)).all()

    return ProjectListResponse(data=[
        ProjectListResponse.Project(id=project.id, name=project.name) for project in
        projects
    ])
