from persistencia import pacientes_db, fila_triagem,historico_atendimento, especialidades

def adicionar_especialidade(especialidade):
    if especialidade not in especialidades:
        especialidades.append(especialidade)
        print(f"Especialidade adicionada com sucesso!")
    else:
        print(f"Especialidade já existe!")