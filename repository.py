from fastapi import status
from fastapi.responses import JSONResponse

from database import *
from elastic import *
from services import add_unique_ids, get_data_from_csv

__all__ = (
    'ActionRepository',
)


class ActionRepository:
    @classmethod
    async def fill_database(cls) -> JSONResponse:
        # Getting data from .csv
        df = get_data_from_csv('task/posts_9.csv')

        # Generate unique keys
        add_unique_ids(df)

        # Putting data into elastic
        await put_df_into_elastic(df)

        # Putting data into database
        await put_df_into_db(df)

        response = JSONResponse(
            content={
                "message": f"Database & Elastic index successfully filled with test data",
            },
            status_code=status.HTTP_201_CREATED)
        return response

    @classmethod
    async def clear_database(cls) -> JSONResponse:
        # Elastic clearance
        await clear_elastic_index()

        # Database clearance
        await clear_database_table()

        response = JSONResponse(
            content={
                "message": f"Database & Elastic index successfully cleared!",
            },
            status_code=status.HTTP_200_OK)
        return response

    @classmethod
    async def get_amount(cls) -> JSONResponse:
        index_name, amount_in_index = await get_index_count()
        table_name, amount_in_table = await get_table_count()

        response = JSONResponse(
            content={
                "elastic": f"index (name={index_name}) contains {amount_in_index} items!",
                "database": f"table (name={table_name}) contains {amount_in_table} items!",
            },
            status_code=status.HTTP_200_OK)
        return response

    @staticmethod
    async def search_posts(query: str) -> List_of_Posts:
        # TODO
        # Search for text in index and return their ids
        # Select posts from db with ORDER BY creation date , LIMIT = 20
        pass

    @staticmethod
    async def delete_by_id(post_id: str) -> JSONResponse:
        # TODO
        # Deletion from index
        await delete_post_by_id_from_elastic(post_id=post_id)

        # Deletion from database
        # await delete_post_by_id_from_database(post_id=post_id)

        response = JSONResponse(
            content="Post was successfully deleted!",
            status_code=status.HTTP_200_OK
        )
        return response
