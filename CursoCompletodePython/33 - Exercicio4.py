import Exercicio3_modulo #modulo tem que estar na mesma pasta!

continuar = ''

while True:
    continuar = input('\nDeseja jogar par ou impar? S/N ')
    if continuar.lower() == 'n':
        break
    else:
        jogador1 = input('Digite o nome do jogador 1: ')
        jogador2 = input('Digite o nome do jogador 2: ')
        par_ou_impar = input(jogador1 + ', digite 1 para impar e 2 para par: ')

        if par_ou_impar != '1' and par_ou_impar != '2':
            print('Opcao invalida!')
            continue

        else:
            num_jog1 = int(input(jogador1 + ', digite um numero qualquer: '))
            num_jog2 = int(input(jogador2 + ', digite um numero qualquer: '))
            soma = Exercicio3_modulo.soma(num_jog1, num_jog2)
            resultado = Exercicio3_modulo.par_impar(num_jog1, num_jog2)
            print('\nO ' + jogador1 + ' escolheu ' + str(num_jog1) + ' e o ' + jogador2 + ' escolheu ' + str(num_jog2))
            print('e a soma da ' + str(soma) + ' que é ' + resultado)

            if resultado == 'PAR':
                if par_ou_impar == '1':
                    print('\nParabens ' + jogador2 + ' voce eh o vencedor!')
                else:
                    print('\nParabens ' + jogador1 + ' voce eh o vencedor!')
            else:
                if par_ou_impar == '1':
                    print('\nParabens ' + jogador1 + ' voce eh o vencedor!')
                else:
                    print('\nParabens ' + jogador2 + ' voce eh o vencedor!')

print('\nEspero que tenha se divertido, volte novamente.')
