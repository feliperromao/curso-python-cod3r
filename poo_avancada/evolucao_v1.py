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
    jose = Humano('José')
    gork = Humano('Gork').das_caverndas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'Jose.especie: {jose.especie}')
    print(f'Gork.especie: {gork.especie}')