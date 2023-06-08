from datetime import datetime
from typing import List

from dotenv import dotenv_values
from sqlmodel import Field, SQLModel, create_engine

__all__ = (
    'engine',
)

# Env variables
config = dotenv_values(".env")
username = config["POSTGRES_USER"]
password = config["POSTGRES_PASSWORD"]
db = config["POSTGRES_DB"]


class Posts(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    text: str
    rubrics: List[str]
    created_date: datetime


postgresql_url = f"postgresql://{username}:{password}@localhost/{db}"
engine = create_engine(postgresql_url, echo=True)

SQLModel.metadata.create_all(engine)
