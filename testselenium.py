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

# Espera implícita por 10 segundos
driver.implicitly_wait(10)

# Abra o site
driver.get('https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/indice-financeiro-ifnc-composicao-da-carteira.htm')

# Aceitar cookies
aceitar_button = WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
)
aceitar_button.click()

# Encontre o botão de download
download_button = driver.find_element(By.XPATH, '//*[@id="divContainerIframeB3"]/div/div[1]/form/div[2]/div/div[2]/div/div/div[1]/div[2]/p/a')

# Clique no botão de download usando JavaScript
driver.execute_script("arguments[0].click();", download_button)

# Aguarde o download ser concluído
time.sleep(20)  # Isso pode variar dependendo do tamanho do arquivo

# Feche o navegador
driver.quit()
