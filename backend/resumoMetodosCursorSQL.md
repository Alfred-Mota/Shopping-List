# 📌 Resumo – Cursor e Connection (pyodbc)

## Conceitos básicos
- Connection: representa a conexão com o banco de dados
- Cursor: executa comandos SQL e lê resultados
- O cursor não salva alterações
- A conexão é responsável por `commit`
- Cursor depende da connection

## Regra fundamental
- Cursor executa SQL
- Connection confirma alterações

## Uso geral
- Connection abre comunicação com o banco
- Cursor executa SQL dentro da conexão
- `commit` confirma alterações no banco
- `with` garante fechamento automático da conexão

## Métodos do cursor

### `execute`
- Executa comandos SQL
- Usado para SELECT, INSERT, UPDATE, DELETE, CREATE
- Aceita parâmetros com `?`
- Não persiste alterações sozinho

### `fetchone`
- Retorna uma única linha do resultado
- Usado quando a consulta retorna apenas um registro

### `fetchall`
- Retorna todas as linhas da consulta
- Carrega todo o resultado em memória

### Iteração direta no cursor
- Percorre resultados linha por linha
- Mais eficiente para grandes volumes de dados

### `rowcount`
- Indica quantas linhas foram afetadas
- Útil após DELETE ou UPDATE
- Retorna 0 quando nenhum registro é alterado

### `close`
- Fecha o cursor manualmente
- Normalmente desnecessário quando se usa `with`

## Métodos da connection

### `commit`
- Confirma alterações no banco
- Necessário após INSERT, UPDATE, DELETE, CREATE

### `rollback`
- Desfaz alterações não confirmadas
- Usado em caso de erro

## Boas práticas
- Sempre usar parâmetros em vez de concatenar SQL
- Sempre usar commit após comandos de escrita
- Centralizar conexão em um único módulo
- Manter SQL simples e explícito

## Modelo mental
- Connection = controle da transação
- Cursor = executor de SQL
