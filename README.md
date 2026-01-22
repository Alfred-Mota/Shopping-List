# 🛒 Shopping List — API & Frontend

Projeto educacional para aprendizado prático de desenvolvimento **Full Stack**, utilizando FastAPI no backend e TypeScript Vanilla no frontend.

O foco do projeto **não é o produto final**, mas o processo de aprendizado, abordando:
- Funcionamento de uma API Web
- Integração entre backend e frontend
- Organização e arquitetura de código
- Autenticação e autorização com JWT
- Evolução gradual de um frontend simples para React

---

## 🎯 Objetivo do Projeto

Criar uma aplicação web para gerenciar listas de compras, usando o projeto como base prática para compreender:

- Como funciona o fluxo HTTP (request/response)
- Separação de responsabilidades no backend
- Boas práticas de segurança (hash de senha, JWT)
- Controle de acesso baseado em papéis (RBAC)
- Backend como fonte da verdade

> Este projeto tem foco educacional. Algumas decisões de arquitetura foram tomadas
> visando aprendizado e clareza, não necessariamente produção.

---

## 🧰 Stack Utilizada

### Backend
- Python
- FastAPI
- Uvicorn
- SQL Server
- pyodbc
- Pydantic
- passlib + bcrypt
- python-jose (JWT)

### Frontend
- HTML
- CSS
- TypeScript
- Vite

---

## 📁 Estrutura do Backend

backend/
- app/
  - main.py
  - db/
    - connection.py
    - init_db.py
  - routers/
    - auth.py
    - items.py
  - services/
    - admin_items.py
    - users_items.py
  - schemas/
    - items.py
    - users.py
  - security/
    - security.py
    - test_auth.py

---

## 🚀 Servidor

- FastAPI rodando com Uvicorn
- URL: http://localhost:8000
- Healthcheck: GET /health
- Documentação Swagger: /docs
- CORS configurado para o frontend (localhost:5173)

---

## 🗄️ Banco de Dados

- SQL Server
- Banco: ShoppingDB
- Autenticação: Windows Authentication
- Conexão centralizada via `get_connection`
- Uso de SQL parametrizado (prevenção de SQL Injection)

### Criação automática de tabelas
As tabelas são criadas automaticamente no startup da aplicação.

#### Tabela: users
- id (INT, PK, IDENTITY)
- user_name (NVARCHAR, UNIQUE)
- password_hash (NVARCHAR)
- role (NVARCHAR)
- is_active (BIT)
- created_at (DATETIME2)

#### Tabela: shopping_items
- id (INT, PK, IDENTITY)
- item_name (NVARCHAR)
- quantity (INT)
- created_at (DATETIME2)
- user_id (INT, FK → users.id)

- Foreign Key com `ON DELETE CASCADE`

---

## 🔐 Autenticação e Autorização

A aplicação utiliza **JWT (JSON Web Token)** para autenticação.

### JWT
- Algoritmo: HS256
- Expiração: 30 minutos
- Tipo: access_token
- Claims do token:
  - user_id
  - role
  - exp

O token é retornado no login e no registro (auto-login).

> A SECRET_KEY está definida no código apenas para desenvolvimento.
> Está planejado mover para variáveis de ambiente.

---

## 👮 Controle de Acesso (RBAC)

### Roles
- user
- admin

### Regras
- user:
  - Pode listar, criar e deletar apenas seus próprios itens
- admin:
  - Acesso total a todos os itens

O backend utiliza o `user_id` presente no token como fonte da verdade.

---

## 📦 Endpoints Principais

### Autenticação
- POST /auth/login
- POST /auth/register

### Itens
- GET /items
- POST /items
- DELETE /items/{item_id}

Todas as rotas de itens exigem:
Authorization: Bearer <token>

---

## 🌐 Frontend

Frontend desenvolvido sem frameworks para entendimento profundo do JavaScript no navegador.

### Funcionalidades
- Login
- Registro
- Listagem de itens
- Criação de itens
- Remoção de itens
- Feedback visual de status

### Autenticação no Frontend
- Token armazenado no localStorage
- Wrapper `fetchWithAuth` adiciona automaticamente o header Authorization
- O frontend não envia mais user_name — o backend resolve tudo via JWT

---

## 📚 Conceitos Aprendidos

### Backend
- FastAPI e fluxo de requisição
- SQL Server com pyodbc
- Hash de senha com bcrypt
- JWT (payload, assinatura, expiração)
- Autenticação vs Autorização
- RBAC
- Organização em routers, services e schemas

### Frontend
- TypeScript modular
- Fetch API
- Backend como fonte da verdade
- Fluxo de autenticação com token

---

## 📝 Estado Atual do Projeto

- ✅ Backend funcional
- ✅ Banco conectado
- ✅ Autenticação com JWT
- ✅ Controle de acesso por role
- ✅ Itens vinculados ao usuário autenticado
- ✅ Frontend funcional em TypeScript
- ⏳ Migração para React
- ⏳ Refresh token
- ⏳ Deploy

---

## 🚀 Próximos Passos

- Mover configs sensíveis para variáveis de ambiente
- Implementar refresh token
- Melhorar tratamento de erros (401 / 403)
- Migrar frontend para React
- Deploy com HTTPS
