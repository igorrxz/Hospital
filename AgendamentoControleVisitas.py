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


