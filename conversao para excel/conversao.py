import pandas as pd


caminho_arquivo_txt = r"C:\Users\victo\OneDrive\Documentos\Controle de estoque\projeto_gestao_estoque\registros.txt"


datas = []
nomes = []
materiais = []
quantidades = []


with open(caminho_arquivo_txt, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        
        partes = linha.split('|')

        
        if len(partes) >= 2:
            
            data_hora = partes[0].strip()

            
            dados = partes[1].strip().split(',')

            
            if len(dados) >= 3:
                nome = dados[0].strip().split(': ')[1].strip()
                material = dados[1].strip().split(': ')[1].strip()
                quantidade = dados[2].strip().split(': ')[1].strip()

                
                datas.append(data_hora)
                nomes.append(nome)
                materiais.append(material)
                quantidades.append(quantidade)


dados_excel = pd.DataFrame({
    'Data e Hora': datas,
    'Nome': nomes,
    'Material': materiais,
    'Quantidade': quantidades
})


caminho_saida_excel = r"C:\Users\victo\OneDrive\Documentos\Controle de estoque\projeto_gestao_estoque\conversao para excel\registros.xlsx"


dados_excel.to_excel(caminho_saida_excel, index=False)

print(f'Arquivo Excel gerado com sucesso em: {caminho_saida_excel}')
