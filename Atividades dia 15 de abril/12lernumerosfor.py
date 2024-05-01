"""Faça um programa que leia 10 números e escreva a soma dos mesmos"""

soma = 0

for i in range(1,11):
    n = int(input("Informe um número: "))
    soma = soma + n
print(f"A soma dos números digitados é: {soma}")
