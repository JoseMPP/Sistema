from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import settings



DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True)
    nombre = Column('nombre', String)
    precio = Column('precio',Integer , nullable=True)
    urlimagen = Column('urlimagen', String, nullable=True)
    tipodivisa = Column('divisa', Integer, nullable=True)
    fecha = Column('fechaoferta', DateTime, nullable=True)