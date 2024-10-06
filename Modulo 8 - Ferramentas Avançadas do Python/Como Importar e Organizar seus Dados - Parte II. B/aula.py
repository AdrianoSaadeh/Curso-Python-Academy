"""Aula - Como Importar e Organizar seus Dados - Parte 2A

API : A sigla vem de "Interface de Programação de Aplicativos" e a informação vem de um servidor Web, então toda a informação
        vem da internet (nós vamos usar os dados do "yahoo" finance no decorrer das aulas) o Pandas DataReader vai nos ajudar
        a acessar esses dados

CSV : A Sigla vem de "Valor Separado por Vírgula" e não precisa de internet para ser acessado
"""

import numpy as np
import pandas as pd
import yfinance as yf
from pandas_datareader import data as wb

# Habilita a sobrecarga do pandas_datareader com o yfinance
yf.pdr_override()

# Define os tickers das ações a serem consultadas
tickers = ["PETR4.SA", "GGBR4.SA", "MRVE3.SA", "CVCB3.SA"]
novos_dados = pd.DataFrame()

# Exibe as últimas 10 linhas do DataFrame vazio (será vazio neste momento)
print(novos_dados.tail(10))

# Loop para coletar os dados ajustados de fechamento das ações
for t in tickers:
    # Coleta dados do Yahoo Finance usando pandas_datareader e preenche com "Adj Close"
    novos_dados[t] = wb.get_data_yahoo(t, start="2010-01-01")["Adj Close"]

# Exibe as últimas 10 linhas do DataFrame com os dados preenchidos
print(novos_dados.tail(10))

# Exibe informações sobre o DataFrame
print(novos_dados.info())

# Salva os dados em um arquivo CSV
novos_dados.to_csv("exemploCSV.csv")
# Salva os dados em um arquivo Excel
novos_dados.to_excel("exemploExcel.xlsx")
# Lê os dados de um arquivo CSV e armazena-os em um DataFrame
novos_dados1 = pd.read_csv("exemploCSV.csv")
# Exibe o conteúdo completo do DataFrame recém-carregado
print(novos_dados1)
