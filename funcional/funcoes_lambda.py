#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)

totais = tuple(
     map(
         lambda compra: compra['quantidade'] * compra['preco'],
         compras
     )
)

print(f'Precos totais: { totais }')
print(f'Total geral: {sum(totais)}')