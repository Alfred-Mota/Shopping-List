import type { CreateItem, ShoppingItem, LoginResult, RegisterResult } from "./types";
import { fetchWithAuth } from "./http";

export async function getItems(userName?: string):Promise<ShoppingItem[]> {
    /**
     * Metodo tem como objetivo buscar a lista de items com base em um 
     * usuario especifico ou todos os dados disponiveis no banco.
     * Seu retorno é uma lista de objetos do tipo ShoppingItem.
     * 
     * O metodo utiliza o metodo wrapper, envoltoria.
     */
    const qs = userName ? `?user_name=${encodeURIComponent(userName)}` : "";
    const res = await fetchWithAuth(`/items${qs}`);
    if (!res.ok) {
        throw new Error("Falha ao carregar itens");
    }

    return res.json();
}

export async function createItem(item: CreateItem):Promise<void> {
    /**
     * Possui como objetivo criar um novo item no banco de dados.
     * O parâmetro esperado é do tipo CreateItem.
     * Não possui retorno, alem de excessoes caso ocorram
     */

    const options = {
        method: "POST",
        body: JSON.stringify(item),
    }
    
    const res = await fetchWithAuth("/items", options );

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
    const options = {method: "DELETE"}
    const res = await fetchWithAuth(`/items/${id}`, options);

    if(!res.ok){
        const text = await res.text()
        throw new Error(`DELETE /item falhou: ${res.status} - ${text}`)
    }
}

export async function login(username:string, password:string) : Promise<LoginResult> {
    /**
     * Login do usuario
     */
    
    try {
        const options =  {
        method: "POST",
        body: JSON.stringify({username, password})
    }
        const res = await fetchWithAuth('/auth/login', options)

     if (!res.ok) {
        return {
            'ok':false,
            'message': "Credenciais Invalidas"
        }
    }

    const data = await res.json()
    
    return {
        'ok':true,
        'access_token':data.access_token
    }
    } catch (error) {
       return {
            'ok':false,
            'message': "Erro de conexão"
        }
    }
}

export async function register(username:string, password:string) : Promise<RegisterResult>{
        /**
         * Registro de usuario
         */
    try {
        const options =  {
        method: "POST",
        body: JSON.stringify({username, password})
    }
        const res = await fetchWithAuth('/auth/register', options)

     if (!res.ok) {
        return {
            'ok':false,
            'message': "Credenciais Invalidas"
        }
    }

    const data = await res.json()
    
    return {
        'ok':true,
        'access_token':data.access_token
    }
    } catch (error) {
       return {
            'ok':false,
            'message': "Erro de conexão"
        }
    }
}