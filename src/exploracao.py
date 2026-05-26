import pandas as pd

def carregar_dados():
    return pd.read_csv("../dados/Base_Varejo.csv", delimiter=';')

def exibir_informacoes(df):
    print('\n--> Informações gerais sobre o DataFrame:')

    print('\nPrimeiras linhas do DataFrame:')
    print('-----------------------------------')
    print(df.head())

    print('\nDimensões do DataFrame - Linhas e Colunas:')
    print('-----------------------------------')
    print(df.shape)

    print('\nNomes das colunas:')
    print('-----------------------------------')
    print(df.columns)

    print('\nTipos de dados das colunas:')
    print('-----------------------------------')
    print(df.dtypes)

    print('\nValores nulos por coluna:')
    print('-----------------------------------')
    print(df.isnull().sum())
