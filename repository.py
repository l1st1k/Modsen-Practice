from fastapi import status
from fastapi.responses import JSONResponse

from elastic import get_index_count, put_df_into_elastic
from services import add_unique_ids, get_data_from_csv

__all__ = (
    'ActionRepository',
)


class ActionRepository:
    @classmethod
    async def fill_database(cls) -> JSONResponse:
        # TODO
        # Getting data from .csv
        df = get_data_from_csv('task/posts.csv')

        # Generate unique keys
        add_unique_ids(df)

        # Putting data into elastic
        await put_df_into_elastic(df)

        # Putting data into database
        # put_df_into_db(db)

        response = JSONResponse(
            content={
                "message": f"Database successfully filled with test data",
            },
            status_code=status.HTTP_200_OK)
        return response

    @classmethod
    async def clear_database(cls) -> JSONResponse:
        # TODO
        # Elastic clearance
        # Database clearance
        response = JSONResponse(
            content={
                "message": f"Database successfully cleared!",
            },
            status_code=status.HTTP_200_OK)
        return response

    @classmethod
    async def get_amount(cls) -> JSONResponse:
        index_name, amount = await get_index_count()
        response = JSONResponse(
            content={
                "message": f"Elastic index (name={index_name}) contains {amount} items!",
            },
            status_code=status.HTTP_200_OK)
        return response
