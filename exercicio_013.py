"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

print("Vamos calcular seu peso ideal? ")

input("qual seu sexo? ")
h=float(input("Qual sua altura? "))

ideal_masculino = (72.7*h) - 58 
ideal_feminino = (62.1*h) - 44.7

print("O peso ideal para homens é:", round(ideal_masculino,2))
print("O peso ideal para mulheres é:", round(ideal_feminino,2))
