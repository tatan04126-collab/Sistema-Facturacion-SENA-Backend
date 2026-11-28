from sqlalchemy import create_engine
import pymysql
from sqlalchemy.orm import sessionmaker, declarative_base

#Create a SQLalchemy engine
engine = create_engine('mysql+pymysql://root@localhost:3306/mi_Supermercado?charset=utf8mb4', echo=True)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

Base.metadata.bind = engine