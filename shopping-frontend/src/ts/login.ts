    import { login } from "./api";
    import { saveToken } from "./auth";

    const form = document.querySelector<HTMLFormElement>("#login-form")
    const errorEl = document.querySelector<HTMLParagraphElement>("#login-error")
    const register = document.querySelector<HTMLButtonElement>("#register")

    if(register){
        /**
         * A pagina atual é desmontada automaticamente e o listener tambem é
         */
        register.addEventListener("click", ()=>{
            window.location.href = "register.html"
        })
    }

    form?.addEventListener("submit", async(e)=>{
        e.preventDefault()

        const usernameInput = document.getElementById("username") as HTMLInputElement
        const passwordInput = document.getElementById("password") as HTMLInputElement

        const username = usernameInput.value
        const password = passwordInput.value

        const res = await login(username, password)

        if (!res.ok) {
            if (errorEl) {
            errorEl.textContent = res.message;
            errorEl.classList.remove("hidden");
            }
            return;
        }
        saveToken(res.access_token)
        window.location.href = "/"

    })  