#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

from app.utils.gerador import novo_nome
from app.negocio import nome_existe
from app.negocio.backend import add_nome


def main():
    while True:
        nome = novo_nome()
        print(f'o nome gerado foi {nome}')
        if not nome_existe(nome):
            add_nome(nome)
            break
        else:
            print(f'o nome {nome} ja existe na lista')

if __name__ == '__main__':
    main()