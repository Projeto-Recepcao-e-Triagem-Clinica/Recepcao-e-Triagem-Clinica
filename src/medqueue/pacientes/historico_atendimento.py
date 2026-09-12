from paciente import pacientes_db

def historico_atendimento():
    id_paciente = input("Informe o ID do paciente: ")

    if id_paciente in pacientes_db:
        paciente = pacientes_db[id_paciente]

        acao = input("Informe a ação realizada: ")

        print(f"Ação: {acao}")
        print(f"ID do paciente: {paciente.id_paciente}")

    else:
        print("Paciente não encontrado.")


def registrar_acao(persistencia, acao, id_paciente):
    registro = (acao, id_paciente)
    persistencia.historico_atendimento.append(registro)


def desfazer_ultima_acao(persistencia):
    if not persistencia.historico_atendimento:
        print("Não há ações para desfazer.")
        return

    persistencia.historico_atendimento.pop()