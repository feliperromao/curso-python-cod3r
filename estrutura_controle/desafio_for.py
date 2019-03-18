from random import randint


def sortear_dado():
    return randint(1, 6)


for x in range(1, 7):
    if (x % 2) != 0:
        continue
    if x == sortear_dado():
        print(f'Acertou {x}')
        break
else:
    print('Valor não encontrado :(')
