import type { CreateItem, ShoppingItem } from "./types";

const API_BASE = "http://localhost:8000"

export async function fetchItems(userName?: string):Promise<ShoppingItem[]> {
    /**
     * Metodo tem como objetivo buscar a lista de items com base em um 
     * usuario especifico ou todos os dados disponiveis no banco.
     * Seu retorno é uma lista de objetos do tipo ShoppingItem
     */
    const url = new URL(`${API_BASE}/items`)
    const u = userName ? userName.trim():""
    if(u) url.searchParams.set("user_name", u)

    const res = await fetch(url)
    if(!res.ok) throw new Error (`GET /items falhou: ${res.status}`)
    
    return res.json()

}

export async function createItem(item: CreateItem):Promise<void> {
    /**
     * Possui como objetivo criar um novo item no banco de dados.
     * O parâmetro esperado é do tipo CreateItem.
     * Não possui retorno, alem de excessoes caso ocorram
     */
    const res = await fetch(`${API_BASE}/item`,{
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify(item)
    })

    if(!res.ok){
        const text = await res.text()
        throw new Error(`POST /item falhou : ${res.status} - ${text}`)
    }
}

export async function deleteItem(id:number): Promise<void> {
    /**
     * Possui como objetivo deletar algum item do banco de dados 
     * com base no seu identificador unico, id.
     * Não possui retorno
     */
    const res = await fetch(`${API_BASE}/delete-item/${id}`, {method:"DELETE"})

    if(!res.ok){
        const text = await res.text()
        throw new Error(`DELETE /item falhou: ${res.status} - ${text}`)
    }
}