from math import pi

def calcular(raio):
    area = pi * float(raio) ** 2
    return area

if __name__ == '__main__':
    raio = input('Por favor informe o radio da circuferência em metros: ')
    area = calcular(raio)
    print(f'Área do circulo é: {area} m²')
