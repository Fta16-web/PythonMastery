from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, DeclarativeBase
from scalar_fastapi import get_scalar_api_reference
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

# SQLite DB setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)


# SQLAlchemy Base class
class Base(DeclarativeBase):
    pass


# SQLAlchemy User model
class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


# Create database tables
Base.metadata.create_all(bind=engine)

# Session configuration
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic model for request body
class UserBody(BaseModel):
    name: str
    email: str


# FastAPI app instance
app = FastAPI()


# Route: Get all users
@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.post("/users")
def create_user(user: UserBody, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Route: Scalar Docs
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
