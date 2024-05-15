from mongoengine import connect, Document, StringField
from config import Config
import json

host = str(Config.HOST)
database = str(Config.DB)
port = int(Config.PORT)

try:
    connection = connect(db = database, host = host, port = port)
    if connection:
        print("Connected to MongoDB")

except Exception as e:
    print(e)

class books(Document):
    name = StringField(required=True, max_length=255)
    author = StringField(required=True, max_length=40)
    releaseyear = StringField(required=True, max_length=6)
    genre = StringField()


# ### open the books.json
# with open('../books.json', 'r') as file:
#     books_data = json.load(file)

# ### Bulk insert some documents into collection books
# books.objects.insert_many(books_data)
