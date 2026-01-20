export type ShoppingItem = {
    id:number,
    user_name: string,
    item_name: string,
    quantity: number,
    created_at: string
}

export type CreateItem = {
    user_name: string,
    item_name: string,
    quantity: number,
    
}