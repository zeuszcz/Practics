from src.models import Build
from src.schemas.schema_build import BuildCreate
from sqlalchemy import select, insert, update, delete


class BuildService:

    @staticmethod
    def get_build_count(db):
        stmt = db.query(Build).count()
        return {"result": stmt}

    @staticmethod
    def get_all_build(db):
        stmt = select(Build)
        result = db.execute(stmt).all()
        result = [row._asdict() for row in result]
        return result

    @staticmethod
    def add_build(new_build, db):
        stmt = insert(Build).values(**new_build.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def update_build(old_name: str, new_build, db):
        stmt = update(Build).where(Build.name == old_name).values(**new_build.dict())
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}

    @staticmethod
    def delete_build(old_name: str, db):
        stmt = delete(Build).where(Build.name == old_name)
        result = db.execute(stmt)
        db.commit()
        return {"status": "complete"}
