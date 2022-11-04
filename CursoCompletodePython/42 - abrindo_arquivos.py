texto = ''

while True:
    texto = input('Deseja continuar? S/N ')

    if texto.lower() == 'n':
        break

    else:
        with open('texto.txt', 'a') as arquivo:  # modo de concatenação
            diario = input('O que deseja escrever? Digite: ')
            arquivo.write('\n' + diario)
