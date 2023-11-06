while True:
    print("Opções:")
    print("1. Gestão de Leitos")
    print("2. Controle de equipamentos")
    print("3. Administração de medicamentos")
    print("4. Agendamento e controle de visitas")
    print("5. Prontuário eletrônico")
    print("6. Gestão de equipes")
    print("7. Cadastro de visitantes")
    print("8. Relatórios e análises")
    print("9. Menu de informação")
    print("10. Sair")

    try:
        opcao = int(input('\n-> Selecione a opção que você deseja: '))
    except ValueError:
        print('\nOpção inválida! Por favor, digite apenas números entre 1 e 10.\n')

    if opcao == 1:
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


    elif opcao == 2:
        class Equipamento:
            def __init__(self, nome, modelo, numero_serie, data_aquisicao):
                self.nome = nome
                self.modelo = modelo
                self.numero_serie = numero_serie
                self.data_aquisicao = data_aquisicao
                self.manutencoes = []

            def executar(self):
                print("Você selecionou Controle de Equipamentos.")


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


    elif opcao == 3:
        class Medicamento:
            def __init__(self, nome, principio_ativo, dosagem, forma_administracao):
                self.nome = nome
                self.principio_ativo = principio_ativo
                self.dosagem = dosagem
                self.forma_administracao = forma_administracao
                self.estoque = []

            def executar(self):
                print("Você selecionou Controle de Medicamentos.")

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


    elif opcao == 4:
        
    # Módulo 04

# RF01 - Agendamento de visitas

        print('=' * 125)

        visitas_agendadas = []

        agendamento_horas = ""
        agendamento_dia = ""

        print('\nDias disponíveis para visita:\n')

        print('1 - Segunda-Feira')

        print('2 - Terça-Feira')

        print('3 - Quarta-Feira')

        print('4 - Quinta-Feira')

        print('5 - Sexta-Feira')

        print('6 - Sábado')

        print('7 - Domingo')

        agendamento_dia = input('\n-> Escolha o dia da visita (1-7): ')

        if agendamento_dia not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Dia de visita inválido. Escolha um número de 1 a 7.")
        else:
            print('\nHorários disponíveis para visita:\n')

            print('1 - 10h - 12h')

            print('2 - 12h - 14h')

            print('3 - 14h - 16h')

            print('4 - 16h - 18h')

            agendamento_horas = input('\n-> Escolha o horário da visita (1-4): ')

            if agendamento_horas not in ['1', '2', '3', '4']:
                print("Horário de visita inválido. Escolha um número de 1 a 4.")
            else:
                agendamento_dia = int(agendamento_dia)
                agendamento_horas = int(agendamento_horas)

                visita = {
                    "dia": agendamento_dia,
                    "hora": agendamento_horas
                }

                visitas_agendadas.append(visita)

                print("Visita agendada com sucesso!")

        print("\nVisitas agendadas:")
        for i, visita in enumerate(visitas_agendadas, 1):
            print(f"Visita {i}: Dia {visita['dia']}, Hora {visita['hora']}")


        # RF02 - Restrições de Visitas

        print('=' * 125)

        quantidade_de_visitantes = ""
        horarios_permitidos = ""

        print('\nQuantidade de visitantes por paciente:\n')

        print('1 - 1 Visitante')

        print('2 - 2 Visitantes')

        print('3 - 3 Visitantes')

        print('4 - 4 Visitantes')

        quantidade_de_visitantes = input('\n-> Informe quantos visitantes entrarão na sala: ')

        if quantidade_de_visitantes not in ['1', '2', '3', '4']:
            print("Quantidade máxima de visitantes atingida!")
        else:
            print('\nO tempo máximo permitido para visitas é de 2 horas.\n')
        
            print('\Horários Permitidos para a visita:\n')
        
            print('1 - 10h - 12h')
        
            print('2 - 12h - 14h')
        
            print('3 - 14h - 16h')
        
            print('4 - 16h - 18h')
        
            horarios_permitidos = input('\n-> Escolha um dos horários permitidos (1-4): ')

            if horarios_permitidos not in ['1', '2', '3', '4']:
                print("Este horário de visita não é permitido. Por favor, escolha um número de 1 a 4.")
            else:
                print(f"A visita será feita por {quantidade_de_visitantes} visitante(s), no horário {horarios_permitidos}.")
            
        # RF03 - Registro de Visitantes

        print('=' * 125)
            
        visitantes = []  
        contador = 0  # Variável para contar o número de visitantes

        def cadastrar_visitante():
        
            global contador
        
            nome = input("Digite o nome do visitante: ")
            documento = input("Digite o CPF(000.000.000-00) ou RG(0.000.000): ")
            relacao_paciente = input("Digite a relação com o paciente: ")
        
            visitante = {
                "nome": nome,
                "documento": documento,
                "relacao": relacao_paciente
            }
        
            visitantes.append(visitante)  
            contador += 1  
            print("Informações do visitante registradas com sucesso!")

        def listar_visitantes():
        
            if not visitantes:
                print("Nenhum visitante registrado.")
            
            else:
                print("\nLista de Visitantes: ")
                for i, visitante in enumerate(visitantes, start=1):
                    print(f"Visitante {i}:")
                
                    print(f"Nome: {visitante['nome']}")
                
                    print(f"Documento de Identificação: {visitante['documento']}")
                
                    print(f"Relação com o Paciente: {visitante['relacao']}")
                
                    print()

        while True:
            opcao = input("Escolha uma opção:\n1 - Cadastrar visitante\n2 - Listar visitantes\n3 - Sair\nOpção: ")

            if opcao == '1':
                cadastrar_visitante()
            
            elif opcao == '2':
                listar_visitantes()
            
            elif opcao == '3':
                print("Saindo do programa.")
            
                break
            
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

        # RF04 - Controle de Acesso

        # Solicita ao usuário quantos visitantes autorizados deseja fornecer
        numero_visitantes_autorizados = 0

        print('=' * 125)
        print('\nPor favor, na hora de digitar as informações digite-as igualmente para que a validação seja feita corretamente.\n')

        while True:
            try:
                numero_visitantes_autorizados = int(input('\nDigite a quantidade de visitantes para autorização (Máximo 4)?\n'))
                if 1 <= numero_visitantes_autorizados <= 4:
                    break
                
                else:
                    print('\nPor favor, digite um número de 1 a 4.\n')
                
            except ValueError:
                print('\nPor favor, digite um número válido.\n')
            
        # Fornecer informações dos visitantes autorizados
        visitantes_autorizados = []

        for i in range(numero_visitantes_autorizados):
            nome = input(f"Digite o nome do visitante número {i + 1}: ")
            documento = input(f"Digite o CPF (000.000.000-00) ou RG (0.000.000) do visitante número {i + 1}: ")
            visitantes_autorizados.append({"nome": nome, "documento": documento})

        # Define o número de validações igual ao número de visitantes autorizados
        numero_validacoes = numero_visitantes_autorizados

        def validar_acesso(visitantes_autorizados, numero_validacoes):
        
            for i in range(numero_validacoes):
                nome = input('\nDigite seu nome para validação:\n')
                documento = input('\nDigite seu CPF (000.000.000-00) ou RG (0.000.000) para validação:\n')
                acesso_permitido = False

                for visitante_autorizado in visitantes_autorizados:
                    if nome == visitante_autorizado["nome"] and documento == visitante_autorizado["documento"]:
                        print('\nAcesso permitido. Você pode visitar o paciente.\n')
                        acesso_permitido = True
                        break

                if not acesso_permitido:
                
                    print('\nAcesso negado. Suas informações não correspondem a nenhum visitante autorizado.\n')
                    print('=' * 125)
                    print('\nApenas os visitantes autorizados podem entrar para visitação.\n')

        validar_acesso(visitantes_autorizados, numero_validacoes)

        # RF05 - Notificações de Visitas Agendadas

        print('=' * 125)

        visitas_agendadas = []  

        # Solicite ao usuário o agendamento de visitas
        while True:
            agendamento_dia = input('\n-> Escolha o dia da visita (1-7) ou digite "0" para encerrar: ')

            if agendamento_dia == '0':
                break
        
            if agendamento_dia not in ['1', '2', '3', '4', '5', '6', '7']:
                print("Dia de visita inválido. Escolha um número de 1 a 7.")
                continue
        
            agendamento_horas = input('\n-> Escolha o horário da visita (1-4): ')
        
            if agendamento_horas not in ['1', '2', '3', '4']:
                print("Horário de visita inválido. Escolha um número de 1 a 4.")
                continue
        
            dia_semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]
            dia = dia_semana[int(agendamento_dia) - 1]
            hora = ""

            if agendamento_horas == '1':
                print("10h - 12h")
                hora = "10h - 12h"
            
            elif agendamento_horas == '2':
                print("12h - 14h")
                hora = "12h - 14h"
            
            elif agendamento_horas == '3':
                print("14h - 16h")
                hora = "14h - 16h"
            
            elif agendamento_horas == '4':
                print("16h - 18h")
                hora = "16h - 18h"

            visita = {
                "dia": dia,
                "hora": hora
            }

            visitas_agendadas.append(visita)
            print(f"\nVisita agendada com sucesso para {dia} no horário de {hora}.\n")
            break

        # RF06 - Integração de Prontuário Eletrônico

        print('=' * 125)

        class ProntuarioEletronico:
            def __init__(self):
                self.pacientes = {}

            def adicionar_paciente(self, nome, data_nascimento, genero):
                paciente_id = len(self.pacientes) + 1
                self.pacientes[paciente_id] = {
                    "Nome": nome,
                    "Data de Nascimento": data_nascimento,
                    "Gênero": genero,
                    "Histórico Clínico": [],
                }
                return paciente_id

            def adicionar_historico_clinico(self, paciente_id, informacoes):
                if paciente_id in self.pacientes:
                    self.pacientes[paciente_id]["Histórico Clínico"].append(informacoes)
                else:
                    print("Paciente não encontrado.")

            def exibir_paciente(self, paciente_id):
                if paciente_id in self.pacientes:
                    paciente = self.pacientes[paciente_id]
                    print(f"Paciente ID: {paciente_id}")
                    for chave, valor in paciente.items():
                        if chave == "Histórico Clínico":
                            print(f"{chave}:")
                            for entrada in valor:
                                print(f"  - {entrada}")
                        else:
                            print(f"{chave}: {valor}")
                else:
                    print("Paciente não encontrado.")

        prontuario = ProntuarioEletronico()

        while True:
            print("\nOpções:")
            print("1. Adicionar paciente")
            print("2. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                # Solicitar informações do paciente
                nome = input(f"Nome do paciente: ")
                data_nascimento = input(f"Data de Nascimento DD/MM/AAAA: ")
                genero = input("Gênero (Masculino ou Feminino): ")

                # Verificar o gênero
                if genero.lower() == "masculino":
                    print(f"Olá, Sr. {nome}!")
                elif genero.lower() == "feminino":
                    print(f"Olá, Sra. {nome}!")
                else:
                    print(f"Olá, {nome}!")

                # Adicionar o paciente com informações inseridas pelo usuário
                paciente_id = prontuario.adicionar_paciente(nome, data_nascimento, genero)
                print("Paciente registrado com sucesso!")

                # Solicitar informações clínicas
                informacoes_clinicas = input("Adicionar informações clínicas: ")
            
                if genero.lower() == "masculino":
                    print(f"O Paciente {nome} está com : {informacoes_clinicas} ")
                elif genero.lower() == "feminino":
                    print(f"A Paciente {nome} está com : {informacoes_clinicas} ")
            
                prontuario.adicionar_historico_clinico(paciente_id, informacoes_clinicas)
            
                solucoes_clinicas = input("Adicionar o que será feito para melhora do paciente: ")
            
                if genero.lower() == "masculino":
                    print(f"\nPara melhora do paciente {nome} será feito : {solucoes_clinicas}\n ")
                elif genero.lower() == "feminino":
                    print(f"\nPara melhora da paciente {nome} será feito : {solucoes_clinicas}\n ")
            
            elif escolha == "2":
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Escolha novamente.")



    elif opcao == 5:
        class ProntuarioEletronico:
            def __init__(self):
                self.pacientes = {}

            def executar(self):
                print("Você selecionou o Prontuário Eletrônico.")

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


    elif opcao == 6:
        import csv

        class GestaoEquipes:
            def __init__(self):
                self.equipes = {}

            def executar(self):
                print("Você selecionou Gestão de Equipes.")


        profissionais = []


        def cadastrar_profissional():
            nome = input("\nNome do profissional: ")
            cargo = input("Cargo: ")
            experiencia = input("Experiência (em anos): ")
            contrato = input("Dados do contrato: ")

            profissional = {
                "Nome": nome,
                "Cargo": cargo,
                "Experiência": experiencia,
                "Contrato": contrato
            }

            profissionais.append(profissional)

            print("\nProfissional cadastrado com sucesso!")


        def salvar_em_txt():
            with open("profissionais.txt", "w") as file:
                for profissional in profissionais:
                    file.write(f"Nome: {profissional['Nome']}\n")
                    file.write(f"Cargo: {profissional['Cargo']}\n")
                    file.write(f"Experiência: {profissional['Experiência']} anos\n")
                    file.write(f"Contrato: {profissional['Contrato']}\n\n")
            print("\nDados salvos em profissionais.txt")


        def buscar_em_txt():
            termo_busca = input("\nDigite o termo de busca: ")

            with open("profissionais.txt", "r") as file:
                dados = file.read()
                if termo_busca in dados:
                    print("\nInformações encontradas:\n")
                    print(dados)


        def excluir_em_txt():
            termo_exclusao = input("\nDigite o termo a ser excluído: ")

            with open("profissionais.txt", "r") as file:
                linhas = file.readlines()
            with open("profissionais.txt", "w") as file:
                for linha in linhas:
                    if termo_exclusao not in linha:
                        file.write(linha)
            print(f"\nTermo '{termo_exclusao}' excluído com sucesso!")


        def salvar_em_csv():
            with open("profissionais.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Nome", "Cargo", "Experiência", "Contrato"])
                writer.writeheader()
                writer.writerows(profissionais)
            print("\nDados salvos em profissionais.csv")


        def buscar_em_csv():
            termo_busca = input("\nDigite o termo de busca: ")
            with open("profissionais.csv", "r") as file:
                reader = csv.DictReader(file)
                for profissional in reader:
                    if termo_busca in profissional.values():
                        print("\nInformações encontradas:\n")
                        print(profissional)


        def excluir_em_csv():
            termo_exclusao = input("\nDigite o termo a ser excluído: ")
            profissionais_copia = profissionais.copy()
            for profissional in profissionais_copia:
                if termo_exclusao in profissional.values():
                    profissionais.remove(profissional)
            salvar_em_csv()
            print(f"\nTermo '{termo_exclusao}' excluído com sucesso!")


        while True:
            print("-> Menu\n")
            print("1. Cadastrar profissional")
            print("2. Salvar em arquivo .txt")
            print("3. Excluir em arquivo .txt")
            print("4. Buscar em arquivo .txt")
            print("5. Salvar em arquivo .csv")
            print("6. Excluir em arquivo .csv")
            print("7. Buscar em arquivo .csv")
            print("8. Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                cadastrar_profissional()

            elif opcao == "2":
                salvar_em_txt()

            elif opcao == "3":
                excluir_em_txt()

            elif opcao == "4":
                buscar_em_txt()

            elif opcao == "5":
                salvar_em_csv()

            elif opcao == "6":
                excluir_em_csv()

            elif opcao == "7":
                buscar_em_csv()

            elif opcao == "8":
                break

            else:
                print("\nOpção inválida! Tente novamente.\n")



    elif opcao == 7:
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



    elif opcao == 8:
        import csv

        # Função para gerar relatório em formato .txt
        def gerar_relatorio_txt(relatorio_data, nome_arquivo):
            with open(nome_arquivo + ".txt", 'w') as file:
                for linha in relatorio_data:
                    file.write(linha + '\n')


        # Função para gerar relatório em formato .csv
        def gerar_relatorio_csv(relatorio_data, nome_arquivo):
            with open(nome_arquivo + ".csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(relatorio_data)


        # Função para coletar métricas da UTI
        def coletar_metricas_uti():
            metricas = {
                "Ocupacao_leitos": 85,
                "Eficiencia_equipamentos": 95,
                "Atendimento_pacientes": "Excelente"
            }
            return metricas


        # Função para gerar relatório de performance
        def gerar_relatorio():
            metricas_uti = coletar_metricas_uti()

            relatorio_data = []

            relatorio_data.append("Relatório de Performance da UTI")
            relatorio_data.append(f"Ocupação de Leitos: {metricas_uti['Ocupacao_leitos']}%")
            relatorio_data.append(f"Eficiência de Equipamentos: {metricas_uti['Eficiencia_equipamentos']}%")
            relatorio_data.append(f"Atendimento aos Pacientes: {metricas_uti['Atendimento_pacientes']}")

            gerar_relatorio_txt(relatorio_data, "relatorio_uti")
            gerar_relatorio_csv([relatorio_data], "relatorio_uti")

        if __name__ == "__main__":
            gerar_relatorio()

        def __init__(self):
                print("Você selecionou Relatórios e Análises.")

        def executar(self):
            print("Você selecionou Relatórios e Análises.")

    elif opcao == 9:
        print('\nDe volta ao gereciamento hospitalar, escolha a opção desejada!\n')
        continue
       
    elif opcao == 10:
        print('\nObigado, volte sempre!\n')
        break
       
    else:
        print('\nOpção inválida! Tente novamente.\n')




