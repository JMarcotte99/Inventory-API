from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemasDTO import ProductCreate, ProductRead
from servicesBL.productService import create_product, get_products


router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductCreate)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
     product = create_product(db, product.name, product.quantity)
     return ProductCreate(name = product.name, quantity = product.quantity)

@router.get("/", response_model=list[ProductRead])
def get_products_route(db: Session = Depends(get_db)):
    return get_products(db)
