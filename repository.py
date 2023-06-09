from fastapi.responses import JSONResponse
from fastapi import status

__all__ = (
    'ActionRepository',
)


class ActionRepository:
    @classmethod
    def fill_database(cls) -> JSONResponse:
        # TODO
        # Getting data from .csv
        # Putting data into elastic
        # Putting data into database
        response = JSONResponse(
            content={
                "message": f"Database successfully filled with test data",
            },
            status_code=status.HTTP_200_OK)
        return response
