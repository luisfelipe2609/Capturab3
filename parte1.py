import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Defina o caminho para o diretório onde o ChromeDriver está localizado
chrome_driver_path = 'caminho_para_o_seu_chromedriver'

# Opções do Chrome para configurar o download automático
options = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'caminho_para_o_seu_diretorio_de_download'}
options.add_experimental_option('prefs', prefs)

# Adicione o diretório do ChromeDriver ao PATH do sistema
os.environ['PATH'] += os.pathsep + chrome_driver_path

# Crie o driver com as opções configuradas
driver = webdriver.Chrome(options=options)

# Abra o site
driver.get('https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/indice-agronegocio-free-float-setorial-agfs-composicao-da-carteira.htm')

# Espere até que o botão de download esteja presente na página
aceitar_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
)

# Clique no botão de download
aceitar_button.click()

# Espere até que o botão de download esteja presente na página
download_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="divContainerIframeB3"]/div/div[1]/form/div[2]/div/div[2]/div/div/div[1]/div[2]/p/a'))
)

# Clique no botão de download
download_button.click()

# Aguarde o download ser concluído
time.sleep(10)  # Isso pode variar dependendo do tamanho do arquivo

# Feche o navegador
driver.quit()
