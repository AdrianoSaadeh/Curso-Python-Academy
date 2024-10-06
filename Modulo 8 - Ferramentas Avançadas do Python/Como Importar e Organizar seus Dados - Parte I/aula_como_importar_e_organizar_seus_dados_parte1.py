"""Aula - Como Importar e Organizar seus Dados - Parte1

API : A sigla vem de "Interface de Programação de Aplicativos" e a informação vem de um servidor Web, então toda a informação
        vem da internet (nós vamos usar os dados do "yahoo" finance no decorrer das aulas) o Pandas DataReader vai nos ajudar
        a acessar esses dados

CSV : A Sigla vem de "Valor Separado por Vírgula" e não precisa de internet para ser acessado
"""

import numpy as np
import pandas as pd
import yfinance as yf
from pandas_datareader import data as wb

# Substitui a função padrão do pandas datareader pelo yfinance
yf.pdr_override()

PETR4 = wb.get_data_yahoo("PETR4.SA", start="2024-01-01")
print(PETR4)

VALE3 = wb.get_data_yahoo("VALE3.SA", start="2015-01-01")
print(VALE3)
