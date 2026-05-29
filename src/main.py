from exploracao import carregar_dados, exibir_informacoes

def main():
    df = carregar_dados()
    exibir_informacoes(df)

if __name__ == "__main__":
    main()