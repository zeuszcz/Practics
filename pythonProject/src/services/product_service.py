from src.models import Product
from src.schemas.schema_product import ProductCreate
from sqlalchemy import select, insert, update, delete


class ProductService:

    @staticmethod
    def get_product_name(db):
        stmt = select(Product.name)
        result = db.execute(stmt).scalars().all()
        return result

    @staticmethod
    def add_product(new_product, db):
        stmt = insert(Product).values(**new_product.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def update_product(old_name: str,new_product, db):
        stmt = update(Product).where(Product.name == old_name).values(**new_product.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def delete_product(old_name: str, db):
        stmt = delete(Product).where(Product.name == old_name)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}