from fastapi import FastAPI, HTTPException, Path
from typing import Optional
from pydantic import BaseModel, Field

from .db import get_connection, init_db

app = FastAPI()

class ItemCreate(BaseModel):
    user_name: str = Field(min_length=1, max_length=255)
    item_name: str = Field(min_length=1, max_length=255)
    quantity: int = Field(default=1, ge=1)

@app.on_event("startup")
def startup():
    init_db()

#Criando uma rotas GET
#______________________________________________________________
@app.get("/health")
def health():
    return {
        "result":"ok"
    }

@app.get("/db-test")
def db_test():
    
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("select 1")
        value = cursor.fetchone()[0]
    
        return {
            'db':'ok',
            'value':value
        }

@app.get("/db-table-check")
def db_table_check():
    sql = '''
            select count(*)
            from sys.tables
            where name = 'shopping_items'
          '''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()[0]
        return{
                'shopping_items_exists': bool(result)
        }

@app.get('/items-list')
def items_list():
    '''
    Recuperar uma lista de compras
    '''
    sql = """
            select id, user_name, item_name, quantity, created_at 
            from shopping_items
            order by created_at desc
          """
    
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows =  cursor.fetchall()
            items = []
            for r in rows:
                items.append({
            "id": r[0],
            "user_name": r[1],
            "item_name": r[2],
            "quantity": r[3],
            "created_at": str(r[4]),  # datetime -> string pra JSON
        })
        return{
            'lista': items
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        
@app.get('/items')
def list_items(user_name: Optional[str] = None):
    '''
    Recuperar a lista de um usuario em especifico
    '''
    base_sql = """
                select id, user_name, item_name, quantity, created_at 
                from shopping_items
               """
    order_sql = """ order by created_at desc """

    params = []
    if user_name:
        base_sql+= "where user_name = ?"
        params.append(user_name)

    sql = base_sql + order_sql

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, params)
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

#Fim rotas GET
#______________________________________________________________

#Criando rotas POST
#_______________________________________________________________
@app.post('/item')
def create_item(payload: ItemCreate):
    sql = '''
          insert into dbo.shopping_items (user_name, item_name, quantity)
          values(?,?,?)
          '''
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql,payload.user_name, payload.item_name, payload.quantity)
            cursor.commit()
        return {"created":True}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
#Fim rotas POST
#______________________________________________________________


#Criando Rotas Delete
#_______________________________________________________________

@app.delete("/delete-item/{item_id}")
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

