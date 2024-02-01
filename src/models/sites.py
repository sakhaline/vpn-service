from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.extensions import db

if TYPE_CHECKING:
    from .users import User


class Site(db.Model):
    __tablename__ = "sites"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    page_visits: Mapped[int] = mapped_column(insert_default=text("0"))
    data_sent: Mapped[int] = mapped_column(insert_default=text("0"))
    data_received: Mapped[float] = mapped_column(insert_default=text("0"))
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="sites")

    __table_args__ = (UniqueConstraint("user_id", "url", name="unique_user_url"),)
