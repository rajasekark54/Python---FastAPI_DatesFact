from ast import Return
from datetime import date
from sqlalchemy.orm import Session
from schemas.datefact import DateFactCreate
from model.datefact import DateFact
import calendar
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, status
from core.logger import get_logger
import service.api.request as request
from core.config import settings
from time import strptime

logger = get_logger(__name__)

def insertOrUpdate(dates : DateFactCreate, db : Session):
    try:
        month = dates.month
        day = dates.day
        monthName = calendar.month_name[month]
        existRecord = getByDayMonth(monthName, day, db=db)

        if(existRecord):            
            return update(existRecord.id, existRecord, db)
        else:
            return create(dates, db)
    except SQLAlchemyError as ex:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex))

    
def create(dates : DateFactCreate, db : Session):
    try: 
        monthName = calendar.month_name[dates.month]
        fact = str(getFact(dates.month, dates.day))

        dates = DateFact(month=monthName, day=dates.day, fact = fact)
        db.add(dates)
        db.commit()
        db.refresh(dates)
        logger.info("New DateFact inserted into database.")
        return dates
    except SQLAlchemyError as ex:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex))

def update(id:int, dates: DateFactCreate,  db:Session):
    abbr_to_num = {name: num for num, name in enumerate(calendar.month_name) if num}
    monthNum = abbr_to_num[dates.month]

    fact = str(getFact(monthNum, dates.day))
    db.query(DateFact).filter(DateFact.id == id).update({DateFact.month:dates.month, DateFact.day:dates.day, DateFact.fact:fact});
    db.commit()
    db.refresh(dates)
    return dates

def getFact(month: int, day: int):
    url = settings.NUMBERSAPI + str(month) + '/' + str(day)
    return request.get(url)

def get(id:int, db:Session):
    return db.query(DateFact).filter(DateFact.id == id).first()

def getAll( db:Session):
    return db.query(DateFact).all()

def delete(id:int, db:Session):
    dates = db.query(DateFact).filter(DateFact.id == id).first()
    if dates is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"Record not found": f"There is no record for requested id : {id}"},
        )

    db.delete(dates)
    db.commit()
    return dates;

def getByDayMonth(month: str, day: int, db:Session):
    return db.query(DateFact).filter(DateFact.month == month).first()

def test(db:Session):
    return 'eeee'
    dates = db.query(DateFact).filter(DateFact.month == 'January').first()
    print(dates)
    return dates

def list(month: str, day: int, db:Session):
    return db.query(DateFact).all()
     


