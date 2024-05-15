from mysql.connector import connect
from config import Config

class database:
    def __init__(self):
        # if os.name == 'nt':
        #     print(os.getcwd())
        #     os.chdir("..\..")
        #     path_env = os.getcwd()+"\.env"
        # elif  os.name == 'posix':
        #     os.chdir("../..")
        #     path_env = os.getcwd()+"/.env"
        # print(path_env)
        # load_dotenv(path_env)

        try:
            self.db = connect(
                host= Config.HOST,
                database= Config.DB, 
                user= Config.USER,
                password= Config.PW
            )
        except Exception as e:
            print(e)

    def showBorrowByEmail(self, **params):
        cursor = self.db.cursor()
        query = '''
        SELECT
        customers.username, borrows.*
        FROM borrows
        INNER JOIN customers ON borrows.userid = customers.userid
        WHERE customers.email = "{0}" AND borrows.isactive = 1;
        '''.format(params['email'])
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insertBorrow(self, **params):
        column = ', '.join(list(params.keys()))
        values = tuple(list(params.values()))
        query = '''
        INSERT INTO borrows({0})
        VALUES {1};
        '''.format(column, values)
        print(query)
        cursor = self.db.cursor()
        cursor.execute(query)

    def updateBorrow(self, **params):
        borrowid = params['borrowid']
        query = '''
        UPDATE borrows
        SET isactive = 0 
        WHERE borrowid = {0};
        '''.format(borrowid)
        cursor = self.db.cursor()
        cursor.execute(query)

    def dataCommit(self):
        self.db.commit()


# versi ORM (next update)
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Index, Constraint,UniqueConstraint
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.dialects.mysql import TINYINT
# import datetime import datetime

# Base = declarative_base()

# class database:
#     def __init__(self):
#         engine = create_engine('mysql+mysqlconnector://root:12345@localhost:3306/perpustakaan_project', echo= False)
#         engine = create_engine('mysql+pymysql://root:12345@localhost:3306/perpustakaan_project', echo= False)
#         Session = sessionmaker(bind=engine)
#         self.session = Session()

# class borrows(Base):
#     __tablename__ = 'borrows'
#     borrowid = Column(Integer, primary_key=True)
#     borrowdate = Column(DateTime, default = datetime.utcnow, nullable=False)
#     userid = Column(Integer, ForeignKey("customers.userid"), nullable=False) 
#     bookid = Column(String, nullable=False)
#     bookname = Column(String)
#     isactive = Column(TINYINT)
#     Index(userid)
#     Constraint(userid)