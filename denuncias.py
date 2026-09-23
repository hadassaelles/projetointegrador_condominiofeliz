import tkinter as tk
from tkinter import messagebox
from datetime import datetime

ARQUIVO = "denuncias.txt"

TIPOS_VALIDOS = ["Sugestão", "Denúncia"]


def sanitizar(texto):
    """Remove caracteres que quebrariam o formato do arquivo."""
    return texto.replace("|", "").replace("\r", "").strip()


def registrar_denuncia(nome, unidade, tipo, texto):
    """Salva uma nova sugestão/denúncia no arquivo, com nome, unidade, tipo e data/hora."""
    texto = sanitizar(texto).replace("\n", " ")
    nome = sanitizar(nome)
    unidade = sanitizar(unidade) if unidade else "-"

    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(
            f"Nome: {nome} | Unidade: {unidade} | Tipo: {tipo} | Data: {data} | "
            f"Texto: {texto} | Status: Pendente\n"
        )


def listar_denuncias():
    """Retorna uma lista de dicionários com todas as sugestões/denúncias registradas."""
    registros = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                dados = {}
                for parte in linha.strip().split("|"):
                    if ":" in parte:
                        chave, valor = parte.split(":", 1)
                        dados[chave.strip().lower()] = valor.strip()
                if dados:
                    registros.append(dados)
    except FileNotFoundError:
        pass
    return registros


def tela_denuncia_morador(nome, unidade=""):
    """Tela onde o morador registra uma sugestão ou denúncia."""
    janela = tk.Toplevel()
    janela.title("Sugestão / Denúncia")
    janela.geometry("350x430")
    janela.grab_set()

    tk.Label(janela, text="Sugestão ou Denúncia", font=("Arial", 13, "bold")).pack(pady=(15, 0))

    if unidade and unidade != "-":
        tk.Label(janela, text=unidade, font=("Arial", 9), fg="gray").pack(pady=(0, 5))
    else:
        tk.Frame(janela, height=5).pack()

    tipo_var = tk.StringVar(value=TIPOS_VALIDOS[0])
    frame_tipo = tk.Frame(janela)
    frame_tipo.pack(pady=(5, 10))
    for tipo in TIPOS_VALIDOS:
        tk.Radiobutton(frame_tipo, text=tipo, variable=tipo_var, value=tipo).pack(side="left", padx=10)

    texto_widget = tk.Text(janela, width=38, height=12, wrap="word")
    texto_widget.pack(padx=10)

    def enviar():
        conteudo = texto_widget.get("1.0", "end").strip()
        if not conteudo:
            messagebox.showwarning("Atenção", "Escreva algo antes de enviar.", parent=janela)
            return
        if len(conteudo) > 1000:
            messagebox.showwarning("Atenção", "Texto muito longo (máx. 1000 caracteres).", parent=janela)
            return

        registrar_denuncia(nome, unidade, tipo_var.get(), conteudo)
        messagebox.showinfo("Enviado", "Seu registro foi enviado!", parent=janela)
        janela.destroy()

    tk.Button(janela, text="Enviar", command=enviar, width=15).pack(pady=15)


def tela_ver_denuncias_sindico():
    """Tela onde o síndico visualiza todas as sugestões e denúncias registradas."""
    janela = tk.Toplevel()
    janela.title("Sugestões e Denúncias")
    janela.geometry("450x400")
    janela.grab_set()

    tk.Label(janela, text="Sugestões e Denúncias Recebidas", font=("Arial", 13, "bold")).pack(pady=(15, 10))

    frame = tk.Frame(janela)
    frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    caixa_texto = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set, state="disabled")
    caixa_texto.pack(fill="both", expand=True)
    scrollbar.config(command=caixa_texto.yview)

    registros = listar_denuncias()

    caixa_texto.config(state="normal")
    if not registros:
        caixa_texto.insert("end", "Nenhuma sugestão ou denúncia registrada até o momento.")
    else:
        for r in reversed(registros):
            caixa_texto.insert("end", f"Morador: {r.get('nome', '—')}\n")
            caixa_texto.insert("end", f"Unidade: {r.get('unidade', '—')}\n")
            caixa_texto.insert("end", f"Tipo: {r.get('tipo', '—')}\n")
            caixa_texto.insert("end", f"Data: {r.get('data', '—')}\n")
            caixa_texto.insert("end", f"Status: {r.get('status', '—')}\n")
            caixa_texto.insert("end", f"Texto: {r.get('texto', '—')}\n")
            caixa_texto.insert("end", "-" * 45 + "\n\n")
    caixa_texto.config(state="disabled")

    tk.Button(janela, text="Fechar", command=janela.destroy, width=12).pack(pady=(0, 10))