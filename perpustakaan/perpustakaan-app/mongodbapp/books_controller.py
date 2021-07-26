from os import execlp
from models.books_model import database as db

db = db()

def objIdToStr(obj):
    return str(obj["_id"])

def search_books():
    data_list = []
    for book in db.showBooks():
        book["_id"] = objIdToStr(book)
        data_list.append(book)
    return data_list

def search_books_id(**params):
    result = db.showBookById(**params)
    result["_id"] = objIdToStr(result)
    return result

def search_book_by_name(**params):
    data_list = []
    for book in db.searchBookByName(**params):
        book["_id"] = objIdToStr(book)
        data_list.append(book)
    return data_list

def update_books_id(**params):
    try:
        db.updateBookById(params)
    except Exception as e:
        print(e)

def delete_books_by_id(**params):
    try:
        db.deleteBookById(params)
    except Exception as e:
        print(e)
