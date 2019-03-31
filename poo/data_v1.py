class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(20, 10, 1992)

print(d1)