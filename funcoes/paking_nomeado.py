# **kwargs
def resultado_f1(**poduim):
    for posicao, piloto in poduim.items():
        print(f'{posicao} -> {piloto}')

if __name__ == "__main__":
    resultado_f1(primeiro='L. Hamilton', segundo='M. Verstappen',
                terceiro='S. Vettel')