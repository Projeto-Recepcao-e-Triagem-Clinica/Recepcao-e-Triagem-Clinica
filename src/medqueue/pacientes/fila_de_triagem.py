
def adicionar_na_triagem(persistencia, id_paciente):
    persistencia.fila_triagem.append(id_paciente)


def chamar_proximo_paciente(persistencia):
    if not persistencia.fila_triagem:
        print("Não há pacientes na fila.")
        return None

    return persistencia.fila_triagem.pop(0)
