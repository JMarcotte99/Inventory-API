from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models.products import Product

router = APIRouter(prefix="/products")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_product(name: str, quantity: int, db: Session = Depends(get_db)):
    product = Product(name=name,quantity=quantity)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product