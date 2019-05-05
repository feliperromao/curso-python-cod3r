#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == "__main__":
    funcs = [dobro, quadrado] * 5
    
    for func, numero in zip(funcs, range(1, 11)):
        print(f'O {func.__name__} de {numero} eh: {func(numero)}')
