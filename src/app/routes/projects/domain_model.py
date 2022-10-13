from pydantic import BaseModel


class ProjectCreateRequest(BaseModel):
    name: str


class ProjectListResponse(BaseModel):
    class Project(BaseModel):
        id: int
        name: str

    data: list[Project]
