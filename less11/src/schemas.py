from pydantic import BaseModel, EmailStr, Field, PastDate
from datetime import date


class ContactSchema(BaseModel):
    name: str = Field(min_length=3, max_length=40)
    email: EmailStr
    phone: str = Field(min_length=10, max_length=13)
    birthday: date  # str #PastDate


class ContactResponse(BaseModel):
    id: int = 1
    name: str
    email: EmailStr
    phone: str
    birthday: date  # str #PastDate

    class Config:
        from_attributes = True
