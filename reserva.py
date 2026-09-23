import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re

ARQUIVO = "reservas.txt"

AREAS_VALIDAS = ["Salão de Festas", "Churrasqueira", "Quadra Poliesportiva", "Piscina"]

REGEX_DATA = r"^\d{2}/\d{2}/\d{4}$"


def sanitizar(texto):
    """Remove caracteres que quebrariam o formato do arquivo."""
    return texto.replace("|", "").replace("\r", "").strip()


def validar_data(data_texto):
    if not data_texto:
        return "A data é obrigatória."
    if not re.match(REGEX_DATA, data_texto):
        return "Data inválida. Use o formato dd/mm/aaaa."
    try:
        data = datetime.strptime(data_texto, "%d/%m/%Y")
    except ValueError:
        return "Data inválida."
    if data.date() < datetime.now().date():
        return "Não é possível reservar em uma data passada."
    return None


def validar_horario(horario):
    if not horario:
        return "O horário é obrigatório."
    return None


def registrar_reserva(nome, unidade, area, data_texto, horario):
    nome = sanitizar(nome)
    unidade = sanitizar(unidade) if unidade else "-"
    area = sanitizar(area)
    data_texto = sanitizar(data_texto)
    horario = sanitizar(horario)

    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(
            f"Nome: {nome} | Unidade: {unidade} | Area: {area} | Data: {data_texto} | "
            f"Horario: {horario} | Status: Confirmada\n"
        )


def listar_reservas():
    """Retorna a lista de reservas (dicionários), na ordem em que estão no arquivo."""
    reservas = []
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
                    reservas.append(dados)
    except FileNotFoundError:
        pass
    return reservas


def salvar_reservas(reservas):
    """Reescreve o arquivo inteiro a partir da lista de reservas (usado ao cancelar)."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for r in reservas:
            f.write(
                f"Nome: {r.get('nome', '-')} | Unidade: {r.get('unidade', '-')} | "
                f"Area: {r.get('area', '-')} | Data: {r.get('data', '-')} | "
                f"Horario: {r.get('horario', '-')} | Status: {r.get('status', '-')}\n"
            )


def cancelar_reserva(indice, reservas):
    """Marca a reserva no índice dado (dentro da lista já carregada) como cancelada e persiste."""
    if 0 <= indice < len(reservas):
        reservas[indice]["status"] = "Cancelada"
        salvar_reservas(reservas)


def tela_reserva_morador(nome, unidade=""):
    """Tela onde o morador reserva uma área comum."""
    janela = tk.Toplevel()
    janela.title("Reserva de Áreas")
    janela.geometry("320x340")
    janela.grab_set()

    tk.Label(janela, text="Reservar Área Comum", font=("Arial", 13, "bold")).pack(pady=(15, 10))

    tk.Label(janela, text="Área:").pack()
    area_var = tk.StringVar(value=AREAS_VALIDAS[0])
    tk.OptionMenu(janela, area_var, *AREAS_VALIDAS).pack()

    tk.Label(janela, text="Data (dd/mm/aaaa):").pack(pady=(10, 0))
    entry_data = tk.Entry(janela, width=20)
    entry_data.pack()

    tk.Label(janela, text="Horário (ex: 14:00 às 16:00):").pack(pady=(10, 0))
    entry_horario = tk.Entry(janela, width=20)
    entry_horario.pack()

    def salvar():
        data_texto = entry_data.get().strip()
        horario = entry_horario.get().strip()

        erro = validar_data(data_texto) or validar_horario(horario)
        if erro:
            messagebox.showerror("Erro de validação", erro, parent=janela)
            return

        registrar_reserva(nome, unidade, area_var.get(), data_texto, horario)
        messagebox.showinfo("Sucesso", "Reserva registrada!", parent=janela)
        janela.destroy()

    tk.Button(janela, text="Reservar", command=salvar, width=15).pack(pady=20)


def tela_gerenciar_reservas_sindico():
    """Tela onde o síndico visualiza e cancela reservas."""
    janela = tk.Toplevel()
    janela.title("Gerenciar Reservas")
    janela.geometry("450x420")
    janela.grab_set()

    tk.Label(janela, text="Reservas de Áreas Comuns", font=("Arial", 13, "bold")).pack(pady=(15, 10))

    frame = tk.Frame(janela)
    frame.pack(fill="both", expand=True, padx=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    lista = tk.Listbox(frame, yscrollcommand=scrollbar.set)
    lista.pack(fill="both", expand=True)
    scrollbar.config(command=lista.yview)

    reservas = listar_reservas()

    def preencher_lista():
        lista.delete(0, "end")
        for r in reservas:
            texto = (
                f"{r.get('area', '—')} | {r.get('data', '—')} {r.get('horario', '—')} | "
                f"{r.get('nome', '—')} ({r.get('unidade', '—')}) | {r.get('status', '—')}"
            )
            lista.insert("end", texto)

    preencher_lista()

    def cancelar_selecionada():
        selecionado = lista.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma reserva.", parent=janela)
            return
        indice = selecionado[0]
        if reservas[indice].get("status") == "Cancelada":
            messagebox.showinfo("Info", "Essa reserva já está cancelada.", parent=janela)
            return
        cancelar_reserva(indice, reservas)
        preencher_lista()

    tk.Button(
        janela, text="Cancelar reserva selecionada", command=cancelar_selecionada, width=25
    ).pack(pady=10)
    tk.Button(janela, text="Fechar", command=janela.destroy, width=12).pack(pady=(0, 10))


def tela_reservas_dia_funcionario():
    """Tela onde o funcionário vê as reservas confirmadas para o dia atual."""
    janela = tk.Toplevel()
    janela.title("Reservas do Dia")
    janela.geometry("420x400")
    janela.grab_set()

    hoje = datetime.now().strftime("%d/%m/%Y")

    tk.Label(janela, text=f"Reservas de Hoje ({hoje})", font=("Arial", 13, "bold")).pack(pady=(15, 10))

    frame = tk.Frame(janela)
    frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    caixa_texto = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set, state="disabled")
    caixa_texto.pack(fill="both", expand=True)
    scrollbar.config(command=caixa_texto.yview)

    reservas_hoje = [
        r for r in listar_reservas()
        if r.get("data") == hoje and r.get("status") != "Cancelada"
    ]

    caixa_texto.config(state="normal")
    if not reservas_hoje:
        caixa_texto.insert("end", "Nenhuma reserva para hoje.")
    else:
        for r in reservas_hoje:
            caixa_texto.insert("end", f"Área: {r.get('area', '—')}\n")
            caixa_texto.insert("end", f"Horário: {r.get('horario', '—')}\n")
            caixa_texto.insert("end", f"Morador: {r.get('nome', '—')} ({r.get('unidade', '—')})\n")
            caixa_texto.insert("end", "-" * 40 + "\n\n")
    caixa_texto.config(state="disabled")

    tk.Button(janela, text="Fechar", command=janela.destroy, width=12).pack(pady=(0, 10))