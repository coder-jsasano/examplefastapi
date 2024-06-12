#CRUD Operation = CRUD is an acronym of create:post, read:get, update:put/patch and delete:delete

#Validation

#Documentation = add /docs or /redoc to the normal url so that you can see all of the operations in FastApi and so on

#Database = A collection of organized data that can be easily accessed and managed
#           Databases have datatypes just like any programming language

#Tables = A table represents a subject or event in an application. 
#         ex. Users, Products, Purchases = these tables are related and reffered to as a relational database
#         Tables have rows and columns. Each row represents a different entry in the table and each column represents a different attribute(ID, name, age, sex, etc.)
#Primary key = A column or group of columns that uniquely identifies each row in a table. Table can have one and only one primary key.
#Unique constraints = Similar to Primary key. Make sure every record has a unique value for that column
#Null constraints = By default, when adding a new entry to a database, any column can be left blank. When a column is left black, it has a null value.
#                   If you need column to be properly filled, a NOT NULL constraint can be added to the column to ensure that the column is never left blank.

#Object Relational Mapper(ORM) = Layer of abstraction like interception that sits between the database and us(fastapi)
#                                Instead of manually defining tables in postgres, we can define our tables as python models
#                                Queries can be made exclusively through python code. No SQL is necessary
#SQLALCHEMY = Sqlalchemy is one of the most popular python ORM
#             Standalone library and has no association with FastAPI
#             Can be used with any other python web frameworks or any python based application

#Schema/Pydantic Models = Define the structure of a request and response

#Authentication = In this time, we use JWT(JSON Web Tokens) Authentication  

#Relationship database = Set a foreign key on a certain table column except for user information table to tell the database that there's a relation between this table of this data and that table of that data 

#Voting/Like system = User should be able to like a post
#                     Should only be able to like a post once
#                     Retrieving posts should also fetch the total number of likes
#                     Column referencing post_id and user_id and they all are a unique combination since they should only be able to like a post once
#Composite Keys = Primary Key that spans multiple columns
#                 Since Primary Key must be unique, this will ensure no user can like a post twice

#CORS = Cross Origin Resource Sharing(CORS)
#       allows you to make requests from a web browser on one domain to a server on a different domain
#       By default our API will only allow web browsers runningo the same domain as our server to make requests to it

from fastapi import FastAPI
from API import models
from API.database import engine
from API.config import settings
#Enable routers to access main file
from API.routers import post, user, auth, vote
#CORS
from fastapi.middleware.cors import CORSMiddleware

#If you use alembic, this is no longer needed
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#BEFORE DATABASE
#my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
#            {"title": "favorite foods", "content": "I love ramen", "id": 2}]

#Find post by id
#def find_post(id):
#    for p in my_posts:
#        if p['id'] == id:
#            return p

#def find_index_post(id):
#    for i, p in enumerate(my_posts):
#        if p['id'] == id:
#            return i

#User router in different files in different folders and bring them as router and run the code as app
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#Magical decorator = turns into an actual path operation. The decoration .get("/") below called http methods
@app.get("/")
#async = optional keyword for functions to do some asynchronous tasks
def root():
    #return on the internet. Fastapi converts python dictionary to json
    return {"message": "Welcome to my api!"}
