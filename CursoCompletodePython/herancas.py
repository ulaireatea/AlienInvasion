class Carros:
    """Uma tentativa simples de representar um carro."""

    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descreve um carro"""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 100
        self.odometro = 0

    def descricao_nome(self):
        """Devolve o nome descritivo formatado de modo elegante."""
        nome_longo = str(self.ano) + ' ' + self.fabricante + ' ' + self.modelo
        return nome_longo.title()

    def leia_odometro(self):
        """Exibe uma frase que mostra os kilometros rodados."""
        print('O carro tem ' + str(self.odometro) + ' KM rodados.')

    def altera_odometro(self, novo_odometro):
        """Alterar o odometro pelo valor passado como argumento."""
        self.odometro = novo_odometro

    def incremento_odometro(self, novo_odometro):
        """Incrementa um determinado valor ao odometro."""
        self.odometro += novo_odometro

    def tanque_gasolina(self):
        """Exibe a quantidade de gasolina disponível."""
        print('O tanque de gasolina está ' + str(self.combustivel) + '% cheio.')


carro1 = Carros('honda', 'civic', 2015)
print(carro1.descricao_nome())
carro1.tanque_gasolina()


class CarrosEletricos(Carros):
    """Representa aspectos de um carro especifico."""

    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos da classe pai"""
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()

    def tanque_gasolina(self):  # ignora o mesmo método da classe pai (superclasse)
        """Carros eletricos não usam gasolina."""
        print('Carros eletricos não usam gasolina.')


class Bateria:
    """Uma tentativa simples de criar uma bateria"""
    def __init__(self, bateria=100):
        """Inicializa os atributos da bateria"""
        self.bateria = bateria

    def altera_bateria(self, novo_valor):
        """Altera o valor da bateria"""
        self.bateria = novo_valor

    def mostra_bateria(self):
        print('A bateria do carro está ' + str(self.bateria) + '% cheia.')
