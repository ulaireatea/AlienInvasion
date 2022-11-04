nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade < 16:
    print(nome + ', você tem ' + str(idade) + ' anos e seu voto não pode votar')

elif 16 >= idade <= 17 or idade > 64:
    print(nome + ', você tem ' + str(idade) + ' anos e seu voto é opcional')

else:
    print(nome + ', você tem ' + str(idade) + ' anos e seu voto é obrigatório')
