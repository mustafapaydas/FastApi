from sqlalchemy import Integer, Column, Date

from db import Base


class AbstractModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(Date)
    updated_at = Column(Date)