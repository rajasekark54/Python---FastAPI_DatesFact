from typing import Optional
from wsgiref.validate import validator
from pydantic import Field
from pydantic import BaseModel, EmailStr, ValidationError, validator
import calendar
from datetime import date

#properties required during user creation
class DateFactCreate(BaseModel):
    month : int
    day: int

    @validator("month")
    def month_validator(cls, value):
        if value < 1 or value > 12:
          raise ValueError("Month range should be between 1 to 12")
        return value

    @validator("day")
    def day_validator(cls, value):
        if value < 1 or value > 31:
          raise ValueError("Day range should be between 1 to 31")
        return value

# try:
#     DateFactCreate(month=12, day=1)
# except ValidationError as e:
#     print(e)

