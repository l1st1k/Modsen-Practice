import pandas as pd
from elasticsearch import Elasticsearch

__all__ = (
    'put_df_into_elastic',
)

es = Elasticsearch('localhost:9200')
index_name = 'posts'


def put_df_into_elastic(df: pd.DataFrame) -> None:
    for index, row in df.iterrows():
        document = {
            'id': row['id'],
            'text': row['text']
        }
        es.index(index=index_name, body=document)
