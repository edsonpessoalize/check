from datetime import datetime
import constantes as ct
import re


def formatar_data(registro):
    registro = registro.replace('"', '')
    registro = registro.split()
    data = datetime.strptime(registro[0], "%Y/%m/%d").strftime("%Y/%m/%d")
    hora = datetime.strptime(f"{registro[1]} {registro[2]}", "%I:%M:%S %p").strftime("%H:%M:%S")
    return f"{data} {hora}"


def formatar_nome(nome):
    # cria uma variavel de controle
    ctrl = False

    # remove as aspas, espaços extras e coloca em minuscula
    nome_t = nome.replace('"', '').strip().lower()
    for k in ct.VARIACOES.keys():
        if nome_t in ct.VARIACOES[k]:
            nome_t = k
            ctrl = True
    # Trata o nome para exibição
    if ctrl:
        novo_nome = nome_t.title()
        return novo_nome
    else:
        return False


def tratar_tkt(tkt):
    tkt = tkt.lower()
    numeros = re.sub(r'\D', '', tkt)
    if 'chat' in tkt or len(numeros) == 20:
        ntkt = f"chat: {numeros}"
    elif 'ticket' in tkt or '#' in tkt or len(numeros) == 5:
        ntkt = f"Ticket: #{numeros}"
    elif len(numeros) == 17:
        ntkt = f"Cartão Unimed: #{numeros}"
    else:
        ntkt = False
    return ntkt


def tratar_contrato(contrato):
    contrato = contrato.replace('"', '')
    return contrato
