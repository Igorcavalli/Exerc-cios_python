"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

print("Vamos transformar graus Celsius(ºC) em graus Fahrenheit (ºF)?")

celsius=float(input("Informe a temperatura em ºC" ))
fah=float((celsius * 9/5) + 32)

print("A temperatura em ºF é:", fah)