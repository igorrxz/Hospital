class Leito:
    def __init__(self, numero, gravidade):
        self.numero = numero
        self.ocupado = False
        self.gravidade = gravidade

    def executar(self):
        print("Você selecionou Gestão de Leitos.")

class SistemaGestaoLeitos:
    def __init__(self, capacidade_maxima):
        self.leitos = []
        self.capacidade_maxima = capacidade_maxima
        self.proximo_numero_leito = 1

    def adicionar_leito(self, gravidade):
        leito = Leito(self.proximo_numero_leito, gravidade)
        self.leitos.append(leito)
        self.proximo_numero_leito += 1

    def ocupar_leito(self, numero):
        leito = self.encontrar_leito(numero)
        if leito:
            if not leito.ocupado:
                leito.ocupado = True
                print(f"Leito {numero} ocupado.")
                leitos_livres = [leito for leito in self.leitos if not leito.ocupado]
                if len(leitos_livres) == 0:
                    print("ALERTA: Todos os leitos estão ocupados. Capacidade máxima atingida.")
                elif len(leitos_livres) == 1:
                    print("ALERTA: Capacidade máxima se aproxima.")
            else:
                print(f"Leito {numero} já está ocupado.")
        else:
            print(f"Leito {numero} não existe.")

    def desocupar_leito(self, numero):
        leito = self.encontrar_leito(numero)
        if leito:
            if leito.ocupado:
                leito.ocupado = False
                print(f"Leito {numero} desocupado.")
            else:
                print(f"Leito {numero} já está desocupado.")
        else:
            print(f"Leito {numero} não existe.")

    def encontrar_leito(self, numero):
        for leito in self.leitos:
            if leito.numero == numero:
                return leito
        return None

    def listar_leitos_disponiveis(self):
        leitos_disponiveis = [leito.numero for leito in self.leitos if not leito.ocupado]
        if leitos_disponiveis:
            print("Leitos disponíveis:", leitos_disponiveis)
        else:
            print("Não há Leitos disponíveis!")

    def listar_leitos(self):
        print("Lista de leitos:")
        for leito in self.leitos:
            status = "Ocupado" if leito.ocupado else "Livre"
            print(f"Leito {leito.numero} - Gravidade: {leito.gravidade} - Status: {status}")

    def gerar_relatorio(self):
        if len(self.leitos) == 0:
            print("Não há leitos disponíveis para gerar relatório.")
        else:
            ocupacao = self.calcular_ocupacao()
            print(f"Relatório de ocupação:")
            print(f"Ocupação atual: {ocupacao:.2f}%")
            print(f"Capacidade máxima: {self.capacidade_maxima}")

    def calcular_ocupacao(self):
        leitos_ocupados = sum(1 for leito in self.leitos if leito.ocupado)
        return (leitos_ocupados / len(self.leitos)) * 100 if len(self.leitos) > 0 else 0

def menu_gestao_leitos():
    capacidade_maxima = 20
    sistema = SistemaGestaoLeitos(capacidade_maxima)

    while True:
        print("Opções:")
        print("1. Adicionar leito")
        print("2. Ocupar leito")
        print("3. Desocupar leito")
        print("4. Listar leitos")
        print("5. Listar leitos disponíveis")
        print("6. Gerar relatório")
        print("7. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gravidade = input("Gravidade do caso (Alta/Média/Baixa): ")
            if gravidade in ["Alta", "Média", "Baixa"]:
                sistema.adicionar_leito(gravidade)
            else:
                print("Gravidade inválida. Escolha entre Alta, Média ou Baixa.")
        elif opcao == "2":
            sistema.listar_leitos_disponiveis()
            numero = int(input("Número do leito a ocupar: "))
            leitos_disponiveis = [leito.numero for leito in sistema.leitos if not leito.ocupado]
            if numero in leitos_disponiveis:
                sistema.ocupar_leito(numero)
            else:
                print(f"Leito {numero} não está disponível.")
        elif opcao == "3":
            numero = int(input("Número do leito a desocupar: "))
            sistema.desocupar_leito(numero)
        elif opcao == "4":
            sistema.listar_leitos()
        elif opcao == "5":
            sistema.listar_leitos_disponiveis()
        elif opcao == "6":
            sistema.gerar_relatorio()
        elif opcao == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")
