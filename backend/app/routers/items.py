from fastapi import APIRouter, HTTPException, Path, Depends, status
from ..services.admin_items import get_items, add_item, delete_item
from ..services.users_items import user_add_item, user_get_item, user_delete_item
from ..schemas.items import ItemCreate
from ..security.test_auth import get_current_user_payload
router = APIRouter(prefix='/items', tags=["Items"])

@router.get("/")
def list_items(token = Depends(get_current_user_payload)):
    role = token['role']

    if role ==  'user':
        id = int(token['user_id'])
        item = user_get_item(id)
        return item
    
    elif role == "admin":
        
        items = get_items()
        return items
    raise HTTPException(status.HTTP_405_METHOD_NOT_ALLOWED, detail="Credenciais Invalidas")

@router.post('/')
def create_item(payload: ItemCreate, token = Depends(get_current_user_payload)):
    role = token['role']
    
    if role == 'user':
        id = int(token['user_id'])
        res = user_add_item(payload, id)
        return res
    
    elif role == 'admin':
        res = add_item(payload)
        return res
    raise HTTPException(status.HTTP_405_METHOD_NOT_ALLOWED, detail="Credenciais Invalidas")

@router.delete("/{item_id}")
def delete(item_id: int = Path(..., ge=1, title="ID do Produto", description="Identificador único do produto")):
    
    res = delete_item(item_id)
    return res

