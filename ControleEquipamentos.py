class Equipamento:
    def __init__(self, nome, modelo, numero_serie, data_aquisicao):
        self.nome = nome
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.data_aquisicao = data_aquisicao
        self.manutencoes = []

    def adicionar_manutencao(self, tipo_manutencao, data_manutencao, intervencao):
        manutencao = {"tipo": tipo_manutencao, "data": data_manutencao, "intervencao": intervencao}
        self.manutencoes.append(manutencao)


class ControleEquipamentos:
    def __init__(self):
        self.equipamentos = []

    def adicionar_equipamento(self, nome, modelo, numero_serie, data_aquisicao):
        equipamento = Equipamento(nome, modelo, numero_serie, data_aquisicao)
        self.equipamentos.append(equipamento)
        return equipamento

    def registrar_manutencao(self, equipamento, tipo_manutencao, data_manutencao, intervencao):
        equipamento.adicionar_manutencao(tipo_manutencao, data_manutencao, intervencao)
        print("Manutenção registrada com sucesso.")

    def listar_equipamentos(self):
        print("Lista de Equipamentos:")
        for equipamento in self.equipamentos:
            print(f"Nome: {equipamento.nome}")
            print(f"Modelo: {equipamento.modelo}")
            print(f"Número de Série: {equipamento.numero_serie}")
            print(f"Data de Aquisição: {equipamento.data_aquisicao}")
            print("Manutenções:")
            for manutencao in equipamento.manutencoes:
                print(f"Tipo: {manutencao['tipo']}")
                print(f"Data: {manutencao['data']}")
                print(f"Intervenção: {manutencao['intervencao']}")
            print()

    def programar_manutencao_preventiva(self, equipamento, tipo_manutencao, data_manutencao):
        equipamento.adicionar_manutencao(tipo_manutencao, data_manutencao, "Manutenção Preventiva")
        print("Manutenção preventiva programada com sucesso.")

# Exemplo de uso
controle_equipamentos = ControleEquipamentos()

while True:
    print("Opções:")
    print("1. Adicionar Equipamento")
    print("2. Registrar Manutenção")
    print("3. Listar Equipamentos")
    print("4. Programar Manutenção Preventiva")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do equipamento: ")
        modelo = input("Modelo do equipamento: ")
        numero_serie = input("Número de Série: ")
        data_aquisicao = input("Data de Aquisição: ")
        equipamento = controle_equipamentos.adicionar_equipamento(nome, modelo, numero_serie, data_aquisicao)
        print(f"Equipamento {equipamento.nome} adicionado com sucesso.")
    elif opcao == "2":
        controle_equipamentos.listar_equipamentos()
        equipamento_index = int(input("Selecione o número do equipamento para registrar a manutenção: ")) - 1
        if 0 <= equipamento_index < len(controle_equipamentos.equipamentos):
            equipamento = controle_equipamentos.equipamentos[equipamento_index]
            tipo_manutencao = input("Tipo de Manutenção: ")
            data_manutencao = input("Data da Manutenção: ")
            intervencao = input("Intervenção: ")
            controle_equipamentos.registrar_manutencao(equipamento, tipo_manutencao, data_manutencao, intervencao)
        else:
            print("Equipamento não encontrado.")
    elif opcao == "3":
        controle_equipamentos.listar_equipamentos()
    elif opcao == "4":
        controle_equipamentos.listar_equipamentos()
        equipamento_index = int(input("Selecione o número do equipamento para programar a manutenção preventiva: ")) - 1
        if 0 <= equipamento_index < len(controle_equipamentos.equipamentos):
            equipamento = controle_equipamentos.equipamentos[equipamento_index]
            tipo_manutencao = input("Tipo de Manutenção Preventiva: ")
            data_manutencao = input("Data da Manutenção Preventiva: ")
            controle_equipamentos.programar_manutencao_preventiva(equipamento, tipo_manutencao, data_manutencao)
        else:
            print("Equipamento não encontrado.")
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
