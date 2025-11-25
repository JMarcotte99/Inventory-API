from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
app = FastAPI()

# -------------------------
# 1. DATABASE CONNECTION
# -------------------------
DATABASE_URL = "postgresql://inventory_user:inventory_pass@db:5432/inventory_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------
# 2. ROUTES
# -------------------------

@app.get("/")
def root(db: Session = Depends(get_db)):
    # simple SQL statement to test DB connectivity
    result = db.execute(text("SELECT 'DB connection OK'")).fetchone()
    return {"message": "Hello from FastAPI!", "db_status": result[0]}

