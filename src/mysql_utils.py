from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

ASYNC_DB_URL = "mysql+aiomysql://user:password@mysql:3306/testdb"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await async_engine.dispose()

def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()