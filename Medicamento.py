class Medicamento:
    def __init__(self, nome, principio_ativo, dosagem, forma_administracao):
        self.nome = nome
        self.principio_ativo = principio_ativo
        self.dosagem = dosagem
        self.forma_administracao = forma_administracao
        self.estoque = []

    def adicionar_lote(self, lote, quantidade, data_validade, fornecedor):
        lote_info = {"lote": lote, "quantidade": quantidade, "data_validade": data_validade, "fornecedor": fornecedor}
        self.estoque.append(lote_info)

    def listar_estoque(self):
        print("Estoque do Medicamento:")
        for lote_info in self.estoque:
            print(f"Lote: {lote_info['lote']}")
            print(f"Quantidade: {lote_info['quantidade']}")
            print(f"Data de Validade: {lote_info['data_validade']}")
            print(f"Fornecedor: {lote_info['fornecedor']}")
            print()

class AdministracaoMedicamentos:
    def __init__(self):
        self.medicamentos = []

    def adicionar_medicamento(self, nome, principio_ativo, dosagem, forma_administracao):
        medicamento = Medicamento(nome, principio_ativo, dosagem, forma_administracao)
        self.medicamentos.append(medicamento)
        return medicamento

    def listar_medicamentos(self):
        print("Lista de Medicamentos:")
        for medicamento in self.medicamentos:
            print(f"Nome: {medicamento.nome}")
            print(f"Princípio Ativo: {medicamento.principio_ativo}")
            print(f"Dosagem: {medicamento.dosagem}")
            print(f"Forma de Administração: {medicamento.forma_administracao}")
            medicamento.listar_estoque()

    def adicionar_lote_medicamento(self, medicamento, lote, quantidade, data_validade, fornecedor):
        medicamento.adicionar_lote(lote, quantidade, data_validade, fornecedor)
        print(f"Lote {lote} do medicamento {medicamento.nome} adicionado com sucesso.")

    def listar_estoque_medicamento(self, medicamento):
        medicamento.listar_estoque()

    def verificar_estoque_baixo(self, medicamento, quantidade_minima):
        for lote_info in medicamento.estoque:
            if lote_info['quantidade'] < quantidade_minima:
                print(f"ALERTA: Medicamento {medicamento.nome} está com estoque baixo no lote {lote_info['lote']}.")

# Exemplo de uso
administracao_medicamentos = AdministracaoMedicamentos()

while True:
    print("Opções:")
    print("1. Adicionar Medicamento")
    print("2. Adicionar Lote de Medicamento")
    print("3. Listar Medicamentos")
    print("4. Listar Estoque de Medicamento")
    print("5. Verificar Estoque Baixo")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do medicamento: ")
        principio_ativo = input("Princípio Ativo: ")
        dosagem = input("Dosagem: ")
        forma_administracao = input("Forma de Administração: ")
        medicamento = administracao_medicamentos.adicionar_medicamento(nome, principio_ativo, dosagem, forma_administracao)
        print(f"Medicamento {medicamento.nome} adicionado com sucesso.")
    elif opcao == "2":
        administracao_medicamentos.listar_medicamentos()
        medicamento_index = int(input("Selecione o número do medicamento para adicionar lote: ")) - 1
        if 0 <= medicamento_index < len(administracao_medicamentos.medicamentos):
            medicamento = administracao_medicamentos.medicamentos[medicamento_index]
            lote = input("Número do Lote: ")
            quantidade = int(input("Quantidade: "))
            data_validade = input("Data de Validade: ")
            fornecedor = input("Fornecedor: ")
            administracao_medicamentos.adicionar_lote_medicamento(medicamento, lote, quantidade, data_validade, fornecedor)
        else:
            print("Medicamento não encontrado.")
    elif opcao == "3":
        administracao_medicamentos.listar_medicamentos()
    elif opcao == "4":
        administracao_medicamentos.listar_medicamentos()
        medicamento_index = int(input("Selecione o número do medicamento para listar o estoque: ")) - 1
        if 0 <= medicamento_index < len(administracao_medicamentos.medicamentos):
            medicamento = administracao_medicamentos.medicamentos[medicamento_index]
            administracao_medicamentos.listar_estoque_medicamento(medicamento)
        else:
            print("Medicamento não encontrado.")
    elif opcao == "5":
        quantidade_minima = int(input("Quantidade Mínima para Estoque Baixo: "))
        for medicamento in administracao_medicamentos.medicamentos:
            administracao_medicamentos.verificar_estoque_baixo(medicamento, quantidade_minima)
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")
