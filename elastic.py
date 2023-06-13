import pandas as pd
from elasticsearch import AsyncElasticsearch

__all__ = (
    'put_df_into_elastic',
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
