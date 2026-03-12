from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

BASE_INT_ID_TYPE = BigInteger


class BaseORM(AsyncAttrs, DeclarativeBase):
    """
    Base ORM class with ID as BASE_ID_TYPE(int8)
    """

    id: Mapped[int] = mapped_column(
        BASE_INT_ID_TYPE, primary_key=True, autoincrement=True
    )
