import tkinter as tk
from tkinter import messagebox
import re
import hashlib

ARQUIVO = "cadastros.txt"

# Regras de validação (regex)
REGEX_NOME = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$"                       # só letras e espaços
REGEX_EMAIL = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"           # formato básico de e-mail
REGEX_SENHA = r"^(?=.*[A-Za-z])(?=.*\d).{6,}$"               # mín. 6 caracteres, letra + número
REGEX_UNIDADE = r"^[A-Za-zÀ-ÖØ-öø-ÿ0-9\s\-]+$"               # letras, números, espaço e hífen

TIPOS_VALIDOS = ["Síndico", "Morador", "Funcionário"]
CONDICOES_VALIDAS = ["Proprietário", "Inquilino"]
TIPOS_IMOVEL = ["Apartamento", "Casa"]


def limpar_cpf(cpf):
    """Remove pontos, traço e espaços, deixando só os dígitos."""
    return re.sub(r"\D", "", cpf)


def validar_cpf(cpf):
    """Valida CPF pelo algoritmo oficial dos dígitos verificadores."""
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    resto = 0 if resto == 10 else resto
    if resto != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    resto = 0 if resto == 10 else resto
    if resto != int(cpf[10]):
        return False

    return True


def validar_nome(nome):
    if not nome:
        return "O nome é obrigatório."
    if not re.match(REGEX_NOME, nome):
        return "O nome não pode conter números ou símbolos."
    return None


def validar_email(email):
    if not email:
        return "O e-mail é obrigatório."
    if not re.match(REGEX_EMAIL, email):
        return "E-mail inválido. Use o formato nome@exemplo.com"
    return None


def validar_cpf_campo(cpf):
    if not cpf:
        return "O CPF é obrigatório."
    if not validar_cpf(cpf):
        return "CPF inválido. Confira os números digitados."
    return None


def validar_senha(senha):
    if not senha:
        return "A senha é obrigatória."
    if not re.match(REGEX_SENHA, senha):
        return "A senha deve ter no mínimo 6 caracteres, com letras e números."
    return None


def validar_campo_unidade(valor, nome_campo):
    if not valor:
        return f"O campo {nome_campo} é obrigatório."
    if not re.match(REGEX_UNIDADE, valor):
        return f"{nome_campo} contém caracteres inválidos."
    return None


def sanitizar(texto):
    """Remove caracteres perigosos para evitar quebra do arquivo ou injeção de conteúdo."""
    return texto.replace("|", "").replace("\n", "").replace("\r", "").strip()


def hash_senha(senha):
    """Nunca salvamos a senha em texto puro — guardamos apenas o hash dela."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def email_ja_cadastrado(email):
    """Verifica se o e-mail já existe no arquivo de cadastros."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                for parte in linha.split("|"):
                    if parte.strip().lower().startswith("e-mail:"):
                        email_salvo = parte.split(":", 1)[1].strip().lower()
                        if email_salvo == email.lower():
                            return True
    except FileNotFoundError:
        return False
    return False


def cpf_ja_cadastrado(cpf):
    """Verifica se o CPF já existe no arquivo de cadastros."""
    cpf = limpar_cpf(cpf)
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                for parte in linha.split("|"):
                    if parte.strip().lower().startswith("cpf:"):
                        cpf_salvo = limpar_cpf(parte.split(":", 1)[1])
                        if cpf_salvo == cpf:
                            return True
    except FileNotFoundError:
        return False
    return False


def abrir_cadastro(janela_pai=None, on_sucesso=None):
    """
    Abre a tela de cadastro.
    janela_pai: janela que originou a chamada (ex: tela de login ou painel do síndico).
    on_sucesso: função chamada com (nome, email, tipo, unidade) após cadastro bem-sucedido.
                'unidade' vem vazia ("") quando o tipo não é Morador.
    """
    janela = tk.Toplevel(janela_pai) if janela_pai else tk.Tk()
    janela.title("Cadastro")
    janela.geometry("340x620")
    janela.grab_set()

    tk.Label(janela, text="Cadastro", font=("Arial", 14, "bold")).pack(pady=(15, 10))

    tk.Label(janela, text="Nome:").pack()
    entry_nome = tk.Entry(janela, width=32)
    entry_nome.pack()

    tk.Label(janela, text="E-mail:").pack(pady=(10, 0))
    entry_email = tk.Entry(janela, width=32)
    entry_email.pack()

    tk.Label(janela, text="CPF:").pack(pady=(10, 0))
    entry_cpf = tk.Entry(janela, width=32)
    entry_cpf.pack()

    tk.Label(janela, text="Senha:").pack(pady=(10, 0))
    entry_senha = tk.Entry(janela, width=32, show="*")
    entry_senha.pack()

    tk.Label(janela, text="Confirmar senha:").pack(pady=(10, 0))
    entry_confirmar = tk.Entry(janela, width=32, show="*")
    entry_confirmar.pack()

    tk.Label(janela, text="Você é:").pack(pady=(10, 0))
    tipo_var = tk.StringVar(value=TIPOS_VALIDOS[1])  # padrão: Morador
    for tipo in TIPOS_VALIDOS:
        tk.Radiobutton(janela, text=tipo, variable=tipo_var, value=tipo).pack(anchor="w", padx=90)

    # ---- Bloco de campos exclusivos do morador (condição + endereço) ----
    frame_morador = tk.Frame(janela)

    tk.Label(frame_morador, text="Condição:").pack(pady=(5, 0))
    condicao_var = tk.StringVar(value=CONDICOES_VALIDAS[0])
    frame_condicao = tk.Frame(frame_morador)
    frame_condicao.pack()
    for condicao in CONDICOES_VALIDAS:
        tk.Radiobutton(frame_condicao, text=condicao, variable=condicao_var, value=condicao).pack(side="left", padx=5)

    tk.Label(frame_morador, text="Tipo de imóvel:").pack(pady=(10, 0))
    imovel_var = tk.StringVar(value=TIPOS_IMOVEL[0])
    frame_imovel = tk.Frame(frame_morador)
    frame_imovel.pack()
    for imovel in TIPOS_IMOVEL:
        tk.Radiobutton(frame_imovel, text=imovel, variable=imovel_var, value=imovel).pack(side="left", padx=5)

    # Campos de apartamento (bloco + número do apto)
    frame_apartamento = tk.Frame(frame_morador)
    tk.Label(frame_apartamento, text="Bloco:").pack(pady=(8, 0))
    entry_bloco = tk.Entry(frame_apartamento, width=20)
    entry_bloco.pack()
    tk.Label(frame_apartamento, text="Apartamento (nº):").pack(pady=(8, 0))
    entry_apto = tk.Entry(frame_apartamento, width=20)
    entry_apto.pack()

    # Campo de casa (número da casa)
    frame_casa = tk.Frame(frame_morador)
    tk.Label(frame_casa, text="Número da casa:").pack(pady=(8, 0))
    entry_casa = tk.Entry(frame_casa, width=20)
    entry_casa.pack()

    def atualizar_campos_imovel(*_):
        if imovel_var.get() == "Apartamento":
            frame_casa.pack_forget()
            frame_apartamento.pack()
        else:
            frame_apartamento.pack_forget()
            frame_casa.pack()

    imovel_var.trace_add("write", atualizar_campos_imovel)
    atualizar_campos_imovel()

    def atualizar_campos_tipo(*_):
        if tipo_var.get() == "Morador":
            frame_morador.pack(pady=(5, 0))
        else:
            frame_morador.pack_forget()

    tipo_var.trace_add("write", atualizar_campos_tipo)
    atualizar_campos_tipo()

    def salvar_cadastro():
        nome = entry_nome.get().strip()
        email = entry_email.get().strip()
        cpf = entry_cpf.get().strip()
        senha = entry_senha.get()
        confirmar = entry_confirmar.get()
        tipo = tipo_var.get()

        erro = (
            validar_nome(nome)
            or validar_email(email)
            or validar_cpf_campo(cpf)
            or validar_senha(senha)
        )
        if erro:
            messagebox.showerror("Erro de validação", erro, parent=janela)
            return

        if senha != confirmar:
            messagebox.showerror("Erro de validação", "As senhas não coincidem.", parent=janela)
            return

        # Campos exclusivos de morador
        condicao = "-"
        unidade = "-"
        if tipo == "Morador":
            condicao = condicao_var.get()

            if imovel_var.get() == "Apartamento":
                bloco = entry_bloco.get().strip()
                apto = entry_apto.get().strip()
                erro = (
                    validar_campo_unidade(bloco, "Bloco")
                    or validar_campo_unidade(apto, "Apartamento")
                )
                if erro:
                    messagebox.showerror("Erro de validação", erro, parent=janela)
                    return
                unidade = f"Bloco {sanitizar(bloco)} - Apto {sanitizar(apto)}"
            else:
                casa = entry_casa.get().strip()
                erro = validar_campo_unidade(casa, "Número da casa")
                if erro:
                    messagebox.showerror("Erro de validação", erro, parent=janela)
                    return
                unidade = f"Casa {sanitizar(casa)}"

        if email_ja_cadastrado(email):
            messagebox.showerror("Cadastro duplicado", "Este e-mail já está cadastrado!", parent=janela)
            return

        if cpf_ja_cadastrado(cpf):
            messagebox.showerror("Cadastro duplicado", "Este CPF já está cadastrado!", parent=janela)
            return

        nome_s = sanitizar(nome)
        email_s = sanitizar(email)
        cpf_s = limpar_cpf(cpf)
        senha_hash = hash_senha(senha)

        try:
            with open(ARQUIVO, "a", encoding="utf-8") as f:
                f.write(
                    f"Nome: {nome_s} | E-mail: {email_s} | CPF: {cpf_s} | "
                    f"Senha: {senha_hash} | Tipo: {tipo} | "
                    f"Condicao: {condicao} | Unidade: {unidade}\n"
                )
        except OSError:
            messagebox.showerror("Erro", "Não foi possível salvar o cadastro.", parent=janela)
            return

        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!", parent=janela)
        janela.destroy()

        if on_sucesso:
            on_sucesso(nome_s, email_s, tipo, unidade if tipo == "Morador" else "")

    tk.Button(janela, text="Cadastrar", command=salvar_cadastro, width=15).pack(pady=20)

    if janela_pai is None:
        janela.mainloop()


if __name__ == "__main__":
    abrir_cadastro()