import csv
import pandas as pd

def carregar_dados():
    with open('../dados/Base_Varejo.csv', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=';')

        dados = list(leitor)

    df = pd.DataFrame(dados)
    
     # Converter colunas numéricas
    colunas_numericas = [
        'CO_ID',
        'CL_ID',
        'CL_EC',
        'CL_FHL',
        'PR_ID'
    ]

    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(
            df[coluna],
            errors='coerce'
        )
    return df

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
    print('\n--> Análise por coluna:')

    print('\nAnálise estatística das colunas numéricas:')
    print('-----------------------------------')
    print(df.describe())
    
    print('\n--> Análise de colunas específicas:')
    
    print('\nValores únicos na coluna CL_GENERO:')
    print('-----------------------------------')
    print(df["CL_GENERO"].unique())
    
    print('\nValores únicos na coluna CL_SEG:')
    print('-----------------------------------')
    print(df["CL_SEG"].unique())
    
    print('\nValores únicos na coluna PR_CAT:')
    print('-----------------------------------')
    print(df["PR_CAT"].unique())
    
    print('\nPrimeiros valores da coluna DATA:')
    print('-----------------------------------')
    print(df["DATA"].head(10))

def analisar_duplicatas(df):
    print('\n--> Análise de duplicatas:')
    print('-----------------------------------')
    print(f'Número total de linhas: {len(df)}')
    print(f'Número de linhas duplicadas: {df.duplicated().sum()}')

    print('\nExemplo de linhas duplicadas:')
    print('-----------------------------------')
    print(df[df.duplicated()].head())

    print('\nNúmero de duplicatas considerando apenas as colunas CO_ID, PR_NOME e DATA:')
    print('-----------------------------------')
    print(df[['CO_ID', 'PR_NOME', 'DATA']].duplicated().sum())

def analisar_correspondencia(df):
    print('\n--> Análise de correspondências:')
    print('\nAnálise de correspondência entre PR_NOME e PR_ID:')
    print('-----------------------------------')
    inconsistencias_nome = df.groupby('PR_NOME')['PR_ID'].nunique()
    print(inconsistencias_nome[inconsistencias_nome > 1])

    print('\nProdutos duplicados com diferentes PR_ID:')
    print('-----------------------------------')
    produtos_duplicados = (
        df.groupby('PR_NOME')['PR_ID']
        .unique()
    )
    print(produtos_duplicados[produtos_duplicados.apply(len) > 1])

    print('\nAnálise de correspondência entre PR_CAT e PR_NOME:')
    print('-----------------------------------')
    inconsistencias_cat = df.groupby('PR_CAT')['PR_NOME'].nunique()
    print(inconsistencias_cat[inconsistencias_cat > 1])

    print('\nAnálise de correspondência entre PR_CAT e PR_ID:')
    print('-----------------------------------')
    inconsistencias_pr_id = df.groupby('PR_CAT')['PR_ID'].nunique()
    print(inconsistencias_pr_id[inconsistencias_pr_id > 1])
