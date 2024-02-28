from src.models import Cart,Product,Service,CartItem
from src.schemas.schema_cart import CartUpdate,CartRead
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
    def update_cart(new_cart,old_name,db):
        stmt = update(Cart).where(CartUpdate.name == old_name).values(**new_cart.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def delete_cart(old_name: str, db):
        stmt = delete(Cart).where(Cart.name == old_name)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}


    def add_product_to_cart(cart_id: int,product_id:int, db):
        product_stmt = select(Product).filter(Product.id == product_id)
        product = db.execute(product_stmt).scalar_one_or_none()
        cart_stmt = select(Cart).filter(Cart.id == cart_id)
        cart = db.execute(cart_stmt).scalar_one_or_none()
        new_sum = product.cost + cart.sum
        stmt = update(Cart).values({"sum": new_sum}).where(Cart.id == cart_id)
        result = db.execute(stmt)
        cart_item_stmt = insert(CartItem).values({"product_id": product_id, "cart_id": cart_id})
        result = db.execute(cart_item_stmt)
        db.commit()
        return {"status": "complete"}


    def add_service_to_cart(cart_id: int,service_id:int, db):
        service_stmt = select(Service).filter(Service.id == service_id)
        service = db.execute(service_stmt).scalar_one_or_none()
        cart_stmt = select(Cart).filter(Cart.id == cart_id)
        cart = db.execute(cart_stmt).scalar_one_or_none()
        new_sum = service.cost + cart.sum
        stmt = update(Cart).values({"sum": new_sum}).where(Cart.id == cart_id)
        result = db.execute(stmt)
        cart_item_stmt = insert(CartItem).values({"service_id": service_id,"cart_id": cart_id})
        result = db.execute(cart_item_stmt)
        db.commit()
        return {"status": "complete"}




    def delete_service_from_cart(cart_id: int,service_id:int, db):
        service_stmt = select(Service).filter(Service.id == service_id)
        service = db.execute(service_stmt).scalar_one_or_none()
        cart_stmt = select(Cart).filter(Cart.id == cart_id)
        cart = db.execute(cart_stmt).scalar_one_or_none()
        new_sum = cart.sum - service.cost
        stmt = update(Cart).values({"sum": new_sum}).where(Cart.id == cart_id)
        result = db.execute(stmt)
        cart_item_stmt = delete(CartItem).where(CartItem.cart_id == cart_id,CartItem.service_id == service_id)
        result = db.execute(cart_item_stmt)
        db.commit()
        return {"status": "complete"}



    def delete_product_from_cart(cart_id: int,product_id:int, db):
        product_stmt = select(Product).filter(Product.id == product_id)
        product= db.execute(product_stmt).scalar_one_or_none()
        cart_stmt = select(Cart).filter(Cart.id == cart_id)
        cart = db.execute(cart_stmt).scalar_one_or_none()
        new_sum = cart.sum - product.cost
        stmt = update(Cart).values({"sum": new_sum}).where(Cart.id == cart_id)
        result = db.execute(stmt)
        cart_item_stmt = delete(CartItem).where(CartItem.cart_id == cart_id,CartItem.product_id == product_id)
        result = db.execute(cart_item_stmt)
        db.commit()
        return {"status": "complete"}