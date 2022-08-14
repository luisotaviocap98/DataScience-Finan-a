import imp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import quandl
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import warnings as wn
from datetime import date
import dbnomics as db
import os
import geobr
import geopandas as gpd

def base_estudantes():
    return pd.read_csv('../Pandas/StudentsPerformance.csv')

def magalu():
    return yf.Ticker('MGLU3.SA').history(period='max')

def job():
    return pd.read_csv('../Pandas/STP-20220317102940796.csv', encoding='latin1', sep=';')

def alunos():
    np.random.seed(10)
    # quantidade de observações
    n = 100

    escolaridade = ['Ensino Fundamental', 'Ensino Médio', 'Ensino Superior']

    cidades = ['São Paulo', 'Recife', 'Salvador', 'Salvador', 'Rio de Janeiro']

    sexo = ['Masculino', 'Feminino']


    # dicionário com dados
    data = {
        'Id': np.arange(1, n+1),
        'Idade': np.random.randint(18, 70, size = n),
        'Renda': np.random.randint(1_500, 10_000, size = n),
        'Sexo': np.random.choice(sexo, size = n),
        'Escolaridade': np.random.choice(escolaridade, size = n),
        'Cidade': np.random.choice(cidades, size = n)
    }

    df = pd.DataFrame(data)
    return df

def petrobras():
    return yf.Ticker('PETR3.SA').history(period='max')