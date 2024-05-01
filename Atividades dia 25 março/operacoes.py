"""Faça um programa que leia um número e escreva:
- seu dobro
- sua metade
- seu triplo
- sua terça parte
- seu quadrado
- sua raiz quadrada"""
import math

numero = float(input("Informe o número: "))

dobro = numero * 2
metade = numero / 2
triplo = numero * 3
terca_p = numero / 3
quad = numero ** 2
raiz = math. sqrt(numero)

print(f"""
Seu dobro é: {dobro}
Sua metade é: {metade}
Seu triplo é: {triplo}
Sua terça parte é: {terca_p}
Seu quadrado é: {quad}
Sua raiz quadrada é: {raiz}
""")