import csv

with open('desafio-ibge.csv') as entry:
    for registro in csv.reader(entry):
        print('Região: {} - Cidade: {}'.format(registro[8], registro[3]))