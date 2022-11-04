class Carros:
    'Uma tentativa simples de representar um carro.'

    def __init__(self, fabricante, modelo, ano):
        'Inicializa os atributos que descreve um carro'
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def descricao_nome(self):
        'Devolve o nome descritivo formatado de modo elegante.'
        nome_longo = str(self.ano) + ' ' + self.fabricante + ' ' + self.modelo
        return nome_longo.title()

    def leia_odometro(self):
        'Exibe uma frase que mostra os kilometros rodados.'
        print('O carro tem ' + str(self.odometro) + ' KM rodados.')

    def altera_odometro(self, novo_odometro):
        'Alterar o odometro pelo valor passado como argumento.'
        self.odometro = novo_odometro

    def incremento_odometro(self, novo_odometro):
        'Incrementa um determinado valor ao odometro.'
        self.odometro += novo_odometro



meu_carro = Carros('Audi', 'a4', 2016)

print(meu_carro.descricao_nome())
meu_carro.leia_odometro()
print('')
print('Mudando o odometro!')

meu_carro.odometro = 5
meu_carro.leia_odometro()

print('')
print('Mudando o odometro!')
meu_carro.altera_odometro(10) #outra forma de mudar 'odometro'
meu_carro.leia_odometro()

print('')
print('Mudando o odometro!')
meu_carro.incremento_odometro(10)
meu_carro.leia_odometro()

print('')
print('Mudando o odometro!')
meu_carro.incremento_odometro(3)
meu_carro.leia_odometro()
print('')

meu_outro_carro = Carros('honda', 'civic', 2015)

print(meu_outro_carro.descricao_nome())
meu_outro_carro.leia_odometro()
print('')
print('Mudando o odometro!')

meu_outro_carro.odometro = 5
meu_outro_carro.leia_odometro()

print('')
print('Mudando o odometro!')
meu_outro_carro.altera_odometro(10) #outra forma de mudar 'odometro'
meu_outro_carro.leia_odometro()

print('')
print('Mudando o odometro!')
meu_outro_carro.incremento_odometro(10)
meu_outro_carro.leia_odometro()

print('')
print('Mudando o odometro!')
meu_outro_carro.incremento_odometro(3)
meu_outro_carro.leia_odometro()
print('')