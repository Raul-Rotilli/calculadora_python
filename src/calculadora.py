class Calculadora:

    def __init__(self, n1, n2):
        self._n1 = n1
        self._n2 = n2

    def soma(self):
        return self._n1 + self._n2

    def subtracao(self):
        return self._n1 - self._n2

    def multiplicacao(self):
        return self._n1 * self._n2

    def divisao(self):
        return self._n1 / self._n2
