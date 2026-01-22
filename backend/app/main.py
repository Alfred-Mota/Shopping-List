from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.init_db import init_db
from .routers.auth import router as auth_router
from .routers.items import router as items_router

app = FastAPI()

#Permissoes de CORS para acesso do front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(items_router)

@app.on_event("startup")
def startup():
    init_db()