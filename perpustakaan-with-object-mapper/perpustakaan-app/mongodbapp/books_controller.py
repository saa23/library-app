from models.books_model import books
import json
import re

def showBooks():
    return json.loads(books.objects.to_json())

def showBookById(**params):
    return json.loads(books.objects(id = params['id']).to_json())

def showBookByName(**params):
    naming = params['name']
    regex = re.compile(f'.*{naming}.*', re.IGNORECASE)
    return json.loads(books.objects(name = regex).to_json())

def updateBookById(**params):
    result = books.objects(id=params['id'])
    result.update(**params)
    
def deleteBookById(**params):
    books(id= params['id']).delete()