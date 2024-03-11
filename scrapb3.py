import requests
import json
import pandas as pd

def get_dataframe(url: str):
    r = requests.get(url)
    dataframe = json.loads(r.text)
    return pd.DataFrame(dataframe['results'])

IMOB = get_dataframe('https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJpbmRleCI6IklNT0IiLCJzZWdtZW50IjoiMSJ9')

IFNC = get_dataframe('https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJpbmRleCI6IklGTkMiLCJzZWdtZW50IjoiMSJ9')

IAGRO = get_dataframe('https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJpbmRleCI6IklGTkMiLCJzZWdtZW50IjoiMSJ9')

IMLC = get_dataframe('https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJNTENYIiwic2VnbWVudCI6IjEifQ==')

#Importando IMOB
r = requests.get('https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJpbmRleCI6IklNT0IiLCJzZWdtZW50IjoiMSJ9')
IMOB = json.loads(r.text)
IMOB = pd.DataFrame(IMOB['results'])

