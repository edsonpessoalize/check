import funcoes as fc
base = open('contcontract.csv', 'r', encoding="utf-8")

registro_ok = []
registro_fail = []
for n, linha in enumerate(base):
    if n > 0:
        atendimento = linha.strip().split(",")
        if fc.formatar_nome(atendimento[1]) and fc.tratar_tkt(atendimento[2]):
            with open("sucesso.csv", 'a', encoding="utf-8") as ids_base:
                registro = f"{fc.formatar_data(atendimento[0])}; " \
                           f"{fc.formatar_nome(atendimento[1])}; " \
                           f"{fc.tratar_tkt(atendimento[2])}; " \
                           f"{fc.tratar_contrato(atendimento[3])};\n"
                ids_base.write(registro)
        else:
            with open("falha.csv", 'a', encoding="utf-8") as ids_base:
                registro = f"{linha.strip()}\n"
                ids_base.write(registro)

print("fim do script")
