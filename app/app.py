from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate , PostResponse

from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# @app.on_event("startup") --> old version


# --------------------------------------- old version before connect database
# app = FastAPI()

# @app.get("/hello_world")
# def hello_world():
#     return { "message" : "hello_world"}

# # ------------------------------- get

# # stored in memory

# text_posts = {
#     1 : {"title" : "New post" , "content" : "first post"},
#     2 : {"title" : "New post" , "content" : "Second post"},
#     3 : {"title" : "New post" , "content" : "third post"},
#     4 : {"title" : "New post" , "content" : "fourth post"},
# }


# # @app.get("/posts")
# # def get_all_posts():
# #     return text_posts


# # query parameter + Multiple parameters
# # return limit of posts

# @app.get("/posts")
# def get_all_posts(limit : int = None): # , content_length : int = None
#     if limit:
#         # return ltext_posts[:limit] # error -> operation of list on dict !!
#         return list(text_posts.values())[:limit]
#     return text_posts

# # ------

# # path parameter =  dynamic value
# # HTTPExceptiont
  
# @app.get("/posts/{id}")
# def get_post(id : int) -> PostResponse:
#     if id not in text_posts:
#         raise HTTPException(status_code=404, detail="post not found")
    
#     return text_posts.get(id) 


# # -------------------------------------- Request Body data 38:05

# # Body hide data Vs get data in URL
# # create  shema file + pydantic


# @app.post("/posts") 
# def create_post(post : PostCreate) -> PostResponse: 
#     new_post = { "title" : post.title , "content":  post.content }
#     text_posts[max(text_posts.keys()) + 1 ] = new_post
#     return new_post


#--------------------------------------- Database Connection 46:05
#----- Create Upload + Save Database 59:05
 