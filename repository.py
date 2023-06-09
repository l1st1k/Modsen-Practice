from fastapi.responses import JSONResponse
from fastapi import status
from services import get_data_from_csv, add_unique_ids

__all__ = (
    'ActionRepository',
)


class ActionRepository:
    @classmethod
    def fill_database(cls) -> JSONResponse:
        # TODO
        # Getting data from .csv
        df = get_data_from_csv('task/posts.csv')

        # Generate unique keys
        add_unique_ids(df)

        # Putting data into elastic
        # put_df_into_elastic(df)

        # Putting data into database
        # put_df_into_db(db)

        response = JSONResponse(
            content={
                "message": f"Database successfully filled with test data",
            },
            status_code=status.HTTP_200_OK)
        return response

    @classmethod
    def clear_database(cls) -> JSONResponse:
        # TODO
        # Elastic clearance
        # Database clearance
        response = JSONResponse(
            content={
                "message": f"Database successfully cleared!",
            },
            status_code=status.HTTP_200_OK)
        return response
