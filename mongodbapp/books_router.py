from fastapi import APIRouter
from books_controller import *

router = APIRouter()

@router.get("/books")
async def view_books():
    result = showBooks()
    return result

@router.get("/bookbyid")
async def view_search_books_id(params:dict):
    result = showBookById(**params)
    return result
    
@router.get("/bookbyname")
async def view_search_books_by_name(params:dict):
    result = showBookByName(**params) 
    return result

@router.post("/insertbook")
async def insert_book(params:dict):
    insertBook(**params)
    return {'message':'insert a document successfully!'}


@router.post("/updatebyid")
async def update_books_id(params:dict):
    updateBookById(**params)
    return {'message':'update successfully!'}

@router.post("/deletebyid")
async def delete_books_by_id(params:dict):
    deleteBookById(**params)
    return {'message':'delete successfully!'}