"""Faça um programa que escreva os números primos entre 1 e 50, juntamente com sua soma"""

soma = 0

for i in range(1, 51):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            soma = soma + i
            print(i)
print(f"A soma dos números primos de 1 à 50 é {soma}")