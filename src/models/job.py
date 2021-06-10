from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from src.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    source = Column(String)
    header = Column(String)
    content = Column(String)
    language = Column(String)
    experience = Column(String)
    employment_time = Column(String)
    poster = Column(String)
    application_link = Column(String)
    company_name = Column(String)
    location = Column(String)
    deadline = Column(String)
    community_only = Column(String)
    contact_name = Column(String)



