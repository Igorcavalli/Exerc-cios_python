"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

print("VAMOS CALCULAR SEU SALÁRIO?")

din= float(input("Quanto você ganha por hora? R$ "))
hora= float(input("Quantas horas você trabalha por dia? "))
dia= float(input("Quantos dias você trabalha por semana? "))
semana = float(input("Quantas semanas vocês trabalha por mês? "))

print("Seu salário do mês é: R$", din*hora*dia*semana)
