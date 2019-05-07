#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

def mapear(funcao, lista):
    # result = []
    # for x in lista:
    #     result.append( funcao(x) )
    # return result

    for elemento in lista:
        yield funcao(elemento)


if __name__ == "__main__":
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))