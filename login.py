import tkinter as tk
from tkinter import messagebox

from telas import abrir_tela_por_tipo


ARQUIVO = "cadastros.txt"


def buscar_usuario(email, senha):

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                linha = linha.strip()

                if not linha:
                    continue

                dados = {}

                partes = linha.split("|")

                for parte in partes:

                    if ":" not in parte:
                        continue

                    chave, valor = parte.split(":", 1)

                    dados[chave.strip().lower()] = valor.strip()

                email_salvo = dados.get("e-mail", "")
                senha_salva = dados.get("senha", "")

                if (
                    email_salvo.lower() == email.lower()
                    and senha_salva == senha
                ):
                    return dados

    except FileNotFoundError:

        return None

    return None


def criar_tela_login():

    janela = tk.Tk()

    janela.title("Condomínio Feliz - Login")
    janela.geometry("400x350")

    tk.Label(
        janela,
        text="Condomínio Feliz",
        font=("Arial", 20, "bold")
    ).pack(pady=(30, 5))

    tk.Label(
        janela,
        text="Login",
        font=("Arial", 14)
    ).pack(pady=(0, 25))

    # E-mail

    tk.Label(
        janela,
        text="E-mail:"
    ).pack()

    entry_email = tk.Entry(
        janela,
        width=35
    )

    entry_email.pack()

    # Senha

    tk.Label(
        janela,
        text="Senha:"
    ).pack(pady=(15, 0))

    entry_senha = tk.Entry(
        janela,
        width=35,
        show="*"
    )

    entry_senha.pack()

    def fazer_login():

        email = entry_email.get().strip()
        senha = entry_senha.get()

        if not email:

            messagebox.showerror(
                "Erro",
                "Digite seu e-mail.",
                parent=janela
            )

            return

        if not senha:

            messagebox.showerror(
                "Erro",
                "Digite sua senha.",
                parent=janela
            )

            return

        usuario = buscar_usuario(
            email,
            senha
        )

        if usuario:

            nome = usuario.get(
                "nome",
                ""
            )

            tipo = usuario.get(
                "tipo",
                ""
            )

            unidade = usuario.get(
                "unidade",
                ""
            )

            janela.withdraw()

            abrir_tela_por_tipo(
                tipo,
                nome,
                janela,
                unidade
            )

        else:

            messagebox.showerror(
                "Login inválido",
                "E-mail ou senha incorretos.",
                parent=janela
            )

    tk.Button(
        janela,
        text="Entrar",
        width=20,
        height=2,
        command=fazer_login
    ).pack(pady=25)

    janela.mainloop()


if __name__ == "__main__":
    criar_tela_login()