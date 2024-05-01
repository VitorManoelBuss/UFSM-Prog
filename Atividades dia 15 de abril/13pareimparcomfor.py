"""Faça um programa que leia 10 números e conte e escreva quantos são pares e quantos são ímpares"""

par = 0
impar = 0

for i in range(1,11):
    n = int(input("Informe um número: "))
    if (n % 2 == 0):
        par = par + 1
    if (n % 2 != 0):
        impar = impar + 1    


print(f"Dos números digitados são {impar} ímpares e {par} pares")