carros = ['ferrari', 'mustang', 'BMW', 'corvette', 'civic', 'corola']
print('Eu comprei um carro do modelo ' + carros[0])
# ou ainda...
for carro in carros: #carro variavel local
    print('Eu quero do modelo ' + carro)

numeros = list(range(0, 101, 4))
print(numeros)

for n in numeros:
    print(n)

for n in range(1, 101):
    print(n)

numeros = []
for n in range(1, 101):
    numeros.append(n)  #acrescenta dentro da lista (que esta vazia no inicio)
print(numeros)



