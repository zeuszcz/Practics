import sqlalchemy.orm
from sqlalchemy import text


def get_allcart(session: sqlalchemy.orm.Session):
    stmt = text("""
                    SELECT *
                    FROM cart
                """)
    result = session.execute(stmt)
    return result

def get_cartcount(session: sqlalchemy.orm.Session):
    stmt = text("""
                    select COUNT( name)
                    from cart
                """)
    result = session.execute(stmt)
    return result

def get_productname(session: sqlalchemy.orm.Session):
    stmt = text("""
                    select  name
                    from product  
                """)
    result = session.execute(stmt)
    return result

def get_productcomptype(session: sqlalchemy.orm.Session):
    stmt = text("""
                    select  product_component.name, product_type.name
                    from product_component 
                    inner join product_type
                    on product_type_id = product_type.id
                """)
    result = session.execute(stmt)
    return result

def get_ram_component(session: sqlalchemy.orm.Session):
    stmt = text("""
                    select  product_component.name
                    from product_component 
                    where product_type_id = 3
                """)
    result = session.execute(stmt)
    return result

def get_count_video_component(session: sqlalchemy.orm.Session):
    stmt = text("""
                    select  count(product_component.name)
                    from product_component 
                    where product_type_id = 2
                """)
    result = session.execute(stmt)
    return result


def get_ordered_component(session: sqlalchemy.orm.Session):
    stmt = text("""
                    select * from product_component order by cost
                """)
    result = session.execute(stmt)
    return result

def get_component_count(session: sqlalchemy.orm.Session):
    stmt = text("""
                    select  count( product_type.name ), product_type.name  
                    from product_component 
                    inner join product_type
                    on product_type_id = product_type.id
                    group by product_type.name

                """)
    result = session.execute(stmt)
    return result

# def get_service(session: sqlalchemy.orm.Session, service_id: int):
#     stmt = text("""
#                     select * from service where id=:service_id
#                 """)
#     result = session.execute(stmt, params={'service_id': service_id})
#     return result