class Persistencia:
    def __init__(self):
        self.pacientes_db = {}
        self.fila_triagem = []
        self.historico_atendimento = []
        self.especialidades = [
            "Cardiologia",
            "Pediatria",
            "Fonoaudiologia"
        ]