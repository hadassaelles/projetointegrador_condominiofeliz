import tkinter as tk

from cadastro import abrir_cadastro
from reclamacoes import tela_reclamacao_morador, tela_ver_reclamacoes_sindico
from denuncias import tela_denuncia_morador, tela_ver_denuncias_sindico
from encomendas import tela_registrar_encomenda_funcionario, tela_ver_encomendas_morador
from reserva import tela_reserva_morador, tela_gerenciar_reservas_sindico, tela_reservas_dia_funcionario
from mural import tela_publicar_comunicado, tela_ver_mural


def fechar_sistema(janela_login):
    janela_login.destroy()


def primeiro_nome(nome):
    return nome.strip().split()[0]


def tela_morador(nome, janela_login, unidade=""):

    janela = tk.Toplevel()

    janela.title("Área do Morador")
    janela.geometry("400x500")

    janela.protocol(
        "WM_DELETE_WINDOW",
        lambda: fechar_sistema(janela_login)
    )

    tk.Label(
        janela,
        text=f"Bem-vindo(a), {primeiro_nome(nome)} (Morador)",
        font=("Arial", 16, "bold")
    ).pack(pady=(25, 0))

    if unidade and unidade != "-":
        tk.Label(
            janela,
            text=unidade,
            font=("Arial", 10),
            fg="gray"
        ).pack(pady=(0, 20))
    else:
        tk.Frame(janela, height=20).pack()

    tk.Button(
        janela,
        text="Reclamação",
        width=30,
        height=2,
        command=lambda: tela_reclamacao_morador(nome, unidade)
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Sugestão / Denúncia",
        width=30,
        height=2,
        command=lambda: tela_denuncia_morador(nome, unidade)
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Encomenda",
        width=30,
        height=2,
        command=lambda: tela_ver_encomendas_morador(unidade)
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Reserva de Áreas",
        width=30,
        height=2,
        command=lambda: tela_reserva_morador(nome, unidade)
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Mural de Comunicados",
        width=30,
        height=2,
        command=tela_ver_mural
    ).pack(pady=8)


def tela_funcionario(nome, janela_login):

    janela = tk.Toplevel()

    janela.title("Área do Funcionário")
    janela.geometry("400x500")

    janela.protocol(
        "WM_DELETE_WINDOW",
        lambda: fechar_sistema(janela_login)
    )

    tk.Label(
        janela,
        text=f"Bem-vindo(a), {primeiro_nome(nome)} (Funcionário)",
        font=("Arial", 16, "bold")
    ).pack(pady=25)

    tk.Label(
        janela,
        text="Painel do Funcionário",
        font=("Arial", 12)
    ).pack(pady=(0, 15))

    tk.Button(
        janela,
        text="Registrar Encomenda",
        width=30,
        height=2,
        command=tela_registrar_encomenda_funcionario
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Ver Reservas do Dia",
        width=30,
        height=2,
        command=tela_reservas_dia_funcionario
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Ver Mural de Comunicados",
        width=30,
        height=2,
        command=tela_ver_mural
    ).pack(pady=8)


def tela_sindico(nome, janela_login):

    janela = tk.Toplevel()

    janela.title("Área do Síndico")
    janela.geometry("420x550")

    janela.protocol(
        "WM_DELETE_WINDOW",
        lambda: fechar_sistema(janela_login)
    )

    tk.Label(
        janela,
        text=f"Bem-vindo(a), {primeiro_nome(nome)} (Síndico)",
        font=("Arial", 16, "bold")
    ).pack(pady=25)

    tk.Label(
        janela,
        text="Painel do Síndico",
        font=("Arial", 12)
    ).pack(pady=(0, 15))

    tk.Button(
        janela,
        text="Gerenciar Reclamações",
        width=30,
        height=2,
        command=tela_ver_reclamacoes_sindico
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Gerenciar Denúncias",
        width=30,
        height=2,
        command=tela_ver_denuncias_sindico
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Gerenciar Reservas",
        width=30,
        height=2,
        command=tela_gerenciar_reservas_sindico
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Publicar Comunicado",
        width=30,
        height=2,
        command=lambda: tela_publicar_comunicado(janela)
    ).pack(pady=8)

    tk.Button(
        janela,
        text="Cadastrar Morador / Funcionário",
        width=30,
        height=2,
        command=lambda: abrir_cadastro(janela)
    ).pack(pady=8)


def abrir_tela_por_tipo(tipo, nome, janela_login, unidade=""):

    tipo = tipo.strip().lower()

    if tipo == "síndico" or tipo == "sindico":

        tela_sindico(
            nome,
            janela_login
        )

    elif tipo == "funcionário" or tipo == "funcionario":

        tela_funcionario(
            nome,
            janela_login
        )

    elif tipo == "morador":

        tela_morador(
            nome,
            janela_login,

            unidade
        )