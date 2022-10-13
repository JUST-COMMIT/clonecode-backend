from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.dependencies.rdb_session import db
from app.models.tbl_projects import TblProjects
from app.routes.projects.domain_model import ProjectCreateRequest, ProjectListResponse

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
def get_projects(session: Session = Depends(db.get_session)):
    projects = session.scalars(select(TblProjects)).all()

    return ProjectListResponse(data=[
        ProjectListResponse.Project(id=project.id, name=project.name) for project in
        projects
    ])
