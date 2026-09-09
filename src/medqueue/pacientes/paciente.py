class Pacientes:

    proximo_id = 1

    pacientes_db = {}
    
    def __init__(self, nome, idade, numero_telefone, e_mail, especialidade):
        self.id_paciente = Pacientes.proximo_id
        Pacientes.proximo_id += 1

        self.nome = nome
        self.idade = idade
        self.numero_telefone = numero_telefone
        self.e_mail = e_mail
        self.especialidade = especialidade
        self.status = "Aguardando"

    def iniciar_consulta(self):
        self.status = "Em Consulta"

    def finalizar_consulta(self):
        self.status = "Finalizada"

    def exibir_dados(self):
        print(f"SEU ID: {self.id_paciente}")
        print(f"Paciente: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Telefone: {self.numero_telefone}")
        print(f"E-mail: {self.e_mail}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Status: {self.status}")