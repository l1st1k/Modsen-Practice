from datetime import datetime
from typing import List, Tuple

import pandas as pd
from dotenv import dotenv_values
from fastapi import HTTPException
from sqlalchemy import func, desc
from sqlmodel import Field, Session, SQLModel, create_engine

__all__ = (
    'List_of_Posts',
    'put_df_into_db',
    'clear_database_table',
    'get_table_count',
    'delete_post_by_id_from_database',
    'select_posts_by_ids_from_db',
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


List_of_Posts = List[Posts]

postgresql_url = f"postgresql://{username}:{password}@localhost/{db}"
engine = create_engine(postgresql_url, echo=True)

# SQLModel.metadata.create_all(engine)


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


async def clear_database_table(table=Posts) -> None:
    with Session(engine) as session:
        session.query(table).delete()
        session.commit()


async def get_table_count(table=Posts) -> Tuple[str, int]:
    """Returns table_name & number of items in table"""
    with Session(engine) as session:
        count = session.query(func.count()).select_from(table).scalar()
        table_name = table.__tablename__
        return table_name, count


async def delete_post_by_id_from_database(post_id: str) -> None:
    with Session(engine) as session:
        post = session.query(Posts).filter(Posts.id == post_id).first()
        if post:
            session.delete(post)
            session.commit()
        else:
            raise HTTPException(
                status_code=404,
                detail='Post not found in database.'
            )


async def select_posts_by_ids_from_db(list_of_ids: List[str]) -> List_of_Posts:
    with Session(engine) as session:
        posts = (
            session.query(Posts)
            .filter(Posts.id.in_(list_of_ids))
            .order_by(desc(Posts.created_date))
            .limit(20)
            .all()
        )
        return posts
