"""Faça um programa que leia um número e escreva a soma dos números de 1 até o número lido."""

num = int(input("Informe um número: "))
num1 = num + 1

soma = 0
for i in range(1, num1):
    soma = soma + i

    print(i)
print(f"Soma: {soma}")