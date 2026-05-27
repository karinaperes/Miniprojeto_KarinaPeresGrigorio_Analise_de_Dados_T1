from exploracao import (
    carregar_dados, 
    exibir_informacoes, 
    analisar_colunas, 
    analisar_duplicatas
    )
from limpeza import (
    limpar_texto,
    remover_colunas_vazias, 
    substituir_nulos, 
    limpar_datas
    )
from estatistica import analisar_filhos


def main():
    df = carregar_dados()
    exibir_informacoes(df) 
    analisar_colunas(df)
    analisar_duplicatas(df)
    df = limpar_texto(df)
    df = remover_colunas_vazias(df)
    df = substituir_nulos(df)
    df = limpar_datas(df)

    # Analisar filhos
    estatisticas_filhos = analisar_filhos(df)
    print("\nEstatísticas dos filhos:")
    for chave, valor in estatisticas_filhos.items():
        print(f"{chave.capitalize()}: {valor}")

    print("\nDados limpos:")
    print(df.head())

if __name__ == "__main__":
    main()
