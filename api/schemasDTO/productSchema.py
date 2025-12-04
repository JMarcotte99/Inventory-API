from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    quantity: int

class ProductRead(BaseModel):
    id: int
    name: str
    quantity: int

    class Config:
        orm_mode = True
