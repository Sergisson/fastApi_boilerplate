from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field, Relationship


# class Producer(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str = Field(index=True)


class Film(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    year: Optional[int] = None
    # producer: Optional[Producer] = Relationship(back_populates="films")


