
def calcConceito(nota):
    nota = float(nota)
    if nota > 10 or nota < 0:
        return 'Nota inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota inválida'

if __name__ == '__main__':
    valorInformado = input('Nota do aluno: ')
    conceito = calcConceito(valorInformado)
    print('O conceito informado é: ' + conceito)