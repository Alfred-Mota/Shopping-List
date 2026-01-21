import "../css/style.css";
import { mountApp } from "./ui";
import { isAuthenticated } from "./auth";

const app = document.querySelector<HTMLElement>("#app");
if (!app) throw new Error("Elemento #app não encontrado");

if(isAuthenticated()){
    mountApp(app);
}else{
    window.location.href = "/login.html"
}
