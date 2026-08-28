def historico_atendimento():
    acao = input("Informe a ação realizada: ")
    id_paciente = input("Informe o ID do paciente: ")

    historico = []
    registro = (acao, id_paciente)

    historico.append(registro)

    print(f"Sua ação neste momento é: {acao}")
    print(f"ID do paciente: {id_paciente}")