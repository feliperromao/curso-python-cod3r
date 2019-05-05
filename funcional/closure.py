#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

if __name__ == "__main__":
    dobro = multiplicar(2)
    triplo = multiplicar(3)

    print(f'O dobro de 10 eh {dobro(10)}')
    print(f'O triplo de 10 eh {triplo(10)}')
