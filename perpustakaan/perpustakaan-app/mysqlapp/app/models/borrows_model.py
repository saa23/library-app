from mysql.connector import connect
from config import Config

class database:
    def __init__(self):
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