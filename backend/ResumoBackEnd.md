# 📘 Resumos do Projeto – Backend Python (iniciante)

---

# 🚀 FastAPI

## O que é
- Framework web para criação de APIs em Python
- Focado em simplicidade, desempenho e clareza

## Para que é usado
- Criar endpoints HTTP
- Receber requisições
- Retornar respostas em JSON

## Conceitos principais
- Aplicação FastAPI (`app`)
- Rotas (`GET`, `POST`, `DELETE`, etc.)
- Funções associadas a rotas
- Validação automática de dados
- Documentação automática

## Vantagens
- Fácil de aprender
- Código organizado
- Documentação automática (/docs)
- Ideal para APIs REST

---

# ⚙️ Uvicorn

## O que é
- Servidor ASGI para aplicações Python

## Para que é usado
- Rodar a aplicação FastAPI
- Escutar requisições HTTP
- Encaminhar requisições para o FastAPI

## Conceitos principais
- Porta (ex: 8000)
- Host (localhost / 127.0.0.1)
- Processo do servidor
- Modo desenvolvimento (`reload`)

## Papel no projeto
- FastAPI é a aplicação
- Uvicorn é quem coloca a aplicação “no ar”

---

# 🗄️ pyodbc

## O que é
- Biblioteca Python para conexão com bancos via ODBC

## Para que é usado
- Conectar ao SQL Server
- Executar comandos SQL diretamente
- Ler e gravar dados no banco

## Conceitos principais
- Connection string
- Driver ODBC
- Conexão
- Cursor
- Parâmetros SQL (`?`)

## Vantagens
- Controle total do SQL
- Leve e direto
- Compatível com vários bancos

---

# 🔑 Connection (pyodbc)

## O que é
- Representa a conexão ativa com o banco de dados

## Responsabilidades
- Abrir comunicação com o banco
- Controlar transações
- Confirmar alterações
- Fechar a conexão

## Métodos importantes
- `commit`
- `rollback`
- `close`

## Conceito-chave
- Alterações só são salvas após `commit`

---

# 🧭 Cursor (pyodbc)

## O que é
- Objeto usado para executar SQL e ler resultados

## Responsabilidades
- Executar comandos SQL
- Buscar dados do banco

## Métodos principais
- `execute`
- `fetchone`
- `fetchall`
- Iteração direta
- `rowcount`
- `close`

## Conceito-chave
- Cursor executa SQL
- Cursor não salva alterações

---

# 🧪 Pydantic

## O que é
- Biblioteca de validação de dados

## Para que é usado
- Validar dados recebidos pela API
- Definir formato de entrada e saída
- Garantir tipos corretos

## Conceitos principais
- Modelos de dados
- Tipagem forte
- Validação automática
- Erros claros

## Benefícios
- Menos erros
- Código mais seguro
- Contrato claro entre frontend e backend

---

# 🧠 SQL Server (conceitos usados)

## Tabela
- Estrutura para armazenar dados

## Colunas
- Campos da tabela
- Tipos de dados definidos

## PRIMARY KEY
- Identifica cada registro de forma única
- Não permite valores duplicados

## IDENTITY
- Gera valores automaticamente
- Auto incremento

## DEFAULT
- Valor padrão quando não informado

## DATETIME / DATETIME2
- Armazena data e hora

---

# 🧠 Modelo mental geral do backend

- Uvicorn roda o servidor
- FastAPI define as rotas
- Endpoint chama função Python
- Função abre conexão
- Cursor executa SQL
- Connection faz commit
- Banco persiste dados
