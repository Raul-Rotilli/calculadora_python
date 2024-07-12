import os

from src.calculadora import Calculadora
def menu():
    while(True):
        print('''
        Calculadora
    
        1- Soma
        2- Subtração
        3- Multiplicação
        4- Divisão
        s - Sair
    
        ''')
        escolha = input("Escolha uma opção:").upper()

        if escolha == 'S':
            print(f'\n\nObrigado por utilizar nossa Calculadora')
            break

        if escolha not in ['1', '2', '3', '4']:
            opcao_invalida()
            continue

        n1 = int(input('Primeiro número:'))
        n2 = int(input('Segundo número:'))
        calculadora = Calculadora(n1,n2)

        match escolha:
            case '1':
                formatar_resultado(n1, '+', n2, calculadora.soma())
            case '2':
                formatar_resultado(n1, '-', n2, calculadora.subtracao())
            case '3':
                formatar_resultado(n1, 'X', n2, calculadora.multiplicacao())
            case '4':
                formatar_resultado(n1, '/', n2, calculadora.divisao())
            case _:
                opcao_invalida()


def voltar_menu_principal():
    '''Função com intuito de voltar ao menu principal ao apertar qualquer tecla'''
    input('\nDigite uma tecla para voltar para o menu principal ')
    main()

def opcao_invalida():
    print('Essa opção não existe! Tente de novo.')

def formatar_resultado(n1, operacao, n2, resultado):
    print(f'\nResultado:')
    print(f'{n1} {operacao} {n2} = {resultado}')
    voltar_menu_principal()


def main():
    menu()



if __name__ == '__main__':
    main()