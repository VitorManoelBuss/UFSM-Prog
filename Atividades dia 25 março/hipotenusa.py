#A empresa de internet quer passar o cabo de fibra ótica na diagonal de uma quadra e precisa de um programa 
#que leia os valores correspondentes ao comprimento dos dois lados da quadra e calcule e escreva o 
#comprimento da diagonal (hipotenusa). 

import math

larg = float(input("Qual a largura da quadra em metros "))
comp = float(input("Qual o comprimento da quadra em metros "))

soma = (larg ** 2) + (comp ** 2)
hip = math.sqrt(soma)

print (f"A diagonal da quadra tem {hip:,.2f} metros")

#ou

import math
l1 = float(input("Informe tamanho do 1.o lado: "))
l2 = float(input("Informe tamanho do 2.o lado: "))
diag = math.sqrt(l1**2 + l2**2) ##diag = math.hypot(l1, l2)
print("A diagonal é:", diag)