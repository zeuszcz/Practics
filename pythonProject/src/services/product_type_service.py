from src.models import ProductType
from src.schemas.schema_product_type import ProductTypeCreate
from sqlalchemy import select, insert, update, delete


class ProductTypeService:

    @staticmethod
    def get_product_type_name(db):
        stmt = select(ProductType)
        result = db.execute(stmt).scalars().all()
        return result

    @staticmethod
    def add_product_type(new_product_type, db):
        stmt = insert(ProductType).values(**new_product_type.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def update_product_type(old_name: str, new_product_type, db):
        stmt = update(ProductType).where(ProductType.name == old_name).values(**new_product_type.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def delete_product_type(old_name: str, db):
        stmt = delete(ProductType).where(ProductType.name == old_name)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

