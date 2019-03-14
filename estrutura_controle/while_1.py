from random import randint

numeroInformado = -1
numeroSecreto = randint(0, 9)

while numeroInformado != numeroSecreto:
    numeroInformado = int(input('Digite um número: '))
print('Você acertou:')