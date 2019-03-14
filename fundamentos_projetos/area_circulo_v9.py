from math import pi
import sys

def calcular(raio):
    area = pi * float(raio) ** 2
    return area

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('É necessário informar a área do circulo.')
        print('Sintaxe: {} <raio>'.format(__file__))
    else:
        raio = sys.argv[1]
        area = calcular(raio)
        print(f'Área do circulo é: {area} m²')
        
