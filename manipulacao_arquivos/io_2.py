arquivo = open('pessoas.csv')
for registro in arquivo:
    print('NOME: {} - IDADE: {}'.format( *registro.strip().split(',') ))

arquivo.close()