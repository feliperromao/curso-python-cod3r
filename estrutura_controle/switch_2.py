def get_dia_semana(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Semana',
        3: 'Semana',
        4: 'Semana',
        5: 'Semana',
        6: 'Semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, 'Inválido')


if __name__ == "__main__":
    for x in range(8):
        print(f'{x} = ', get_dia_semana(x))
