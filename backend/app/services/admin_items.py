# 
# !!TODO DO
# 
from fastapi import Path
from typing import Optional
from ..db.connection import get_connection
from ..schemas.items import ItemCreate

def get_items():
    '''
    Recuperar a lista de um usuario em especifico ou toda as compras cadastradas
    '''
    print("Admin recuperando lista")

    sql = """
            select id, item_name, quantity, created_at 
            from shopping_items
            order by created_at desc
            """

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
    
    items = []
    for r in rows:
        items.append({
            "id": r[0],
            "user_name": r[1],
            "item_name": r[2],
            "quantity": r[3],
            "created_at": str(r[4]),
        })

    return items

def add_item(payload: ItemCreate):
    sql = '''
          insert into dbo.shopping_items (item_name, quantity)
          values(?,?,?)
          '''
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql,payload.item_name, payload.quantity)
            cursor.commit()
        return {"created":True}
    except Exception as error:
        return error
    

def delete_item(item_id: int = Path(...,ge=1)):
    '''
    Deleta um item com base no seu id, identificador unico
    '''
    sql = """
            delete 
            from dbo.shopping_items 
            where id = ?
          """
    
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, item_id)
        affected = cursor.rowcount
        cursor.commit()
    
    if affected == 0:
        return{
            "delete":False,
            "message": "Item não encontrado"
        }
    
    return{
            "delete":True,
            "message": "Item deletado"
        }