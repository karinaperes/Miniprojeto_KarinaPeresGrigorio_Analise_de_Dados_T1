from exploracao import carregar_dados, exibir_informacoes, analisar_colunas


def main():
    df = carregar_dados()
    exibir_informacoes(df) 
    analisar_colunas(df)   

if __name__ == "__main__":
    main()