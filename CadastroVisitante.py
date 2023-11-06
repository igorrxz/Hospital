class CadastroVisitantes:
    def __init__(self):
        self.visitantes = {}

    def executar(self):
        print("Você selecionou Cadastrar Visitantes.")

    def cadastrar_visitante(self):
        nome = input("Qual o nome do visitante? ")
        documento = input("Informe seu CPF: ")
        rl = input("Relação com o paciente: ")
        data = input("Informe a data de autorização:")
        autorizacao = input("O visitante está autorizado (True/False)? ").lower() == 'true'
        self.visitantes[nome] = {"Autorizado": autorizacao, "Registro_entrada": None, "Registro_saida": None}
        print(f"Visitante {nome} cadastrado com sucesso!")

    def verificar_autorizacao(self, nome):
        if nome in self.visitantes:
            return self.visitantes[nome]["Autorizado"]
        else:
            return None

    def registrar_entrada(self):
        nome = input("Qual o nome do visitante para registrar entrada? ")
        if nome in self.visitantes and self.visitantes[nome]["Registro_entrada"] is None:
            hora_entrada = input("Hora de entrada (hh:mm:ss): ")
            self.visitantes[nome]["Registro_entrada"] = hora_entrada
            print(f"Entrada de {nome} registrada às {hora_entrada}.")
        else:
            print("Visitante não encontrado ou já registrou entrada.")

    def registrar_saida(self):
        nome = input("Qual o nome do visitante para registrar saída? ")
        if nome in self.visitantes and self.visitantes[nome]["Registro_saida"] is None:
            hora_saida = input("Hora de saída (hh:mm:ss): ")
            self.visitantes[nome]["Registro_saida"] = hora_saida
            print(f"Saida de {nome} registrada às {hora_saida}.")
        else:
            print("Visitante não encontrado ou já registrou saída.")

    def verificar_limite_por_paciente(self, paciente):
        visitantes_paciente = [v for v in self.visitantes.values() if v["Registro_entrada"] is not None and v["Registro_saida"] is None]
        return len(visitantes_paciente)

    def aplicar_restricoes_acesso(self):
        nome = input("Qual o nome do visitante para aplicar restrições de acesso? ")
        restricoes = input("Informe as restrições de acesso: ")
        if nome in self.visitantes:
            self.visitantes[nome]["Restricoes"] = restricoes
            print(f"Restrições de acesso aplicadas para {nome}.")
        else:
            print("Visitante não encontrado.")

    def notificar_visitas_pendentes(self):
        visitantes_pendentes = [v for v in self.visitantes if self.visitantes[v]["Registro_entrada"] is None]
        if visitantes_pendentes:
            print("Visitas pendentes:")
            for visitante in visitantes_pendentes:
                print(f"Nome: {visitante} - Autorizado: {self.visitantes[visitante]['Autorizado']}")
        else:
            print("Não há visitas pendentes.")

cadastro = CadastroVisitantes()

while True:
    print("Menu:")
    print("1. Cadastrar visitante")
    print("2. Verificar autorização de visitante")
    print("3. Registrar entrada")
    print("4. Registrar saída")
    print("5. Verificar limite de visitantes por paciente")
    print("6. Aplicar restrições de acesso")
    print("7. Notificar visitas pendentes")
    print("8. Sair")
    choice = input("Escolha uma opção: ")

    if choice == '1':
      cadastro.cadastrar_visitante()
    elif choice == '2':
        nome = input("Informe o nome do visitante: ")
        autorizacao = cadastro.verificar_autorizacao(nome)
        if autorizacao is not None:
            print(f"Autorização de {nome}: {autorizacao}")
        else:
            print("Visitante não encontrado.")
    elif choice == '3':
        cadastro.registrar_entrada()
    elif choice == '4':
        cadastro.registrar_saida()
    elif choice == '5':
        paciente = input("Informe o nome do paciente: ")
        limite_por_paciente = cadastro.verificar_limite_por_paciente(paciente)
        print(f"Limite de visitantes por paciente: {limite_por_paciente}")
    elif choice == '6':
        cadastro.aplicar_restricoes_acesso()
    elif choice == '7':
        cadastro.notificar_visitas_pendentes()
    elif choice == '8':
        print("Volte sempre!")
        break

