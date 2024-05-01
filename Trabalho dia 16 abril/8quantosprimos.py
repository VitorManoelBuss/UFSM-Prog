"""Faça um programa que escreva qual é a quantidade de números primos entre 1 e 100"""

contador = 0

for i in range(1, 101):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
           contador = contador + 1

print(f"Entre os números 1 e 100, há {contador} números primos")