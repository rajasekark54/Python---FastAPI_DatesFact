from typing import Text
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, time, timedelta

from db.base_model import BaseModel

class DateFact(BaseModel):
  id = Column(Integer,primary_key=True,index=True)
  month = Column(String,nullable=False)
  day = Column(Integer,nullable=False,index=True)
  fact = Column(Text,nullable=False)