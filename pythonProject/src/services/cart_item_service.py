from src.models import CartItem
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
    def add_cart_item(new_SI: int, new_PI: int, new_CI: int, db):
        stmt = insert(CartItem).values(product_id=new_PI, cart_id=new_CI, service_id=new_SI)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def update_cart_item(CI: int, new_product_id: int, new_cart_id: int, new_service_id: int,
                         db):
        stmt = update(CartItem).where(CartItem.cart_id == CI).values(product_id=new_product_id,
                                                                     cart_id=new_cart_id, service_id=new_service_id)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def delete_cart_item(CI: int, db):
        stmt = delete(CartItem).where(CartItem.cart_id == CI)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}