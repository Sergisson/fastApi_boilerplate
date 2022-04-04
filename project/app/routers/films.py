from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_session
from app.database.models import Film
from app.usescases.films import add_film_usecase, get_all_films_usecase

router = APIRouter(prefix="/films", tags=["films"])

# @router.get("/songs", response_model=list[Song])
# async def get_songs(session: AsyncSession = Depends(get_session)):
#     result = await session.execute(select(Song))
#     songs = result.scalars().all()
#     return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]
#
#
@router.post("/add")
async def add_film(
        film: Film,
        session: AsyncSession = Depends(get_session),
):
    film = await add_film_usecase(
        film=film,
        session=session,
    )
    result = film if film else "error"
    return result

@router.get("/all")
async def get_all_films(
        session: AsyncSession = Depends(get_session),
):
    films = await get_all_films_usecase(session)
    return films