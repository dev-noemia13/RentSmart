# Classe pai que representa um imóvel genérico
class Imovel:
    def __init__(self, aluguel_base):
        self.aluguel_base = aluguel_base

    # Retorna o valor do aluguel
    def calcular_aluguel(self):
        return self.aluguel_base


# Classe Apartamento herdando de Imovel
class Apartamento(Imovel):

    # Construtor da classe
    def __init__(self, quartos, garagem, possui_criancas):
        super().__init__(700)  # aluguel base do apartamento

        self.quartos = quartos
        self.garagem = garagem
        self.possui_criancas = possui_criancas

    # Calcula o aluguel do apartamento
    def calcular_aluguel(self):

        valor = self.aluguel_base

        # Adicional para 2 quartos
        if self.quartos == 2:
            valor += 200

        # Adicional de garagem
        if self.garagem:
            valor += 300

        # Desconto de 5% para quem não possui crianças
        if not self.possui_criancas:
            valor *= 0.95

        return valor


# Classe Casa herdando de Imovel
class Casa(Imovel):

    def __init__(self, quartos, garagem):
        super().__init__(900)  # aluguel base da casa

        self.quartos = quartos
        self.garagem = garagem

    # Calcula o valor da locação da casa
    def calcular_aluguel(self):

        valor = self.aluguel_base

        # Adicional para 2 quartos
        if self.quartos == 2:
            valor += 250

        # Adicional de garagem
        if self.garagem:
            valor += 300

        return valor


# Classe Estudio herdando de Imovel
class Estudio(Imovel):

    def __init__(self, vagas):
        super().__init__(1200)  # aluguel base do estúdio

        self.vagas = vagas

    # Calcula aluguel do estúdio
    def calcular_aluguel(self):

        valor = self.aluguel_base

        # Pacote inicial de duas vagas
        if self.vagas >= 2:

            valor += 250

            # Vagas extras acima de duas
            if self.vagas > 2:
                valor += (self.vagas - 2) * 60

        return valor