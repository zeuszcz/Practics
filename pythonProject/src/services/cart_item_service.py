from src.models import CartItem, Cart
from src.schemas.schema_cart_item import CartItemCreate
from sqlalchemy import select, insert, update, delete


class CartItemService:

    @staticmethod
    def get_cart_item_count(db):
        stmt = db.query(CartItem).count()
        return {"result": stmt}

    @staticmethod
    def get_all_cart_item(db):
        stmt = select(CartItem)
        result = db.execute(stmt).all()
        result = [row._asdict() for row in result]
        return result

    @staticmethod
    def add_cart_item(new_cart_item, db):
        stmt = insert(CartItem).values(**new_cart_item.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def update_cart_item(CI: int, new_cart_item,db):
        stmt = update(CartItem).where(CartItem.cart_id == CI).values(**new_cart_item.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def delete_cart_item(cartid: int, db):
        stmt = delete(CartItem).where(CartItem.cart_id == cartid)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

