import os
from dotenv import load_dotenv

load_dotenv("./.env")

# API
API_VERSION = os.environ["API_VERSION"]
API_PATH = os.environ["API_PATH"]
API_DOC = os.environ["API_DOC"]
SERVER_ROLE = os.environ["SERVER_ROLE"]
JWT_PUBLIC_KEY = os.environ["JWT_PUBLIC_KEY"]
HOST = os.environ["HOST"]

#### DATABASE ####
DATABASE_NAME = os.environ["DATABASE_NAME"]
DATABASE_SERVER = os.environ["DATABASE_SERVER"]
DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
DATABASE_PORT = os.environ["DATABASE_PORT"]