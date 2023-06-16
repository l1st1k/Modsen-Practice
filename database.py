from datetime import datetime

import pandas as pd
from dotenv import dotenv_values
from sqlmodel import Field, Session, SQLModel, create_engine

__all__ = (
    'put_df_into_db'
)

# Env variables
config = dotenv_values(".env")
username = config["POSTGRES_USER"]
password = config["POSTGRES_PASSWORD"]
db = config["POSTGRES_DB"]


class Posts(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    text: str
    rubrics: str
    created_date: datetime


postgresql_url = f"postgresql://{username}:{password}@localhost/{db}"
engine = create_engine(postgresql_url, echo=True)

SQLModel.metadata.create_all(engine)


async def put_df_into_db(df: pd.DataFrame) -> None:
    with Session(engine) as session:
        for _, row in df.iterrows():
            post = Posts(
                id=row['id'],
                text=row['text'],
                rubrics=row['rubrics'],
                created_date=row['created_date']
            )
            session.add(post)
        session.commit()

