palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=', ')

print('FIM')

aprovados = ['Felipe', 'Marina', 'Ana', 'Pedro', 'Junior']
for nome in aprovados:
    print(nome)


for indice, nome in enumerate(aprovados):
    print(f'{indice+1} => {nome}')

dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta',
               'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for numero in {1, 2, 3, 4, 5, 6, 7}:
    print(numero)