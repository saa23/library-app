from app.models.borrows_model import database
from app.models.customers_model import database as cust_db
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime, requests

mysqldb = database()
cust_db = cust_db()

@jwt_required()
def shows():
    # getting the payload from token
    params = get_jwt_identity()
    dbresult = mysqldb.showBorrowByEmail(**params)
    result = []
    if dbresult is not None:
        for item in dbresult:
            id = json.loads(json.dumps({'id' : item[4]}))
            bookdetail = getBookById(id)
            user = {
                'username' : item[0],
                'borrowid' : item[1],
                'borrowdate' : item[2],
                'bookid' : item[4],
                'bookname' : item[5],
                'author' : bookdetail['author'],
                'releaseyear' : bookdetail['releaseyear'],
                'genre' : bookdetail['genre']
            }
            result.append(user)
    else:
        result = dbresult
    return jsonify(result)


@jwt_required()
def insert(**params):
    token = get_jwt_identity()
    userId = cust_db.showUserByEmail(**token)[0]
    borrowdate = datetime.datetime.now().isoformat()
    id = json.loads(json.dumps({'id' : params['bookid']}))
    bookname = getBookById(id)['name']
    params.update({
        'userid' : userId,
        'borrowdate' : borrowdate,
        'bookname' : bookname,
        'isactive' : 1
        })  
    mysqldb.insertBorrow(**params)
    mysqldb.dataCommit()
    return jsonify({'message' : 'Success'})
  
@jwt_required()
def changeStatus(**params):
    mysqldb.updateBorrow(**params)
    mysqldb.dataCommit()
    return jsonify({'message' : 'Success'})

def getBookById(data):
    book_data = requests.get(url="http://localhost:8000/bookbyid", json=data)
    return json.loads(book_data.text)