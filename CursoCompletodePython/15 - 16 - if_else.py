num = 0
cor = 'preta'

if num == 1:

    if cor == 'azul':
        print(cor)

    elif cor == 'amarelo':
        print(cor)

    else:
        print('Cor não é azul nem amarelo')

else:
    print('Não executei os ifs anteriores')

carros = ['audi', 'bmw', 'ferrari', 'honda']

for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())
        