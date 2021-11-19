import pytest
from fibonacci import inicializacao_fibonacci, Fibonacci


class TesteProjeto:
    def setup(self):
        pass

    def testeIter(self):
        x = iter(Fibonacci(5))

        assert next(x) == 0
        assert next(x) == 1
        assert next(x) == 1
        assert next(x) == 2
        assert next(x) == 3

    def testeInicializacao(self):
        x = inicializacao_fibonacci(6)

        assert x[0] == 0
        assert x[2] == 1
        assert x[4] == 3
        assert x[5] == 5
