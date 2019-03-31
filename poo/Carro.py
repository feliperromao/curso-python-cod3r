class Carro:
    def __init__(self, velocidadeMaxima=0):
        self.velocidadeMaxima = velocidadeMaxima
        self.velocidadeAtual = 0
    

    def acelerar(self, delta=5):
        if self.velocidadeMaxima >= self.velocidadeAtual + delta:
            self.velocidadeAtual += delta
        else:
            self.velocidadeAtual = self.velocidadeMaxima
        return self.velocidadeAtual

    def frear(self, delta=5):
        if self.velocidadeAtual - delta > 0:
            self.velocidadeAtual -= delta
        else:
            self.velocidadeAtual = 0
        return self.velocidadeAtual
        

if __name__ == "__main__":
    carro = Carro(180)
    for _ in range(20):
        print(carro.acelerar(20))

    for _ in range(20):
        print(carro.frear(20))