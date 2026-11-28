from sqlalchemy import Column, Integer, String
from src.models import Base, session


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __init__(self, name): 
        self.name = name

    def __repr__(self):
        return f"<category(id={self.id}, name='{self.name}')>"

    def get ():
        categories = session.query(Categories).all()
        return categories

    def save(self):
        session.add(self)
        session.commit()