"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário 
no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$"""

hora_trabalhada = float(input("Quanto você ganha por hora trabalhada? "))

hora_mês = float(input("Quantas horas você trabalha no mês? "))

salario_bruto = hora_trabalhada * hora_mês
print("Seu salario bruto corresponde a R$","{:.2f}".format(salario_bruto,))

valor_ir = float(11/100* salario_bruto)
print("Desconto IR R$","{:.2f}".format(valor_ir))

valor_inss = float(8/100* salario_bruto)
print("Desconto INSS R$","{:.2f}".format(valor_inss))

sindicato = float(5/100* salario_bruto)
print("Desconto Sindicato R$","{:.2f}".format(sindicato))

salario_liquido = salario_bruto - valor_ir - valor_inss - sindicato
print("Salário liquido R$","{:.2f}".format (salario_liquido))
