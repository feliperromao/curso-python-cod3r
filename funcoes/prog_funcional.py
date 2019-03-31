def executar(func):
    if callable(func):
        func()


def bom_dia():
    print('Bom dia')


def boa_tarde():
    print('Boa tarde')


if __name__ == "__main__":
    executar(boa_tarde)