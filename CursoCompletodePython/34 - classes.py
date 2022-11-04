class Cachorro(): #começa com letra maiúscula por conveção
    'Uma tentativa simples de modelar um cachorro.'
    def __init__(self, nome, idade): #self é obrigatório, os outros são atributos que escolhesse
        'Inicializa os atributos nome e idade.'
        self.nome = nome
        self.idade = idade

    def sentar(self): #método
        'Simula um cachorro sentando em resposta a um comando.'
        print(self.nome.title() + ' está sentando.')

    def rolar(self): #método
        'Simula um cachorro rolando em resposta a um comando.'
        print(self.nome.title() + ' está rolando.')


meu_cachorro = Cachorro('Aquiles', 6) #instância

meu_cachorro.rolar() #executar método
meu_cachorro.sentar() #executar método

meu_outro_cachorro = Cachorro('Bingo', 5)

meu_outro_cachorro.rolar()
meu_outro_cachorro.sentar()

