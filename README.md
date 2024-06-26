# Library-App


# 1. Introduction
Library Application to simulate borrowing book and record all the borrowing and returning (active or not active) by which customer and book in database.


# 2. Dataset
Syntetic data that manually created using sql. Specifically create table `customers` and `borrows` in MySQL. Whereas create a table `books` in MongoDB.


# 3. Requirements
For this exercise project, very important to have installed both DB below:
- MySQL
- MongoDB


Here, used two libraries to generate API:
- Flask
- FastApi

Besides, other required libraries as following:
- PyMySQL
- SQLAlchemy
- Mongoengine
- Flask-JWT-Extended


# 4. Project Flow

<img src="./images/flow-diagram.png" alt="the concept" widht="400" height="300"/>

To be specific here is the ERD:

<img src="./images/erd-with-flow.jpg" alt="the concept" widht="400" height="300"/>

Shown in the figure, there are two blocks based on the component frameworks:
- **MySQL + Flask** (using SQLAlchemy as the ORM)
- **MongoDB + FastAPI** (using MongoEngine as the ODM)

Each of them have three components:
1. **Model**: connecting database and API 
2. **Controller**: accessing all functionalities
3. **Router**: connecting all endpoints

While to access the `borrows` tables we set the microservice security layer by adding the token requirement from JWT.


## 4.1. Project Structure
```
├──  library-app\

  ├── venv\ (the virtual environment in gitignore list)

  ├── .gitignore
  ├── README.md
  ├── requirements.txt
  ├── db.sql (query to CREATE and INSERT of table `customers` and CREATE of `borrows`)
  
  ├── images\

  ├── mongodbapp\
    ├── __init__.py
    ├── config.py
    ├── main.py
    ├── books_controller.py
    ├── books_router.py

    ├── models\
      ├── __init__.py
      ├── books_model.py

  ├── mysqlapp\
    ├── config.py
    ├── main.py

    ├── app\
      ├── __init__.py

      ├── models\
        ├── __init__.py
        ├── borrows_model.py
        ├── customers_model.py

      ├── controllers\
        ├── __init__.py
        ├── borrows_controller.py
        ├── customers_controller.py

      ├── routers\
        ├── __init__.py
        ├── borrows_router.py
        ├── customers_router.py
```

## 4.2. How to run the apps
### 4.2.1. Run server FastAPI
Need to run the FastAPI, since it the API for `books` data will be consumed by `borrows` (Flask).

First of all, go to `mongodbapp\` folder.

Then, here is the format to execute FastAPI
```
uvicorn {module name}:{FastAPI instance name} --port {any port available} --reload
```

That means here is the command for the project
```
uvicorn main:app --port 8000 --reload
```
If run locally, the server will be running on `http://127.0.0.1:8000`.
To view the API docs go to `http://127.0.0.1:8000/docs` on the browser.
![fastapi-api-docs](./images/fastapi-api-docs.png
)

### 4.2.2. Run server Flask
After FastAPI server has been started, open another terminal windows. Next, go to `mysqlapp\` folder.

Subsequently, run the Flask server, by simply using format command
```
python {python file containing Flask instance}
```

That means, here is the command for the project
```
python main.py
```
If run locally, by default Flask server will be run on port 5000. Thus the server will be running on `http://127.0.0.1:5000`


# 5. Output
Postman can be used to test routers API.
Here are some results of router API testing:

### 1. GET `/books`
<img src="./images/get-books.png" alt="get-books" widht="400" height="300"/>

### 2. GET `/bookbyname`
<img src="./images/get-bookbyname.png" alt="get-bookbyname" widht="400" height="300"/>

### 3. POST `/insertbook`
<img src="./images/post-insertbook.png" alt="post-insertbook" widht="400" height="300"/>

### 4. GET `/users`
<img src="./images/get-users.png" alt="get-users" widht="400" height="300"/>

### 5. GET `/requesttoken`
<img src="./images/get-requesttoken.png" alt="get-requesttoken" widht="400" height="300"/>

For user to accessing data in table `borrows` need to input the token from JWT (obtained from router */requesttoken*).

Go to tab `Authorization`. Select the auth type `Bearer Token`, then input the token in the provided text box.

<img src="./images/bearer-token.png" alt="bearer-token" widht="400" height="300"/>

### 6. GET `/borrows`
<img src="./images/get-borrows.png" alt="get-borrows" widht="400" height="300"/>

### 6. POST `/borrows/insert`
<img src="./images/post-borrows-insert.png" alt="post-borrows-insert" widht="400" height="300"/>


# Appendix
## MongoDB Basic Commands
#### 1. Run `Mongod`
It is responsible for running the MongoDB server.

- open cmd (for OS windows)
- use this command:
```
mongod
```

#### 2. Run `Mongosh`
It is responsible for running the MongoDB server.

- open cmd (for OS windows)
- use this command:
```
mongosh
```

#### 3. Create New Database
- using mongosh
- check existing database
```
show dbs
```
![show-dbs](./images/show-dbs.png)
- Here we created new database named `perpustakaan`
- the newly created database will not appear using command `show dbs`, since to appear need a collection that have at least a record data within it.

#### 4. Create New Collection
- using mongosh
- select `perpustakaan` database
```
use perpustakaan
```
![use-perpustakaan](./images/use-perpustakaan.png)
- create new collection named `books` then insert a testing data
```
db.books.insertOne({name:"test"})
```
![insert-one-data](./images/insert-one-data.png)
- check the newly created collection
```
show collections
```
![show-collections](./images/show-collections.png)
