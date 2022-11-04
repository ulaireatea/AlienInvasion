convidados = []

while True:
    convidado = input('Digite o nome do convidado ou digite FIM: ')

    if convidado.lower() == 'fim':
        break
    else:
        convidados.append(convidado.title())
convidados.sort()

print('\n########## Lista de Convidados ############\n')

for convidado in convidados:
    print(convidado)
