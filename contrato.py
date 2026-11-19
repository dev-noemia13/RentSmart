# Classe responsável pelos dados do contrato
class Contrato:

    def __init__(self, parcelas):

        # Taxa contratual fixa definida pela imobiliária
        self.taxa_contratual = 2000

        # Quantidade de parcelas escolhida
        self.parcelas = parcelas

    # Calcula o valor de cada parcela
    def calcular_parcela(self):
        return self.taxa_contratual / self.parcelas