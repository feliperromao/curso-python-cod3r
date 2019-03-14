from decimal import Decimal, getcontext

print(dir(int))
print(dir(float))

# Alterando a precisão
getcontext().prec = 4

# calculando com precisão
print(Decimal(1) / Decimal(7))

# retornando o maior numero entre dois valores
print(Decimal.max(Decimal(1), Decimal(7)))

print(Decimal(1.1) + Decimal(2.2))