import { register } from "./api"
import { saveToken } from "./auth"

const form = document.querySelector<HTMLFormElement>("#register-form")
const errorEl = document.querySelector<HTMLParagraphElement>("#register-error")

form?.addEventListener('submit', async (e) => {
    e.preventDefault()

    const usernameInput = document.getElementById("username") as HTMLInputElement
    const passwordInput = document.getElementById("password") as HTMLInputElement

    const username = usernameInput.value
    const password = passwordInput.value

    const res = await register(username, password)

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