import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch


load_dotenv(verbose=True)

cloud_id =  os.environ['CLOUD_ID']
user_name = os.environ['USER_NAME']
password = os.environ['PASSWORD']

# יצירת חיבור
elastic_client = Elasticsearch(
    cloud_id=cloud_id,
    basic_auth=(user_name, password)
)
