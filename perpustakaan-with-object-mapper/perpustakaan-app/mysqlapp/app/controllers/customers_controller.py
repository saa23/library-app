from app.models.customers_model import customers, database
from sqlalchemy import exc, delete, update
from flask import jsonify
from flask_jwt_extended import *
import datetime

db = database()

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row,column.name))
    return d

def shows():
    resultdb = db.session.query(customers).all()
    result = [row2dict(row) for row in resultdb]
    return jsonify(result)

def show(**params):
    resultdb = db.session.query(customers).filter(customers.userid == params['userid']).one()
    result = row2dict(resultdb)
    return jsonify(result)

def inserts(**params):
    try:
        db.session.add(customers(**params))
        db.session.commit() 
        return jsonify({"message" : "Inserting Success!"})
    except exc.IntegrityError as e: 
        # anticipating if inserting existing data in db
        db.session.rollback()
        print()
        return jsonify({"error data already exist in database" : "{}".format(e)})

def updates(**params):
    query_result = db.session.query(customers).filter(customers.userid == params['userid'])
    query_result.update(params)
    db.session.commit()
    return jsonify({"message" : "Updating Success!"})

def deletes(**params):
    query_result = db.session.query(customers).filter(customers.userid == params['userid'])
    query_result.delete()
    db.session.commit()
    return jsonify({"message" : "Deleting Success!"})

def token(**params):
    # dbresult = mysqldb.showUserByEmail(**params)
    resultdb = db.session.query(customers).filter(customers.email == params['email']).one()
    result = row2dict(resultdb)
    if result is not None:
        # payload untuk JWT
        user = {
            "username" : result['username'],
            "email" : result['email']
        }
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(user, fresh = True, expires_delta = expires)

        data = {
            "data" : user,
            "token_access" : access_token
        }
    
    else:
        data = {
            "message" : "email tidak terdaftar"
        }
    return jsonify(data)