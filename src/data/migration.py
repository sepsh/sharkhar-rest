import os

from sqlmodel import SQLModel, create_engine

from .models import User

# FIXME alembic this

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    # os.remove("database.db")
    SQLModel.metadata.create_all(engine)
