#Zé do Peixe quer colocar uma cerca ao redor dos seus açudes, que tem o formato circular. 
#Para isso, ele precisa de um programa que leia o diâmetro do açude e calcule o valor da circunferência, com a
#fórmula: c = diâmetro * Pi

diametro = float(input("Informe o diâmetro do seu açude em metros "))

circun = diametro * 3.14

print (f"A circunferência do seu açude é de {circun:,.2f} metros")

#ou dá pra fazer dessa forma

import math
d = float(input("Informe tamanho do diâmetro: "))
c = math.pi * d
print("A circunferência é:", c)