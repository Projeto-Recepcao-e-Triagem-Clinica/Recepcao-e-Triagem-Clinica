from src.medqueue.pacientes.persistencia import Persistencia
from src.medqueue.pacientes.paciente import Pacientes
from src.medqueue.pacientes.fila_de_triagem import adicionar_na_triagem, chamar_proximo_paciente
from src.medqueue.pacientes.historico_atendimento import registrar_acao, desfazer_ultima_acao


class Gerenciador:

    def __init__(self):
        self.persistencia = Persistencia()

    def adicionar_especialidade(self, especialidade):
        especialidade = especialidade.strip()

        if not especialidade:
            print("Informe uma especialidade válida.")
            return

        if especialidade in self.persistencia.especialidades:
            print("Essa especialidade já existe.")
            return

        self.persistencia.especialidades.append(especialidade)
        print("Especialidade adicionada com sucesso.")

    def cadastrar_paciente(self, id_paciente, nome, idade, numero_telefone, e_mail, especialidade):
        if especialidade not in self.persistencia.especialidades:
            print("Especialidade não cadastrada.")
            return

        if id_paciente in self.persistencia.pacientes_db:
            print("ID do paciente já cadastrado.")
            return

        paciente = Pacientes(
            id_paciente,
            nome,
            idade,
            numero_telefone,
            e_mail,
            especialidade
        )

        dados_paciente = {
            "id": paciente.id_paciente,
            "paciente": paciente.nome,
            "especialidade": paciente.especialidade,
            "status": paciente.status
        }

        self.persistencia.pacientes_db[id_paciente] = dados_paciente
        adicionar_na_triagem(self.persistencia, id_paciente)
        registrar_acao(self.persistencia, "CADASTRAR", id_paciente)

        print(f"Paciente cadastrado com sucesso. ID: {id_paciente}")

    def chamar_proximo_paciente(self):
        id_paciente = chamar_proximo_paciente(self.persistencia)

        if id_paciente is None:
            return

        paciente = self.persistencia.pacientes_db[id_paciente]
        paciente["status"] = "Em Consulta"

        registrar_acao(self.persistencia, "CHAMAR", id_paciente)

        print(f"Paciente chamado: {paciente['paciente']}")
        print(f"Especialidade: {paciente['especialidade']}")

    def finalizar_consulta(self, id_paciente):
        if id_paciente not in self.persistencia.pacientes_db:
            print("Paciente não encontrado.")
            return

        paciente = self.persistencia.pacientes_db[id_paciente]

        if paciente["status"] != "Em Consulta":
            print("O paciente não está em consulta.")
            return

        paciente["status"] = "Finalizada"
        registrar_acao(self.persistencia, "FINALIZAR", id_paciente)

        print("Consulta finalizada com sucesso.")

    def desfazer_ultima_acao(self):
        ultima_acao = desfazer_ultima_acao(self.persistencia)

        if ultima_acao is None:
            return

        acao, id_paciente = ultima_acao

        if acao == "CHAMAR":
            paciente = self.persistencia.pacientes_db[id_paciente]
            paciente["status"] = "Aguardando"
            self.persistencia.fila_triagem.insert(0, id_paciente)
            print(f"Chamada do paciente {id_paciente} desfeita.")

        elif acao == "CADASTRAR":
            if id_paciente in self.persistencia.fila_triagem:
                self.persistencia.fila_triagem.remove(id_paciente)

            if id_paciente in self.persistencia.pacientes_db:
                del self.persistencia.pacientes_db[id_paciente]

            print(f"Cadastro do paciente {id_paciente} desfeito.")

        elif acao == "FINALIZAR":
            paciente = self.persistencia.pacientes_db.get(id_paciente)

            if paciente is not None:
                paciente["status"] = "Em Consulta"
                print(f"Finalização da consulta do paciente {id_paciente} desfeita.")

    def exibir_painel(self):
        print("\n" + "=" * 50)
        print("                 PAINEL MEDQUEUE")
        print("=" * 50)

        print("\n--- FILA DE TRIAGEM ---")
        if self.persistencia.fila_triagem:
            print(self.persistencia.fila_triagem)
        else:
            print("Fila vazia.")

        print("\n--- PACIENTES ---")
        if self.persistencia.pacientes_db:
            for paciente in self.persistencia.pacientes_db.values():
                print(
                    f"ID: {paciente['id']} | "
                    f"Paciente: {paciente['paciente']} | "
                    f"Especialidade: {paciente['especialidade']} | "
                    f"Status: {paciente['status']}"
                )
        else:
            print("Nenhum paciente cadastrado.")

        print("\n--- HISTÓRICO ---")
        if self.persistencia.historico_atendimento:
            for acao in self.persistencia.historico_atendimento:
                print(acao)
        else:
            print("Histórico vazio.")

        print("\n--- ESPECIALIDADES ---")
        for especialidade in self.persistencia.especialidades:
            print(f"- {especialidade}")

        print("=" * 50)