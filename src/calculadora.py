# Requisitos Funcionais:
#
# Menu principal:
#
# Calculadora Simples
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# s. Sair
# Funcionamento:
#
# O usuário deve escolher a operação desejada digitando o número correspondente à opção no menu e pressionando Enter.
# Uma vez escolhida a operação, o aplicativo deve solicitar ao usuário que digite dois números.
# O aplicativo deve então executar a operação matemática selecionada sobre os dois números e exibir o resultado na tela.
# Importante: O aplicativo deve tratar a divisão por zero,
# exibindo uma mensagem de erro caso o usuário tente dividir um número por zero.
# Entradas:
#
# "Primeiro número:"
# "Segundo número:"
# Saída:
#
# "O resultado da [OPERAÇÃO SELECIONADA] é: [RESULTADO]"
# Ex.: "O resultado da soma é: 42"
# Retorno ao menu principal:
#
# Após a conclusão da operação, o aplicativo deve retornar ao menu principal.
# Finalização do aplicativo:
#
# Se o usuário digitar "s" no menu principal, o aplicativo deve agradecer ao usuário e sair.
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
