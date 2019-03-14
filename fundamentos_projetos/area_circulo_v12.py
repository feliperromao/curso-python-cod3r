from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def calcular(raio):
    area = pi * float(raio) ** 2
    return area


def myHelp():
    print('É necessário informar a área do circulo.')
    print('Sintaxe: {} <raio>'.format(__file__))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        myHelp()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        myHelp()

        print(TerminalColor.ERRO +
              '- É necessário informar um valor númérico' +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = calcular(raio)
    print(f'Área do circulo é: {area} m²')
