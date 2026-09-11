import tkinter as tk
from tkinter import messagebox
from datetime import datetime

ARQUIVO = "mural.txt"


def sanitizar(texto):
    """Remove caracteres que quebrariam o formato do arquivo."""
    return texto.replace("|", "").replace("\r", "").strip()


def publicar_comunicado(titulo, texto):
    titulo = sanitizar(titulo)
    texto = sanitizar(texto).replace("\n", " ")
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"Titulo: {titulo} | Data: {data} | Texto: {texto}\n")


def listar_comunicados():
    """Retorna a lista de comunicados (dicionários), na ordem em que estão no arquivo."""
    comunicados = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                dados = {}
                for parte in linha.strip().split("|"):
                    if ":" in parte:
                        chave, valor = parte.split(":", 1)
                        dados[chave.strip().lower()] = valor.strip()
                if dados:
                    comunicados.append(dados)
    except FileNotFoundError:
        pass
    return comunicados


def tela_publicar_comunicado(janela_pai=None):
    """Tela onde o síndico redige e publica um novo comunicado."""
    janela = tk.Toplevel(janela_pai)
    janela.title("Publicar Comunicado")
    janela.geometry("340x360")
    janela.grab_set()

    tk.Label(janela, text="Novo Comunicado", font=("Arial", 13, "bold")).pack(pady=(15, 10))

    tk.Label(janela, text="Título:").pack()
    entry_titulo = tk.Entry(janela, width=36)
    entry_titulo.pack()

    tk.Label(janela, text="Texto:").pack(pady=(10, 0))
    texto_widget = tk.Text(janela, width=38, height=10, wrap="word")
    texto_widget.pack(padx=10)

    def publicar():
        titulo = entry_titulo.get().strip()
        conteudo = texto_widget.get("1.0", "end").strip()

        if not titulo:
            messagebox.showerror("Erro", "Informe um título.", parent=janela)
            return
        if not conteudo:
            messagebox.showerror("Erro", "Escreva o texto do comunicado.", parent=janela)
            return

        publicar_comunicado(titulo, conteudo)
        messagebox.showinfo("Sucesso", "Comunicado publicado!", parent=janela)
        janela.destroy()

    tk.Button(janela, text="Publicar", command=publicar, width=15).pack(pady=15)


def tela_ver_mural():
    """Tela onde moradores e funcionários visualizam os comunicados publicados."""
    janela = tk.Toplevel()
    janela.title("Mural de Comunicados")
    janela.geometry("420x420")
    janela.grab_set()

    tk.Label(janela, text="Mural de Comunicados", font=("Arial", 13, "bold")).pack(pady=(15, 10))

    frame = tk.Frame(janela)
    frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    caixa_texto = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set, state="disabled")
    caixa_texto.pack(fill="both", expand=True)
    scrollbar.config(command=caixa_texto.yview)

    comunicados = listar_comunicados()

    caixa_texto.config(state="normal")
    if not comunicados:
        caixa_texto.insert("end", "Nenhum comunicado publicado até o momento.")
    else:
        caixa_texto.tag_config("titulo", font=("Arial", 10, "bold"))
        for c in reversed(comunicados):
            caixa_texto.insert("end", f"{c.get('titulo', '—')}\n", "titulo")
            caixa_texto.insert("end", f"({c.get('data', '—')})\n\n")
            caixa_texto.insert("end", f"{c.get('texto', '—')}\n")
            caixa_texto.insert("end", "-" * 40 + "\n\n")
    caixa_texto.config(state="disabled")

    tk.Button(janela, text="Fechar", command=janela.destroy, width=12).pack(pady=(0, 10))