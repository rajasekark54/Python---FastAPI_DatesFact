from fastapi import Depends, APIRouter, Header, HTTPException

from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from schemas.datefact import DateFactCreate
import service.datefact as DateFactService

datefact=APIRouter()

# @datefact.get('/')
# async def heloworld():
#   return {"message": "Hello World"}

@datefact.post('/dates')
async def createDateFact(dates : DateFactCreate, db: Session = Depends(get_db)):
  return DateFactService.insertOrUpdate(dates=dates, db=db)
  
# @datefact.get('/dates/{id}')
# async def getDateFact(id: int, db: Session = Depends(get_db)):
#   return DateFactService.get(id = id, db = db)

@datefact.get('/dates')
async def getDateFactList(db: Session = Depends(get_db)):
  return DateFactService.getAll(db = db)

async def verify_apiKey(X_API_KEY: str = Header()):
  if X_API_KEY != "SECRET_API_KEY":
      raise HTTPException(status_code=400, detail="X_API_KEY header invalid")

@datefact.get('/popular')
async def getPopular(db: Session = Depends(get_db)):
  return DateFactService.getMonthRankingList(db = db)

@datefact.delete('/dates/{id}', dependencies=[Depends(verify_apiKey)])
async def deleteDateFact(id: int, db: Session = Depends(get_db)):
  return DateFactService.delete(id=id, db = db)
