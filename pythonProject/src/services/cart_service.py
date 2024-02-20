from src.models import Cart
from src.schemas.schema_cart import CartCreate
from sqlalchemy import select, insert, update, delete


class CartService:

    @staticmethod
    def get_count(db):
        stmt = db.query(Cart).count()
        return {"result": stmt}

    @staticmethod
    def get_all(db):
        stmt = select(Cart)
        result = db.execute(stmt).all()
        result = [row._asdict() for row in result]
        return result

    @staticmethod
    def add_cart(new_cart, db):
        stmt = insert(Cart).values(**new_cart.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def update_cart(old_name: str, new_name: str, new_sum: int, new_product_component: CartCreate,
                    db):
        stmt = update(Cart).where(Cart.name == old_name).values(name=new_name, sum=new_sum)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def delete_cart(old_name: str, db):
        stmt = delete(Cart).where(Cart.name == old_name)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}
