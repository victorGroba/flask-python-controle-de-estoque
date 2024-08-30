import pandas as pd

# Caminho do arquivo Excel
caminho_arquivo = "Z:/Controles do Setor de Meios de Cultura/Controle de Qualidade.xlsx"

# Carregar as planilhas
xls = pd.ExcelFile(caminho_arquivo)
entrada_saida_df = pd.read_excel(xls, sheet_name="ENTRADA | SAÍDA", engine='openpyxl')

# Verificar os nomes das colunas
print("Colunas na aba 'ENTRADA | SAÍDA':", entrada_saida_df.columns)

# Verificar as primeiras linhas para entender como os dados estão organizados
print(entrada_saida_df.head())

# Ajustar o índice da linha para a partir de 1562
linha_inicio = 1562
dados_filtrados = entrada_saida_df.loc[linha_inicio - 1:]

# Filtrar os dados que têm 'PREPARO' na coluna C
# Nota: Certifique-se de que o nome da coluna esteja correto
if 'C' in dados_filtrados.columns:
    dados_filtrados = dados_filtrados[dados_filtrados['C'] == 'PREPARO']
else:
    print("Erro: A coluna 'C' não foi encontrada.")

# Selecionar as colunas A e D para copiar
# Verifique se as colunas estão corretas
if {'A', 'D'}.issubset(dados_filtrados.columns):
    dados_para_copiar = dados_filtrados[['A', 'D']]
else:
    print("Erro: Uma ou mais colunas esperadas ('A', 'D') não foram encontradas.")
    dados_para_copiar = pd.DataFrame()  # Definir como DataFrame vazio para evitar erro posterior

# Carregar a aba PERFORMANCE
performance_df = pd.read_excel(xls, sheet_name="PERFORMANCE", engine='openpyxl')

# Encontrar a primeira linha disponível na aba PERFORMANCE
ultima_linha_performance = performance_df.shape[0]
primeira_linha_vazia = ultima_linha_performance + 1

# Adicionar os dados à aba PERFORMANCE
if not dados_para_copiar.empty:
    performance_df = pd.concat([performance_df, dados_para_copiar], ignore_index=True)
else:
    print("Nenhum dado para copiar.")

# Salvar as alterações de volta ao arquivo Excel
with pd.ExcelWriter(caminho_arquivo, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    performance_df.to_excel(writer, sheet_name="PERFORMANCE", index=False)

print("Dados transferidos com sucesso!")
