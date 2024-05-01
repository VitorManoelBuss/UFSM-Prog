#Faça um programa em Python que leia o raio de um círculo e calcule e escreva sua área e seu perímetro:
#area = Pi * raio2
#perimetro = 2 * Pi * raio

import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio

print(f"Área :{area:,.2f}")
print(f"Perímetro :{perimetro:,.2f}")