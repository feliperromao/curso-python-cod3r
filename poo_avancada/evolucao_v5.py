#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python
from abc import ABCMeta, abstractproperty

class Humano(metaclass=ABCMeta):
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade

    @abstractproperty
    def inteligente(self):
        pass


    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo')
        else:
            self._idade = idade

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

    @property
    def inteligente(self):
        return False

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    try:
        anonimo = Humano('Fulano')
        print(anonimo.inteligente)
    except TypeError:
        print('Classe abstrata')

    jose = HomoSapiens('José')
    jose.idade = 50

    ogro = Neanderthal('Ogro')
    ogro.idade = 700

    print(f'Nome: {jose.nome} - Idade: {jose.idade} - Inteligente: {jose.inteligente}')
    print(f'Nome: {ogro.nome} - Idade: {ogro.idade} - Inteligente: {ogro.inteligente}')
