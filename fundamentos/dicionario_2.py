pessoa = {
    'nome': 'Fulano',
    'idade': 43,
    'cursos': ['React', 'Python']
}

print(pessoa)
pessoa.pop('idade')
print(pessoa)

pessoa.update({
    'cargo': 'Analista Desemvolvedor',
    'sexo': 'M'
})

print(pessoa)
pessoa.clear()

print(pessoa)