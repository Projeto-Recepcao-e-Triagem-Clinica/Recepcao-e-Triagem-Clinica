class Pacientes:

    proximo_id = 1

    def __init__(self, nome, idade, numero_telefone, e_mail, especialidade):
        self.id_paciente = f"{Pacientes.proximo_id:04d}"
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

pacientes_db = {}

def cadastrar_paciente(nome, idade, numero_telefone, e_mail, especialidade):

    paciente = Pacientes(
        nome,
        idade,
        numero_telefone,
        e_mail,
        especialidade
    )

    pacientes_db[paciente.id_paciente] = paciente

    print(f"Paciente {nome} cadastrado com sucesso!")
    print(f"ID do paciente: {paciente.id_paciente}")

def buscar_paciente(id_paciente):

    if id_paciente in pacientes_db:
        return pacientes_db[id_paciente]

    print("Paciente não encontrado.")
    return None

def remover_paciente(id_paciente):

    if id_paciente in pacientes_db:
        paciente = pacientes_db.pop(id_paciente)
        print(f"Paciente {paciente.nome} removido com sucesso!")

    else:
        print("Paciente não encontrado.")

def listar_pacientes():

    if not pacientes_db:
        print("Nenhum paciente cadastrado.")
        return

    print("\n===== PACIENTES CADASTRADOS =====")

    for paciente in pacientes_db.values():
        paciente.exibir_dados()
        print("------------------------------")