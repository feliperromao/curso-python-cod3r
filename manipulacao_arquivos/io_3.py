try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('NOME: {} - IDADE: {}'.format( *registro.strip().split(',') ))

finally:
    arquivo.close()