from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemasDTO import UserCreate, UserRead
from servicesBL.userService import create_user, get_users
from modelsEntities.userModel import User
from enums.userRoles import UserRoles
from uuid import uuid4


router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserRead)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):

    # FAUX admin pour test (à remplacer plus tard par auth réelle)
    fake_admin = User(
        id=uuid4(),
        email="admin@test.com",
        role=UserRoles.admin
    )
    created_user = create_user(db, str(user.email), current_user=fake_admin)
    return created_user

@router.get("/", response_model=list[UserRead])
def get_users_route(db: Session = Depends(get_db)):

    fake_admin = User(
        id=uuid4(),
        email="admin@test.com",
        role=UserRoles.admin
    )

    return get_users(db, current_user=fake_admin)