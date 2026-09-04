from paciente import pacientes_db

historico = []

def historico_atendimento():
    id_paciente = input("informe o ID do paciente: ")

    if id_paciente in pacientes_db:

        paciente = pacientes_db[id_paciente]

        acao = input("Informe a ação realizada: ")

        registro = (acao, paciente.id_paciente)

        historico.append(registro)

        print("\nHistórico registrado com sucesso!")
        print(f"Paciente: {paciente.nome}")
        print(f"Ação realizada: {acao}")
        print(f"ID do paciente: {paciente.id_paciente}")

    else:
        print("Paciente não encontrado.")


