"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias."""

from math import ceil

area = float(input("Informe a área em (m²) a ser pintada: "))
litros = (area / 6)

latas = ceil(litros /18)
galoes = ceil(litros /3.6)

preço_lata = (80)
preço_galao = (25)

latas_economia = ceil(litros //18)
galoes_economia = ceil((litros %18 *1.1) / 3.6 )

print(f"Para pintar {area} m² você precisará de: {latas} lata(s), essa quantidade custará R$ {latas * preço_lata} reais\n")
print(f"Para pintar {area} m² você precisará de {galoes} galão(ões), essa quantidade custará R$ {galoes * preço_galao} reais\n")
print(f"para pintar {area} m² você precisará de {latas_economia}, lata(s) e {galoes_economia} galão(ões), essa quantidade custará R$ {((latas_economia * preço_lata) + (galoes_economia * preço_galao))} reais\n")
