import { getToken, logout } from "./auth";
export const API_BASE = "http://localhost:8000";

/**
 * Essa classe tem como objetivo ser um wrapper, envoltoria, para chamadas em rotas protegidas.
 * 
 * Explicando TyperScript utilizado:
 * - RequestInit -> é um tipo do TypeScript que descreve o segundo argumento de fetch(url, {method, headers, body, ...})
 *   logo, RequestInit = {method, headers, body, ...}
 * 
 * - Omit<T, K> -> peque todas as propriedades T e retira a propriedade K: 
 *   type User = {id: number; name: string; password: string;};
 *   type PublicUser = Omit<User, "password">;
 *   PublicUser = { id: number; name: string;}
 * 
 * - Record<K,V> -> é um tipo utilitario para objetos, descreve o tipo da chave K e o tipo do valor,
 *   ou seja, headers?:Record<string, string> -> {"chave string" : "valor string"}
 * 
 * - O operador & esta concatenando objetos: {"A":"ola"} & {"B":"tudo bem?"} = {"A":"ola" , "B":"tudo bem?"}
 */

type FetchOptions = Omit<RequestInit, "headers"> & {

    headers?:Record<string, string>

}

export async function fetchWithAuth(path: string, options: FetchOptions = {}) {
    /**
     * Responsalvel por centralizar as chamadas com token
     */
    const token = getToken();

    const headers: Record<string, string> = {
        ...(options.headers ?? {}),
    };

    // Se tiver body e ainda não definiu Content-Type, definimos JSON por padrão
    if (options.body && !headers["Content-Type"]) {
        headers["Content-Type"] = "application/json";
    }

    // Só adiciona Authorization se tiver token
    if (token) {
        /**
         * Utilizar Bearer é um padrão que especifica essa autilização
         * como sendo um token. Esse padrão permite automatizar a leitura da requisição
         * com o metodo OAuth2PasswordBearer
         * Em http o header Authorization segue o formato: Authorization: <tipo> <credencial>
         * 
         * O tipo informa ao servidor como interpretar a credencial.
         * Tipos comuns:
         * *Basic → usuário:senha (base64)
         * *Bearer → token opaco ou JWT
         * *Digest → desafio/resposta (raro hoje)
         * *Negotiate → Kerberos (corporativo)
         */
        headers["Authorization"] = `Bearer ${token}`;
    }

    const res = await fetch(`${API_BASE}${path}`, {
        ...options,
        headers,
    });

    // Se o backend diz "não autenticado", derruba sessão e volta pro login
    if (res.status === 401) {
        logout();
        // interrompe o fluxo atual
        throw new Error("Sessão expirada ou inválida");
    }

    return res;
}