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

    print('\nInformações gerais do DataFrame, incluindo tipos de dados e valores nulos:')
    print('-----------------------------------')
    print(df.info())

    print('\nNomes das colunas:')
    print('-----------------------------------')
    print(df.columns)

    print('\nTipos de dados das colunas:')
    print('-----------------------------------')
    print(df.dtypes)

    print('\nValores nulos por coluna:')
    print('-----------------------------------')
    print(df.isnull().sum())

def analisar_colunas(df):
    print('\n--> Análise estatística das colunas numéricas:')
    print('-----------------------------------')
    print(df.describe())
    
    print('\n--> Análise de colunas específicas:')
    print('-----------------------------------')
    
    print('\nValores únicos na coluna CL_GENERO:')
    print(df["CL_GENERO"].unique())
    
    print('\nValores únicos na coluna CL_SEG:')
    print(df["CL_SEG"].unique())
    
    print('\nValores únicos na coluna PR_CAT:')
    print(df["PR_CAT"].unique())
    
    print('\nPrimeiros valores da coluna DATA:')
    print(df["DATA"].head(10))
