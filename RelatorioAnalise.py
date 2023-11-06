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