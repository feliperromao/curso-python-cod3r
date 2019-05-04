#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome} - {self.idade} anos'

    def is_adult(self):
        return True if self.idade >= 18 else False


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def ultima_compra(self):
        return self.compras[-1].data

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total

def main():
    vendedor = Vendedor('Marina Lacerda', 88, 4000)
    cliente = Cliente('Felipe Romao', 90)
    compra = Compra(vendedor, datetime.now(), 50)
    cliente.registrar_compra(compra)

if __name__ == "__main__":
    main()