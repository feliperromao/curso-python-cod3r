#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

from generators_v1 import cores_arco_iris

if __name__ == "__main__":
    generator = cores_arco_iris()
    for cor in generator:
        print(cor)

    print('fim')