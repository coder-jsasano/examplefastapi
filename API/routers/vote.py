#Vote Route
#Path will be at "/vote"
#The user id will be extracted from the JWT token
#The body will contain the id of the pos the user is voting on as wel as the direction of the vote
#A vote direction of 1 means we wanna add a vote, a direction of 0 means we wanna delete a vote.

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from API import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags = ['vote']
    )

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), 
         current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Oist with id: {vote.post_id} does not exist!")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    
    found_vote = vote_query.first()

    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"Message": "Succesfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Vote does not exist!")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"Message": "Succesfully deleted vote"}
        




