import pandas as pd
from uuid import uuid4

__all__ = (
    'get_data_from_csv',
    'add_unique_ids',
)


def get_data_from_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def get_uuid() -> str:
    """Returns unique UUID (UUID4)"""
    return str(uuid4())


def add_unique_ids(df: pd.DataFrame) -> None:
    """Adding new column to df with unique IDs"""
    df['id'] = df.apply(lambda row: get_uuid(), axis=1)
