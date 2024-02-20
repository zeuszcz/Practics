from src.models import ProductComponent
from src.schemas.schema_component import ProductComponentCreate
from sqlalchemy import select, insert, update, delete


class ComponentService:

    @staticmethod
    def get_ram_component(db):
        stmt = select(ProductComponent.name).where(ProductComponent.product_type_id == 3)
        result = db.execute(stmt).scalars().all()
        return result

    @staticmethod
    def get_video_component(db):
        stmt = select(ProductComponent.name).where(ProductComponent.product_type_id == 2)
        result = db.execute(stmt).scalars().all()
        return result

    @staticmethod
    def get_ordered_component(db):
        stmt = select(ProductComponent).order_by(ProductComponent.cost)
        result = db.execute(stmt).all()
        result = [row._asdict() for row in result]
        return result

    @staticmethod
    def add_product_component(pti: int, new_name: str, new_cost: int, db):
        stmt = insert(ProductComponent).values(product_type_id=pti, name=new_name, cost=new_cost)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def update_product_component(old_name: str, pti: int, new_name: str, new_cost: int,
                                 db):
        stmt = update(ProductComponent).where(ProductComponent.name == old_name).values(product_type_id=pti,
                                                                                        name=new_name, cost=new_cost)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def delete_product_component(old_name: str, db):
        stmt = delete(ProductComponent).where(ProductComponent.name == old_name)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}