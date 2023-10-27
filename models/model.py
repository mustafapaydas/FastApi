from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import AbstractModel


class Shop(AbstractModel):
    __tablename__ = "tbl_shop"
    name = Column(String)
    city = Column(String)
    address = Column(String)
    employees = relationship("Employee", back_populates="shop")

ShopSchema = sqlalchemy_to_pydantic(Shop, exclude=['id'])

class Employee(AbstractModel):
    __tablename__ = "tbl_employee"
    name = Column(String)
    surname = Column(String)
    phone = Column(String)
    identity_card_no = Column(Integer)
    shop_id = Column(Integer, ForeignKey('tbl_shop.id'))
    shop = relationship("Shop", back_populates="employees")

EmployeeSchema = sqlalchemy_to_pydantic(Employee, exclude=['id'])
