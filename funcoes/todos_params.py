#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

def todos_params(*args, **kwargs):
    print(f'{args}')
    print(f'{kwargs}')


if __name__ == "__main__":
    print('________________________________________')
    todos_params('a','b','c')
    print('________________________________________')
    todos_params(nome='Romao', idade=27)
    print('________________________________________')
    todos_params(1,2,3, legal=True, valor=12.99)