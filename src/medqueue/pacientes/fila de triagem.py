from paciente import pacientes_db 

fila_triagem = []

def adicionar_na_triagem(id_paciente):
    fila_triagem.append(id_paciente)


def chamar_proximo_paciente():
    if fila_triagem:
        id_paciente = fila_triagem.pop(0)
        return pacientes_db[id_paciente]

    print("Não há pacientes na fila.")
    return None

