import tkinter as tk
from tkinter import messagebox
from datetime import datetime

ARQUIVO = "reclamacoes.txt"


def sanitizar(texto):
    """Remove caracteres que quebrariam o formato do arquivo."""
    return texto.replace("|", "").replace("\r", "").strip()


def registrar_reclamacao(nome, unidade, texto):
    """Salva uma nova reclamação no arquivo, com nome, unidade e data/hora."""
    texto = sanitizar(texto).replace("\n", " ")
    nome = sanitizar(nome)
    unidade = sanitizar(unidade) if unidade else "-"
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(
            f"Nome: {nome} | Unidade: {unidade} | Data: {data} | "
            f"Reclamação: {texto} | Status: Pendente\n"
        )


def listar_reclamacoes():
    """Retorna uma lista de dicionários com todas as reclamações registradas."""
    reclamacoes = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                dados = {}
                for parte in linha.strip().split("|"):
                    if ":" in parte:
                        chave, valor = parte.split(":", 1)
                        dados[chave.strip().lower()] = valor.strip()
                if dados:
                    reclamacoes.append(dados)
    except FileNotFoundError:
        pass
    return reclamacoes


def tela_reclamacao_morador(nome, unidade=""):
    """Tela onde o morador escreve e envia uma reclamação."""
    janela = tk.Toplevel()
    janela.title("Nova Reclamação")
    janela.geometry("350x380")
    janela.grab_set()

    tk.Label(janela, text="Escreva sua reclamação", font=("Arial", 13, "bold")).pack(pady=(15, 0))

    if unidade and unidade != "-":
        tk.Label(janela, text=unidade, font=("Arial", 9), fg="gray").pack(pady=(0, 10))
    else:
        tk.Frame(janela, height=10).pack()

    texto_reclamacao = tk.Text(janela, width=38, height=12, wrap="word")
    texto_reclamacao.pack(padx=10)

    def enviar():
        conteudo = texto_reclamacao.get("1.0", "end").strip()
        if not conteudo:
            messagebox.showwarning("Atenção", "Escreva algo antes de enviar.", parent=janela)
            return
        if len(conteudo) > 1000:
            messagebox.showwarning("Atenção", "Texto muito longo (máx. 1000 caracteres).", parent=janela)
            return

        registrar_reclamacao(nome, unidade, conteudo)
        messagebox.showinfo("Enviado", "Sua reclamação foi registrada!", parent=janela)
        janela.destroy()

    tk.Button(janela, text="Enviar", command=enviar, width=15).pack(pady=15)


def tela_ver_reclamacoes_sindico():
    """Tela onde o síndico visualiza todas as reclamações registradas."""
    janela = tk.Toplevel()
    janela.title("Reclamações dos Moradores")
    janela.geometry("450x400")
    janela.grab_set()

    tk.Label(janela, text="Reclamações Recebidas", font=("Arial", 13, "bold")).pack(pady=(15, 10))

    frame = tk.Frame(janela)
    frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    caixa_texto = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set, state="disabled")
    caixa_texto.pack(fill="both", expand=True)
    scrollbar.config(command=caixa_texto.yview)

    reclamacoes = listar_reclamacoes()

    caixa_texto.config(state="normal")
    if not reclamacoes:
        caixa_texto.insert("end", "Nenhuma reclamação registrada até o momento.")
    else:
        for r in reversed(reclamacoes):  # mais recentes primeiro
            caixa_texto.insert("end", f"Morador: {r.get('nome', '—')}\n")
            caixa_texto.insert("end", f"Unidade: {r.get('unidade', '—')}\n")
            caixa_texto.insert("end", f"Data: {r.get('data', '—')}\n")
            caixa_texto.insert("end", f"Status: {r.get('status', '—')}\n")
            caixa_texto.insert("end", f"Reclamação: {r.get('reclamação', r.get('reclamacao', '—'))}\n")
            caixa_texto.insert("end", "-" * 45 + "\n\n")
    caixa_texto.config(state="disabled")

    tk.Button(janela, text="Fechar", command=janela.destroy, width=12).pack(pady=(0, 10))