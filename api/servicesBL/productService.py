from sqlalchemy.orm import Session
from modelsEntities.productModel import Product

def create_product(db: Session, name: str, quantity: int):
    product = Product(name=name,quantity=quantity)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session):
    return db.query(Product).all()