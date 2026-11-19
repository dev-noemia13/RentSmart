# Importação das classes de imóveis
from imovel import Apartamento, Casa, Estudio

# Importação da classe Contrato
from contrato import Contrato

# Importação das funções auxiliares
from utilitarios import (
    ler_tipo_imovel,
    ler_quartos,
    ler_sim_nao,
    ler_vagas,
    ler_parcelas,
    gerar_csv
)


# Título do sistema
print("=" * 50)
print("RENTSMART - SISTEMA DE LOCAÇÃO")
print("=" * 50)

# Solicita o tipo de imóvel
tipo = ler_tipo_imovel()


# ------ APARTAMENTO ------

if tipo == "apartamento":

    quartos = ler_quartos()

    garagem = ler_sim_nao(
        "Possui garagem? (S/N): "
    )

    possui_criancas = ler_sim_nao(
        "Possui crianças? (S/N): "
    )

    # Cria objeto apartamento
    imovel = Apartamento(
        quartos,
        garagem,
        possui_criancas
    )


# ------ CASA ------

elif tipo == "casa":

    quartos = ler_quartos()

    garagem = ler_sim_nao(
        "Possui garagem? (S/N): "
    )

    # Cria objeto casa
    imovel = Casa(
        quartos,
        garagem
    )


# ------ ESTÚDIO ------

else:

    vagas = ler_vagas()

    # Cria objeto estúdio
    imovel = Estudio(vagas)


# Solicita parcelamento da taxa contratual
parcelas = ler_parcelas()

# Cria objeto contrato
contrato = Contrato(parcelas)

# Calcula aluguel
valor_aluguel = imovel.calcular_aluguel()

# Calcula valor da parcela
valor_parcela = contrato.calcular_parcela()

# Exibe resultado
print("\n" + "=" * 50)
print("RESUMO DO ORÇAMENTO")
print("=" * 50)

print(
    f"Valor do aluguel mensal: R$ {valor_aluguel:.2f}"
)

print(
    f"Taxa contratual: R$ {contrato.taxa_contratual:.2f}"
)

print(
    f"Parcelamento da taxa: "
    f"{parcelas}x de R$ {valor_parcela:.2f}"
)

print("=" * 50)

# Gera projeção em CSV
gerar_csv(valor_aluguel)