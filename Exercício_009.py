"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

print("QUER CONVERTER A TEMPERATURA DE ºF PARA ºC?")

fah = float(input("Acrescente a temperatura em ºF "))
celsius = float(5* ((fah -32) / 9))
print("A temperatura em º C é:", celsius)

                