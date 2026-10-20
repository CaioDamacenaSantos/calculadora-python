print('OBS:: Esta é uma calculadora simples feita em Python. Suporta 6 operações matemáticas entre 2 números reais.\n')

# ------------ título ------------
print('=' * 20 + '\n' + '{:^20}'.format('CALCULADORA') + '\n' + '=' * 20)

# ------------ funções ------------

def ler_numero(mensagem):
    #Função que fica presa em repetição até o usuário digitar um número válido
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('ERRO! Digite um valor numérico válido!')

# ------------ código ------------

loop = 'y'
while loop == 'y':
    while True:
        try:
            operacao = int(input('''Escolha a Operação:
[1] - Adição
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
[5] - Potenciação
[6] - Raiz Quadrada
''' + '-' * 18 + '\n'))
            print('-=' * 15)

            if operacao == 1:
                n1 = ler_numero('Digite o primeiro número: ')
                n2 = ler_numero('Digite o segundo número: ')
                print(f'{n1} + {n2} = {n1 + n2}')
                break

            elif operacao == 2:
                n1 = ler_numero('Digite o primeiro número: ')
                n2 = ler_numero('Digite o segundo número: ')
                print(f'{n1} - {n2} = {n1 - n2}')
                break

            elif operacao == 3:
                n1 = ler_numero('Digite o primeiro número: ')
                n2 = ler_numero('Digite o segundo número: ')
                print(f'{n1} * {n2} = {n1 * n2}')
                break

            elif operacao == 4:
                n1 = ler_numero('Digite o numerador: ')
                n2 = ler_numero('Digite o denominador: ')
                if n2 == 0:
                    print('Não é possível dividir por zero!')
                else:
                    print(f'{n1} ÷ {n2} = {n1 / n2}')
                break

            elif operacao == 5:
                n1 = ler_numero('Digite a base: ')
                n2 = ler_numero('Digite o expoente: ')
                print(f'{n1} elevado à {n2} potência é igual a: {n1 ** n2}')
                break

            elif operacao == 6:
                while True:
                    n1 = ler_numero('Digite o número para a raiz quadrada: ')
                    if n1 < 0:
                        print('Não é possível calcular a raiz de um número negativo!')
                    else:
                        print(f'√{n1} = {n1 ** 0.5}')
                        break
                break
            else:
                print('ERRO! Selecione uma Opção Válida entre 1 e 6!')
                

        except ValueError:
            print('ERRO! Digite um número inteiro correspondente à operação.')

    print('-=' * 15)

    # ------ Finaliza ou prossegue o Loop ------
    loop = ''
    while loop != 'n' and loop != 'y':
        loop = input('Deseja fazer um novo cálculo? (y/n): ').lower().strip()
        if loop != 'n' and loop != 'y':
            print('Por favor, digite apenas [y] ou [n].')
# ------------ Fim do Algoritmo ------------
print('=' * 20)
print('DESLIGANDO...')
