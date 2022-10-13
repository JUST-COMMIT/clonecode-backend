from sqlalchemy import Column, Integer, String, DateTime, func

from app.models import Base


class TblProjects(Base):
    __tablename__ = "tbl_projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
