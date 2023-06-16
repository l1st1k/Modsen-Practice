from fastapi import status
from fastapi.responses import JSONResponse

from database import clear_database_table, get_table_count, put_df_into_db
from elastic import clear_elastic_index, get_index_count, put_df_into_elastic
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
