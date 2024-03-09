import requests
import os

# URL direta do arquivo de download
url = 'https://www.b3.com.br/indexPage/day/IFNC?language=pt-br'

# Defina o caminho para o diretório onde você deseja salvar o arquivo
download_directory = 'Github'

# Verifica se o diretório de download existe e o cria se não existir
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Nome do arquivo que você deseja salvar
file_name = 'downloadb3'

# Caminho completo do arquivo que você deseja salvar
file_path = os.path.join(download_directory, file_name)

# Faça a solicitação HTTP para baixar o arquivo
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Abra o arquivo em modo de escrita binária e escreva os dados nele
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print('Download concluído com sucesso.')
else:
    print('Falha ao fazer o download. Código de status:', response.status_code)
