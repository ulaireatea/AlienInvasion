alien_0 = {'cor': 'verde', 'pontuacao': 5} #dicionario é representado entre chaves

print(alien_0['cor'])

alien_0['cor'] = 'azul' #altera info do dicionario

print(alien_0['cor'])
print(alien_0['pontuacao'])

alien_0['pontuacao'] = 4 #altera info do dicionario

print('O alien agora tem ' + str(alien_0['pontuacao']) + ' pontos.')

print(alien_0)

alien_0['posicao_x'] = 0 #inclui info no dicionario
alien_0['posicao_y'] = 25 #inclui info no dicionario

print(alien_0)
