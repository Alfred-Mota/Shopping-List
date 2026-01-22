# 📌 Frontend — Shopping List (TypeScript Vanilla)

Este documento descreve a estrutura, decisões e conceitos aplicados no **frontend** do projeto Shopping List.

O frontend foi desenvolvido **sem frameworks**, com foco em aprendizado real do funcionamento do navegador e da comunicação com uma API.

---

## 🎯 Objetivo do Frontend

O objetivo principal foi **entender como o frontend funciona de verdade**, antes de utilizar abstrações como React.

Este frontend foi criado para:
- aprender JavaScript e TypeScript no navegador
- entender o fluxo HTTP entre frontend e backend
- manipular o DOM manualmente
- evitar abstrações no início
- criar uma base sólida para evolução futura

---

## 🧰 Stack Utilizada

- **HTML** → estrutura da aplicação
- **CSS** → estilização e layout
- **TypeScript** → JavaScript com tipagem
- **Vite** → ambiente de desenvolvimento e build

---

## 🗂️ Estrutura do Frontend

frontend/
├── src/
│   ├── main.ts
│   ├── api.ts
│   ├── ui.ts
│   ├── http.ts
│   ├── types.ts
│   └── styles.css
└── index.html

---

## 📁 Organização dos Arquivos

### `main.ts`
- Ponto de entrada da aplicação
- Inicializa o frontend
- Importa estilos
- Dispara a montagem da interface
- Não contém lógica de negócio

---

### `http.ts` (Wrapper HTTP)
Arquivo responsável por **centralizar e padronizar as requisições HTTP**.

Responsabilidades:
- Encapsular o uso da Fetch API
- Adicionar headers comuns automaticamente
- Injetar o token JWT no header `Authorization`
- Centralizar tratamento de erros HTTP (401, 403, etc.)

Benefícios:
- Menos repetição de código
- Código mais limpo e legível
- Facilita manutenção e evolução
- Preparação para APIs autenticadas

---

### `api.ts`
Responsável por **toda a comunicação com o backend**.

Funções principais:
- Buscar itens da API
- Criar novos itens
- Remover itens

Utiliza o wrapper `http.ts`, evitando chamadas diretas à Fetch API.

Benefícios:
- Backend tratado como fonte da verdade
- Contrato claro entre frontend e backend
- Facilita mudanças futuras (ex: React)

---

### `ui.ts`
Responsável pela **interface e interação do usuário**.

Contém:
- Renderização da tela
- Manipulação do DOM
- Eventos de clique e formulários
- Atualização da lista de compras
- Feedback visual ao usuário

Aqui fica concentrada toda a lógica visual da aplicação.

---

### `types.ts`
Define os **tipos TypeScript** utilizados no frontend.

Exemplos:
- Estrutura de um item de compra
- Payloads enviados para a API
- Tipos de resposta do backend

Benefícios:
- Evita erros de tipo
- Melhora legibilidade
- Ajuda no autocomplete
- Facilita refatorações

---

### `styles.css`
Responsável pela estilização da aplicação.

Inclui:
- Layout básico
- Estilos de botões
- Hover com gradiente
- Transições suaves
- Uso de `data-*` attributes
- Feedback visual (loading, erro, sucesso)

---

## 🔄 Comunicação com o Backend

A comunicação é feita utilizando:
- Fetch API
- `async / await`
- JSON como formato padrão

Características:
- Requisições HTTP (`GET`, `POST`, `DELETE`)
- Tratamento de erros de rede e HTTP
- Backend como **única fonte da verdade**
- Nenhuma lógica de negócio no frontend

---

## 🔁 Conceito do método `refresh()`

O método `refresh()` foi criado para manter a interface sincronizada com o backend.

Responsabilidades:
- Buscar os dados atualizados da API
- Atualizar a lista exibida
- Garantir consistência da interface
- Centralizar a lógica de atualização

Sempre que algo muda no backend (criar ou remover item), o `refresh()` é chamado.

---

## 🔐 Segurança no Frontend

Mesmo sendo um projeto de estudo, foram aplicados cuidados importantes:

- Uso de `escapeHtml` para evitar XSS
- Cuidado com `innerHTML`
- Preferência por `textContent`
- Separação clara entre dados e apresentação
- Token JWT armazenado no `localStorage`
- Envio do token apenas via header HTTP

---

## 🎨 CSS e Experiência do Usuário

Foram utilizados recursos modernos de CSS:
- Gradientes
- Transições
- Feedback visual
- Interface simples e clara

O foco foi funcionalidade e clareza, não design complexo.

---

## 📚 Conceitos Aprendidos e Consolidados

- TypeScript como JavaScript tipado
- Organização modular do frontend
- Manipulação manual do DOM
- Fetch API
- Tratamento de erros
- Comunicação frontend ↔ backend
- Uso de JWT no frontend
- Backend como fonte da verdade
- Preparação para frameworks modernos

---

## 🚀 Planejamento Futuro

Este frontend servirá como base para:
- Migração para **React**
- Componentização
- Estado reativo
- Contexto de autenticação
- Consumo de APIs protegidas

A migração será feita de forma consciente, reaproveitando
todo o aprendizado adquirido neste frontend vanilla.

---

## 🧠 Filosofia do Frontend

- Entender antes de abstrair
- Controlar o DOM antes de frameworks
- Priorizar aprendizado real
- Criar uma base reutilizável e sólida

Esse conhecimento facilita a adoção de qualquer framework no futuro.

---

**Fim do documento**
