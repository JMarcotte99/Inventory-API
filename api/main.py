from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import engine, SessionLocal
from api.models.products import Base
from routes.products import router
app = FastAPI()
app.include_router(router)

# -------------------------
# CREATION TABLES
# -------------------------
Base.metadata.create_all(bind=engine)

# -------------------------
# DEPENDANCES BD
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------
# ROUTES
# -------------------------

@app.get("/")
def root(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 'DB connection OK'")).fetchone()
    return {"message": "Hello from FastAPI!", "db_status": result[0]}

