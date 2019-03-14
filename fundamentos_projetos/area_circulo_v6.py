from math import pi

def calcular(raio):
    area = pi * float(raio) ** 2
    print(f'A área da circuferência é: {area} m²')

if __name__ == '__main__':
    raio = input('Por favor informe o radio da circuferência em metros: ')
    calcular(raio)
