import matematico

continuar = ''

while True:
    continuar = input('\nDeseja calcular? S/N ')

    if continuar.lower() == 'n':
        break
    else:
        try:

            operacao = input('Qual operação deseja fazer? Digite\n1 para soma\n2 para subtração'
                             '\n3 para multiplicação\n4 para divisão\n')
            if operacao == '1':
                num1 = int(input('Digite um número: '))
                num2 = int(input('Digite outro número: '))
                print(matematico.soma(num1, num2))
                print('')

            if operacao == '2':
                num1 = int(input('Digite um número: '))
                num2 = int(input('Digite outro número: '))
                print(matematico.sub(num1, num2))
                print('')

            if operacao == '3':
                num1 = int(input('Digite um número: '))
                num2 = int(input('Digite outro número: '))
                print(matematico.mult(num1, num2))
                print('')

            if operacao == '4':
                num1 = int(input('Digite um número: '))
                num2 = int(input('Digite outro número: '))
                print(matematico.div(num1, num2))
                print('')

            else:
                print('\nVocê digitou uma opção inválida, tente novamente.\n')

        except ZeroDivisionError:
            print('\nOcorreu algum erro inesperado, verifique sua operação.')

print('\nObrigado por utilizar a calculadora')
