"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

print("escolha dois números inteiros.")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = float(input("Digite um número real: "))

resultado1 = float (2*n1) * (n2/2)
resultado2 = float((3*n1) + n3)
resultado3 = float(n3**3)

print("O produto do dobro do primeiro com metade do segundo é:", resultado1)
print("A soma do triplo do primeiro com o terceiro", resultado2)
print("O terceiro elevado ao cubo", resultado3)

