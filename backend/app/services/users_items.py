from fastapi import Path
from typing import Optional
from ..db.connection import get_connection
from ..schemas.items import ItemCreate

def user_get_item(user_id: int):
    '''
    Recuperar a lista de um usuario em especifico
    '''
    print("Enviando lista ao usuario: ")
    print(user_id)
    print()
    sql = """
                select id, item_name, quantity, created_at 
                from shopping_items
                where user_id = ?
                order by created_at desc
               """

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, user_id)
        rows = cursor.fetchall()
    
    items = []
    for r in rows:
        items.append({
            "id": r[0],
            "item_name": r[1],
            "quantity": r[2],
            "created_at": str(r[3]),
        })

    return items

def user_add_item(payload: ItemCreate, user_id:int):
    sql = '''
          insert into dbo.shopping_items (item_name, quantity,user_id)
          values(?,?,?)
          '''
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql,payload.item_name, payload.quantity, user_id)
            cursor.commit()
        return {"created":True}
    except Exception as error:
        return error

def user_delete_item(item_id: int = Path(...,ge=1)):
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