import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os.path
from pprint import pprint
from dotenv import load_dotenv
from models import create_tables



dotenv_path = 'config.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DSN = os.getenv("dsn")
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

session.close()