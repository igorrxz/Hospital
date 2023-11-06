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

