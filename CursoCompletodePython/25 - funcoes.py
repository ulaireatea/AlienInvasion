def soma(num1, num2):
    soma1 = num1
    soma2 = num2
    soma_total = soma1 + soma2
    return soma_total


def sub(num1, num2):
    sub1 = num1
    sub2 = num2
    sub_total = sub1 - sub2
    return sub_total


def mult(num1, num2):
    mult1 = num1
    mult2 = num2
    mult_total = mult1 * mult2
    return mult_total


def div(num1, num2):
    div1 = num1
    div2 = num2
    div_total = div1 / div2
    return div_total


soma = soma(5, 3)
sub = sub(5, 3)
mult = mult(5, 3)
div = div(5, 3)

conta_final = soma + sub + mult + div
print(conta_final)
