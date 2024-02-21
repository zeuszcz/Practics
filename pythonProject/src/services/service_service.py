from src.models import Service
from src.schemas.schema_service import ServiceCreate
from sqlalchemy import select, insert, update, delete


class ServiceService:

    @staticmethod
    def get_service_name(db):
        stmt = select(Service)
        result = db.execute(stmt).scalars().all()
        return result

    @staticmethod

    def add_service(new_service, db):
        stmt = insert(Service).values(**new_service.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod

    def update_service(old_name: str, new_service, db):
        stmt = update(Service).where(Service.name == old_name).values(**new_service.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def delete_service(old_name: str, db):
        stmt = delete(Service).where(Service.name == old_name)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}