"""Faça um programa que escreva os números de 1 a 50, juntamente com sua soma"""

soma = 0
for i in range(1, 51):
    soma = soma + i

    print(i)
print(f"Soma: {soma}")