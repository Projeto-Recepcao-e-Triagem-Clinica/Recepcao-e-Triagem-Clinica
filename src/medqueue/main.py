from src.medqueue.pacientes.gerenciador import Gerenciador

def menu():
    gerenciador = Gerenciador()
    
    while True:
        print("\n" + "=" * 49)
        print("====           MENU GERAL MEDQUEUE           ====")
        print("=" * 49)
        print("""
              1 - Adicionar especialidade
              2 - Cadastrar paciente
              3 - Chamar próximo paciente
              4 - Finalizar consulta
              5 - Desfazer última ação
              6 - Exibir painel
              0 - Sair
              """)
        print("-" * 49)

        opcao = input("Digite a opção desejada: ").strip()

        if opcao == "1":
            especialidade = input("Digite a especialidade: ").strip()
            gerenciador.adicionar_especialidade(especialidade)

        elif opcao == "2":
            try:
                nome = input("Nome do paciente: ").strip()
                idade = int(input("Idade: "))
                numero_telefone = input("Telefone: ").strip()
                e_mail = input("E-mail: ").strip()
                especialidade = input("Especialidade: ").strip()

                gerenciador.cadastrar_paciente(
                    nome,
                    idade,
                    numero_telefone,
                    e_mail,
                    especialidade
                )
            except ValueError:
                print("ID e idade devem ser números inteiros!")

        elif opcao == "3":
            gerenciador.chamar_proximo_paciente()

        elif opcao == "4":
            try:
                id_paciente = int(input("ID do paciente: "))
                gerenciador.finalizar_consulta(id_paciente)
            except ValueError:
                print("O ID deve ser um número inteiro.")

        elif opcao == "5":
            gerenciador.desfazer_ultima_acao()

        elif opcao == "6":
            gerenciador.exibir_painel()

        elif opcao == "0":
            print("-" * 49)
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()