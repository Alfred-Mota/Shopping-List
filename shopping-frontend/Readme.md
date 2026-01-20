# 📌 Resumo do Frontend – Shopping List

## 🎯 Objetivo do Frontend

O frontend deste projeto foi criado com o objetivo de **entender o funcionamento real
da comunicação entre navegador e API**, antes de utilizar frameworks como React.

A ideia principal foi:
- aprender JavaScript/TypeScript no navegador
- entender o fluxo de dados entre frontend e backend
- evitar abstrações no início
- criar uma base sólida para evolução futura

---

## 🧰 Stack Utilizada (Frontend)

- **HTML** → estrutura da página
- **CSS** → estilização e layout
- **TypeScript** → JavaScript com tipagem
- **Vite** → ambiente de desenvolvimento e build

---

## 🗂️ Estrutura do Frontend

# 📌 Resumo do Frontend – Shopping List

## 🎯 Objetivo do Frontend

O frontend deste projeto foi criado com o objetivo de **entender o funcionamento real
da comunicação entre navegador e API**, antes de utilizar frameworks como React.

A ideia principal foi:
- aprender JavaScript/TypeScript no navegador
- entender o fluxo de dados entre frontend e backend
- evitar abstrações no início
- criar uma base sólida para evolução futura

---

## 🧰 Stack Utilizada (Frontend)

- **HTML** → estrutura da página
- **CSS** → estilização e layout
- **TypeScript** → JavaScript com tipagem
- **Vite** → ambiente de desenvolvimento e build

---

## 🗂️ Estrutura do Frontend

frontend/
├── src/
│ ├── main.ts
│ ├── api.ts
│ ├── ui.ts
│ ├── types.ts
│ └── styles.css
├── index.html


---

## 📁 Organização dos Arquivos

### `main.ts`
- Ponto de entrada da aplicação
- Inicializa o frontend
- Importa estilos e monta a interface
- Não contém lógica de negócio

---

### `api.ts`
Responsável por **toda comunicação com o backend**.

Funções principais:
- Buscar itens da API
- Criar novos itens
- Remover itens

Benefícios:
- Centraliza chamadas HTTP
- Facilita manutenção
- Evita repetição de código

---

### `ui.ts`
Responsável pela **interface e interação do usuário**.

Contém:
- Renderização da tela
- Manipulação do DOM
- Eventos de clique e formulário
- Atualização da lista de compras

Aqui está concentrada a lógica visual da aplicação.

---

### `types.ts`
Define os **tipos TypeScript** utilizados no frontend.

Exemplos:
- Estrutura de um item de compra
- Payloads enviados para a API

Benefícios:
- Evita erros de tipo
- Facilita leitura do código
- Melhora autocomplete e manutenção

---

### `styles.css`
Responsável pela estilização da aplicação.

Inclui:
- Layout básico
- Estilos de botões
- Hovers com gradiente
- Uso de `data-*` attributes
- Feedback visual para ações do usuário

---

## 🔄 Comunicação com o Backend

A comunicação é feita utilizando a **Fetch API**.

- Requisições HTTP diretas (`GET`, `POST`, `DELETE`)
- Uso de `async/await`
- Tratamento de erros de rede e HTTP
- Envio e recebimento de JSON

O backend é tratado como a **única fonte da verdade**.

---

## 🔁 Conceito do método `refresh()`

O método `refresh()` foi criado para manter a interface sincronizada com o backend.

Funções do `refresh()`:
- Buscar os dados atualizados da API
- Atualizar a lista exibida
- Garantir consistência da interface
- Centralizar a lógica de atualização

Sempre que algo muda no banco (criar ou remover item), o `refresh()` é chamado.

---

## 🔐 Segurança no Frontend

Mesmo sendo um projeto de estudo, foram aplicados conceitos importantes:

- Uso de `escapeHtml` para evitar XSS
- Cuidado com uso de `innerHTML`
- Preferência por `textContent` quando possível
- Uso de parâmetros ao montar URLs
- Separação clara entre dados e apresentação

---

## 🎨 CSS e Experiência do Usuário

Foram utilizados recursos modernos de CSS:
- Hover com `linear-gradient`
- Transições suaves
- Uso de `data-id` para integração com JavaScript
- Feedback visual de status (loading, erro, sucesso)

O foco foi manter a interface simples, clara e funcional.

---

## 📚 Conceitos Aprendidos e Consolidados

- TypeScript como JavaScript tipado
- Diferença entre `string` e `String`
- Tipagem de respostas da API
- Manipulação do DOM sem frameworks
- Fetch API
- Tratamento de erros
- Organização modular do frontend
- Estado sincronizado com backend
- Boas práticas básicas de segurança

---

## 🚀 Planejamento Futuro

Este frontend servirá como base para:

- Migração para **React**
- Uso de estado reativo
- Componentização
- Contexto de autenticação
- Consumo de APIs protegidas com JWT

A migração será feita de forma consciente, reaproveitando
todo o aprendizado obtido neste frontend vanilla.

---

## 🧠 Filosofia do Frontend

Este frontend foi desenvolvido com a seguinte filosofia:

- Entender antes de abstrair
- Controlar o DOM manualmente antes de frameworks
- Priorizar clareza e aprendizado
- Criar uma base reutilizável

Esse conhecimento facilita a adoção de qualquer framework no futuro.

---

**Fim do documento**
