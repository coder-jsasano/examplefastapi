from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from API import models, schemas, oauth2
from API.database import get_db

router = APIRouter(
    prefix="/posts", #address that always start with
    tags=['Posts']
)


#**************************************************************************************************************************
#add /posts after the standard link so that the code below is gonna be returned
#if you set the path the same as the upper one ("/"), the upper one is gonna be returned
#@router.get("/", response_model=List[schemas.PostResponse])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), 
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    #cursor.execute("""SELECT * FROM posts """)
    #posts = cursor.fetchall()
    #print(limit)
    print(search) #if you wanna add a space in search, type %20 cuz it's equal to space
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
            models.Post.title.contains(search)).limit(limit).offset(skip).all()
    #print(results)
    
    #if you want posts to be inpublic as the user can only see his posts
    #posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    
    #print(posts) #print SQL codes
    #return posts
    return posts
#**************************************************************************************************************************
#Create a post with a default http response(201)
#@router.post("/", status_code=status.HTTP_201_CREATED)
#def create_posts(post: Post): #payload: dict = Body(...) : for extracting body
    #print(post) 
    #print(post.dict()) #.dict key = extract the key arg of dict key ex. new_post.title
    #post_dict = post.dict()
    #post_dict['id'] = randrange(0, 1000000)
    #my_posts.append(post_dict)
    #return {"data": post_dict}
#**************************************************************************************************************************
#Create a post with SQL code  
#@router.post("/", status_code=status.HTTP_201_CREATED)
#def create_posts(post: Post):
#    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
#                    (post.title, post.content, post.published))
#    new_post = cursor.fetchone()
#    conn.commit() #save the post on Postgres#
#
#    return {"data": new_post}
#**************************************************************************************************************************
#Create a post with SQLalchemy 
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post= models.Post(owner_id=current_user.id, **post.dict()) #**.dict() = Dont have to type each values like title=post.titile
    print(current_user.id)
    #print(curent_user.email)
    #add  to a database and retrieve a data and put it into values
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
#**************************************************************************************************************************

#Make sure to put this code above the {id} decorator cuz /latest could be {id} and casue an error
#@router.get("/latest")
#def get_latest_post():
#    post = my_posts[len(my_posts)-1]
#    return {"detail": post}
#**************************************************************************************************************************
#Get one post by id
#@router.get("/{id}")
#(: int) = convert the data into a specified type
#Response = Find a detail error and inform it. Ex. http responses
#def get_post(id: int, response: Response): 
#    post = find_post(id)
#    if not post:
        #status. = enable to find http responses
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                            detail=f"post with id: {id} was not found!")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id: {id} was not found!"}
#    return {"post_detail": post}
#**************************************************************************************************************************
#Get one post by id on Postgres
#@router.get("/{id}")
#def get_post(id: int): 
#    cursor.execute("""SELECT * FROM posts WHERE id = (%s) """, (str(id)))
#    post = cursor.fetchone()
#    post = find_post(id)
#    if not post:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                            detail=f"post with id: {id} was not found!")
#    return {"post_detail": post}
#**************************************************************************************************************************
#Get one post with SQLalchemy
#@router.get("/{id}", response_model=schemas.PostResponse)
@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)): 
    #post = db.query(models.Post).filter(models.Post.id == id).first()
    
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found!")
    
    #if you want posts to be inpublic as the user can only see his posts
    #if post.owner_id != current_user.id:
    #    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
    #                        detail="Not authorized to perform requested action")
    
    return post
#**************************************************************************************************************************
#Delete a post
#def find_index_post(id):
#    for i, p in enumerate(my_posts):
#        if p['id'] == id:
#            return i
#**************************************************************************************************************************
#@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
#def delete_post(id: int):
    #deleting post
    #find the index in the array that has required ID
    #my_posts.pop(index)
#    index = find_index_post(id)

#    if index == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id: {id} doesn't exist!")

#    my_posts.pop(index)
#    return Response(status_code=status.HTTP_204_NO_CONTENT)
#**************************************************************************************************************************
#Delete a post on Postgres
#@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
#def delete_post(id: int):
#    cursor.execute("""DELETE FROM posts WHERE id = (%s) RETURNING *""", (str(id)))
#    deleted_post = cursor.fetchone()
#    conn.commit()
    
#    if deleted_post == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id: {id} doesn't exist!")

#    return Response(status_code=status.HTTP_204_NO_CONTENT)
#**************************************************************************************************************************
#Delete a post with SQLalchemy
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"The post with id: {id} doesn't exist!")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
#**************************************************************************************************************************
#Update a post
#@router.put("/{id}")
#def update_post(id: int, post: Post):
#    index = find_index_post(id)

#    if index == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id: {id} doesn't exist!")

#    post_dict = post.dict()
#    post_dict['id'] = id
#    my_posts[index] = post_dict
#    return {"message": post_dict}
#**************************************************************************************************************************
#Update a post on Postgres
#@router.put("/{id}")
#def update_post(id: int, post: Post):
#    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = (%s) RETURNING *""", 
#                   (post.title,post.content,post.published,str(id)))
#    updated_post = cursor.fetchone()
#    conn.commit()

#    if updated_post == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id: {id} doesn't exist!")

#    return {"message": updated_post}
#**************************************************************************************************************************
#Update a post with SQLalchemy
@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, updated_post:schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"The post with id: {id} doesn't exist!")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Not authorized to perform requested action")

    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
