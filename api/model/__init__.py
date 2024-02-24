from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os


client = MongoClient(os.environ.get('MONGODB_URI'), server_api=ServerApi('1'))
db = client.get_database('renoti')