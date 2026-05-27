from exploracao import carregar_dados, exibir_informacoes, analisar_colunas, analisar_duplicatas
from limpeza import remover_colunas_vazias, substituir_nulos, limpar_datas, limpar_duplicatas


def main():
    df = carregar_dados()
    exibir_informacoes(df) 
    analisar_colunas(df)
    analisar_duplicatas(df)
    df = remover_colunas_vazias(df)
    df = substituir_nulos(df)
    df = limpar_datas(df)
    df = limpar_duplicatas(df)

    print("\nDados limpos:")
    print(df.head())

if __name__ == "__main__":
    main()