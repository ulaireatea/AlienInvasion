nome1 = "marcelo"
nome2 = "cabral"
nome_completo = " " + nome1 + " " + nome2 + " "
#nome_completo = nome_completo.upper()
num = 5
nome_completo = nome_completo.title()

print(nome_completo.title())
print(nome1)
#print(nome_completo)
print("Olá " + nome_completo + ", tudo bem?")
print("Olá %s, tudo bem?" %nome_completo)
print("Olá %s %s, tudo bem?" %(nome1, nome2))
print("Olá %s %i, tudo bem?" %(nome_completo, num))
print("Olá " + nome_completo.lstrip() + ", tudo bem?") #elimina o espaço do lado esquerdo
                                                                # rstrip elimina do lado direito
                                                                # strip elimina os dois lados
print("Olá " + nome_completo.strip() + ", tudo bem?\nComo vai a família\nManda um abraço!")



