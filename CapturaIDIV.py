import requests
import json
import pandas as pd
from IPython.display import display

def get_dataframe(url: str):
    r = requests.get(url)
    dataframe = json.loads(r.text)
    return pd.DataFrame(dataframe['results'])

# Dicionário contendo os nomes dos arquivos Excel e suas respectivas URLs
excel_urls = {
    'IDIV': 'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJRElWIiwic2VnbWVudCI6IjEifQ==',
}

def search_and_display_index(index_name: str):
    if index_name in excel_urls:
        url = excel_urls[index_name]
        df = get_dataframe(url)
        # Remover as colunas "segment" e "partAcum"
        df = df.drop(columns=['segment', 'partAcum'])
        # Ordenar o DataFrame pela coluna "part" do maior para o menor
        df_sorted = df.sort_values(by='part', ascending=False)
        # Selecionar apenas as 10 primeiras linhas
        df_top_10 = df_sorted.head(14)
        # Exibir o DataFrame no Jupyter Notebook
        display(df_top_10)
        # Exportar o DataFrame ordenado para um arquivo Excel
        filename = f"{index_name}_top_10_data.xlsx" 
        df_top_10.to_excel(filename, index=False)
        print(f"As 10 primeiras linhas do DataFrame '{index_name}' exportadas com sucesso para o arquivo '{filename}'")
    else:
        print(f"Índice '{index_name}' não encontrado.")

# Chamando a função para exibir o DataFrame 'IDIV' no Jupyter Notebook e exportar para Excel
search_and_display_index('IDIV')
