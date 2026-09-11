import tkinter as tk
from tkinter import messagebox
from datetime import datetime

ARQUIVO = "encomendas.txt"


def sanitizar(texto):
    """Remove caracteres que quebrariam o formato do arquivo."""
    return texto.replace("|", "").replace("\r", "").strip()


def registrar_encomenda(unidade, descricao):
    """Salva uma nova encomenda no arquivo, com status inicial 'Aguardando retirada'."""
    unidade = sanitizar(unidade)
    descricao = sanitizar(descricao).replace("\n", " ")
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(
            f"Unidade: {unidade} | Descricao: {descricao} | Data: {data} | "
            f"Status: Aguardando retirada\n"
        )


def listar_encomendas():
    """Retorna a lista de encomendas (dicionários), na ordem em que estão no arquivo."""
    encomendas = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                dados = {}
                for parte in linha.split("|"):
                    if ":" in parte:
                        chave, valor = parte.split(":", 1)
                        dados[chave.strip().lower()] = valor.strip()
                if dados:
                    encomendas.append(dados)
    except FileNotFoundError:
        pass
    return encomendas


def salvar_encomendas(encomendas):
    """Reescreve o arquivo inteiro a partir da lista de encomendas (usado ao marcar retirada)."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for e in encomendas:
            f.write(
                f"Unidade: {e.get('unidade', '-')} | Descricao: {e.get('descricao', '-')} | "
                f"Data: {e.get('data', '-')} | Status: {e.get('status', '-')}\n"
            )


def marcar_retirada(indice, encomendas):
    """Marca a encomenda no índice dado (dentro da lista já carregada) como retirada e persiste."""
    if 0 <= indice < len(encomendas):
        encomendas[indice]["status"] = "Retirada"
        salvar_encomendas(encomendas)


def tela_registrar_encomenda_funcionario():
    """Tela onde o funcionário registra novas encomendas e marca as já retiradas."""
    janela = tk.Toplevel()
    janela.title("Encomendas")
    janela.geometry("380x480")
    janela.grab_set()

    tk.Label(janela, text="Registrar Encomenda", font=("Arial", 13, "bold")).pack(pady=(15, 10))

    tk.Label(janela, text="Unidade (ex: Bloco A - Apto 12):").pack()
    entry_unidade = tk.Entry(janela, width=36)
    entry_unidade.pack()

    tk.Label(janela, text="Descrição:").pack(pady=(10, 0))
    entry_descricao = tk.Entry(janela, width=36)
    entry_descricao.pack()

    tk.Label(janela, text="Encomendas registradas:").pack(pady=(15, 0))

    frame_lista = tk.Frame(janela)
    frame_lista.pack(fill="both", expand=True, padx=10, pady=(5, 5))

    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side="right", fill="y")

    lista = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set)
    lista.pack(fill="both", expand=True)
    scrollbar.config(command=lista.yview)

    encomendas = listar_encomendas()

    def preencher_lista():
        lista.delete(0, "end")
        for e in encomendas:
            texto = f"{e.get('unidade', '—')} | {e.get('descricao', '—')} | {e.get('status', '—')}"
            lista.insert("end", texto)

    preencher_lista()

    def registrar():
        unidade = entry_unidade.get().strip()
        descricao = entry_descricao.get().strip()

        if not unidade:
            messagebox.showerror("Erro", "Informe a unidade.", parent=janela)
            return
        if not descricao:
            messagebox.showerror("Erro", "Informe uma descrição da encomenda.", parent=janela)
            return

        registrar_encomenda(unidade, descricao)
        encomendas.clear()
        encomendas.extend(listar_encomendas())
        preencher_lista()
        entry_unidade.delete(0, "end")
        entry_descricao.delete(0, "end")
        messagebox.showinfo("Sucesso", "Encomenda registrada!", parent=janela)

    tk.Button(janela, text="Registrar", command=registrar, width=15).pack(pady=(5, 10))

    def marcar_selecionada():
        selecionado = lista.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma encomenda na lista.", parent=janela)
            return
        indice = selecionado[0]
        if encomendas[indice].get("status") == "Retirada":
            messagebox.showinfo("Info", "Essa encomenda já foi retirada.", parent=janela)
            return
        marcar_retirada(indice, encomendas)
        preencher_lista()

    tk.Button(
        janela, text="Marcar selecionada como retirada", command=marcar_selecionada, width=28
    ).pack(pady=(0, 10))
    tk.Button(janela, text="Fechar", command=janela.destroy, width=12).pack(pady=(0, 10))


def tela_ver_encomendas_morador(unidade):
    """Tela onde o morador vê as encomendas registradas para a sua unidade."""
    janela = tk.Toplevel()
    janela.title("Minhas Encomendas")
    janela.geometry("400x400")
    janela.grab_set()

    tk.Label(janela, text="Encomendas da Unidade", font=("Arial", 13, "bold")).pack(pady=(15, 10))

    if unidade and unidade != "-":
        tk.Label(janela, text=unidade, font=("Arial", 9), fg="gray").pack(pady=(0, 10))

    frame = tk.Frame(janela)
    frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    caixa_texto = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set, state="disabled")
    caixa_texto.pack(fill="both", expand=True)
    scrollbar.config(command=caixa_texto.yview)

    encomendas = [
        e for e in listar_encomendas()
        if e.get("unidade", "").lower() == (unidade or "").lower()
    ]

    caixa_texto.config(state="normal")
    if not encomendas:
        caixa_texto.insert("end", "Nenhuma encomenda registrada para sua unidade.")
    else:
        for e in reversed(encomendas):
            caixa_texto.insert("end", f"Descrição: {e.get('descricao', '—')}\n")
            caixa_texto.insert("end", f"Data: {e.get('data', '—')}\n")
            caixa_texto.insert("end", f"Status: {e.get('status', '—')}\n")
            caixa_texto.insert("end", "-" * 40 + "\n\n")
    caixa_texto.config(state="disabled")

    tk.Button(janela, text="Fechar", command=janela.destroy, width=12).pack(pady=(0, 10))