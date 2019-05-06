#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'Romao', 'idade': 50},
    {'nome': 'Marina', 'idade': 52},
    {'nome': 'Felipe', 'idade': 54},
]

so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))