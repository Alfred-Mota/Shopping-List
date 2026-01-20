import type { ShoppingItem } from "./types";
import { fetchItems, createItem, deleteItem } from "./api";

function escapeHtml(s: string) {
    /**
     * Essa função tem como objetivo proteção contra entradas maliciosas
     * substitui caracteres especiais por texto comum evitando injeção de script
     */
  return s
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

export function mountApp(root: HTMLElement) {
  root.innerHTML = `
    <div class="container">
      <h1>Shopping List</h1>

      <div class="row">
        <input type="text" id="user_name" placeholder="Usuário (ex: ana)" />
        <input type="text" id="item_name" placeholder="Item (ex: leite)" />
        <input type="number" id="quantity" min="1" value="1" style="width:90px;" />
        <button id="addBtn">Adicionar</button>
      </div>

      <div class="row">
        <input type="text" id="filter_user" placeholder="Filtrar por usuário (opcional)" />
        <button id="listBtn">Buscar</button>
        <span id="status" class="status"></span>
      </div>

      <ul id="list" class="list"></ul>
    </div>
  `;

  // elementos
  const userInput = root.querySelector<HTMLInputElement>("#user_name")!;
  const itemInput = root.querySelector<HTMLInputElement>("#item_name")!;
  const qtyInput = root.querySelector<HTMLInputElement>("#quantity")!;
  const filterInput = root.querySelector<HTMLInputElement>("#filter_user")!;
  const addBtn = root.querySelector<HTMLButtonElement>("#addBtn")!;
  const listBtn = root.querySelector<HTMLButtonElement>("#listBtn")!;
  const statusEl = root.querySelector<HTMLSpanElement>("#status")!;
  const listEl = root.querySelector<HTMLUListElement>("#list")!;

  function setStatus(msg: string) {
    statusEl.textContent = msg;
  }

  function render(items: ShoppingItem[]) {
    if (items.length === 0) {
      listEl.innerHTML = `<li class="status">Sem itens.</li>`;
      return;
    }

    listEl.innerHTML = items
      .map(
        (it: ShoppingItem) => `
          <li class="card">
            <div>
              <div><strong>${escapeHtml(it.item_name)}</strong> (qtd: ${it.quantity})</div>
              <div class="meta">
                usuário: ${escapeHtml(it.user_name)} • id: ${it.id} • ${new Date(it.created_at).toLocaleString()}
              </div>
            </div>
            <button data-id="${it.id}">Remover</button>
          </li>
        `
      )
      .join("");

    // bind remove
    listEl.querySelectorAll<HTMLButtonElement>("button[data-id]").forEach((btn) => {
      btn.addEventListener("click", async () => {
        const id = Number(btn.dataset.id);
        try {
          setStatus("Removendo...");
          await deleteItem(id);
          setStatus("Removido!");
          await refresh();
        } catch (err) {
          setStatus(String(err));
        }
      });
    });
  }

  async function refresh() {
    try {
      setStatus("Carregando...");
      const items = await fetchItems(filterInput.value);
      render(items);
      setStatus(`OK • ${items.length} item(ns)`);
    } catch (err) {
      setStatus(String(err));
    }
  }

  listBtn.addEventListener("click", refresh);

  addBtn.addEventListener("click", async () => {
    const user_name = userInput.value.trim();
    const item_name = itemInput.value.trim();
    const quantity = Number(qtyInput.value);

    if (!user_name) return setStatus("Preencha o usuário.");
    if (!item_name) return setStatus("Preencha o item.");
    if (!Number.isFinite(quantity) || quantity < 1) return setStatus("Quantidade inválida.");

    try {
      setStatus("Salvando...");
      await createItem({ user_name, item_name, quantity });
      setStatus("Salvo!");

      itemInput.value = "";
      qtyInput.value = "1";

      await refresh();
    } catch (err) {
      setStatus(String(err));
    }
  });

  // carrega ao abrir
  refresh();
}
