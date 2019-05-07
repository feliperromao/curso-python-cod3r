#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

def cores_arco_iris():
    yield 'vermelho'
    yield 'larajna'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'

if __name__ == "__main__":
    generator = cores_arco_iris()
    print(type(generator))

    while True:
        print(next(generator))