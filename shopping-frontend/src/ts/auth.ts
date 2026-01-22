const TOKEN_KEY =  'shopping_token'

export function saveToken(token:string){
    /**
     * Salvar o token do usuario no LocalStorage
     */
    localStorage.setItem(TOKEN_KEY, token)
}

export function getToken() : string|null{
    /**
     * Recuperar o token
     */
    return localStorage.getItem(TOKEN_KEY)
}

export function logout(){
    /**
     * Remover o token e redirecionar ao pagina de login
     */
    console.log("CLICK")
    localStorage.removeItem(TOKEN_KEY)
    window.location.href='/login.html'
}

export function isAuthenticated() : boolean{
    /**
     * Verificar a autenticação, se o usuario estiver logado retorna true caso contrario false
     * O uso de interrogação (!) converte o valor para boolean, porem em forma de negação
     * O uso de um segundo interrogação (!!) retorna o valor de volta
     */
    return !!getToken()
}