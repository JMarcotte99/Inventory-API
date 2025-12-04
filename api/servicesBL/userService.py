from sqlalchemy.orm import Session
from modelsEntities.userModel import User
from enums.userRoles import UserRoles
from fastapi import HTTPException, status
from uuid import uuid4

def create_user(db: Session, email: str, current_user: User):
    if current_user.role != UserRoles.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )

    user = User(
                 id =uuid4()
                ,email=email
                ,role=UserRoles.employee
               )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session, current_user: User):
    if current_user.role != UserRoles.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return db.query(User).all()