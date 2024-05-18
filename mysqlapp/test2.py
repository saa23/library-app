from app.models.borrows_model import database
# from app.models.customers_model import database as cust_db
from app.controllers.customers_controller import showUserByEmail
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime, requests

mysqldb = database()
# cust_db = cust_db()

# @jwt_required()
def inserts(**params):
    """
    In this process, token is required considered the security
    Thus, getting the payload from token
    """

    # payload = get_jwt_identity()      ### get token from JWT payload
    print(f'param = {payload}')
    # userId = cust_db.showUserByEmail(**payload)[0]
    userId = showUserByEmail(**payload)
    print(f'userId: {userId}')
    print(type(userId))
    print(f'userId: {userId.text}')
    # borrowdate = datetime.datetime.now().isoformat()
    # id = json.loads(json.dumps({'id' : params['bookid']}))
    # bookname = getBookById(id)['name']
    # params.update({
    #     'userid' : userId,
    #     'borrowdate' : borrowdate,
    #     'bookname' : bookname,
    #     'isactive' : 1
    #     })  
    # mysqldb.insertBorrow(**params)
    # mysqldb.dataCommit()
    return jsonify({'message' : 'Success'})
    # return jsonify({'msg':userId})
  


def getBookById(data):
    book_data = requests.get(url="http://localhost:8000/bookbyid", json=data)   ### url from books_router (managed using FastAPI and MongoDB)
    return json.loads(book_data.text)[0]


param = {'username': 'userkedua', 'email': 'shiroe.ishigami@gmail.com'}
userId: <Response 138 bytes [200 OK]>
<class 'flask.wrappers.Response'>