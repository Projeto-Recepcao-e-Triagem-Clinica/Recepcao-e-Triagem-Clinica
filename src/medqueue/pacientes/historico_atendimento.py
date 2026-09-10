def registrar_acao(persistencia, acao, id_paciente):
    registro = (acao, id_paciente)
    persistencia.historico_atendimento.append(registro)


def desfazer_ultima_acao(persistencia):
    if not persistencia.historico_atendimento:
        print("Não há ações para desfazer.")
        return None

    return persistencia.historico_atendimento.pop()

