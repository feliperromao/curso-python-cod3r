pessoa = {
    'nome': 'Feipe',
    'idade': 27,
    'cursos': ['JavaScript', 'MySql', 'PHP', 'Python', 'ReactJS']
}
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][2])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', []))

