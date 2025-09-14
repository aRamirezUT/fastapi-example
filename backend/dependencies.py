from datetime import datetime, timezone
from typing import Annotated
from fastapi.concurrency import asynccontextmanager
from fastapi import Depends, Header, FastAPI, HTTPException
from sqlmodel import select, create_engine, SQLModel, Session
from backend.schemas.campaigns import Campaign

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    with Session(engine) as session:
        if not session.exec(select(Campaign)).first():
            session.add_all([
                Campaign(name="Summer Lunch", due_date=datetime.now(timezone.utc)),
                Campaign(name="Black Friday", due_date=datetime.now(timezone.utc))
            ])
            session.commit()
    yield

def get_session():
    with Session(engine) as session:
        yield session
    
SessionDep = Annotated[Session, Depends(get_session)]

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secure-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    
async def get_query_token(token: str):
    if token != "Aren":
        raise HTTPException(status_code=400, detail="No Aren token provided")