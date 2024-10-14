from sqlalchemy import ForeignKey, String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

engine = create_engine(url="sqlite:///db.sqlite3")

SessionLocal = sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "product_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(128))
    cost: Mapped[int] = mapped_column(Integer)
    amount: Mapped[int] = mapped_column(Integer)


Base.metadata.create_all(bind=engine)
