import pandas as pd
import unicodedata

def limpar_texto(df):
    # Remove espaços extras, acentos e converte textos para maiúsculo
    colunas_texto = df.select_dtypes(include=['object']).columns

    for coluna in colunas_texto:

        # Ignora DATA pois será tratada separadamente
        if coluna == 'DATA':
            continue

        df[coluna] = df[coluna].astype(str).str.strip()

        df[coluna] = df[coluna].apply(
            lambda x: unicodedata.normalize('NFKD', x)
            .encode('ascii', 'ignore')
            .decode('utf-8')
        )

        df[coluna] = df[coluna].str.upper()

    return df

def remover_colunas_vazias(df):
    # Remove colunas totalmente nulas
    df = df.dropna(axis=1, how='all')

    # Remove colunas com nome vazio
    df = df.loc[:, df.columns.str.strip() != '']  

    return df

def substituir_nulos(df):
    #Substitui valores "#N/D" por "SEM CATEGORIA" na coluna PR_CAT
    df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'SEM CATEGORIA')
    # Substitui nomes inválidos por valor nulo
    df['PR_NOME'] = df['PR_NOME'].replace('#N/D', pd.NA)
    return df

def limpar_datas(df):
    # Remove espaços e converte a coluna DATA para datetime
    df['DATA'] = (
        df['DATA']
        .astype(str)
        .str.strip()
        .str.replace(r'[^0-9/]', '', regex=True)
    )

    df['DATA'] = pd.to_datetime(
        df['DATA'],
        format='%d/%m/%Y',
        errors='coerce'
    )
    
    return df

def salvar_dados_limpos(df):
    print("\nSalvando arquivo limpo...")
    df.to_csv('../dados/Base_Varejo_Limpa.csv', index=False)
    print("Arquivo salvo com sucesso!")
    
    return df
