class Usuario:
    def __init__(self, primeiro_nome, ultimo_nome, idade, cidade, sexo):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.cidade = cidade
        self.sexo = sexo

    def descricao_usuario(self):
        print(self.primeiro_nome.title() + ' ' + self.ultimo_nome.title() + ', de ' + str(self.idade) + ' anos,' + ' nascido em ' + self.cidade + ', sexo ' + self.sexo)


usuario1 = Usuario('Marcelo', 'Cabral', 40, 'Porto Alegre', 'masculino')
usuario2 = Usuario('Julia', 'Silva', 47, 'São Paulo', 'feminino')
usuario3 = Usuario('Alfredo', 'Costa', 53, 'Manaus', 'masculino')

usuario1.descricao_usuario()
usuario2.descricao_usuario()
usuario3.descricao_usuario()
