#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

pessoas = [
    {'nome': 'Jose Romao', 'idade': 17},
    {'nome': 'Marina', 'idade': 52},
    {'nome': 'Felipe Martins', 'idade': 54},
    {'nome': 'Felipe', 'idade': 12},
]

result = filter(lambda p: len(p['nome']) >= 7,  pessoas)

print(list(result))