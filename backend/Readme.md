# 📘 Backend — Resumo Técnico do Projeto (Python + FastAPI)

Este documento descreve os **conceitos, ferramentas e responsabilidades** utilizadas no backend do projeto, com foco **educacional**, partindo do zero até uma API funcional com autenticação e banco de dados.

---

## 🚀 FastAPI

### O que é
Framework web moderno para criação de APIs em Python, focado em **simplicidade**, **clareza** e **alto desempenho**.

### Para que é usado no projeto
- Definir endpoints HTTP
- Receber requisições do frontend
- Validar dados automaticamente
- Retornar respostas em JSON
- Gerar documentação automática

### Conceitos fundamentais
- Aplicação FastAPI (`app`)
- Rotas (`GET`, `POST`, `DELETE`, etc.)
- Funções Python ligadas às rotas
- Request / Response
- Validação automática com Pydantic
- Dependências (`Depends`)

### Vantagens
- Curva de aprendizado curta
- Código limpo e organizado
- Documentação automática em `/docs`
- Ideal para APIs REST modernas

---

## ⚙️ Uvicorn

### O que é
Servidor **ASGI** responsável por executar a aplicação FastAPI.

### Para que é usado
- Colocar a API “no ar”
- Escutar requisições HTTP
- Encaminhar as requisições para o FastAPI

### Conceitos importantes
- Host (`localhost`, `127.0.0.1`)
- Porta (ex: `8000`)
- Processo do servidor
- Modo desenvolvimento (`--reload`)

### Papel no projeto
- **FastAPI** → define a lógica
- **Uvicorn** → executa e expõe a API

---

## 🗄️ pyodbc

### O que é
Biblioteca Python para conexão com bancos de dados via **ODBC**, utilizada neste projeto para acessar o **SQL Server**.

### Para que é usado
- Abrir conexão com o banco
- Executar comandos SQL
- Ler e gravar dados

### Conceitos principais
- Connection string
- Driver ODBC
- Conexão
- Cursor
- SQL parametrizado (`?`)

### Por que usar
- Controle total do SQL
- Leve e explícito
- Ótimo para aprender como o banco realmente funciona

---

## 🔑 Connection (pyodbc)

### O que é
Objeto que representa uma **conexão ativa** com o banco de dados.

### Responsabilidades
- Abrir comunicação com o banco
- Controlar transações
- Confirmar alterações
- Encerrar a conexão

### Métodos importantes
- `commit()` → confirma alterações
- `rollback()` → desfaz alterações
- `close()` → fecha a conexão

### Conceito-chave
> Nenhuma alteração é persistida no banco sem `commit()`

---

## 🧭 Cursor (pyodbc)

### O que é
Objeto responsável por **executar comandos SQL** e **ler resultados**.

### Responsabilidades
- Executar SQL (`SELECT`, `INSERT`, `DELETE`, etc.)
- Buscar dados retornados pelo banco

### Métodos principais
- `execute()`
- `fetchone()`
- `fetchall()`
- Iteração direta (`for row in cursor`)
- `rowcount`

### Conceito-chave
- Cursor executa SQL
- Cursor **não** salva alterações
- Quem salva é a `Connection` via `commit`

---

## 🧪 Pydantic

### O que é
Biblioteca de validação e tipagem de dados usada pelo FastAPI.

### Para que é usado
- Validar dados recebidos pela API
- Definir formato dos payloads
- Garantir tipos corretos
- Gerar erros claros automaticamente

### Conceitos principais
- Models
- Tipagem forte
- Validação automática
- Contrato entre frontend e backend

### Benefícios
- Menos erros em tempo de execução
- Código mais seguro
- Comunicação clara entre camadas

---

## 🧠 SQL Server — Conceitos Utilizados

### Tabela
Estrutura que armazena dados.

### Colunas
Campos da tabela com tipos definidos.

### PRIMARY KEY
- Identificador único
- Não permite valores duplicados ou nulos

### IDENTITY
- Geração automática de valores
- Auto incremento

### DEFAULT
- Valor padrão quando não informado

### DATETIME / DATETIME2
- Armazenamento de data e hora

### FOREIGN KEY
- Relaciona tabelas
- Garante integridade dos dados

---

## 🧠 Modelo Mental do Backend

Fluxo completo de uma requisição:

1. **Uvicorn** recebe a requisição HTTP
2. **FastAPI** identifica a rota correta
3. O endpoint chama uma função Python
4. A função abre uma conexão com o banco
5. Um cursor executa o SQL
6. A connection faz `commit()` (se necessário)
7. O banco persiste os dados
8. A API retorna uma resposta em JSON

---

## 🎯 Objetivo do Backend

- Servir como base sólida para aprendizado
- Entender como APIs funcionam de verdade
- Evitar abstrações mágicas no início
- Construir confiança em fundamentos reais
