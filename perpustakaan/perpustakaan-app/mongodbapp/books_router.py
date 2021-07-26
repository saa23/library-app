from fastapi import APIRouter
from books_controller import *

router = APIRouter()

@router.get("/books")
async def view_search_books_by_name():
    result = search_books()
    return result

@router.get("/bookbyid")
async def view_search_books_id(params:dict):
    result = search_books_id(**params)
    return result
  
@router.get("/bookbyname")
async def view_search_books_by_name(params:dict):
    result = search_book_by_name(**params) 
    return result

@router.post("/updatebyid")
async def commit_update_books_id(params:dict):
    result = update_books_id(**params) 
    return {'message':'update successfully!'}

@router.post("/deletebyid")
async def commit_delete_books_id(params:dict):
    result = delete_books_by_id(**params) 
    return {'message':'delete successfully!'}