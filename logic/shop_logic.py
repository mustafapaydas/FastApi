from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select

from db import engine
from models.model import Shop, ShopSchema, Employee, EmployeeSchema


def convert_to_employee_entity(_employee:EmployeeSchema):
    employee = Employee
    employee.name = _employee.name
    employee.phone = _employee.phone
    employee.shop = _employee.shop
    return employee

def convert_to_shop_entity(_shop:ShopSchema):
    shop = Shop()
    shop.name = _shop.name
    shop.city = _shop.city
    shop.address = _shop.address
    if shop.employees:
        employees = []
        for i in shop.employees:
            employees.append(convert_to_employee_entity(i))
        shop.employees = employees
    return shop

def get_shops():
    Session = sessionmaker(bind=engine)
    session = Session()
    shops = session.query(Shop).all()
    session.close()
    session.close()
    return shops

async def generate_shop(shop:ShopSchema):
    async with engine.begin() as connection:
        async with connection.begin() as transaction:
            shop = convert_to_shop_entity(shop)
            connection.execute(Shop.__table__.insert().values(shop))
            await transaction.commit()

async def update_shop(shop:ShopSchema):
   async with engine.begin() as connection:
       async with connection.begin() as transaction:
            shop = convert_to_shop_entity(shop)
            exist_query = select(Shop).where(Shop.id == shop.id)
            result = await connection.execute(exist_query)
            _shop = await result.scalar()

            if _shop and _shop.id:
                _shop = shop
                await transaction.commit()

async def delete_shop(id):
    async with engine.begin() as conn:
        stmt = select(Shop).where(Shop.id == id)
        result = await conn.execute(stmt)
        shop = await result.scalar()

        if shop:
            conn.delete(shop)
            await conn.commit()
