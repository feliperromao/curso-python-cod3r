#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce


# Portugues do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano que tenham 31 dias
# meses_31_dias = map(lambda m: m == 31, mdays)
meses_31_dias = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nomes= map(lambda mes: month_name[mes], meses_31_dias)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}', meses_nomes, 'Meses com 31 dias:')

print(juntar_meses)