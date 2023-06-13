from typing import Tuple

import pandas as pd
from elasticsearch import AsyncElasticsearch

__all__ = (
    'put_df_into_elastic',
    'get_index_count',
)

es = AsyncElasticsearch(
    [{
        'scheme': "http",
        'host': 'localhost',
        'port': 9200
      }]
)

index_name = 'posts'


async def put_df_into_elastic(df: pd.DataFrame) -> None:
    async with es:
        for index, row in df.iterrows():
            document = {
                'id': row['id'],
                'text': row['text']
            }
            await es.index(index=index_name, body=document)


async def get_index_count(name: str = index_name) -> Tuple[str, int]:
    """Returns index_name & number of items in index"""
    response = await es.count(index=name)
    return name, response['count']

