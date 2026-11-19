import csv


# Lê e valida números inteiros
def ler_inteiro(mensagem):

    while True:

        try:
            valor = int(input(mensagem))
            return valor

        except ValueError:
            print("Erro: digite apenas números inteiros.")


# Valida o tipo de imóvel
def ler_tipo_imovel():

    while True:

        tipo = input(
            "Tipo de imóvel (apartamento/casa/estudio): "
        ).strip().lower()

        if tipo in ["apartamento", "casa", "estudio"]:
            return tipo

        print(
            "Erro: escolha apartamento, casa ou estudio."
        )


# Valida quantidade de quartos
def ler_quartos():

    while True:

        quartos = ler_inteiro(
            "Quantidade de quartos (1 ou 2): "
        )

        if quartos in [1, 2]:
            return quartos

        print("Erro: informe apenas 1 ou 2.")


# Valida respostas Sim ou Não
def ler_sim_nao(mensagem):

    while True:

        resposta = input(
            mensagem
        ).strip().lower()

        if resposta in ["s", "n"]:
            return resposta == "s"

        print("Erro: digite apenas S ou N.")


# Valida quantidade de vagas
def ler_vagas():

    while True:

        vagas = ler_inteiro(
            "Quantidade de vagas: "
        )

        if vagas >= 0:
            return vagas

        print(
            "Erro: quantidade de vagas não pode ser negativa."
        )


# Valida a quantidade de parcelas
def ler_parcelas():

    while True:

        parcelas = ler_inteiro(
            "Número de parcelas (1 a 5): "
        )

        if 1 <= parcelas <= 5:
            return parcelas

        print(
            "Erro: informe um valor entre 1 e 5."
        )


# Gera arquivo CSV com a projeção de 12 meses
def gerar_csv(valor_aluguel):

    with open(
        "projecao_locacao.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        # Cabeçalho do arquivo
        escritor.writerow(
            ["Mes", "Valor do Aluguel"]
        )

        # Escreve os 12 meses da projeção
        for mes in range(1, 13):

            escritor.writerow(
                [mes, f"{valor_aluguel:.2f}"]
            )

    print("\nCSV gerado com sucesso!")