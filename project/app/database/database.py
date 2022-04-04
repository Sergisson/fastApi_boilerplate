from sqlalchemy.exc import DatabaseError
from sqlmodel import SQLModel

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from settings import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


def commit_decorator(func):
    async def commit_wrapper(session: AsyncSession, *args, **kwargs):
        result = await func(session=session, *args, **kwargs)
        session.add(result)
        try:
            await session.commit()
        except DatabaseError as err:
            print(err)
            result = None
        else:
            await session.refresh(result)
        return result
    return commit_wrapper
