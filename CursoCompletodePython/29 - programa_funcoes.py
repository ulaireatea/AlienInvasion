import modulo  # ou ainda é possível escrever: from modulo import *, neste caso não é preciso colocar modulo.soma

print(modulo.soma(1, 2))

from modulo import soma  # importando apenas o que for usar fica mais leve o programa

print(soma(3, 5))

from modulo import nome_completo

print(soma(4, 5))
nome_completo(('Marcelo', 'de Moura', 'Cabral'))
