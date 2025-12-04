from pydantic import BaseModel, EmailStr
from datetime import datetime
from enums.userRoles import UserRoles

class UserCreate(BaseModel):
    email: EmailStr

class UserRead(BaseModel):
    email: EmailStr
    role: UserRoles
    created_at: datetime

    class Config:
        orm_mode = True
