from requests import session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/todoapp"
SQLALCHEMY_DATABASE_URL = "postgresql://lrpqigjj:f5xlQLkVDM6JtA-ijl6Gf4LpUDft3Jg9@isilo.db.elephantsql.com/lrpqigjj"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()
