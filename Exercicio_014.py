"""joão Papo-de-Pescador, homem de bem, comprou um microcomputador 
para controlar o rendimento diário de seu trabalho. Toda vez que ele traz
um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado 
de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade 
de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas."""

peso_de_peixes = 50
excesso = 0
multa_quilo = 4

pescado = float(input("Digite os Kg de peixe pesca: "))
if pescado > peso_de_peixes:
    excesso = pescado - peso_de_peixes
    multa = excesso * multa_quilo 
    print("você excedeu o" , peso_de_peixes, "em Kg. sua multa será:", multa, "pois excedeu", excesso, "kg") 
else:
    print("Você está dentro da cota de pescados" ,peso_de_peixes,"kg")
    