"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

area = float(input("Informe a área a ser pintada (em m²) "))

cobertura_m2 = 3
cobertura_lata = 54
latas = 1
preço = 80
quantidade_tinta = latas * area / cobertura_lata

if area <= cobertura_lata:
    print ("Uma lata é suficiente, o custo é de R$","{:.2f}".format( preço))
    
else:
    quantidade_latas = int((area /54) +1 )
    print("Você precisará de:",quantidade_latas, "lata(s)")
    preço_final = quantidade_latas * preço
    print("Valor total da compra R$","{:.2f}".format(preço_final))
    