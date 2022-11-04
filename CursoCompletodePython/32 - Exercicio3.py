import Exercicio3_modulo

continuar = ''

while True:
    continuar = input('\nDeseja calcular? S/N ')

    if continuar.lower() == 'n':
        break
    else:
        operacao = input('Qual operação deseja fazer? Digite\n 1 para soma\n2 para subtracao'
                         '\n3 para multiplicacao\n4 para divisao\n')
        if operacao == '1':
            num1 = int(input('Digite um numero: '))
            num2 = int(input('Digite um numero: '))
            print(Exercicio3_modulo.soma(num1, num2))
            print('')

        elif operacao == '2':
            num1 = int(input('Digite um numero: '))
            num2 = int(input('Digite um numero: '))
            print(Exercicio3_modulo.sub(num1, num2))
            print('')

        elif operacao == '3':
            num1 = int(input('Digite um numero: '))
            num2 = int(input('Digite um numero: '))
            print(Exercicio3_modulo.mult(num1, num2))
            print('')

        elif operacao == '4':
            num1 = int(input('Digite um numero: '))
            num2 = int(input('Digite um numero: '))
            print(Exercicio3_modulo.div(num1, num2))
            print('')

        else:
            print('\nOpcao invalida, tente novamente.\n')

print('Obrigado por utilizar a calculadora.')
