from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, DeclarativeBase
from pydantic import BaseModel

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class User(Base):
    __table__name = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserBody(BaseModel):
    name: str
    email: str
