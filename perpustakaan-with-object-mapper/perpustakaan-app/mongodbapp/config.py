import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    HOST = os.getenv('HOST')
    DB = os.getenv('DB')
    USER = os.getenv('USER')
    PORT = os.getenv('PORT')