#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python
from functools import reduce

pessoas = [
    {'nome': 'Jose Romao', 'idade': 17},
    {'nome': 'Marina', 'idade': 40},
    {'nome': 'Felipe Martins', 'idade': 24},
    {'nome': 'Felipe', 'idade': 12},
]

valor_inicial = 0
soma_idades = reduce(lambda idades, pessoa: idades + pessoa['idade'], pessoas, valor_inicial)

print(soma_idades)