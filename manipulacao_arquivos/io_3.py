try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('NOME: {} - IDADE: {}'.format( *registro.strip().split(',') )) # Linha com erro, falta um *

except IndexError:
    pass
finally:
    arquivo.close()

if arquivo.closed:
    print('O arquivo está fechado')