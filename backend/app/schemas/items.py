from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    item_name: str = Field(min_length=1, max_length=255)
    quantity: int = Field(default=1, ge=1)
