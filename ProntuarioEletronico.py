class ProntuarioEletronico:
    def __init__(self):
        self.pacientes = {}  # Dicionário para armazenar informações dos pacientes

    def cadastrar_paciente(self, id_paciente, nome, data_nascimento, genero, endereco, telefone, email):
        if id_paciente not in self.pacientes:
            self.pacientes[id_paciente] = {
                "Nome": nome,
                "Data de Nascimento": data_nascimento,
                "Gênero": genero,
                "Endereço": endereco,
                "Telefone": telefone,
                "E-mail": email,
                "Diagnósticos": [],
                "Tratamentos": [],
                "Evolução Clínica": [],
                "Anexos": []
            }
            print(f"Paciente {nome} cadastrado com sucesso!")
        else:
            print("ID de paciente já existe. Tente outro ID.")

    def adicionar_diagnostico(self, id_paciente, data_diagnostico, diagnostico, medico):
        if id_paciente in self.pacientes:
            self.pacientes[id_paciente]["Diagnósticos"].append({
                "Data do Diagnóstico": data_diagnostico,
                "Diagnóstico": diagnostico,
                "Médico": medico
            })
            print("Diagnóstico registrado com sucesso!")
        else:
            print("Paciente não encontrado.")

    def adicionar_tratamento(self, id_paciente, data_inicio, tratamento, prescricao):
        if id_paciente in self.pacientes:
            self.pacientes[id_paciente]["Tratamentos"].append({
                "Data de Início do Tratamento": data_inicio,
                "Tratamento": tratamento,
                "Prescrição Médica": prescricao
            })
            print("Tratamento registrado com sucesso!")
        else:
            print("Paciente não encontrado.")

    def adicionar_evolucao_clinica(self, id_paciente, data_visita, resumo_visita):
        if id_paciente in self.pacientes:
            self.pacientes[id_paciente]["Evolução Clínica"].append({
                "Data da Visita": data_visita,
                "Resumo da Visita": resumo_visita
            })
            print("Evolução clínica registrada com sucesso!")
        else:
            print("Paciente não encontrado.")

    def adicionar_anexo(self, id_paciente, anexo):
        if id_paciente in self.pacientes:
            self.pacientes[id_paciente]["Anexos"].append(anexo)
            print("Anexo adicionado com sucesso!")
        else:
            print("Paciente não encontrado.")

    def obter_informacoes_paciente(self, id_paciente):
        if id_paciente in self.pacientes:
            return self.pacientes[id_paciente]
        else:
            return None

# Function to display the menu and handle user input
def main_menu(prontuario):
    while True:
        print("Menu:")
        print("1. Cadastrar Paciente")
        print("2. Adicionar Diagnóstico")
        print("3. Adicionar Tratamento")
        print("4. Adicionar Evolução Clínica")
        print("5. Adicionar Anexo")
        print("6. Obter Informações do Paciente")
        print("7. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            id_paciente = input("Informe o ID do paciente: ")
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (dd/mm/yyyy): ")
            genero = input("Gênero: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            prontuario.cadastrar_paciente(id_paciente, nome, data_nascimento, genero, endereco, telefone, email)
        elif choice == '2':
            id_paciente = input("Informe o ID do paciente: ")
            data_diagnostico = input("Data do Diagnóstico (dd/mm/yyyy): ")
            diagnostico = input("Diagnóstico: ")
            medico = input("Médico: ")
            prontuario.adicionar_diagnostico(id_paciente, data_diagnostico, diagnostico, medico)
        elif choice == '3':
            id_paciente = input("Informe o ID do paciente: ")
            data_inicio = input("Data de Início do Tratamento (dd/mm/yyyy): ")
            tratamento = input("Tratamento: ")
            prescricao = input("Prescrição Médica: ")
            prontuario.adicionar_tratamento(id_paciente, data_inicio, tratamento, prescricao)
        elif choice == '4':
            id_paciente = input("Informe o ID do paciente: ")
            data_visita = input("Data da Visita (dd/mm/yyyy): ")
            resumo_visita = input("Resumo da Visita: ")
            prontuario.adicionar_evolucao_clinica(id_paciente, data_visita, resumo_visita)
        elif choice == '5':
            id_paciente = input("Informe o ID do paciente: ")
            anexo = input("Nome do Anexo: ")
            prontuario.adicionar_anexo(id_paciente, anexo)
        elif choice == '6':
            id_paciente = input("Informe o ID do paciente: ")
            informacoes_paciente = prontuario.obter_informacoes_paciente(id_paciente)
            if informacoes_paciente:
                print(informacoes_paciente)
            else:
                print("Paciente não encontrado.")
        elif choice == '7':
          print("obrigado pela sua visita!")
          break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    prontuario = ProntuarioEletronico()
    main_menu(prontuario)