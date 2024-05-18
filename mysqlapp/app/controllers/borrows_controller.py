from app.models.borrows_model import database
# from app.models.customers_model import database as cust_db
from app.controllers.customers_controller import showUserByEmail
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime, requests

mysqldb = database()
# cust_db = cust_db()

@jwt_required()
def shows():
    """
    In this process, token is required considered the security
    Thus, getting the payload from token
    """

    payload = get_jwt_identity()     ### get token from JWT payload
    dbresult = mysqldb.showBorrowByEmail(**payload)
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
def inserts(**params):
    """
    In this process, token is required considered the security
    Thus, getting the payload from token.

    template format body request:
    {"bookid":""}
    """

    payload = get_jwt_identity()      ### get token from JWT payload
    email_payload = payload['email']
    userdata_str = showUserByEmail(email = email_payload).get_data(as_text=True)
    userdata_json = json.loads(userdata_str)
    userId = userdata_json['userid']
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
    # return jsonify({'msg':userId})
  
@jwt_required()
def changeStatus(**params):
    """
    In this process, token is required considered the security
    Thus, getting the payload from token.

    template format body request:
    {"borrowid":""}

    But for better flow, it should be using user email and book id, and borrow date
    {
        "bookid":"",
        "email":"",
        "borrow date":""
    }
    """

    mysqldb.updateBorrow(**params)
    mysqldb.dataCommit()
    return jsonify({'message' : 'Success'})

def getBookById(data):
    book_data = requests.get(url="http://localhost:8000/bookbyid", json=data)   ### url from books_router (managed using FastAPI and MongoDB)
    return json.loads(book_data.text)[0]