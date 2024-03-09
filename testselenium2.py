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
driver.get('https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/indice-financeiro-ifnc-composicao-da-carteira.htm')

# Espera até que o botão de aceitar cookies seja clicável
aceitar_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
)

# Clique no botão de aceitar cookies
aceitar_button.click()

# Espera até que o botão de download seja visível
download_button = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#divContainerIframeB3 div.form-layout div:nth-child(2) div:nth-child(2) p a'))
)

# Espera até que o botão de download seja clicável
download_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#divContainerIframeB3 div.form-layout div:nth-child(2) div:nth-child(2) p a'))
)

# Clique no botão de download usando JavaScript
driver.execute_script("arguments[0].click();", download_button)

# Aguarde o download ser concluído
time.sleep(30)  # Isso pode variar dependendo do tamanho do arquivo

# Feche o navegador
#driver.quit()
