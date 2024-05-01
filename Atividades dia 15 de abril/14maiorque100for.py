"""Faça um programa que leia 10 números e escreva quantos são maiores e quantos são menores que 100."""

maior = 0
menor = 0
igual = 0

for i in range (1, 11):
    n = float(input("Informe um número: "))

    if (n > 100):
        maior = maior + 1

    elif (n < 100):
        menor = menor + 1

    else:
        igual = igual + 1 


print (f"Dos números digitados {maior} são maiores que 100 e {menor} são menores que 100 e igual a 
       100 é {igual}")
