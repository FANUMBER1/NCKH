from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from database import SessionLocal

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    @staticmethod
    def get_all_users():
        session = SessionLocal()
        users = session.query(User).all()
        session.close()
        return users
