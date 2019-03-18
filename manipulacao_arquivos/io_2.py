arquivo = open('pessoas.csv')
for registro in arquivo:
    print('NOME: {} - IDADE: {}'.format( *registro.split(',') ))

arquivo.close()