# -*- coding: utf-8 -*-
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

yf.pdr_override()

PETR4 = wb.get_data_yahoo("PETR4.SA", start="2010-01-01")

print(PETR4)

print(PETR4.info())

print(PETR4.head(10))

print(PETR4.tail(9))
print("+=" * 40, "\n")

tickers = ["PETR4.SA", "GGBR4.SA", "MRVE3.SA", "CVCB3.SA"]
novos_dados = pd.DataFrame()
print(novos_dados.tail(10))

for t in tickers:
    novos_dados[t] = wb.get_data_yahoo(t, start="2010-1-1")["Adj Close"]
    print(novos_dados.tail(10))
# print(novos_dados.tail(10))
