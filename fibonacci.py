class Fibonacci:
    def __init__(self, iteracao, anterior=0, proximo=1):
        self.iteracao = iteracao
        self.anterior = anterior
        self.proximo = proximo
        self.contador = 0

    def __iter__(self):
        self.var = 0
        return self

    def __next__(self):
        if self.iteracao == 0:
            raise StopIteration

        elif self.contador == 0:
            self.contador += 1
            self.iteracao -= 1
            return self.anterior

        elif self.contador == 1:
            self.contador += 1
            self.iteracao -= 1
            return self.proximo

        else:
            atual = self.anterior + self.proximo
            self.anterior = self.proximo
            self.proximo = atual
            self.iteracao -= 1
            return self.proximo


def inicializacao_fibonacci(iteracao):
    serie = Fibonacci(iteracao)
    fibonacci = iter(serie)
    return {k: v for k, v in enumerate(fibonacci)}
