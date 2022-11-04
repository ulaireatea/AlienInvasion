def animais(especie, nome):
    especie = especie
    nome = nome
    print('Eu tenho um ' + especie + ' chamado ' + nome)


animais(nome='Aquiles', especie='cachorro')
animais('cachorro', 'Aquiles')
animais(especie='gato', nome='Bichano')
animais('gato', 'Pantera Negra')
animais('Aquiles', 'cachorro')
animais('', 'Aquiles')


def nome_completo(primeiro_nome='', ultimo_nome='', nome_do_meio=''):
    primeiro_nome = primeiro_nome
    ultimo_nome = ultimo_nome
    nome_do_meio = nome_do_meio

    if nome_do_meio != '':
        print('O nome digitado foi ' + primeiro_nome.title() + ' ' + nome_do_meio.title() + ' ' + ultimo_nome.title())

    else:
        print('O nome digitado foi ' + primeiro_nome.title() + ' ' + ultimo_nome.title())


nome_completo(primeiro_nome='Marcelo', nome_do_meio='de Moura', ultimo_nome='Cabral')
nome_completo('Marcelo', 'Cabral')

