from fastapi import FastAPI
from books_router import router as books_router

app = FastAPI()

app.include_router(books_router)

@app.get("/")
async def read_main():
    return {"message": "Welcome to Main Page!"}

# URL: http://localhost:8000/