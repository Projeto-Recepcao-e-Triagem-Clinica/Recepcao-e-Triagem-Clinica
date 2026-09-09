from paciente import pacientes_db

historico = []

def historico_atendimento():
    id_paciente = input("informe o ID do paciente: ")

    if id_paciente in pacientes_db:

        paciente = pacientes_db[id_paciente]

        acao = input("Informe a ação realizada: ")

        def registrar_acao(persistencia, acao, id_paciente):
            registro = (acao, id_paciente)
            persistencia.historico_atendimento.append(registro)


        def desfazer_ultima_acao(persistencia):
            if not persistencia.historico_atendimento:
                print("Não há ações para desfazer.")
        return None


        return persistencia.historico_atendimento.pop()

    print("\nHistórico registrado com sucesso!")
    print(f"Paciente: {paciente.nome}")
    print(f"Ação realizada: {acao}")
    print(f"ID do paciente: {paciente.id_paciente}")

