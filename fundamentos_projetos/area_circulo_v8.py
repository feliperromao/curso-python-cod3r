from math import pi
import sys

def calcular(raio):
    area = pi * float(raio) ** 2
    return area

if __name__ == '__main__':
    raio = sys.argv[1]
    area = calcular(raio)
    print(f'Área do circulo é: {area} m²')
