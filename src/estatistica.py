
def analisar_filhos(df):
    coluna_filhos = df['CL_FHL']

    # Média
    media_filhos = coluna_filhos.mean()

    # Mediana
    mediana_filhos = coluna_filhos.median()

    # Moda
    moda_filhos = coluna_filhos.mode()[0]

    # Máximo
    maximo_filhos = coluna_filhos.max()

    # Mínimo
    minimo_filhos = coluna_filhos.min()

    # Desvio Padrão
    desvio_padrao_filhos = coluna_filhos.std()

    # Contagem
    contagem_filhos = coluna_filhos.count()

    # Quartis
    quartis_filhos = {
    '25%': float(coluna_filhos.quantile(0.25)),
    '50%': float(coluna_filhos.quantile(0.50)),
    '75%': float(coluna_filhos.quantile(0.75))
}

    return {
        'media': media_filhos,
        'mediana': mediana_filhos,
        'moda': moda_filhos,
        'maximo': maximo_filhos,
        'minimo': minimo_filhos,
        'desvio_padrao': desvio_padrao_filhos,
        'contagem': contagem_filhos,
        'quartis': quartis_filhos
    }
