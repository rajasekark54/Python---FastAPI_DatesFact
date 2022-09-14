from sqlalchemy import Column, Integer, String, Text

from db.base_model import BaseModel

class DateFact(BaseModel):
  id = Column(Integer,primary_key=True,index=True)
  month = Column(String,nullable=False)
  day = Column(Integer,nullable=False,index=True)
  fact = Column(Text,nullable=False)