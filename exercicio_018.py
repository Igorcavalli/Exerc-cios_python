"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""


arquivo= float(input("informe o tamanho do arquivo em Mega Bites(MB). "))
internet = float(input("informe a velocidade da sua internet em MBPs. "))
tempo_segundos = arquivo / 20
tempo_minutos = (tempo_segundos/60) 
arredondamento = round(tempo_minutos)
print(f"o tempo estimado para download é:,{arredondamento} minutos")
