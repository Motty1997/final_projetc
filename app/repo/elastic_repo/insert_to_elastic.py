from typing import List, Dict
from app.db.elastic.database import create_index
from app.settings.elastic_config import elastic_client


def insert_many_descriptions(description:List[Dict[str,str]]) -> None:
    create_index("events")
    try:
        for x in description:
            elastic_client.index(index="events", body=x)
    except Exception as e:
        print(e)
