import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    JSON_SORT_KEYS = False
    base_dir = os.path.abspath(os.path.dirname(__file__))
    JWT_SECRET_KEY = os.getenv("JWT_SECRET")
    HOST = os.getenv('HOST')
    DB = os.getenv('DB')
    USER = os.getenv('USER')
    PW = os.getenv('PW')
    PORT = os.getenv('PORT')