from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import commit_decorator
from app.database.models import Film
from sqlalchemy import select

@commit_decorator
async def add_film_usecase(
        film: Film,
        session: AsyncSession,
):
    film = Film(
        name=film.name,
        year=film.year,
        #producer=film.producer
    )
    return film

async def get_all_films_usecase(session: AsyncSession):
    result = await session.execute(select(Film))
    films = result.scalars().all()
    return films