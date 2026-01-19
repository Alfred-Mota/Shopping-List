# 📌 Bibliotecas do Projeto (e por que usar)

Este projeto é uma aplicação web simples para gerenciamento de **listas de compras**, utilizando **Python no backend**, **JavaScript no frontend** e **banco de dados SQL** para persistência.

Abaixo está a explicação das principais bibliotecas utilizadas no backend e o motivo de cada escolha.

---

## 🚀 FastAPI

**O que é:**  
FastAPI é um framework web moderno para Python, focado na criação de APIs REST de forma simples, rápida e organizada.

**Por que usar:**
- Criação fácil de rotas HTTP (`GET`, `POST`, `DELETE`, etc.).
- Documentação automática da API (Swagger e ReDoc).
- Integração nativa com validação de dados.
- Código limpo, legível e fácil de manter.
- Ótimo desempenho mesmo em projetos maiores.

**Uso no projeto:**
- Definição da aplicação backend.
- Criação dos endpoints da API.
- Organização da lógica do servidor.

---

## ⚙️ Uvicorn

**O que é:**  
Uvicorn é um **servidor ASGI** responsável por executar a aplicação FastAPI e escutar as requisições HTTP.

**Por que usar:**
- É o servidor recomendado para aplicações FastAPI.
- Suporte a aplicações assíncronas (ASGI).
- Modo de desenvolvimento com `--reload`.
- Simples de configurar e rodar.

**Uso no projeto:**
- Inicialização do servidor web localmente.
- Exposição da API na porta configurada (ex.: `http://localhost:8000`).

---

## 🗄️ pyodbc

**O que é:**  
pyodbc é uma biblioteca Python que permite a conexão com bancos de dados através de **ODBC (Open Database Connectivity)**.

**Por que usar:**
- Compatível com vários bancos SQL (SQL Server, PostgreSQL, MySQL, entre outros).
- Permite escrita direta de comandos SQL.
- Ideal para projetos simples e para quem quer controle total das queries.
- Boa opção antes de adotar um ORM mais complexo.

**Pontos de atenção:**
- É necessário ter o driver ODBC do banco instalado.
- SQL pode variar conforme o banco utilizado.

**Uso no projeto:**
- Conexão com o banco de dados.
- Execução de comandos SQL para criar tabelas, inserir e consultar dados.

---

## ✅ Pydantic

**O que é:**  
Pydantic é uma biblioteca para **validação e serialização de dados**, amplamente utilizada junto com FastAPI.

**Por que usar:**
- Garante que os dados recebidos pela API estejam corretos.
- Reduz erros causados por dados inválidos.
- Define claramente o formato das requisições e respostas.
- Facilita manutenção e leitura do código.

**Uso no projeto:**
- Definição de modelos de entrada (request).
- Definição de modelos de saída (response).
- Validação automática dos dados enviados pelo frontend.

---

## 📦 Resumo das dependências

| Biblioteca | Função no projeto |
|----------|------------------|
| FastAPI | Criação da API e definição das rotas |
| Uvicorn | Execução do servidor web |
| pyodbc | Conexão e comunicação com banco SQL |
| Pydantic | Validação e estruturação de dados |

---

Este conjunto de bibliotecas permite criar uma aplicação **simples, organizada e escalável**, servindo como uma boa base para evoluções futuras como autenticação, novos endpoints e deploy em produção.
