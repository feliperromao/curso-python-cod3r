#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_caverndas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Autralopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    gork = Neanderthal('Gork')

    print(f'Evolução (a partir da classe): { ", ".join(HomoSapiens.especies()) }')
    print(f'Evolução (a partir da instancia): { ", ".join(gork.especies()) }')
    print(f'Homo Sapiens evoluido:? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido:? {Neanderthal.is_evoluido()}')
    print(f'José evoluido:? {jose.is_evoluido()}')
    print(f'Gork evoluido:? {gork.is_evoluido()}')
