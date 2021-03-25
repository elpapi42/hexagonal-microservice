import os
import pathlib

from dotenv import load_dotenv


# Load .env vars
load_dotenv(pathlib.Path('.').parent/'.env')

MONGO_URL = os.getenv('MONGO_URL')
MONGO_DATABASE = os.getenv('MONGO_DATABASE')
