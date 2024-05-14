from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config

Base = declarative_base()

class database:
    def __init__(self):
        host = Config.HOST
        database = Config.DB
        user = Config.USER
        password = Config.PW
        port = Config.PORT
        # engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}', echo= False)
        
        
        ### pymysql connector supports for "caching_sha2_password"
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}', echo= False)
        Session = sessionmaker(bind=engine)
        self.session = Session()
 
        
class customers(Base):
    __tablename__ = 'customers'
    userid = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    UniqueConstraint(username,email)