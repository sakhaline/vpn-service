from typing import TYPE_CHECKING, List

from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.extensions import db


if TYPE_CHECKING:
    from .sites import Site


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(65), unique=True,
                                          nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True,
                                       nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)

    sites: Mapped[List["Site"]] = relationship(back_populates="user")
