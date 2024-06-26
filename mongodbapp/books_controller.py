from models.books_model import books
import json
import re

def showBooks():
    """
    Show all documents
    """
    return json.loads(books.objects.to_json())

def showBookById(**params):
    """
    Show a document based on given book id
    """
    return json.loads(books.objects(id = params['id']).to_json())

def showBookByName(**params):
    """
    Show a document based on given book name
    """
    naming = params['name']
    regex = re.compile(f'.*{naming}.*', re.IGNORECASE)
    return json.loads(books.objects(name = regex).to_json())


def insertBook(**params):
    """
    Insert a document into collection books.
    The document must be contains:
    - name
    - author
    - releaseyear
    - genre
    """
    Books = books(name=params['name'], 
                 author=params['author'], 
                 releaseyear=params['releaseyear'],
                 genre=params['genre']
                )
    Books.save()
    print('successfully insert a document!')


def updateBookById(**params):
    """
    update a document base on book id, then specify the key that will be updated
    """
    result = books.objects(id=params['id'])
    result.update(**params)

def deleteBookById(**params):
    """
    delete a document based on given book id
    """
    books(id= params['id']).delete()
    print('successfully deleted a document!')